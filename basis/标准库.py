import os
print(os.getcwd()) 

# os.mkdir("dir1")
# os.chdir("dir1")
# os.system('mkdir today')

# fp = open("demo.txt","w")
# fp.write("hello moto")
# fp.close()


# import shutil
# shutil.copyfile("demo.txt","demo_copy.txt")

# shutil.move("demo_copy.txt","dir1/today")


# import glob
# print(glob.glob("*.py")) 


import re

print(re.findall(r'\bf[a-z]*','which foot or hand fell fastest')) 
print(re.sub(r'(\b[a-z]+) \1', r'\1','cat in the the hat')) 




def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
print(doctest.testmod())    # 自动验证嵌入测试



import unittest

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        self.assertRaises(ZeroDivisionError, average, [])
        self.assertRaises(TypeError, average, 20, 30, 70)

unittest.main()