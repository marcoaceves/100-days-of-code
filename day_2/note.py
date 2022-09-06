#Data Types 

#String

print('Hello'[0])
print('Hello'+" 123" + " World")
string = '123'

# int
num=123

# print(string+num) #error
print(int(string)+num) #need to convert string to int   

# float
3.123456

# boolean
True 
False



# Type Error, Type Checking and Type Conversion

# len(456)
# need to convert data type to string to get len

print(len(str(456)))


# to check a data type by placing value into type()

num = 123
num2= "123"
num3 = False
num4 =str(num)
print(type(num))
print(type(num2))
print(type(num3))
print(type(num4))



# 


# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
num1=int(two_digit_number[0])
num2=int(two_digit_number[1])
print(num1+num2)




# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
weight= float(weight)
height= float(height)

bmi = weight / (height**2)
bmi = int(bmi)
print(bmi)

pass


