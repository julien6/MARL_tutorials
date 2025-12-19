"""
Simple Multi-Agent GridWorld Environment

A basic multi-agent gridworld for educational purposes.
Agents can move in 4 directions and need to reach their goals.
"""

import numpy as np
from typing import Dict, List, Tuple, Optional
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle


class SimpleMAGridWorld:
    """
    Simple multi-agent gridworld environment.
    
    Features:
    - Grid-based world
    - Multiple agents with individual goals
    - Optional obstacles
    - Configurable rewards
    """
    
    def __init__(
        self,
        grid_size: Tuple[int, int] = (5, 5),
        n_agents: int = 2,
        max_steps: int = 50,
        reward_goal: float = 10.0,
        reward_step: float = -0.1,
        reward_collision: float = -1.0
    ):
        """
        Initialize the gridworld.
        
        Args:
            grid_size: (height, width) of the grid
            n_agents: Number of agents
            max_steps: Maximum steps per episode
            reward_goal: Reward for reaching goal
            reward_step: Reward for each step (typically negative)
            reward_collision: Reward for collision with another agent
        """
        self.grid_size = grid_size
        self.n_agents = n_agents
        self.max_steps = max_steps
        
        self.reward_goal = reward_goal
        self.reward_step = reward_step
        self.reward_collision = reward_collision
        
        # Action space: 0=up, 1=right, 2=down, 3=left, 4=stay
        self.n_actions = 5
        self.action_space = list(range(self.n_actions))
        
        # State: positions of all agents (flattened)
        self.observation_dim = 2 * n_agents  # (x, y) for each agent
        
        self.agent_positions = None
        self.goal_positions = None
        self.obstacles = []
        self.steps = 0
        
    def reset(self) -> Dict[int, np.ndarray]:
        """
        Reset the environment.
        
        Returns:
            Dictionary mapping agent IDs to their observations
        """
        self.steps = 0
        
        # Random initial positions for agents
        self.agent_positions = {}
        for i in range(self.n_agents):
            while True:
                pos = (
                    np.random.randint(0, self.grid_size[0]),
                    np.random.randint(0, self.grid_size[1])
                )
                if pos not in self.agent_positions.values() and pos not in self.obstacles:
                    self.agent_positions[i] = pos
                    break
        
        # Random goal positions
        self.goal_positions = {}
        for i in range(self.n_agents):
            while True:
                pos = (
                    np.random.randint(0, self.grid_size[0]),
                    np.random.randint(0, self.grid_size[1])
                )
                if (pos not in self.goal_positions.values() and 
                    pos not in self.agent_positions.values() and
                    pos not in self.obstacles):
                    self.goal_positions[i] = pos
                    break
        
        return self._get_observations()
    
    def step(
        self,
        actions: Dict[int, int]
    ) -> Tuple[Dict[int, np.ndarray], Dict[int, float], Dict[int, bool], Dict]:
        """
        Execute actions for all agents.
        
        Args:
            actions: Dictionary mapping agent IDs to actions
            
        Returns:
            observations: Dictionary of observations
            rewards: Dictionary of rewards
            dones: Dictionary of done flags
            info: Dictionary of additional information
        """
        self.steps += 1
        new_positions = {}
        
        # Compute new positions
        for agent_id, action in actions.items():
            new_pos = self._get_new_position(self.agent_positions[agent_id], action)
            new_positions[agent_id] = new_pos
        
        # Check for collisions and update positions
        rewards = {i: self.reward_step for i in range(self.n_agents)}
        
        for agent_id in range(self.n_agents):
            # Check if reached goal
            if new_positions[agent_id] == self.goal_positions[agent_id]:
                rewards[agent_id] += self.reward_goal
            
            # Check for collisions with other agents
            collision = False
            for other_id in range(self.n_agents):
                if other_id != agent_id and new_positions[agent_id] == new_positions[other_id]:
                    collision = True
                    break
            
            if collision:
                rewards[agent_id] += self.reward_collision
                # Don't move if collision
            else:
                self.agent_positions[agent_id] = new_positions[agent_id]
        
        observations = self._get_observations()
        
        # Episode done if all agents reached goals or max steps
        all_at_goal = all(
            self.agent_positions[i] == self.goal_positions[i]
            for i in range(self.n_agents)
        )
        dones = {
            i: all_at_goal or self.steps >= self.max_steps
            for i in range(self.n_agents)
        }
        
        info = {
            'steps': self.steps,
            'all_at_goal': all_at_goal
        }
        
        return observations, rewards, dones, info
    
    def _get_new_position(
        self,
        position: Tuple[int, int],
        action: int
    ) -> Tuple[int, int]:
        """
        Compute new position given current position and action.
        
        Args:
            position: Current (row, col) position
            action: Action to take
            
        Returns:
            New position
        """
        row, col = position
        
        # Actions: 0=up, 1=right, 2=down, 3=left, 4=stay
        if action == 0:  # up
            row = max(0, row - 1)
        elif action == 1:  # right
            col = min(self.grid_size[1] - 1, col + 1)
        elif action == 2:  # down
            row = min(self.grid_size[0] - 1, row + 1)
        elif action == 3:  # left
            col = max(0, col - 1)
        # action == 4: stay
        
        new_pos = (row, col)
        
        # Check obstacles
        if new_pos in self.obstacles:
            return position  # Stay in place if hit obstacle
        
        return new_pos
    
    def _get_observations(self) -> Dict[int, np.ndarray]:
        """
        Get observations for all agents.
        
        For now, each agent observes all agent positions (fully observable).
        
        Returns:
            Dictionary mapping agent IDs to observations
        """
        # Flatten all positions
        obs = []
        for i in range(self.n_agents):
            obs.extend(self.agent_positions[i])
        obs = np.array(obs, dtype=np.float32)
        
        # Return same observation to all agents (centralized)
        return {i: obs.copy() for i in range(self.n_agents)}
    
    def render(self, mode: str = 'human') -> Optional[np.ndarray]:
        """
        Render the environment.
        
        Args:
            mode: Rendering mode ('human' for display, 'rgb_array' for image)
            
        Returns:
            RGB array if mode='rgb_array', None otherwise
        """
        fig, ax = plt.subplots(figsize=(6, 6))
        
        # Draw grid
        for i in range(self.grid_size[0] + 1):
            ax.axhline(i, color='black', linewidth=0.5)
        for j in range(self.grid_size[1] + 1):
            ax.axvline(j, color='black', linewidth=0.5)
        
        # Draw obstacles
        for obs in self.obstacles:
            rect = Rectangle((obs[1], self.grid_size[0] - obs[0] - 1), 
                           1, 1, facecolor='gray', edgecolor='black')
            ax.add_patch(rect)
        
        # Draw goals
        colors = plt.cm.Set1(np.linspace(0, 1, self.n_agents))
        for agent_id, goal_pos in self.goal_positions.items():
            rect = Rectangle((goal_pos[1], self.grid_size[0] - goal_pos[0] - 1),
                           1, 1, facecolor=colors[agent_id], alpha=0.3, 
                           edgecolor='black', linewidth=2)
            ax.add_patch(rect)
            ax.text(goal_pos[1] + 0.5, self.grid_size[0] - goal_pos[0] - 0.5,
                   f'G{agent_id}', ha='center', va='center', fontsize=12)
        
        # Draw agents
        for agent_id, pos in self.agent_positions.items():
            circle = Circle((pos[1] + 0.5, self.grid_size[0] - pos[0] - 0.5),
                          0.3, facecolor=colors[agent_id], edgecolor='black', 
                          linewidth=2)
            ax.add_patch(circle)
            ax.text(pos[1] + 0.5, self.grid_size[0] - pos[0] - 0.5,
                   str(agent_id), ha='center', va='center', 
                   fontsize=10, color='white', weight='bold')
        
        ax.set_xlim(0, self.grid_size[1])
        ax.set_ylim(0, self.grid_size[0])
        ax.set_aspect('equal')
        ax.set_title(f'Step: {self.steps}/{self.max_steps}')
        ax.axis('off')
        
        plt.tight_layout()
        
        if mode == 'rgb_array':
            fig.canvas.draw()
            image = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
            image = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))
            plt.close(fig)
            return image
        else:
            plt.show()
            return None
    
    def add_obstacles(self, obstacles: List[Tuple[int, int]]) -> None:
        """
        Add obstacles to the grid.
        
        Args:
            obstacles: List of (row, col) positions
        """
        self.obstacles = obstacles


# Example usage
if __name__ == "__main__":
    # Create environment
    env = SimpleMAGridWorld(grid_size=(5, 5), n_agents=2)
    
    # Add some obstacles
    env.add_obstacles([(2, 2), (2, 3)])
    
    # Reset and render
    obs = env.reset()
    print("Initial observations:", obs)
    env.render()
    
    # Take random actions
    for step in range(10):
        actions = {i: np.random.randint(0, env.n_actions) 
                  for i in range(env.n_agents)}
        obs, rewards, dones, info = env.step(actions)
        
        print(f"\nStep {step + 1}")
        print(f"Actions: {actions}")
        print(f"Rewards: {rewards}")
        print(f"Dones: {dones}")
        
        if dones[0]:
            print("Episode finished!")
            break
