# Quick Start Guide

Get started with the MARL Tutorial in 5 minutes!

## ⚡ Quick Setup

### Option 1: Local Installation (Recommended)

```bash
# Clone the repository
git clone https://github.com/julien6/MARL_tutorials.git
cd MARL_tutorials

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Verify installation
python test_setup.py

# Launch Jupyter
jupyter notebook
```

Then open `notebooks/01_introduction_to_rl.ipynb` and start learning!

### Option 2: Google Colab (No Installation)

1. Go to [Google Colab](https://colab.research.google.com/)
2. File → Open Notebook → GitHub
3. Enter: `julien6/MARL_tutorials`
4. Open any notebook
5. Run the first cell to install dependencies

## 📖 Learning Path

### Week 1: RL Foundations
- **Notebook 01**: [Introduction to RL](notebooks/01_introduction_to_rl.ipynb)
  - Learn the RL basics
  - Implement multi-armed bandits
  - Understand exploration vs exploitation

### Week 2: Value-Based Methods
- **Notebook 02**: [MDPs and Value Methods](notebooks/02_mdps_and_value_methods.ipynb)
  - Master Q-learning
  - Understand Bellman equations
  - Solve GridWorld

### Week 3: Policy Gradients
- **Notebook 03**: [Policy Gradient Methods](notebooks/03_policy_gradient_methods.ipynb)
  - Learn REINFORCE
  - Implement Actor-Critic
  - Train on CartPole

### Week 4: Multi-Agent Basics
- **Notebook 04**: [Introduction to Multi-Agent](notebooks/04_introduction_to_multi_agent.ipynb)
  - Understand multi-agent challenges
  - Learn game theory basics
  - Build multi-agent environments

### Weeks 5-13: Advanced MARL
Continue through notebooks 05-13 to master:
- Independent learning
- Centralized training
- Communication
- Coordination
- Value decomposition (QMIX)
- Modern methods (MAPPO)

## 🎯 What You'll Build

By the end of this course, you'll have implemented:

1. **Classic RL Algorithms**
   - Q-learning, SARSA
   - REINFORCE, A2C

2. **MARL Algorithms**
   - Independent Q-Learning (IQL)
   - MADDPG
   - QMIX
   - MAPPO

3. **Applications**
   - Multi-agent navigation
   - Cooperative tasks
   - Competitive games
   - Communication protocols

## 💡 Quick Tips

- **Complete in order**: Each notebook builds on previous ones
- **Run all cells**: Execute code to understand behavior
- **Experiment**: Change parameters and observe effects
- **Do exercises**: Practice reinforces learning
- **Visualize**: Plots help intuition
- **Ask questions**: Use GitHub issues for help

## 🆘 Common Issues

**Import Error?**
```bash
pip install -r requirements.txt --upgrade
python test_setup.py
```

**Slow Training?**
- Reduce environment size
- Decrease batch size
- Use GPU if available

**Results Differ?**
- Set random seeds
- Check hyperparameters
- Verify package versions

## 📚 Resources

- **Course Outline**: [docs/COURSE_OUTLINE.md](docs/COURSE_OUTLINE.md)
- **Setup Help**: [docs/SETUP_GUIDE.md](docs/SETUP_GUIDE.md)
- **FAQ**: [docs/FAQ.md](docs/FAQ.md)
- **References**: [docs/REFERENCES.md](docs/REFERENCES.md)

## 🎓 For Instructors

Teaching this course?
- **Syllabus**: [docs/SYLLABUS.md](docs/SYLLABUS.md)
- **Instructor Guide**: [docs/INSTRUCTOR_GUIDE.md](docs/INSTRUCTOR_GUIDE.md)

## 🤝 Contributing

Found an issue? Want to improve something?
See [CONTRIBUTING.md](CONTRIBUTING.md)

## 📧 Get Help

- **Issues**: For bugs and questions
- **Discussions**: For general MARL topics
- **Pull Requests**: For contributions

---

## Ready to Start?

🚀 **Open [Notebook 01](notebooks/01_introduction_to_rl.ipynb) and begin your MARL journey!**

---

**Time to First Code**: Less than 5 minutes with Colab  
**Time to First Agent**: Complete Notebook 01 (~4 hours)  
**Time to MARL Expert**: Complete all notebooks (~12 weeks)

*Happy Learning!* 🎉
