def getNumber(n):
    while True:
        try:
            number = int(input("Ganze Zahl " + str(n) + "    : "))
        except ValueError:
            print ("Das war keine ganze Zahl. Nochmal")
            continue
        else:
            break
    return number
    
def calculation(number1, number2):
    calcOperations = ["+", "-", "*", "/"]
    while True:
        if num2 != 0:
            calcOp = input("Wählen + - * /  : ")
        else:
            calcOp = input("Wählen + - *    : ")
        if calcOp not in calcOperations:
            print ("Keine gültige Rechenoperation. Nochmal")
        elif calcOp == "/" and num2 == 0:
            print ("Nicht durch 0 teilbar. Nochmal")
        else:
            if calcOp == "+":
                erg = number1 + number2
            elif calcOp == "-":
                erg = number1 - number2
            elif calcOp == "*":
                erg = number1 * number2
            elif calcOp == "/":
                erg = number1 / number2
            print ("Ergebis         : " + str(erg))
            break

while True:
    print ("Calculator start: ")
    num1 = getNumber(1)
    num2 = getNumber(2)
    calculation(num1,num2)
    
    restartInputList = ["y", "yes", "j", "ja"]
    restartCalculation = input("""
Nochmal?
Ja              [   y   ]
Nein            [any key]
""")
    if restartCalculation.lower() not in restartInputList:
        break

