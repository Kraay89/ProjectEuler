
natural_numbers = range(1,101)
natural_numbers_squares = [i**2 for i in natural_numbers]
natural_numbers_squares_sum = sum(natural_numbers_squares)
natural_numbers_sums_square = sum(natural_numbers)**2

print "The natural numbers are:", natural_numbers
print "The squares of the natural numbers are: ", natural_numbers_squares
print "The sum of the squares of the natural numbers is: ", natural_numbers_squares_sum
print "The square of the sums of the natural numbers is: ", natural_numbers_sums_square
print "the difference is %d - %d = %d" % (natural_numbers_sums_square, 
    natural_numbers_squares_sum, natural_numbers_sums_square-natural_numbers_squares_sum)
