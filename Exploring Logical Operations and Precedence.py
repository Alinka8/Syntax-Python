# task 6 part 1:  Validating Calculations
fruits = 10
vegatables=15
total_without_parentethes=fruits+vegatables/2
total_with_parentethes=(fruits+vegatables)/2
print(total_without_parentethes)
print(total_with_parentethes)
if total_without_parentethes == total_with_parentethes:
    print("The expressions are match")
else:
    print("The expressions are not match")



# task 6 part 2: Mix and Match
expression=(10+20)>8 or (10+30)<7
print(expression)
