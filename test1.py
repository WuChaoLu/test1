# -*- coding: utf-8 -*-

import time
start = time.time()
fib = []
for i in range(1000):
    if (i < 2):
        fib.append(i)
    else:
        fib.append(fib[i -2 ]+ fib[i-1])
else:
    print(fib)
print(time.time()-start)
   
#sudo()

def sudo():
    ''' this is a test function. '''
    print("這是測試。")