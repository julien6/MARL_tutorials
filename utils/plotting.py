"""
Utility Functions for MARL Tutorials

This module contains helper functions used across multiple notebooks
for visualization, logging, evaluation, and common operations.
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import List, Dict, Any, Optional, Tuple
import seaborn as sns

# Set style for consistent visualizations
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)


def set_seed(seed: int = 42) -> None:
    """
    Set random seeds for reproducibility.
    
    Args:
        seed: Random seed value
    """
    np.random.seed(seed)
    try:
        import torch
        torch.manual_seed(seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(seed)
    except ImportError:
        pass


def plot_learning_curve(
    rewards: List[float],
    window: int = 100,
    title: str = "Learning Curve",
    xlabel: str = "Episode",
    ylabel: str = "Return",
    show_std: bool = True
) -> None:
    """
    Plot learning curve with moving average.
    
    Args:
        rewards: List of episode rewards
        window: Window size for moving average
        title: Plot title
        xlabel: X-axis label
        ylabel: Y-axis label
        show_std: Whether to show standard deviation band
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    
    episodes = np.arange(len(rewards))
    ax.plot(episodes, rewards, alpha=0.3, label='Raw')
    
    if len(rewards) >= window:
        moving_avg = np.convolve(rewards, np.ones(window)/window, mode='valid')
        ax.plot(np.arange(window-1, len(rewards)), moving_avg, 
                linewidth=2, label=f'Moving Average (window={window})')
        
        if show_std and len(rewards) > window:
            moving_std = np.array([
                np.std(rewards[max(0, i-window):i]) 
                for i in range(window, len(rewards)+1)
            ])
            avg_episodes = np.arange(window-1, len(rewards))
            ax.fill_between(avg_episodes, 
                           moving_avg - moving_std,
                           moving_avg + moving_std,
                           alpha=0.2)
    
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def plot_multi_agent_learning_curves(
    agent_rewards: Dict[str, List[float]],
    window: int = 100,
    title: str = "Multi-Agent Learning Curves"
) -> None:
    """
    Plot learning curves for multiple agents.
    
    Args:
        agent_rewards: Dictionary mapping agent names to reward lists
        window: Window size for moving average
        title: Plot title
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    
    for agent_name, rewards in agent_rewards.items():
        episodes = np.arange(len(rewards))
        
        if len(rewards) >= window:
            moving_avg = np.convolve(rewards, np.ones(window)/window, mode='valid')
            ax.plot(np.arange(window-1, len(rewards)), moving_avg, 
                   linewidth=2, label=agent_name)
    
    ax.set_xlabel("Episode")
    ax.set_ylabel("Average Return")
    ax.set_title(title)
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def plot_value_function(
    values: np.ndarray,
    title: str = "Value Function",
    cmap: str = "viridis"
) -> None:
    """
    Plot a 2D value function heatmap.
    
    Args:
        values: 2D array of state values
        title: Plot title
        cmap: Colormap name
    """
    fig, ax = plt.subplots(figsize=(8, 6))
    im = ax.imshow(values, cmap=cmap, aspect='auto')
    ax.set_title(title)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    plt.colorbar(im, ax=ax, label="Value")
    plt.tight_layout()
    plt.show()


def plot_policy(
    policy: np.ndarray,
    action_names: Optional[List[str]] = None,
    title: str = "Policy Visualization"
) -> None:
    """
    Visualize a policy as arrows in a grid.
    
    Args:
        policy: 2D array of action indices
        action_names: Optional list of action names
        title: Plot title
    """
    # Standard grid world actions: up, right, down, left
    arrows = ['↑', '→', '↓', '←']
    
    height, width = policy.shape
    fig, ax = plt.subplots(figsize=(width, height))
    
    for i in range(height):
        for j in range(width):
            action = policy[i, j]
            if action < len(arrows):
                ax.text(j, i, arrows[action], 
                       ha='center', va='center', fontsize=20)
    
    ax.set_xlim(-0.5, width - 0.5)
    ax.set_ylim(-0.5, height - 0.5)
    ax.set_xticks(range(width))
    ax.set_yticks(range(height))
    ax.grid(True)
    ax.set_title(title)
    ax.invert_yaxis()
    plt.tight_layout()
    plt.show()


def moving_average(data: List[float], window: int = 100) -> np.ndarray:
    """
    Compute moving average of data.
    
    Args:
        data: List of values
        window: Window size
        
    Returns:
        Array of moving averages
    """
    return np.convolve(data, np.ones(window)/window, mode='valid')


def evaluate_agent(
    agent: Any,
    env: Any,
    n_episodes: int = 100,
    render: bool = False
) -> Tuple[float, float]:
    """
    Evaluate an agent's performance.
    
    Args:
        agent: Agent to evaluate
        env: Environment
        n_episodes: Number of evaluation episodes
        render: Whether to render episodes
        
    Returns:
        Tuple of (mean_return, std_return)
    """
    returns = []
    
    for _ in range(n_episodes):
        obs, _ = env.reset()
        episode_return = 0
        done = False
        
        while not done:
            if render:
                env.render()
            
            action = agent.select_action(obs, eval_mode=True)
            obs, reward, terminated, truncated, _ = env.step(action)
            episode_return += reward
            done = terminated or truncated
        
        returns.append(episode_return)
    
    return np.mean(returns), np.std(returns)


class RunningMeanStd:
    """
    Running mean and standard deviation computation.
    Useful for reward/observation normalization.
    """
    
    def __init__(self, epsilon: float = 1e-4, shape: Tuple = ()):
        self.mean = np.zeros(shape, dtype=np.float64)
        self.var = np.ones(shape, dtype=np.float64)
        self.count = epsilon
    
    def update(self, x: np.ndarray) -> None:
        """Update running statistics with new data."""
        batch_mean = np.mean(x, axis=0)
        batch_var = np.var(x, axis=0)
        batch_count = x.shape[0]
        self.update_from_moments(batch_mean, batch_var, batch_count)
    
    def update_from_moments(
        self,
        batch_mean: np.ndarray,
        batch_var: np.ndarray,
        batch_count: int
    ) -> None:
        """Update from batch statistics."""
        delta = batch_mean - self.mean
        tot_count = self.count + batch_count
        
        new_mean = self.mean + delta * batch_count / tot_count
        m_a = self.var * self.count
        m_b = batch_var * batch_count
        M2 = m_a + m_b + np.square(delta) * self.count * batch_count / tot_count
        new_var = M2 / tot_count
        
        self.mean = new_mean
        self.var = new_var
        self.count = tot_count


def print_hyperparameters(params: Dict[str, Any]) -> None:
    """
    Pretty print hyperparameters.
    
    Args:
        params: Dictionary of hyperparameters
    """
    print("=" * 50)
    print("Hyperparameters:")
    print("=" * 50)
    for key, value in params.items():
        print(f"{key:.<30} {value}")
    print("=" * 50)


def save_results(
    results: Dict[str, Any],
    filepath: str
) -> None:
    """
    Save experimental results.
    
    Args:
        results: Dictionary of results
        filepath: Path to save file
    """
    import json
    
    # Convert numpy arrays to lists for JSON serialization
    serializable_results = {}
    for key, value in results.items():
        if isinstance(value, np.ndarray):
            serializable_results[key] = value.tolist()
        else:
            serializable_results[key] = value
    
    with open(filepath, 'w') as f:
        json.dump(serializable_results, f, indent=2)
    
    print(f"Results saved to {filepath}")


def load_results(filepath: str) -> Dict[str, Any]:
    """
    Load experimental results.
    
    Args:
        filepath: Path to results file
        
    Returns:
        Dictionary of results
    """
    import json
    
    with open(filepath, 'r') as f:
        results = json.load(f)
    
    return results
