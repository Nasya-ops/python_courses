"""
while True:
    pass
    if check0: continue
    if check1: break
else:
    pass

Необязательная часть else выполняются, если не произведен
выход из цикла с помощью break.

"""
import time


while True:
    time.sleep(0.0001)
    print('test')
