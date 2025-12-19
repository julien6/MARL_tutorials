# MARL Tutorial Notebooks

This directory contains all Jupyter notebooks for the Multi-Agent Reinforcement Learning tutorial course.

## 📚 Notebook Index

### Part I: Reinforcement Learning Foundations

| # | Notebook | Topics | Status |
|---|----------|--------|--------|
| 01 | [Introduction to RL](01_introduction_to_rl.ipynb) | RL basics, bandits, exploration-exploitation | 🔲 Coming Soon |
| 02 | [MDPs and Value Methods](02_mdps_and_value_methods.ipynb) | MDPs, Bellman equations, Q-learning, SARSA | 🔲 Coming Soon |
| 03 | [Policy Gradient Methods](03_policy_gradient_methods.ipynb) | REINFORCE, Actor-Critic, A2C | 🔲 Coming Soon |
| 04 | [Introduction to Multi-Agent](04_introduction_to_multi_agent.ipynb) | Multi-agent systems, game theory basics | 🔲 Coming Soon |

### Part II: MARL Foundations

| # | Notebook | Topics | Status |
|---|----------|--------|--------|
| 05 | [Stochastic Games & Nash](05_stochastic_games_nash.ipynb) | Stochastic games, Nash equilibrium | 🔲 Coming Soon |
| 06 | [Independent Learners](06_independent_learners.ipynb) | IQL, non-stationarity, convergence | 🔲 Coming Soon |
| 07 | [Centralized Training](07_centralized_training.ipynb) | CTDE, MADDPG, centralized critics | 🔲 Coming Soon |

### Part III: Advanced MARL Concepts

| # | Notebook | Topics | Status |
|---|----------|--------|--------|
| 08 | [Communication in MARL](08_communication_marl.ipynb) | CommNet, learnable communication | 🔲 Coming Soon |
| 09 | [Coordination & Cooperation](09_coordination_cooperation.ipynb) | Coordination graphs, social dilemmas | 🔲 Coming Soon |
| 10 | [Opponent Modeling](10_opponent_modeling.ipynb) | Theory of mind, best response | 🔲 Coming Soon |

### Part IV: Modern MARL Methods

| # | Notebook | Topics | Status |
|---|----------|--------|--------|
| 11 | [Value Decomposition](11_value_decomposition.ipynb) | VDN, QMIX, credit assignment | 🔲 Coming Soon |
| 12 | [Multi-Agent Actor-Critic](12_multi_agent_actor_critic.ipynb) | COMA, MAPPO, attention | 🔲 Coming Soon |
| 13 | [Advanced Topics & Applications](13_advanced_topics_applications.ipynb) | Mean-field, GNNs, real-world applications | 🔲 Coming Soon |

## 🎯 How to Use These Notebooks

1. **Sequential Learning**: Complete notebooks in order (01 → 13)
2. **Prerequisites**: Each notebook assumes knowledge from previous ones
3. **Hands-On**: Execute all code cells and complete exercises
4. **Experimentation**: Modify parameters and try variations

## 📋 Notebook Structure

Each notebook follows a consistent structure:

1. **Overview**: Learning objectives and prerequisites
2. **Motivation**: Why this topic matters
3. **Theory**: Concepts and mathematical foundations
4. **Implementation**: Step-by-step code development
5. **Experiments**: Testing and visualization
6. **Exercises**: Practice problems with solutions
7. **Summary**: Key takeaways and next steps
8. **References**: Papers and additional resources

## 🛠️ Setup

Before starting the notebooks, ensure you have:

1. Installed all dependencies:
   ```bash
   pip install -r ../requirements.txt
   ```

2. Verified your setup:
   ```bash
   python ../test_setup.py
   ```

3. Started Jupyter:
   ```bash
   jupyter notebook
   ```

## 📖 Additional Resources

- **Course Outline**: [`../docs/COURSE_OUTLINE.md`](../docs/COURSE_OUTLINE.md) - Detailed course structure
- **Setup Guide**: [`../docs/SETUP_GUIDE.md`](../docs/SETUP_GUIDE.md) - Installation help
- **Syllabus**: [`../docs/SYLLABUS.md`](../docs/SYLLABUS.md) - Course syllabus
- **Instructor Guide**: [`../docs/INSTRUCTOR_GUIDE.md`](../docs/INSTRUCTOR_GUIDE.md) - Teaching notes

## 💡 Tips for Success

- **Take Notes**: Annotate cells with your observations
- **Run Everything**: Execute cells to see outputs
- **Break Things**: Experiment and debug errors
- **Ask Questions**: Use discussions/issues for help
- **Share**: Contribute improvements back

## 🔧 Troubleshooting

Common issues and solutions:

- **Kernel crashes**: Reduce batch sizes, restart kernel
- **Import errors**: Check environment activation, reinstall packages
- **Slow training**: Reduce environment complexity, use GPU
- **Plot not showing**: Run `%matplotlib inline` at notebook start

For more help, see the [Setup Guide](../docs/SETUP_GUIDE.md).

## 🤝 Contributing

Found an error? Have a suggestion? We welcome:
- Bug reports
- Clarification requests
- Exercise additions
- Code improvements

Please open an issue or submit a pull request!

## 📜 License

All notebooks are released under the MIT License. See [../LICENSE](../LICENSE) for details.

---

**Ready to start?** Open [Notebook 01: Introduction to Reinforcement Learning](01_introduction_to_rl.ipynb) and begin your MARL journey!
