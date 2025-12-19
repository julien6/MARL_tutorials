# Frequently Asked Questions (FAQ)

## General Questions

### Q: What are the prerequisites for this course?

**Required:**
- Basic Python programming (functions, classes, loops)
- Linear algebra fundamentals (vectors, matrices, matrix multiplication)
- Basic probability and statistics
- Calculus basics (derivatives, gradients)

**Helpful but not required:**
- Machine learning background
- Neural networks knowledge
- Prior RL experience

### Q: How long does the course take?

The full course is designed for 12-13 weeks with approximately 4-6 hours per week. However:
- **Self-paced**: Take as long as you need
- **Intensive**: Can complete core material in 8 weeks
- **Extended**: Can spread over 16 weeks with deeper exploration

### Q: Do I need a GPU?

**No, but it helps.** 
- Most exercises work fine on CPU
- Later notebooks benefit from GPU acceleration
- Cloud options available (Google Colab, Kaggle)

### Q: Can I use this for self-study?

**Absolutely!** The course is designed to be self-contained:
- All theory is explained in notebooks
- Code examples are provided
- Exercises include hints and solutions
- No instructor required (though community discussion helps)

## Installation and Setup

### Q: I'm getting import errors. What should I do?

1. **Check environment activation:**
   ```bash
   # Activate your virtual environment
   source venv/bin/activate  # or: conda activate marl
   ```

2. **Verify installation:**
   ```bash
   python test_setup.py
   ```

3. **Reinstall if needed:**
   ```bash
   pip install -r requirements.txt --upgrade
   ```

### Q: How much disk space do I need?

- **Minimum**: 2 GB for packages and dependencies
- **Recommended**: 5 GB to include saved models and results
- **Cloud alternative**: Use Google Colab (free, no local storage needed)

### Q: Can I use Windows?

**Yes!** The course works on Windows, but:
- Use Windows 10 or later
- Some packages may require Visual C++ Build Tools
- Consider using WSL (Windows Subsystem for Linux) for better compatibility
- Or use cloud platforms like Google Colab

## Course Content

### Q: Should I complete notebooks in order?

**Yes, strongly recommended.** Each notebook builds on previous ones:
- Concepts are introduced progressively
- Code reuses earlier implementations
- Exercises assume prior knowledge

Exception: If you're already familiar with single-agent RL, you might skim Notebooks 1-3.

### Q: How challenging are the exercises?

Exercises are marked by difficulty:
- ⭐ **Basic**: Test understanding of concepts (everyone should complete)
- ⭐⭐ **Intermediate**: Implement variations (recommended)
- ⭐⭐⭐ **Advanced**: Extensions and research-level (optional but valuable)

### Q: Are there solutions to exercises?

- Basic exercises: Solutions provided in notebooks (hidden by default)
- Intermediate: Hints provided, some solutions in separate file
- Advanced: Often open-ended, multiple valid solutions

### Q: Can I skip notebooks?

**Not recommended**, but if pressed for time:
- **Core notebooks** (must complete): 01, 02, 03, 04, 06, 07, 11, 12
- **Important but can skim**: 05, 09
- **Can skip if time-limited**: 08, 10, 13 (but valuable for depth)

### Q: What if I get stuck?

1. **Re-read explanations**: Sometimes a second read helps
2. **Run code cell by cell**: See what each part does
3. **Check documentation**: Links to papers and docs provided
4. **Search online**: Many concepts have great blog posts
5. **Ask for help**: Open an issue or use discussion forum
6. **Take a break**: Sometimes stepping away helps

## Technical Questions

### Q: Why use Gymnasium instead of Gym?

Gymnasium is the maintained fork of OpenAI Gym:
- More active development
- Better documentation
- Fixes for deprecated features
- Compatible API

### Q: Can I use TensorFlow instead of PyTorch?

The notebooks use PyTorch, but concepts are framework-agnostic:
- You can translate to TensorFlow if you prefer
- Core algorithms work in any framework
- PyTorch chosen for simplicity and research use

### Q: My training is very slow. How can I speed it up?

1. **Reduce environment complexity**: Smaller grids, fewer agents
2. **Reduce batch size**: Trade memory for speed
3. **Use GPU**: If available
4. **Vectorize environments**: Run multiple in parallel
5. **Reduce logging frequency**: Less overhead
6. **Profile code**: Find bottlenecks

### Q: Why do my results differ from the notebook?

Common reasons:
- **Random seeds**: Set seeds for reproducibility
- **Hyperparameters**: Small changes can have big effects
- **Environment versions**: Update to match requirements.txt
- **Hardware differences**: GPU vs CPU can differ slightly
- **Stochasticity**: RL has inherent randomness

## Algorithms and Theory

### Q: Why do we start with single-agent RL?

MARL builds directly on single-agent RL:
- Most algorithms extend single-agent methods
- Understanding value functions and policy gradients is essential
- Many MARL challenges relate to single-agent concepts
- Progressive learning: simple to complex

