for i in range(1,101):
  //see if its divisable by 3 and 5
  if(i%3==0 and i%5==0):
    print("FizzBuzz")
    //see if number is divisable 3
  elif(i%3 == 0):
    print("Fizz")
    //see if number is divisable by 5
  elif(i%5 == 0):
    //if number is not divisable by three or four print number
    print("Buzz")
  else:
    print(i)
