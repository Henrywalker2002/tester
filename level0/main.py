import sys 

sys.path.append('D:\project\\tester') # Add the parent directory to the path
import unittest
from addUser import TestAddUser


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAddUser)
    unittest.TextTestRunner(verbosity=2).run(suite)
