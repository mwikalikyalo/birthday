from ast import Break
from urllib import response
from click import prompt

print("Hello, welcome to the birthday generator!")

def main():
  name= input("What is your name? ")
  q1= input("How old are you? ")
  age= int(q1)
  as_string= str(age)

  #age is valid
  if age <= 0:
    print("The age entered is invalid")
  else:
    print(name +",Your age is " + as_string)

  #when you were born
  q2= input("Which year were you born?")
  year_born= int(q2)
  for year in q2:
    print(year_born)
  Break
  
  #turning 80
  q1= prompt("Would you like to find out when you will be 80?")

if __name__ == '__main__':
    main()