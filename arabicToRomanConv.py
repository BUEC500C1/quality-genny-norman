# Gennifer Norman
# EC 500 HW 1
def prompt():
    while True:
        arabicNumInput = input('\nEnter a number in Arabic Numerals: ')
        try:
            arabicNumInput = int(arabicNumInput)
            break;
        except ValueError:
            try:
                float(arabicNumInput)
                print("\nnot a valid input, no decimals")
            except ValueError:
                print("\nnot a valid input, please enter a positive integer")
    return arabicNumInput

def conversion(arabicNumIn):
    romanNumOut = ""
    while (arabicNumIn > 0):
        checkFours = 0
        if (arabicNumIn >= 1000):
            romanNumOut += "M"
            arabicNumIn = arabicNumIn - 1000
        elif (arabicNumIn >= 500):
            romanNumOut += "D"
            romanNumOut = romanNumOut.replace("DD", "M")
            arabicNumIn = arabicNumIn - 100
        elif (arabicNumIn >= 100):
            romanNumOut += "C"
            romanNumOut = romanNumOut.replace("CCCC", "CD")
            arabicNumIn = arabicNumIn - 100
        elif (arabicNumIn >= 50):
            romanNumOut += "L"
            arabicNumIn = arabicNumIn - 50
        elif (arabicNumIn >= 10):
            romanNumOut += "X"
            romanNumOut = romanNumOut.replace("XXXX", "XL")
            arabicNumIn = arabicNumIn - 10
        elif (arabicNumIn >= 5):
            romanNumOut += "V"
            arabicNumIn = arabicNumIn - 5
        elif (arabicNumIn >= 1):
            romanNumOut += "I"
            romanNumOut = romanNumOut.replace("IIII", "IV")
            arabicNumIn = arabicNumIn - 1
        romanNumOut = romanNumOut.replace("VIV", "IX") # check for 9
        romanNumOut = romanNumOut.replace("LXL", "XC") # check for 90
        romanNumOut = romanNumOut.replace("DCD", "CM") # check for 900
    return romanNumOut


def main_loop():
    while True:
        arabicNumInput = prompt()
        romanNumOutput = conversion(arabicNumInput)
        print("\n",arabicNumInput, "in roman numerals is", romanNumOutput)
        quitChar = input('\ndo you want to quit? (y/n) ')
        if (quitChar == "y"):
            break
