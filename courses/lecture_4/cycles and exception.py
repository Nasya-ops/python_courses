"""Cycles, try...except block, lambdas"""

import os
import sys
import tracemalloc
from datetime import datetime



class Employee(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age


tracemalloc.start()

try:
    # sys.exit()        #finally will be executed
    # os._exit(1)       #finally will not work
    '''while True:
        a=1
    '''  # finally will have never been executed
    emp1 = Employee("Daniel", 24, 65)

except TypeError as err:
    print(f"Unexpected {err=},{type(err)=}")
else:
    set_check = set()
    list_1 = [2, 'Hello', emp1]
    for i in list_1:
        set_check.add(i)
    print(set_check)
finally:
    print("I will work anyway")

start_time = datetime.now()

lambda_in_lambda = lambda x, y, z, func1: x ** func1(y, z)
print(f"((x)^y)^z -> {lambda_in_lambda(2, 3, 2, lambda y, z: y ** z)}")

print(f"\nPython try...except performance:\nTime -> {datetime.now() - start_time}"
      f"\nMemory -> Current: %d, Peak %d" % tracemalloc.get_traced_memory(),
      )
