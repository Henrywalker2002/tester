import sys

sys.path.append('\\tester') # Add the parent directory to the path
import unittest

from addUser import TestAddUser
from editProfile import TestEditProfile

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestEditProfile)
    unittest.TextTestRunner(verbosity=2).run(suite)