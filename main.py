from logo import logo
import os

def add(n1,n2):
  return n1+n2
def multiply(n1,n2):
  return n1*n2
def divide(n1,n2):
  return n1/n2
def subtract(n1,n2):
  return n1-n2


operations={
  "+":add,
  "*":multiply,
  "/":divide,
  "-":subtract,
}
def calculater():
  
  print(logo)
  
  first_number=float(input("enter the first number: "))
  calculation_done=False
  while calculation_done==False:
      
      
      for operation  in operations:  
       print(operation)
      
      operation=input(" chos an operation : ")
      second_number=float(input("enter the second number: "))
      if operation in operations:
        wanted_operation=operations[operation]
        anser=round(wanted_operation(first_number,second_number))
        print(f"{first_number} {operation} {second_number} = {anser}")
      continue_calculating=input(f"do you want to continue calculatin with {anser}? type y or n ")
      if continue_calculating=="n":
        calculation_done=True
        os.system('clear')
        calculater()
      else:
        first_number=anser
        os.system('clear')


calculater()














