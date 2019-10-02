verbalise = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 
            8: 'eight', 9: 'nine', 10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen',
            14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',
            19:'nineteen', 20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',
            70:'seventy',80:'eighty',90:'ninety', 100:'hundred', 1000:'thousand'}

def num2txt(n, hyphenate=True):
    
    global verbalise
    word = ''
    digits = n%10
    tens = (n-digits)%100
    hundreds = (n-tens-digits)%1000
    
    if hundreds > 0:
        if tens > 0 and n<20:
            word += verbalise[n]
        elif tens >0
            if digits > 0:
                pass
                
    
    
    return word
#     print n, hundreds, tens, digits
#     if digits == 0:
#         if tens == 0:
#             if hundreds == 0:
#                 word += verbalise[thousands/1000] + " " + verbalise[1000]
#             else:
#                 word += verbalise[hundreds/100] + " " + verbalise[100]
#         else:
#             word
#     return word
# 
# 
print num2txt(15)





""" 
BOOOOOOOO - Screw it!!!

Using logics i found that:

first
digit   'hundred'   'and'    1-99    "thousand"
36*100 +  900*7   + 891*3 + 10*854 +      11     = 21124

"""