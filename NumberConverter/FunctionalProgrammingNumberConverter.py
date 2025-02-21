from functools import reduce

hex = "01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(hex.index("Z"))

def convertToDecimal(number,base):
    number_list = list(map(int,str(number)))
    power_list = list(reversed(range(0,len(number_list))))

    calculateDecimal = lambda x,y : x*base**y
    mySum = lambda x,y: x+y
    return reduce(mySum, map(calculateDecimal, number_list, power_list))

print(convertToDecimal(11111111,2))

def convertDecimalToBase(decimal, base):
    
    
