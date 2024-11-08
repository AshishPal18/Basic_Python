try:
    age = int(input('Age: '))
    print(age)
except ValueError:
    print('Invalid Value')    



try:
   age = int(input('Age : '))
   income = 20000
   risk = income / age
except ValueError:
    print('Age cannot be 0.')  
except ValueError:
    print('Invalid Value')          