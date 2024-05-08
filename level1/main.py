import sys

sys.path.append('C:\\Users\\admin\\Desktop\\BKer\\HCMUT\\HK232\\KTPM\Ass3\\tester') # Add the parent directory to the path
import unittest

from addUser import TestAddUser
from editProfile import TestEditProfile
from exportCalendar import TestExportCalendar

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestExportCalendar)
    unittest.TextTestRunner(verbosity=2).run(suite)