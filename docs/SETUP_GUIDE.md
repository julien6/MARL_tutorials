# Setup Guide for MARL Tutorials

This guide will help you set up your environment to run all notebooks in the MARL tutorial series.

## System Requirements

- **Operating System**: Linux, macOS, or Windows 10/11
- **Python**: 3.8 or higher (3.9+ recommended)
- **RAM**: At least 8GB (16GB recommended for larger experiments)
- **Storage**: At least 2GB free space
- **GPU**: Optional but recommended for deep RL experiments (CUDA-compatible)

## Installation Methods

### Method 1: Using pip (Recommended for most users)

1. **Clone the repository**
   ```bash
   git clone https://github.com/julien6/MARL_tutorials.git
   cd MARL_tutorials
   ```

2. **Create a virtual environment**
   
   Using venv (built-in):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
   
   Or using conda:
   ```bash
   conda create -n marl python=3.9
   conda activate marl
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Verify installation**
   ```bash
   python -c "import gymnasium; import torch; import pettingzoo; print('All imports successful!')"
   ```

### Method 2: Using conda (Alternative)

1. **Clone the repository**
   ```bash
   git clone https://github.com/julien6/MARL_tutorials.git
   cd MARL_tutorials
   ```

2. **Create conda environment from file** (if environment.yml exists)
   ```bash
   conda env create -f environment.yml
   conda activate marl
   ```

3. **Or create manually**
   ```bash
   conda create -n marl python=3.9 numpy matplotlib scipy jupyter
   conda activate marl
   pip install torch gymnasium pettingzoo
   # Install remaining packages
   pip install -r requirements.txt
   ```

## Running Jupyter Notebooks

### Starting Jupyter

From the project root directory:

```bash
jupyter notebook
```

This will open Jupyter in your default web browser. Navigate to the `notebooks/` directory and open any notebook.

### Alternative: JupyterLab

For a more modern interface:

```bash
pip install jupyterlab  # If not already installed
jupyter lab
```

### Alternative: VS Code

If you prefer VS Code:
1. Install the Jupyter extension
2. Open the project folder in VS Code
3. Open any `.ipynb` file
4. Select your virtual environment as the kernel

## GPU Support (Optional)

### For PyTorch with CUDA

If you have an NVIDIA GPU and want to use it:

1. Check CUDA version:
   ```bash
   nvidia-smi
   ```

2. Install PyTorch with CUDA support:
   
   Visit [pytorch.org](https://pytorch.org/get-started/locally/) and use their selector, or:
   
   For CUDA 11.8:
   ```bash
   pip install torch --index-url https://download.pytorch.org/whl/cu118
   ```
   
   For CUDA 12.1:
   ```bash
   pip install torch --index-url https://download.pytorch.org/whl/cu121
   ```

3. Verify GPU is available:
   ```python
   import torch
   print(f"CUDA available: {torch.cuda.is_available()}")
   print(f"CUDA device: {torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'N/A'}")
   ```

## Environment-Specific Setup

### For Gymnasium Environments

Most classic control environments should work out of the box. For additional environment support:

```bash
# For Atari games
pip install gymnasium[atari]
pip install gymnasium[accept-rom-license]

# For MuJoCo environments (requires MuJoCo installation)
pip install gymnasium[mujoco]

# For Box2D environments
pip install gymnasium[box2d]
```

### For PettingZoo Environments

Basic installation is included in requirements.txt. For specific environment families:

```bash
# For Atari multi-agent games
pip install multi-agent-ale-py

# For classic environments
pip install pettingzoo[classic]

