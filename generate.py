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
    q1= input("Which year were you born? ")
    for year_born in q1:
      if q1 >= 0:
        print(year_born)

    #turning 80
    q2= prompt("Would you like to find out when you will be 80?")
    prompt=input(str())
    if q2== "Yes" or 'yes':
        print(year_born+80)
    else:
        print("Thank you for playing the birthday game.")

if __name__ == '__main__':
    main()