# MARL Course Syllabus

**Course Title**: Multi-Agent Reinforcement Learning: Foundations and Modern Approaches  
**Format**: Self-paced online tutorial series / 13-week course  
**Level**: Graduate level (MS/PhD) or advanced undergraduate  
**Credits**: 3 (if used in academic setting)  

## Course Description

This course provides a comprehensive introduction to Multi-Agent Reinforcement Learning (MARL), combining theoretical foundations with hands-on implementations. Students will progress from single-agent reinforcement learning basics through advanced multi-agent algorithms, implementing classic and state-of-the-art methods. The course follows an inductive learning approach, building concepts progressively through concrete examples before formal theory.

## Learning Outcomes

By completing this course, students will be able to:

1. **Understand Core RL Concepts**
   - Formulate problems as Markov Decision Processes
   - Implement value-based and policy-based RL algorithms
   - Apply appropriate exploration strategies
   - Debug and optimize RL implementations

2. **Master Multi-Agent Fundamentals**
   - Analyze multi-agent interactions using game theory
   - Identify cooperative, competitive, and mixed scenarios
   - Understand non-stationarity in multi-agent learning
   - Formulate problems as stochastic games

3. **Implement MARL Algorithms**
   - Independent learners (IQL, IAC)
   - Centralized training methods (MADDPG, COMA)
   - Value decomposition methods (VDN, QMIX)
   - Modern actor-critic methods (MAPPO)

4. **Apply Advanced Techniques**
   - Design communication mechanisms
   - Implement coordination strategies
   - Use opponent modeling
   - Apply attention and graph neural networks

5. **Solve Real-World Problems**
   - Select appropriate algorithms for given tasks
   - Implement end-to-end MARL solutions
   - Evaluate and compare algorithm performance
   - Identify current limitations and open problems

## Prerequisites

**Required**:
- Programming: Intermediate Python (functions, classes, NumPy)
- Mathematics: Linear algebra (vectors, matrices, operations)
- Probability: Basic probability theory and statistics
- Calculus: Derivatives, gradients, chain rule

**Recommended but not required**:
- Prior exposure to machine learning
- Experience with neural networks
- Familiarity with Jupyter notebooks

**Will be taught in the course**:
- Reinforcement learning fundamentals
- Game theory basics
- Deep learning for RL
- Multi-agent systems concepts

## Course Schedule

### Part I: Single-Agent RL Foundations (Weeks 1-3)

#### Week 1: Introduction to Reinforcement Learning
- **Topics**: RL paradigm, agent-environment interaction, exploration-exploitation, multi-armed bandits
- **Implementations**: ε-greedy, UCB, Thompson sampling
- **Deliverables**: Exercise set 1
- **Reading**: Sutton & Barto Ch. 1-2

#### Week 2: Markov Decision Processes and Value Methods
- **Topics**: MDPs, Bellman equations, dynamic programming, temporal difference learning
- **Implementations**: Q-learning, SARSA, value/policy iteration
- **Deliverables**: Exercise set 2, Mini-project 1 (GridWorld solver)
- **Reading**: Sutton & Barto Ch. 3-6

#### Week 3: Policy Gradient Methods
- **Topics**: Policy parameterization, policy gradient theorem, actor-critic
- **Implementations**: REINFORCE, A2C
- **Deliverables**: Exercise set 3
- **Reading**: Sutton & Barto Ch. 13, Schulman et al. (2016) on GAE

### Part II: Multi-Agent Foundations (Weeks 4-7)

#### Week 4: Introduction to Multi-Agent Systems
- **Topics**: Multi-agent interactions, types of games, partial observability, game theory basics
- **Implementations**: Simple multi-agent environments
- **Deliverables**: Exercise set 4
- **Reading**: Albrecht et al. Ch. 1-2

#### Week 5: Stochastic Games and Solution Concepts
- **Topics**: Stochastic games, Nash equilibrium, correlated equilibrium, social welfare
- **Implementations**: Nash equilibrium solvers for matrix games
- **Deliverables**: Exercise set 5
- **Reading**: Albrecht et al. Ch. 3-4, Shoham & Leyton-Brown Ch. 3

