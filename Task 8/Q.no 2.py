import numpy as np
a = np.random.randint(0,2,5)
print("First array:")
print(a)
b = np.random.randint(0,2,5)
print("Second array:")
print(b)
print("Testing  above two arrays are same or not!")
array_equal = np.allclose(a, b)
print(array_equal)