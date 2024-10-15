import random
var=random.randint(0,30)
print(var)
if var==15 or var==30:
    print("FizzBuzz")
elif var==5 or var==10 or var==15 or var==20 or var==25 or var==30:
    print("Buzz")
elif var==3 or var==6 or var==9 or var==12 or var==15 or var==18 or var==21 or var==24 or var==27 or var==30:
    print("Fizz")
else:
    print(var)