#### Week 6: Independent Learners
- **Topics**: IQL, non-stationarity, convergence issues
- **Implementations**: Independent Q-learning, hysteretic Q-learning
- **Deliverables**: Exercise set 6, Mini-project 2 (IQL comparison)
- **Reading**: Tan (1993), Matignon et al. (2007)

#### Week 7: Centralized Training Approaches
- **Topics**: CTDE paradigm, centralized critics, MADDPG
- **Implementations**: MADDPG
- **Deliverables**: Exercise set 7
- **Reading**: Lowe et al. (2017), Kraemer & Banerjee (2016)

### Part III: Advanced Concepts (Weeks 8-10)

#### Week 8: Communication in MARL
- **Topics**: Learnable communication, CommNet, TarMAC, emergent protocols
- **Implementations**: CommNet architecture
- **Deliverables**: Exercise set 8
- **Reading**: Sukhbaatar et al. (2016), Das et al. (2019)

#### Week 9: Coordination and Cooperation
- **Topics**: Coordination graphs, social dilemmas, reward shaping, role learning
- **Implementations**: Coordination graph solver, reward shaping
- **Deliverables**: Exercise set 9, Mini-project 3 (cooperation study)
- **Reading**: Guestrin et al. (2002), Leibo et al. (2017)

#### Week 10: Opponent Modeling
- **Topics**: Opponent modeling, theory of mind, best response, self-play
- **Implementations**: Opponent model learner
- **Deliverables**: Exercise set 10
- **Reading**: He et al. (2016), Albrecht & Stone (2018)

### Part IV: Modern Methods (Weeks 11-13)

#### Week 11: Value Decomposition Methods
- **Topics**: VDN, QMIX, QTRAN, IGM principle
- **Implementations**: QMIX (with starter code)
- **Deliverables**: Exercise set 11
- **Reading**: Sunehag et al. (2018), Rashid et al. (2018), Son et al. (2019)

#### Week 12: Multi-Agent Actor-Critic
- **Topics**: COMA, MAPPO, attention mechanisms, transformers
- **Implementations**: MAPPO, attention mechanisms
- **Deliverables**: Exercise set 12, Mini-project 4 (algorithm comparison)
- **Reading**: Foerster et al. (2018), Yu et al. (2021)

#### Week 13: Advanced Topics and Applications
- **Topics**: Mean-field MARL, GNNs, imitation learning, applications, future directions
- **Implementations**: Case study implementation
- **Deliverables**: Final project proposal or final project
- **Reading**: Albrecht et al. Ch. 10-11, recent papers

## Grading Breakdown

**For Academic Use**:
- Exercise Sets (13 × 2%): 26%
- Mini-Projects (4 × 10%): 40%
- Final Project: 30%
- Participation (discussions, peer review): 4%

**For Self-Study**:
- Complete all exercises for full understanding
- Mini-projects provide hands-on experience
- Final project consolidates learning

## Exercise Sets

Each notebook includes exercises of varying difficulty:
- **Basic** (⭐): Test understanding of concepts
- **Intermediate** (⭐⭐): Implement variations
- **Advanced** (⭐⭐⭐): Extensions and research-level questions

Students should complete at minimum all basic exercises.

## Mini-Projects

### Mini-Project 1: GridWorld Solver (Week 2)
Implement and compare DP, MC, and TD methods on a custom GridWorld environment.

### Mini-Project 2: Independent Learners Study (Week 6)
Systematic comparison of IQL across cooperative, competitive, and mixed scenarios.

### Mini-Project 3: Cooperation Study (Week 9)
Implement reward shaping and analyze emergence of cooperation in social dilemmas.

### Mini-Project 4: Algorithm Comparison (Week 12)
Compare IQL, MADDPG, QMIX, and MAPPO on benchmark tasks.

## Final Project Options

Students choose one of the following:

