import random
from enum import Enum
from decimal import Decimal

class OperationType(Enum):
    PLUS = 0
    MINUS = 1
    MULTIPLY = 2
    DIVIDE = 3

pairs = {
    OperationType.PLUS: "+",
    OperationType.MINUS: "-",
    OperationType.MULTIPLY: "x",
    OperationType.DIVIDE: "÷",
}

def level01() :
    count = 0

    while (count < 10):
        sign = OperationType(random.randrange(0, 2))

        if sign == OperationType.PLUS:
            values = __creat2Values(20, 20)
            value1 = values[0]
            value2 = values[1]
            result = Decimal(value1) + Decimal(value2)
        elif sign == OperationType.MINUS:
            values = __creat2Values(20, 20)
            value1 = values[0]
            value2 = values[1]
            result = Decimal(value1) - Decimal(value2)

        print(str(value1) + " " +  pairs[sign] + " " + str(value2) + " = " + str(result))
        count += 1

def level02() :
    count = 0

    while (count < 10):
        sign = OperationType(random.randrange(0, 3))

        if sign == OperationType.PLUS:
            values = __creat2Values(30, 30)
            value1 = values[0]
            value2 = values[1]
            result = Decimal(value1) + Decimal(value2)
        elif sign == OperationType.MINUS:
            values = __creat2Values(30, 30)
            value1 = values[0]
            value2 = values[1]
            result = Decimal(value1) - Decimal(value2)
        elif sign == OperationType.MULTIPLY:
            values = __creat2Values(10, 10)
            value1 = values[0]
            value2 = values[1]
            result = Decimal(value1) * Decimal(value2)

        print(str(value1) + " " +  pairs[sign] + " " + str(value2) + " = " + str(result))
        count += 1
    
def level03() :
    count = 0

    while (count < 10):
        sign = OperationType(random.randrange(0, 4))

        if sign == OperationType.PLUS:
            values = __creat2Values(40, 40)
            value1 = values[0]
            value2 = values[1]
            result = Decimal(value1) + Decimal(value2)
        elif sign == OperationType.MINUS:
            values = __creat2Values(40, 40)
            value1 = values[0]
            value2 = values[1]
            result = Decimal(value1) - Decimal(value2)
        elif sign == OperationType.MULTIPLY:
            values = __creat2Values(20, 10)
            value1 = values[0]
            value2 = values[1]
            result = Decimal(value1) * Decimal(value2)
        elif sign == OperationType.DIVIDE:
            values = __creat2Values(40, 10)
            value1 = values[0]
            value2 = values[1]
            result = Decimal(value1) / Decimal(value2)

        if (str(result).__contains__(".")):
            continue
        else:
            print(str(value1) + " " +  pairs[sign] + " " + str(value2) + " = " + str(result))
            count += 1

def __creat2Values(max1: int, max2: int) -> tuple[int]: 
        tmp1 = random.randrange(1, max1 + 1)
        tmp2 = random.randrange(1, max2 + 1)

        if tmp2 <= tmp1:
            value1 = tmp1
            value2 = tmp2
        else :
            value1 = tmp2
            value2 = tmp1

        return (value1, value2)