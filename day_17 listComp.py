num=[1,-2,-3,-4,5,-6,7,8]
positive_numbers=[number for number in num if number>=0]
negative_numbers=[number for number in num if number<0]
even_num=[number for number in num if number%2==0]
odd_num=[number for number in num if number%2==1]
print(positive_numbers)
print(negative_numbers)
print(even_num)
print(odd_num)