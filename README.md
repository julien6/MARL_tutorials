# Multi-Agent Reinforcement Learning: A Comprehensive Tutorial Series

Welcome to this comprehensive tutorial series on Multi-Agent Reinforcement Learning (MARL)! This course takes an inductive, chronological approach to teaching MARL, starting from foundational reinforcement learning concepts and progressively building towards advanced multi-agent techniques.

## 📚 Course Philosophy

This course is designed with the following principles:
- **Progressive Learning**: Each notebook builds logically on previous ones
- **Minimal Prerequisites**: Starts almost from scratch (basic Python, linear algebra, probability)
- **Hands-On Approach**: Theory paired with practical implementations
- **Modern Coverage**: Inspired by "Multi-Agent Reinforcement Learning: Foundations and Modern Approaches" by Albrecht, Christianos, and Schäfer

## 🎯 Learning Objectives

By the end of this course, you will:
- Understand fundamental reinforcement learning concepts and algorithms
- Master the theoretical foundations of multi-agent systems
- Implement classic and modern MARL algorithms
- Apply MARL techniques to real-world scenarios
- Understand coordination, cooperation, and competition in multi-agent settings

## 📋 Prerequisites

- Basic Python programming
- Fundamental linear algebra (vectors, matrices)
- Basic probability and statistics
- Calculus fundamentals (derivatives, gradients)

## 🗓️ Course Structure

The course is organized into 13 progressive notebooks spanning approximately 12-13 weeks:

### **Part I: Reinforcement Learning Foundations (Weeks 1-3)**

#### [Notebook 01: Introduction to Reinforcement Learning](notebooks/01_introduction_to_rl.ipynb)
- What is Reinforcement Learning?
- Key concepts: agents, environments, rewards
- The RL problem formulation
- Exploration vs. exploitation
- Simple bandit problems
- **Hands-on**: Implement a multi-armed bandit solver

#### [Notebook 02: Markov Decision Processes and Value-Based Methods](notebooks/02_mdps_and_value_methods.ipynb)
- Markov Decision Processes (MDPs)
- Bellman equations
- Dynamic programming: policy iteration, value iteration
- Monte Carlo methods
- Temporal Difference learning: Q-learning, SARSA
- **Hands-on**: Implement Q-learning for GridWorld

#### [Notebook 03: Policy Gradient Methods](notebooks/03_policy_gradient_methods.ipynb)
- From value-based to policy-based methods
- Policy gradient theorem
- REINFORCE algorithm
- Actor-Critic methods
- Advantage functions
- **Hands-on**: Implement REINFORCE and A2C on CartPole

#### [Notebook 04: Introduction to Multi-Agent Systems](notebooks/04_introduction_to_multi_agent.ipynb)
- From single-agent to multi-agent settings
- Types of multi-agent interactions
- Cooperative, competitive, and mixed scenarios
- Partial observability in multi-agent systems
- Introduction to game theory basics
- **Hands-on**: Build a simple multi-agent environment

### **Part II: MARL Foundations (Weeks 4-6)**

#### [Notebook 05: Stochastic Games and Solution Concepts](notebooks/05_stochastic_games_nash.ipynb)
- Normal-form and extensive-form games
- Stochastic games (Markov games)
- Nash equilibrium and variants
- Correlated equilibrium
- Social welfare and fairness
- **Hands-on**: Find Nash equilibria in simple games

#### [Notebook 06: Independent Learners](notebooks/06_independent_learners.ipynb)
- Independent Q-learning (IQL)
- Independent Actor-Critic (IAC)
- Challenges: non-stationarity, moving target problem
- Empirical analysis of convergence
- When do independent learners work?
- **Hands-on**: Implement IQL in cooperative and competitive settings

#### [Notebook 07: Centralized Training Approaches](notebooks/07_centralized_training.ipynb)
- Centralized Training with Decentralized Execution (CTDE)
- Joint action spaces
- Credit assignment problem
- Centralized critic methods
- Multi-Agent Deep Deterministic Policy Gradient (MADDPG)
- **Hands-on**: Implement MADDPG for cooperative navigation

### **Part III: Advanced MARL Concepts (Weeks 7-9)**

