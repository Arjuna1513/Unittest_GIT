import unittest
import sys
from UnitTestPackage.screen_shot import ScreenShot
from selenium import webdriver
import inspect


class UnitTestEx1(unittest.TestCase):
    driver = webdriver.Firefox()

    def setUp(self):
        print("I run before every test method")

    def tearDown(self):
        print("I run after every test method")
        if sys.exc_info()[0]:
            ScreenShot().take_screen_shot(inspect.stack()[0][3], self.driver)



    def test_method1(self):
        print("I am the test method1")

    def test_method2(self):
        print("I am the test method2")

    def test_method3(self):
        print("I am the test method3")
        self.assertEqual(8, 9)

    @classmethod
    def setUpClass(cls):
        print("*" * 50)
        print("I run once before the class starts execution")
        print("*" * 50)
        print()

    @classmethod
    def tearDownClass(cls):
        print("*" * 50)
        print("I run once after the class execution stops")
        print("*" * 50)


if __name__ == "__main__":
    unittest.main(verbosity=51)


"""
import unittest, this is similar to testng in java.
setUp=beforeMethod
tearDown=afterMethod
setUpClass=BeforeClass
tearDownClass=AfterClass

u need to extend TestCase class that is present in unittest Module to use all the
unittest methods like mentioned above.
"""