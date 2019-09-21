
def fromArabic(arab):
    roman = ""

    while arab > 0:
        if arab >= 1000:
            roman += "M"
            arab -= 1000
        elif arab >= 900:
            roman += "CM"
            arab -= 900
        elif arab >= 500:
            roman += "D"
            arab -= 500
        elif arab >= 400:
            roman += "CD"
            arab -= 400
        elif arab >= 100:
            roman += "C"
            arab -= 100
        elif arab >= 90:
             roman += "XC"
             arab -= 90
        elif arab >= 50:
            roman += "L"
            arab -= 50
        elif arab >= 40:
            roman += "XL"
            arab -= 40
        elif arab >= 10:
            roman += "X"
            arab -= 10
        elif arab == 9:
            roman += "IX"
            arab -= 9
        elif arab >= 5:
            roman += "V"
            arab -= 5
        elif arab == 4:
            roman += "IV"
            arab -= 4
        elif arab < 4:
            roman += "I"
            arab -= 1
    return roman

def toArabic(roman):
    arab = 0
    last = ""
    for c in roman:
        if c == "I":
            arab += 1
        elif c == "V":
            arab += 5
            if last == "I":
                arab -= 2
        elif c == "X":
            arab += 10
            if last == "I":
                arab -= 2
        elif c == "L":
            arab += 50
            if last == "X":
                arab -= 20
        elif c == "C":
            arab += 100
            if last == "X":
                arab -= 20
        elif c == "D":
            arab += 500
            if last == "C":
                arab -= 200
        elif c =="M":
            arab += 1000
            if last == "C":
                arab -= 200
        last = c
    return arab

