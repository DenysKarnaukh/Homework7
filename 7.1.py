def say_hi(name, age):
    return f"Hi. My name is {name} and I'm {age} years old"

name = input("Enter your name: ")
age = input("Enter your age: ")

age = int(age)

print(say_hi(name, age))