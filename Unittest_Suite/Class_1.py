import unittest

class Class_1(unittest.TestCase):
    def setUp(self):
        # print("*_" * 30)
        print("Runs before every method")
        # print("*_" * 30)

    def tearDown(self):
        # print("*_" * 30)
        print("Runs after every method")
        # print("*_" * 30)

    @classmethod
    def setUpClass(cls):
        print("*_" * 15)
        print("Runs before every class")
        print("*_" * 15)
        print()

    @classmethod
    def tearDownClass(cls):
        print("*_" * 15)
        print("Runs after every class")
        print("*_" * 15)

    def test_class1Method1(self):
        print("Class1Method1")

    def test_class1Method2(self):
        print("Class1Method2")

# if __name__=="__main__":
#     unittest.main()