# convert an integer to a number phrase; TO DO: convert to roman numerals*****

x = 167

hundreds = ['one hundred', 'two hundred', 'three hundred', 'four hundred', 'five hundred', 'six hundred', 'seven hundred', 'eight hundred', 'nine hundred']
tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

hundreds_digit = x // 100
tens_digit = x // 10 % 10
ones_digit = x % 10
phrase1 = ""

if x < 100:
    if x < 10:
        print(ones[x])
    elif tens_digit == 1:
        print(teens[ones_digit])
    elif tens_digit >= 2 and tens_digit <= 9:
        if ones_digit > 0:
            print(tens[tens_digit - 2], ones[ones_digit])
        else:
            print(tens[tens_digit - 2])
else:
    print(hundreds[hundreds_digit - 1],tens[tens_digit - 2], ones[ones_digit] )