1. **Novel Implementation**
   - Implement a recent MARL algorithm from a research paper
   - Test on appropriate benchmarks
   - Compare with baselines

2. **Application Project**
   - Apply MARL to a domain of interest
   - Complete problem formulation through solution
   - Analyze results and discuss challenges

3. **Comparative Study**
   - Systematic comparison of algorithms
   - Multiple environments and metrics
   - Statistical analysis and insights

4. **Algorithmic Extension**
   - Extend an existing algorithm with novel mechanism
   - Theoretical motivation
   - Empirical validation

5. **Theoretical Analysis**
   - Formal analysis of MARL algorithm
   - Convergence properties or sample complexity
   - Connection to empirical behavior

### Final Project Timeline
- **Week 11**: Project proposal (1 page)
- **Week 12**: Midpoint check-in
- **Week 13+**: Final submission (code + report)
- **Optional**: Presentation

### Final Project Rubric
- **Technical Implementation** (40%): Correctness, quality, documentation
- **Analysis and Evaluation** (30%): Experiments, metrics, interpretation
- **Presentation** (20%): Report clarity, visualizations, writing
- **Novelty/Difficulty** (10%): Ambition, originality, challenge level

## Required Materials

### Textbook
- **Primary**: Albrecht, S. V., Christianos, F., & Schäfer, L. (2024). *Multi-Agent Reinforcement Learning: Foundations and Modern Approaches*. MIT Press. [Available free online]

### Supplementary Texts
- Sutton, R. S., & Barto, A. G. (2018). *Reinforcement Learning: An Introduction* (2nd ed.). MIT Press. [Free online]
- Shoham, Y., & Leyton-Brown, K. (2008). *Multiagent Systems*. Cambridge University Press.

### Software
- Python 3.8+
- PyTorch
- Gymnasium (OpenAI Gym)
- PettingZoo
- Jupyter notebooks
- See requirements.txt for complete list

### Computing Resources
- Personal laptop sufficient for most exercises
- GPU recommended but not required
- Cloud computing credits available (if academic course)

## Reading List

### Week 1
- Sutton & Barto (2018), Chapters 1-2
- Auer et al. (2002), "Finite-time Analysis of the Multiarmed Bandit Problem"

### Week 2
- Sutton & Barto (2018), Chapters 3-6
- Mnih et al. (2015), "Human-level control through deep RL" (DQN paper)

### Week 3
- Sutton & Barto (2018), Chapter 13
- Williams (1992), "Simple Statistical Gradient-Following Algorithms"
- Mnih et al. (2016), "Asynchronous Methods for Deep RL" (A3C paper)

### Week 4
- Albrecht et al. (2024), Chapters 1-2
- Stone & Veloso (2000), "Multiagent Systems: A Survey"

### Week 5
- Albrecht et al. (2024), Chapters 3-4
- Shoham & Leyton-Brown (2008), Chapters 1-3
- Littman (1994), "Markov Games as a Framework"

### Week 6
- Tan (1993), "Multi-Agent Reinforcement Learning"
- Matignon et al. (2007), "Hysteretic Q-Learning"
- Claus & Boutilier (1998), "Dynamics of Reinforcement Learning"

### Week 7
- Lowe et al. (2017), "Multi-Agent Actor-Critic" (MADDPG)
- Kraemer & Banerjee (2016), "Multi-agent RL: A Selective Overview"
- Foerster et al. (2016), "Learning to Communicate"

### Week 8
- Sukhbaatar et al. (2016), "Learning Multiagent Communication" (CommNet)
- Das et al. (2019), "TarMAC: Targeted Multi-Agent Communication"
- Foerster et al. (2016), "Learning to Communicate with Deep MARL"

### Week 9
- Guestrin et al. (2002), "Coordinated Reinforcement Learning"
- Leibo et al. (2017), "Multi-agent Reinforcement Learning in Sequential Social Dilemmas"
- Wang et al. (2020), "ROMA: Multi-Agent RL with Emergent Roles"

