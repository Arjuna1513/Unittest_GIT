import unittest
from Unittest_Suite.Class_1 import Class_1
from Unittest_Suite.Class_2 import Class_2

cl1 = unittest.TestLoader().loadTestsFromTestCase(Class_1)
cl2 = unittest.TestLoader().loadTestsFromTestCase(Class_2)

sanity_suite = unittest.TestSuite([cl1, cl2])
unittest.TextTestRunner().run(sanity_suite)

"""
In the above we have first imported the classes and then 
we have loaded all the tests from each class and then put them in a suite using TestLoader()
and then we have created a suite using the list of suites using TestSuite()
unittest.TestSuite([suite1, suite2])

 and then we have run that suite using unittest.TextTestRunner().run(suiteName)

"""