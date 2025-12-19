#!/usr/bin/env python
"""
Test script to verify that all required packages are installed correctly.
Run this after installation to ensure your environment is ready.
"""

import sys


def test_imports():
    """Test that all required packages can be imported."""
    print("Testing package imports...")
    print(f"Python version: {sys.version}")
    print("-" * 60)
    
    tests_passed = 0
    tests_failed = 0
    
    # Core packages
    packages = [
        ("numpy", "NumPy"),
        ("matplotlib", "Matplotlib"),
        ("scipy", "SciPy"),
        ("pandas", "Pandas"),
        ("seaborn", "Seaborn"),
    ]
    
    for module, name in packages:
        try:
            mod = __import__(module)
            version = getattr(mod, "__version__", "unknown")
            print(f"✓ {name:.<30} {version}")
            tests_passed += 1
        except ImportError as e:
            print(f"✗ {name:.<30} NOT FOUND")
            print(f"  Error: {e}")
            tests_failed += 1
    
    # Jupyter
    try:
        import jupyter
        print(f"✓ {'Jupyter':.<30} installed")
        tests_passed += 1
    except ImportError:
        print(f"✗ {'Jupyter':.<30} NOT FOUND")
        tests_failed += 1
    
    # PyTorch
    try:
        import torch
        print(f"✓ {'PyTorch':.<30} {torch.__version__}")
        cuda_available = torch.cuda.is_available()
        if cuda_available:
            print(f"  → CUDA available: {torch.cuda.get_device_name(0)}")
        else:
            print(f"  → CUDA available: No (CPU only)")
        tests_passed += 1
    except ImportError as e:
        print(f"✗ {'PyTorch':.<30} NOT FOUND")
        print(f"  Error: {e}")
        tests_failed += 1
    
    # Gymnasium
    try:
        import gymnasium
        print(f"✓ {'Gymnasium':.<30} {gymnasium.__version__}")
        tests_passed += 1
    except ImportError as e:
        print(f"✗ {'Gymnasium':.<30} NOT FOUND")
        print(f"  Error: {e}")
        tests_failed += 1
    
    # PettingZoo
    try:
        import pettingzoo
        print(f"✓ {'PettingZoo':.<30} {pettingzoo.__version__}")
        tests_passed += 1
    except ImportError as e:
        print(f"✗ {'PettingZoo':.<30} NOT FOUND")
        print(f"  Error: {e}")
        tests_failed += 1
    
    # Optional packages
    print("\nOptional packages:")
    
    optional = [
        ("tensorboard", "TensorBoard"),
        ("tqdm", "tqdm"),
        ("networkx", "NetworkX"),
    ]
    
    for module, name in optional:
        try:
            mod = __import__(module)
            version = getattr(mod, "__version__", "unknown")
            print(f"✓ {name:.<30} {version}")
        except ImportError:
            print(f"  {name:.<30} not installed (optional)")
    
    # Summary
    print("\n" + "=" * 60)
    print(f"Tests passed: {tests_passed}")
    print(f"Tests failed: {tests_failed}")
    
    if tests_failed == 0:
        print("\n✓ All required packages are installed!")
        print("  You're ready to start the tutorials.")
        return True
    else:
        print("\n✗ Some packages are missing.")
        print("  Please run: pip install -r requirements.txt")
        return False


def test_basic_functionality():
    """Test basic functionality of key packages."""
    print("\n" + "=" * 60)
    print("Testing basic functionality...")
    print("-" * 60)
    
    try:
        # Test NumPy
        import numpy as np
        arr = np.array([1, 2, 3])
        assert arr.sum() == 6
        print("✓ NumPy: Array operations work")
        
        # Test PyTorch
        import torch
        tensor = torch.tensor([1.0, 2.0, 3.0])
        assert torch.sum(tensor).item() == 6.0
        print("✓ PyTorch: Tensor operations work")
        
        # Test Gymnasium
        import gymnasium as gym
        env = gym.make('CartPole-v1')
        obs, info = env.reset()
        assert obs.shape == (4,)
        env.close()
        print("✓ Gymnasium: Can create and reset environment")
        
        # Test PettingZoo
        from pettingzoo.classic import rps_v2
        env = rps_v2.env()
        env.reset()
        assert len(env.agents) > 0
        env.close()
        print("✓ PettingZoo: Can create multi-agent environment")
        
        print("\n✓ All functionality tests passed!")
        return True
        
    except Exception as e:
        print(f"\n✗ Functionality test failed: {e}")
        return False


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("MARL Tutorial Environment Setup Test")
    print("=" * 60 + "\n")
    
    imports_ok = test_imports()
    
    if imports_ok:
        functionality_ok = test_basic_functionality()
        
        if functionality_ok:
            print("\n" + "=" * 60)
            print("🎉 Setup complete! You're ready to start learning MARL.")
            print("=" * 60)
            sys.exit(0)
    
    print("\n" + "=" * 60)
    print("⚠️  Setup incomplete. Please install missing packages.")
    print("=" * 60)
    sys.exit(1)
