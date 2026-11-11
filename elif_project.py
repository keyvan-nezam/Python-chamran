while True:
    userin=input("Enter your grade between 0 and 20 or type exit: ")
    if userin.lower()=="exit":
       print("ok!goodbye")
       break
    
    try:
      grade = float(userin)
            
      if grade < 0 or grade > 20:
         print("warning!! your grade most be between 0 and 20  ")

      elif grade <= 11:
         print("Failled")
         
      elif grade <= 15:
         print("Passed")
         
      else:
         print("Grate")
         
    except ValueError:
      print("Pleas just enter a number")