### Q: What's the difference between IQL and QMIX?

**IQL (Independent Q-Learning)**:
- Each agent learns independently
- Treats other agents as environment
- Simple but non-stationary
- Works in some cases

**QMIX**:
- Centralized training, decentralized execution
- Factorizes joint Q-value
- Credit assignment through mixing network
- More complex but better coordination

### Q: When should I use which algorithm?

**General guidelines:**
- **Fully cooperative + shared reward**: QMIX or MAPPO
- **Competitive**: MADDPG or self-play
- **Mixed cooperative-competitive**: MADDPG
- **Simple + quick**: IQL (surprisingly effective)
- **Scalability**: MAPPO (handles many agents well)

### Q: Why is MARL harder than single-agent RL?

Key challenges:
1. **Non-stationarity**: Other agents change the environment
2. **Credit assignment**: Which agent caused the outcome?
3. **Scalability**: Exponential growth in joint action space
4. **Partial observability**: Agents may not see everything
5. **Coordination**: How to cooperate without communication?

### Q: What is CTDE (Centralized Training, Decentralized Execution)?

**Centralized Training**:
- Use global information during training
- Learn with full observability
- Coordinate learning

**Decentralized Execution**:
- Each agent acts on local observations
- No communication needed at test time
- Scalable deployment

**Why?**: Get benefits of coordination during training while maintaining practical execution.

## Projects and Applications

### Q: Can I use this for my research?

**Yes!** The course is designed to prepare you for MARL research:
- Implementations are research-quality
- References to recent papers
- Extensions suggested in exercises
- Foundation for novel algorithms

### Q: What are good final project ideas?

1. **Novel Algorithm**: Implement recent paper
2. **Application**: Apply MARL to new domain
3. **Comparative Study**: Systematic algorithm comparison
4. **Extension**: Add mechanism to existing algorithm
5. **Theoretical**: Analyze convergence or sample complexity

See Syllabus for detailed project guidelines.

### Q: Where is MARL used in practice?

**Current applications:**
- Autonomous vehicles (coordination)
- Robotics (multi-robot systems)
- Game AI (StarCraft, Dota, poker)
- Traffic control (smart cities)
- Energy management (smart grids)
- Network routing
- Financial trading

## Learning Tips

### Q: How can I learn most effectively?

**Best practices:**
1. **Active learning**: Run and modify code
2. **Take notes**: Annotate notebooks with your insights
3. **Visualize**: Plot everything you can
4. **Experiment**: Try different parameters
5. **Break things**: Debug to understand
6. **Teach others**: Explaining solidifies understanding
7. **Connect concepts**: Link to what you already know

### Q: Should I read the referenced papers?

**Recommended but not required:**
- Papers provide deeper understanding
- See original motivations and experiments
- Learn research methodology
- Good for projects and research

**Strategy:**
- Skim abstracts and introductions
- Focus on algorithms and results
- Deep read for topics of special interest

### Q: How do I stay updated after the course?

1. **Follow conferences**: NeurIPS, ICML, ICLR, AAMAS
2. **Read surveys**: Periodic MARL surveys
3. **ArXiv**: Search "multi-agent reinforcement learning"
4. **Twitter/X**: Follow MARL researchers
5. **GitHub**: Watch MARL repositories
6. **Join community**: MARL reading groups

## Contributing and Community

### Q: Can I contribute to the course?

**Yes, please!** Contributions welcome:
- Fix errors or typos
- Improve explanations
- Add exercises
- Enhance visualizations
- Share extensions

See CONTRIBUTING.md for guidelines.

### Q: How do I report bugs?

Open an issue on GitHub with:
- Description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Environment details (OS, Python version, etc.)

### Q: Can I share my solutions?

**Yes!** Sharing helps everyone:
- Post in discussions
- Create blog posts
- Share on social media
- Contribute back to repo

Please mark spoilers for exercises!

## Career and Further Learning

### Q: What jobs use MARL?

- **Research Scientist**: Academia or industry research
- **ML Engineer**: Implementing MARL systems
- **Robotics Engineer**: Multi-robot coordination
- **Game AI Developer**: Intelligent agents in games
- **Autonomous Systems**: Self-driving cars, drones
- **Optimization Specialist**: Resource allocation problems

### Q: What should I learn next?

**To deepen MARL:**
- Read recent papers
- Implement novel algorithms
- Work on real applications
- Contribute to open-source

**Related areas:**
- Deep reinforcement learning
- Game theory
- Multi-agent systems
- Distributed systems
- Optimization

### Q: Is MARL research active?

**Very active!** Growing rapidly:
- Hundreds of papers per year
- New applications emerging
- Improved algorithms regularly
- Open challenges remaining

Good time to get involved!

## Still Have Questions?

- **GitHub Issues**: For course-related questions
- **Discussions**: For general MARL questions
- **Email**: Contact maintainers for specific concerns

---

**Happy Learning! 🚀**
