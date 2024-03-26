#coding = utf-8
import unittest
import os

#运行所有case, 当作所有程序的主入口

class RunCase(unittest.TestCase):
    def testcase01(self):
        case_path = os.path.join(os.getcwd(), 'testcase')
        suite = unittest.defaultTestLoader.discover(case_path, 'unitcase_*.py')
        unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    unittest.main()

