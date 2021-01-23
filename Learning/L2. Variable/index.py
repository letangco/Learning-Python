x = 5
y = 'Le Tang Co'
z = 8.0
print(x, y, z)
# type of variable
print(type(x))
print(type(y))
print(type(z))

# Name of variable 
# 1. Camel case
myVariableName = 'John'
print(myVariableName)
# 2. Pascal Case
MyVariableName = 'John Pascal'
print(MyVariableName)
# 3. Snake case
my_variable_name = 'John Snake case'
print(my_variable_name)

# Assign multiple value
Cam, Chuoi, Cherry = "Orange", "Banana", "Cherry"
print(Cam)
print(Chuoi)
print(Cherry)

Ti = Teo = Mao = Dan = '1m80'
print (Ti, Teo, Dan, Mao)

food = ['apple', 'tomato', 'watermelon', 1]
tao, ca_chua, dua_hau, numberOne = food
print(tao, ca_chua, dua_hau, numberOne)
print(food)

# Global Variables
material = 'awesome'

def myFunction(x):
    print('Python is '+ x)

myFunction(material)