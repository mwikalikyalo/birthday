print("Hello, welcome to the birthday generator!")

def main():
  name= input("What is your name? ").capitalize()
  q1= int(input("How old are you? "))
  as_string= str(q1)

  #age is valid
  if q1 <= 0:
    print("The age entered is invalid")
  else:
    print(name +",Your age is " + as_string)

  #when you were born
  q3= int(input("Which year were you born? "))
  if q3 >= 0:
      print(q3)
  else:
      print("There is an error in the age you entered.")
  
  #when you will turn 80      
  q2= input("Would you like to find out when you will be 80?").capitalize()
  if q2== "Yes":
      print(q3+80)
  else:
      print("Thank you for playing the birthday game.")

if __name__ == '__main__':
    main()