# For all environments (large download)
pip install pettingzoo[all]
```

## Troubleshooting

### Common Issues and Solutions

#### 1. Import errors for gymnasium/gym

**Problem**: `ModuleNotFoundError: No module named 'gym'`

**Solution**: This course uses `gymnasium` (the maintained fork of `gym`). Make sure you have:
```bash
pip install gymnasium>=0.28.0
```

If code references `gym`, update imports to `gymnasium`.

#### 2. PyTorch installation issues

**Problem**: PyTorch fails to install or runs very slowly

**Solution**: 
- Ensure you're using Python 3.8+
- Try installing from PyTorch's official wheel:
  ```bash
  pip install torch --index-url https://download.pytorch.org/whl/cpu
  ```

#### 3. PettingZoo rendering issues

**Problem**: Environments don't render or crash when rendering

**Solution**:
- Ensure you have a display server (X11 on Linux, not needed on Windows/Mac)
- For headless servers, use virtual display:
  ```bash
  pip install pyvirtualdisplay
  sudo apt-get install xvfb  # On Ubuntu/Debian
  ```

#### 4. Jupyter kernel not found

**Problem**: Jupyter can't find the virtual environment

**Solution**:
```bash
python -m ipykernel install --user --name=marl --display-name="Python (MARL)"
```

Then select the "Python (MARL)" kernel in Jupyter.

#### 5. Memory errors during training

**Problem**: Out-of-memory errors during agent training

**Solution**:
- Reduce batch size in training scripts
- Reduce replay buffer size
- Close other applications
- Use gradient accumulation for effective larger batches

#### 6. Windows-specific issues

**Problem**: Some packages fail to install on Windows

**Solution**:
- Install Visual C++ Build Tools if needed
- Use Windows Subsystem for Linux (WSL2) as alternative
- Some environments may have limited Windows support

### Getting Help

If you encounter issues not covered here:

1. **Check the notebook**: Many notebooks include troubleshooting sections
2. **Search issues**: Check the [GitHub issues](https://github.com/julien6/MARL_tutorials/issues)
3. **Create an issue**: Include:
   - Your OS and Python version
   - Full error message
   - Steps to reproduce
   - Output of `pip list`

## Testing Your Setup

Run this script to test all major dependencies:

```python
# test_setup.py
import sys
print(f"Python version: {sys.version}")

try:
    import numpy as np
    print(f"✓ NumPy {np.__version__}")
except ImportError as e:
    print(f"✗ NumPy: {e}")

try:
    import matplotlib
    print(f"✓ Matplotlib {matplotlib.__version__}")
except ImportError as e:
    print(f"✗ Matplotlib: {e}")

try:
    import torch
    print(f"✓ PyTorch {torch.__version__}")
    print(f"  CUDA available: {torch.cuda.is_available()}")
except ImportError as e:
    print(f"✗ PyTorch: {e}")

try:
    import gymnasium as gym
    print(f"✓ Gymnasium {gym.__version__}")
except ImportError as e:
    print(f"✗ Gymnasium: {e}")

try:
    import pettingzoo
    print(f"✓ PettingZoo {pettingzoo.__version__}")
except ImportError as e:
    print(f"✗ PettingZoo: {e}")

try:
    import jupyter
    print(f"✓ Jupyter")
except ImportError as e:
    print(f"✗ Jupyter: {e}")

print("\nSetup test complete!")
```

Save this as `test_setup.py` and run:
```bash
python test_setup.py
```

All checks should show ✓. If any show ✗, install the missing package.

## Development Setup (Optional)

If you plan to contribute or modify the code:

1. **Install development dependencies**
   ```bash
   pip install -r requirements-dev.txt  # If provided
   # Or manually:
   pip install black flake8 pytest mypy
   ```

2. **Set up pre-commit hooks** (if using)
   ```bash
   pip install pre-commit
   pre-commit install
   ```

3. **Run tests**
   ```bash
   pytest tests/
   ```

## Performance Optimization

### For faster training

1. **Use GPU**: See GPU Setup section above

2. **Enable cuDNN autotuner** (PyTorch):
   ```python
   import torch
   torch.backends.cudnn.benchmark = True
   ```

3. **Use vectorized environments**:
   ```python
   from gymnasium.vector import AsyncVectorEnv
   # Create multiple environments in parallel
   ```

4. **Adjust workers for data loading**:
   ```python
   # In PyTorch DataLoader
   DataLoader(..., num_workers=4)
   ```

## Next Steps

Once your environment is set up:

1. **Start with Notebook 01**: [Introduction to Reinforcement Learning](../notebooks/01_introduction_to_rl.ipynb)
2. **Follow the sequence**: Each notebook builds on previous ones
3. **Complete exercises**: Reinforce learning through practice
4. **Experiment**: Modify code and try different approaches

Happy learning!