#### [Notebook 08: Communication in MARL](notebooks/08_communication_marl.ipynb)
- Why communication matters
- Communication protocols
- CommNet and TarMAC
- Learning when and what to communicate
- Emergent communication
- **Hands-on**: Implement learnable communication for coordination tasks

#### [Notebook 09: Coordination and Cooperation](notebooks/09_coordination_cooperation.ipynb)
- Coordination graphs
- Role assignment and task allocation
- Learning to cooperate
- Social dilemmas in MARL
- Reward shaping for cooperation
- **Hands-on**: Solve coordination games with different approaches

#### [Notebook 10: Opponent Modeling and Theory of Mind](notebooks/10_opponent_modeling.ipynb)
- Modeling other agents
- Belief-based approaches
- Theory of mind in MARL
- Recursive reasoning
- Applications in competitive settings
- **Hands-on**: Implement opponent modeling for poker-like games

### **Part IV: Modern MARL Methods (Weeks 10-12)**

#### [Notebook 11: Value Decomposition Methods](notebooks/11_value_decomposition.ipynb)
- Value decomposition networks (VDN)
- QMIX: Monotonic value function factorization
- QTRAN and other extensions
- When and why value decomposition works
- Comparison with other CTDE methods
- **Hands-on**: Implement QMIX for StarCraft Multi-Agent Challenge (SMAC)

#### [Notebook 12: Multi-Agent Actor-Critic Methods](notebooks/12_multi_agent_actor_critic.ipynb)
- Counterfactual multi-agent policy gradients (COMA)
- Multi-Agent PPO (MAPPO)
- Attention mechanisms in MARL
- Transformers for multi-agent coordination
- **Hands-on**: Implement MAPPO for complex coordination tasks

#### [Notebook 13: Advanced Topics and Applications](notebooks/13_advanced_topics_applications.ipynb)
- Mean-field MARL for many agents
- Graph neural networks in MARL
- Multi-agent imitation learning
- Real-world applications: robotics, traffic control, resource allocation
- Current challenges and future directions
- **Hands-on**: Case study on a real-world MARL application

## 🛠️ Setup Instructions

### Installation

1. Clone this repository:
```bash
git clone https://github.com/julien6/MARL_tutorials.git
cd MARL_tutorials
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Launch Jupyter:
```bash
jupyter notebook
```

### Requirements

The course uses the following main libraries:
- NumPy and Matplotlib for numerical computing and visualization
- Gymnasium (formerly OpenAI Gym) for RL environments
- PyTorch for deep learning
- PettingZoo for multi-agent environments
- Additional libraries for specific algorithms and visualizations

See [requirements.txt](requirements.txt) for the complete list.

## 📖 Recommended Reading

**Primary Reference:**
- Albrecht, S. V., Christianos, F., & Schäfer, L. (2024). *Multi-Agent Reinforcement Learning: Foundations and Modern Approaches*. MIT Press.

**Additional Resources:**
- Sutton, R. S., & Barto, A. G. (2018). *Reinforcement Learning: An Introduction*. MIT Press.
- Shoham, Y., & Leyton-Brown, K. (2008). *Multiagent Systems: Algorithmic, Game-Theoretic, and Logical Foundations*. Cambridge University Press.
- Recent papers on MARL (linked throughout notebooks)

## 🎓 How to Use This Course

1. **Follow the Sequence**: Notebooks are designed to be completed in order
2. **Run the Code**: Execute all cells and experiment with parameters
3. **Complete Exercises**: Each notebook includes exercises to reinforce learning
4. **Extend and Explore**: Try implementing variations and testing on new environments
5. **Join the Community**: Share your solutions and discuss challenges

## 🤝 Contributing

Contributions are welcome! Whether it's fixing typos, improving explanations, adding exercises, or suggesting new topics, please feel free to:
- Open an issue for discussions
- Submit a pull request with improvements
- Share your extended implementations

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by the excellent textbook by Albrecht, Christianos, and Schäfer
- Built on the shoulders of the open-source RL community
- Thanks to developers of Gymnasium, PettingZoo, and other libraries used

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

---

**Ready to start learning?** Head to [Notebook 01: Introduction to Reinforcement Learning](notebooks/01_introduction_to_rl.ipynb) to begin your journey into Multi-Agent Reinforcement Learning!