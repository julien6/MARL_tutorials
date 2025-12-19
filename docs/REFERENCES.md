# MARL References and Resources

This document provides a comprehensive list of references for Multi-Agent Reinforcement Learning.

## Primary Textbook

**Albrecht, S. V., Christianos, F., & Schäfer, L. (2024)**. *Multi-Agent Reinforcement Learning: Foundations and Modern Approaches*. MIT Press.
- [Free online version](https://www.marl-book.com/)
- Comprehensive coverage of MARL theory and algorithms
- Modern methods and applications

## Foundational Books

### Reinforcement Learning

1. **Sutton, R. S., & Barto, A. G. (2018)**. *Reinforcement Learning: An Introduction* (2nd ed.). MIT Press.
   - [Free online](http://incompleteideas.net/book/the-book-2nd.html)
   - The definitive RL textbook
   - Essential background for MARL

2. **Bertsekas, D. P. (2019)**. *Reinforcement Learning and Optimal Control*. Athena Scientific.
   - Mathematical foundations
   - Dynamic programming perspective

### Game Theory and Multi-Agent Systems

3. **Shoham, Y., & Leyton-Brown, K. (2008)**. *Multiagent Systems: Algorithmic, Game-Theoretic, and Logical Foundations*. Cambridge University Press.
   - [Free PDF available](http://www.masfoundations.org/)
   - Game theory foundations
   - Multi-agent coordination

4. **Nisan, N., et al. (2007)**. *Algorithmic Game Theory*. Cambridge University Press.
   - Computational game theory
   - Mechanism design

## Key Papers by Topic

### Multi-Agent Bandits and Basics

- **Tan, M. (1993)**. "Multi-Agent Reinforcement Learning: Independent vs. Cooperative Agents." *ICML*.
  - Pioneering work on MARL
  
- **Claus, C., & Boutilier, C. (1998)**. "The Dynamics of Reinforcement Learning in Cooperative Multiagent Systems." *AAAI*.
  - Analysis of cooperative learning

### Stochastic Games

- **Littman, M. L. (1994)**. "Markov Games as a Framework for Multi-Agent Reinforcement Learning." *ICML*.
  - Formalizes MARL as Markov games

- **Hu, J., & Wellman, M. P. (2003)**. "Nash Q-Learning for General-Sum Stochastic Games." *JMLR*.
  - Learning Nash equilibria

### Independent Learning

- **Matignon, L., Laurent, G. J., & Le Fort-Piat, N. (2007)**. "Hysteretic Q-Learning: An Algorithm for Decentralized Reinforcement Learning in Cooperative Multi-Agent Teams." *IROS*.
  - Addresses non-stationarity

- **Lauer, M., & Riedmiller, M. (2000)**. "An Algorithm for Distributed Reinforcement Learning in Cooperative Multi-Agent Systems." *ICML*.
  - Distributed Q-learning

### Centralized Training

- **Lowe, R., et al. (2017)**. "Multi-Agent Actor-Critic for Mixed Cooperative-Competitive Environments." *NeurIPS*.
  - MADDPG algorithm
  - [Paper](https://arxiv.org/abs/1706.02275)

- **Foerster, J., et al. (2016)**. "Learning to Communicate with Deep Multi-Agent Reinforcement Learning." *NeurIPS*.
  - Communication in MARL
  - [Paper](https://arxiv.org/abs/1605.06676)

### Value Decomposition

- **Sunehag, P., et al. (2018)**. "Value-Decomposition Networks For Cooperative Multi-Agent Learning." *AAMAS*.
  - VDN algorithm
  - [Paper](https://arxiv.org/abs/1706.05296)

- **Rashid, T., et al. (2018)**. "QMIX: Monotonic Value Function Factorisation for Decentralised Multi-Agent Reinforcement Learning." *ICML*.
  - QMIX algorithm
  - [Paper](https://arxiv.org/abs/1803.11485)

- **Son, K., et al. (2019)**. "QTRAN: Learning to Factorize with Transformation for Cooperative Multi-Agent Reinforcement Learning." *ICML*.
  - Extends value decomposition
  - [Paper](https://arxiv.org/abs/1905.05408)

### Policy Gradient Methods

- **Foerster, J., et al. (2018)**. "Counterfactual Multi-Agent Policy Gradients." *AAAI*.
  - COMA algorithm
  - [Paper](https://arxiv.org/abs/1705.08926)

- **Yu, C., et al. (2021)**. "The Surprising Effectiveness of PPO in Cooperative Multi-Agent Games." *NeurIPS*.
  - MAPPO algorithm
  - [Paper](https://arxiv.org/abs/2103.01955)

### Communication

- **Sukhbaatar, S., Szlam, A., & Fergus, R. (2016)**. "Learning Multiagent Communication with Backpropagation." *NeurIPS*.
  - CommNet
  - [Paper](https://arxiv.org/abs/1605.07736)

- **Das, A., et al. (2019)**. "TarMAC: Targeted Multi-Agent Communication." *ICML*.
  - Attention-based communication
  - [Paper](https://arxiv.org/abs/1810.11187)

- **Lazaridou, A., & Baroni, M. (2020)**. "Emergent Multi-Agent Communication in the Deep Learning Era." *arXiv*.
  - Survey of emergent communication
  - [Paper](https://arxiv.org/abs/2006.02419)

### Coordination and Cooperation

- **Guestrin, C., Koller, D., & Parr, R. (2002)**. "Multiagent Planning with Factored MDPs." *NeurIPS*.
  - Coordination graphs

- **Leibo, J. Z., et al. (2017)**. "Multi-Agent Reinforcement Learning in Sequential Social Dilemmas." *AAMAS*.
  - Social dilemmas in MARL
  - [Paper](https://arxiv.org/abs/1702.03037)

- **Wang, T., et al. (2020)**. "ROMA: Multi-Agent Reinforcement Learning with Emergent Roles." *ICML*.
  - Role-based learning
  - [Paper](https://arxiv.org/abs/2003.08039)

### Opponent Modeling

- **He, H., et al. (2016)**. "Opponent Modeling in Deep Reinforcement Learning." *ICML*.
  - Deep opponent modeling
  - [Paper](https://arxiv.org/abs/1609.05559)

- **Albrecht, S. V., & Stone, P. (2018)**. "Autonomous Agents Modelling Other Agents: A Comprehensive Survey and Open Problems." *AIJ*.
  - Comprehensive survey
  - [Paper](https://arxiv.org/abs/1709.08071)

### Attention and Transformers

- **Iqbal, S., & Sha, F. (2019)**. "Actor-Attention-Critic for Multi-Agent Reinforcement Learning." *ICML*.
  - Attention mechanisms
  - [Paper](https://arxiv.org/abs/1810.02912)

- **Vaswani, A., et al. (2017)**. "Attention Is All You Need." *NeurIPS*.
  - Transformer architecture
  - [Paper](https://arxiv.org/abs/1706.03762)

### Graph Neural Networks

- **Jiang, J., et al. (2018)**. "Graph Convolutional Reinforcement Learning." *ICLR*.
  - GNNs for MARL
  - [Paper](https://arxiv.org/abs/1810.09202)

- **Battaglia, P. W., et al. (2018)**. "Relational Inductive Biases, Deep Learning, and Graph Networks." *arXiv*.
  - GNN foundations
  - [Paper](https://arxiv.org/abs/1806.01261)

### Mean Field Methods

- **Yang, Y., et al. (2018)**. "Mean Field Multi-Agent Reinforcement Learning." *ICML*.
  - Mean field approach
  - [Paper](https://arxiv.org/abs/1802.05438)

### Applications

- **Vinyals, O., et al. (2019)**. "Grandmaster Level in StarCraft II Using Multi-Agent Reinforcement Learning." *Nature*.
  - AlphaStar
  - [Paper](https://www.nature.com/articles/s41586-019-1724-z)

- **OpenAI, et al. (2019)**. "Dota 2 with Large Scale Deep Reinforcement Learning." *arXiv*.
  - OpenAI Five
  - [Paper](https://arxiv.org/abs/1912.06680)

## Survey Papers

- **Busoniu, L., Babuska, R., & De Schutter, B. (2008)**. "A Comprehensive Survey of Multiagent Reinforcement Learning." *IEEE Transactions on Systems, Man, and Cybernetics*.
  - Classic survey

- **Zhang, K., Yang, Z., & Basar, T. (2021)**. "Multi-Agent Reinforcement Learning: A Selective Overview of Theories and Algorithms." *Handbook of Reinforcement Learning and Control*.
  - Modern survey
  - [Paper](https://arxiv.org/abs/1911.10635)

- **Hernandez-Leal, P., Kartal, B., & Taylor, M. E. (2019)**. "A Survey and Critique of Multiagent Deep Reinforcement Learning." *AAMAS*.
  - Deep MARL survey
  - [Paper](https://arxiv.org/abs/1810.05587)

## Benchmarks and Environments

### PettingZoo
- Terry, J. K., et al. (2021). "PettingZoo: Gym for Multi-Agent Reinforcement Learning." *NeurIPS*.
- [Documentation](https://pettingzoo.farama.org/)

### SMAC (StarCraft Multi-Agent Challenge)
- Samvelyan, M., et al. (2019). "The StarCraft Multi-Agent Challenge." *arXiv*.
- [Paper](https://arxiv.org/abs/1902.04043)
- [GitHub](https://github.com/oxwhirl/smac)

### Multi-Agent Particle Environments
- Mordatch, I., & Abbeel, P. (2018). "Emergence of Grounded Compositional Language in Multi-Agent Populations." *AAAI*.
- Part of OpenAI baselines

## Online Courses and Tutorials

1. **David Silver's RL Course**
   - [YouTube Playlist](https://www.youtube.com/playlist?list=PLqYmG7hTraZDM-OYHWgPebj2MfCFzFObQ)
   - Foundational RL

2. **Berkeley CS 285: Deep RL**
   - [Course Website](http://rail.eecs.berkeley.edu/deeprlcourse/)
   - Modern deep RL

3. **Stanford CS 234: Reinforcement Learning**
   - [Course Website](https://web.stanford.edu/class/cs234/)

4. **Multi-Agent Learning (Stefano Albrecht)**
   - [Course Materials](https://agents.inf.ed.ac.uk/teaching/marl/)

## Blogs and Online Resources

- **Spinning Up in Deep RL (OpenAI)**
  - [Link](https://spinningup.openai.com/)
  - Excellent RL resource

- **Lil'Log (Lilian Weng)**
  - [Link](https://lilianweng.github.io/)
  - Great ML/RL blog posts

- **Distill.pub**
  - [Link](https://distill.pub/)
  - Interactive ML explanations

## Code Libraries

### MARL Libraries

1. **PyMARL**
   - [GitHub](https://github.com/oxwhirl/pymarl)
   - Implementations of QMIX, COMA, etc.

2. **EPyMARL**
   - [GitHub](https://github.com/uoe-agents/epymarl)
   - Extended PyMARL

3. **MARLlib**
   - [GitHub](https://github.com/Replicable-MARL/MARLlib)
   - Comprehensive MARL library

### RL Libraries

1. **Stable-Baselines3**
   - [Documentation](https://stable-baselines3.readthedocs.io/)
   - Reliable RL implementations

2. **RLlib (Ray)**
   - [Documentation](https://docs.ray.io/en/latest/rllib/)
   - Scalable RL

3. **CleanRL**
   - [GitHub](https://github.com/vwxyzjn/cleanrl)
   - Single-file implementations

## Conferences and Workshops

- **NeurIPS**: Neural Information Processing Systems
- **ICML**: International Conference on Machine Learning
- **ICLR**: International Conference on Learning Representations
- **AAMAS**: International Conference on Autonomous Agents and Multiagent Systems
- **AAAI**: Association for the Advancement of Artificial Intelligence

## Research Groups

- **WhiRL (Oxford)**: [Link](https://whirl.cs.ox.ac.uk/)
- **AIML Lab (Edinburgh)**: [Link](https://agents.inf.ed.ac.uk/)
- **MAIL (Imperial)**: [Link](https://www.imperial.ac.uk/machine-learning/)

## Staying Updated

- **arXiv**: Search for "multi-agent reinforcement learning"
- **Papers with Code**: [MARL section](https://paperswithcode.com/task/multi-agent-reinforcement-learning)
- **Twitter/X**: Follow MARL researchers
- **Reddit**: r/MachineLearning, r/reinforcementlearning

---

*This list is not exhaustive. The field is rapidly evolving, so check for recent papers and resources regularly.*
