'''
compute power of a^b where b can be -ve or +ve without using the math module

'''

def powerneg(a,b):
    if(b>0):
        return 0 #error
    elif(b==0):
        return 1
    else:
        return (1/a)*powerneg(a,b+1)
def powerpos(a,b):
    if(b<0):
        return 0 #error
    elif(b==0):
        return 1
    else:
        return a*powerpos(a,b-1)
    
def power(a,b):
    if(b<0):
        return powerneg(a,b)
    else:
        return powerpos(a,b)
print(power(2,0))
