import unittest
class AssertsDemo(unittest.TestCase):

    def test_assertEqualDemo(self):
        a = 100
        b = 100
        self.assertEqual(a, b, "A is not equal to b")
        # will pass only if a and b are equal else message passed as argument will be displayed.

    def test_assertNotEqualDemo(self):
        a = 100
        b = 101
        self.assertNotEqual(a, b, "A is equal to b")
        # will pass only if a and b are not equal else message passed as argument will be displayed.

    def test_assertTrueDemo(self):
        a = True
        b = False
        self.assertTrue(a), "A is not true"
        # will pass only if a is True else message passed as argument will be displayed.

    def test_assertFalseDemo(self):
        a = False
        b = False
        self.assertFalse(a), "A is not False"
        # will pass only if a is False else message passed as argument will be displayed.

    def test_assertIsNoneDemo(self):
        a = None
        self.assertIsNone(a, "a is not None")
        # will pass only if a is None else message passed as argument will be displayed.

    def test_assertIsNotNoneDemo(self):
        a = 100
        self.assertIsNotNone(a, "a is not None")
        # will pass only if a is not None else message passed as argument will be displayed.

    def test_assertLessDemo(self):
        a = 100
        b = 200
        self.assertLess(a,b, "a is not less than b")
        # will pass only if a is less than b, else message passed as argument will be displayed.

    def test_assertLessEqualDemo(self):
        a = 200
        b = 200
        self.assertLessEqual(a,b, "a is not less than b")
        # will pass only if a is less than or equal to b, else message passed as argument will be displayed.

    def test_assertGreaterDemo(self):
        a = 300
        b = 200
        self.assertGreater(a,b, "a is not greater than b")
        # will pass only if a is greater than b, else message passed as argument will be displayed.

    def test_assertGreaterEqualDemo(self):
        a = 201
        b = 200
        self.assertGreaterEqual(a,b, "a is not greater than or equal to b")
        # will pass only if a is greater than or equal to b, else message passed as argument will be displayed.

    def test_assertEquals(self):
        a = 200
        b = 200
        self.assertEquals(a,b, "a is not equal to b")
        # will pass only if a is equal to b, else message passed as argument will be displayed.
        # this method is similar to assertEqual just for convenience we have two methods for same function.

    def test_assertNotEqualsDemo(self):
        a = 201
        b = 200
        self.assertNotEquals(a,b, "a is equal to b")
        # will pass only if a is not equal to b, else message passed as argument will be displayed.

    def test_assertIsInstanceDemo(self):
        a = "Arjuna"
        x = AssertsDemo()
        self.assertIsInstance(x, AssertsDemo,  "a is not an instance of class str --> String")
        # will pass only if a is an instance of the class passed as argument than or equal to b, else message
        # passed as argument will be displayed.

    def test_assertInDemo(self):
        a = 201
        b = [10,20,200,201]
        self.assertIn(a,b, "a is not part of b container")
        # will pass only if a is part of b, else message passed as argument will be displayed.

    def test_assertNotInDemo(self):
        a = 201
        b = [10,20,200,202]
        self.assertNotIn(a,b, "a is part of b container")
        # will pass only if a is not part of b, else message passed as argument will be displayed.

    def test_assertListEqualDemo(self):
        a = [10,20,200,201]
        b = [10,20,200,201]
        self.assertListEqual(a,b, "lists re not equal")
        # will pass only if both the lists are equal, else message passed as argument will be displayed.

    def test_assertIsNotDemo(self):
        a = [10,20,200,201]
        b = [10,20,200,201]
        self.assertIsNot(a,b, "object reference are equal, i.e. both variables are pointing to same object")
        # will pass only if both the variables are not pointing to the same object

    def test_assertIsNDemo(self):
        a = [10,20,200,201]
        b = [10,20,200,201]
        b = a
        self.assertIs(a,b, "both variables are pointing to same object")
        # will pass only if both the variables are pointing to the same object

    def test_assertDictEqualNotDemo(self):
        a = {1 : "a", 2 : "b"}
        b = {1 : "a", 2 : "b"}
        self.assertDictEqual(a,b, "dictionaries are not equal")
        # will pass only if both the dictionaries are equal.
if __name__ == "__main__":
    unittest.main()