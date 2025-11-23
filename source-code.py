import random as rd
print("---------------------------------------------------------------------------------------------")
print("WELCOME TO THE NUMBER GUESSING GAME")
print("Rules: ")
print("1. There are 5 guesses")
print("2. The number is between 0 to 100")
print("3.If the guess is wrong, then the message will be given whether the number is less or high")
print("4.If the guess is correct,a message will be given")
print("Lets Start the Game")
print("---------------------------------------------------------------------------------------------")
c='y'
while c=='y':
  a=rd.randint(0,100)
  for i in range(5,0,-1):
    guess=int(input("Enter your guess(0-100): "))
    if guess<a:
      print("The number is less.Please Try a greater number.")
      print(i-1," tries left")
      if i-1==0:
        print("Sorry.You Lost")
        print("The Number was: ",a)
        break
      continue
    elif guess>a:
      print("The number is greater.Please Try a lesser number.")
      print(i-1," tries left")
      if i-1==0:
        print("Sorry.You Lost")
        print("The Number was: ",a)
      continue
    elif guess==a:
      print("CONGRATULATIONS!!!")
      print("You have guessed the number right and the number is: ",guess)
      break
    else:
      print("Sorry.You Lost")
      print("The Number was: ",a)
      break


  c=input('Do You Wish to Play Again(y/n)')

print("---------------------------------------------------------------------------------------------")
print("THANK YOU FOR PLAYING")
print("---------------------------------------------------------------------------------------------")
