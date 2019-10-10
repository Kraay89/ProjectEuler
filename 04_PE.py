numbers = []


def palindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False


a = b = 1

maxPalindrome = 1
top = 999
while a < top:
    for b in range(1, top+1):
        if a*b > maxPalindrome and palindrome(a*b):
            maxPalindrome = a*b
            max_a = a
            max_b = b
            print("new max: ", maxPalindrome)
        # print "b = %d" % b
    a += 1
    # print "a = %d" % a

print("Largest Palindrome is: ", maxPalindrome,
      "with factors %d and %d" % (max_a, max_b))
