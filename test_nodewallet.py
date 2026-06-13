# test_nodewallet.py
"""
Tests for NodeWallet module.
"""

import unittest
from nodewallet import NodeWallet

class TestNodeWallet(unittest.TestCase):
    """Test cases for NodeWallet class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NodeWallet()
        self.assertIsInstance(instance, NodeWallet)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NodeWallet()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
