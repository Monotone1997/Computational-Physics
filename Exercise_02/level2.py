import time
import math
import sys
import os
#module above
x='1'
d={'1':' '}
for x in range(2):
    for k in range(0,60):
        i=os.system('cls')        
        print ('\n')*int(math.pow((k-30),2)*0.02+2)   
        print d['1']*int(math.fabs(k)),'#####   #    #  #####'
        print d['1']*int(math.fabs(k)),'   #     #  #   #'
        print d['1']*int(math.fabs(k)),'  #        #    ####'
        print d['1']*int(math.fabs(k)),' #         #    #'
        print d['1']*int(math.fabs(k)),'#####      #    #'      
        time.sleep(0.06)
        #define the motion   
i=os.system('cls') 
print('Thanks for watching')