### Week 10
- He et al. (2016), "Opponent Modeling in Deep RL"
- Albrecht & Stone (2018), "Autonomous Agents Modelling Other Agents"
- Raileanu et al. (2018), "Modeling Others using Oneself"

### Week 11
- Sunehag et al. (2018), "Value-Decomposition Networks" (VDN)
- Rashid et al. (2018), "QMIX: Monotonic Value Function Factorisation"
- Son et al. (2019), "QTRAN: Learning to Factorize"

### Week 12
- Foerster et al. (2018), "Counterfactual Multi-Agent Policy Gradients" (COMA)
- Yu et al. (2021), "The Surprising Effectiveness of PPO in Cooperative MARL"
- Iqbal & Sha (2019), "Actor-Attention-Critic"

### Week 13
- Yang et al. (2018), "Mean Field Multi-Agent Reinforcement Learning"
- Jiang et al. (2018), "Graph Convolutional Reinforcement Learning"
- Recent MARL papers from NeurIPS/ICML/ICLR

## Course Policies

### Academic Integrity
- Collaboration is encouraged on concepts and debugging
- All code submissions must be individual work
- Cite all external sources and prior work
- Use of AI assistants (ChatGPT, Copilot) should be acknowledged

### Late Policy
- Exercises: 10% deduction per day late
- Mini-projects: 15% deduction per day late
- Final project: No late submissions accepted
- Exceptions for documented emergencies

### Accessibility
- All materials provided in accessible formats
- Accommodations available upon request
- Contact instructor early if needed

### Communication
- Discussion forum for questions (encouraged)
- Office hours: [Schedule]
- Response time: Within 24 hours on weekdays

## Technical Requirements

### Software Environment
- Operating System: Linux, macOS, or Windows 10+
- Python 3.8 or higher
- 8GB RAM minimum (16GB recommended)
- 2GB free disk space
- GPU optional but recommended

### Cloud Alternatives
- Google Colab (free GPU access)
- Kaggle Kernels
- University computing clusters

### Installation Support
- Detailed setup guide provided
- Office hours for installation help
- Docker containers available

## Additional Resources

### Online Resources
- Course GitHub repository: All code and notebooks
- Discussion forum: Q&A and discussions
- Video lectures: Recorded sessions (if available)
- Office hours: Live help sessions

### Community
- MARL reading group (optional)
- Slack/Discord channel (if available)
- Study groups encouraged

### Career and Research
- Links to MARL research groups
- Industry applications of MARL
- Conference and workshop information
- PhD opportunities in MARL

## Course Feedback

Continuous improvement is important. Students are encouraged to:
- Provide feedback on notebooks (GitHub issues)
- Suggest improvements or corrections
- Share interesting applications or papers
- Participate in course evaluation

## Instructor Information

**Instructor**: [To be filled]  
**Office Hours**: [Schedule]  
**Email**: [Contact]  
**Office**: [Location/Virtual]  

**Teaching Assistants**: [If applicable]

## Important Dates

- **Week 1**: Course begins
- **Week 2**: Mini-project 1 due
- **Week 6**: Mini-project 2 due
- **Week 9**: Mini-project 3 due
- **Week 11**: Final project proposal due
- **Week 12**: Mini-project 4 due
- **Week 13**: Course ends
- **Week 14**: Final project due

## Course Adaptation

This syllabus is designed to be flexible:

- **Self-paced learning**: Complete at your own speed
- **8-week intensive**: Focus on core notebooks (1, 2, 3, 4, 6, 7, 11, 12)
- **16-week comprehensive**: Add deeper dives and more projects
- **Workshop format**: Select specific topics of interest

## Conclusion

This course provides a rigorous yet accessible path to mastering Multi-Agent Reinforcement Learning. Through progressive learning, hands-on implementation, and modern algorithms, students will gain the skills needed to apply MARL to research and real-world problems.

**Ready to begin?** Start with [Notebook 01: Introduction to Reinforcement Learning](../notebooks/01_introduction_to_rl.ipynb)

---

*This syllabus is subject to modification. Updates will be announced and documented in the course repository.*
