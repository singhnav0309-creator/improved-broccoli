def fact_rec(num):
   if num == 1:
      return 1
   else:
       factorial = num * fact_rec(num -1)
       return factorial

num = int(input("Enter a number: "))
print(f"Factorial of {num} is: {fact_rec(num)}")


""" We take a number as an arguement for fact_rec function
if number is equal to 1, it returns 1
otherwise, it returns factorial of the number.
return None """

print(fact_rec)





