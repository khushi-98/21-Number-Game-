import pandas as pd
import numpy as np 
import math 
import random

print("Hello, Welcome to the game")
name=input('enter your name:-')
print('Lets start game '+name)

print("Choose F or S to start the game")
print("Type 'F' for first turn")
print("Type 'S' for second turn")
turn=input()
game_num=[]

if turn =='F':
    while(len(game_num)<21):
      print("Your Turn")
      n=int(input('Enter the number of input you want to give'))
      a=len(game_num)
      for i in range(a+1,a+1+n):
       game_num.append(i)
      print(game_num)
      

      if (len(game_num)>20):
            print("You lose")
      else:
       print("Computer's turn")
       num1=random.randint(1,6)
    #   print(num1)
       b=len(game_num)

    #   print(a)
       if(b<21):
        for i in range(b+1,b+1+num1 ):
         game_num.append(i)
        print(game_num)
      
      if(len(game_num)>20):
            print("Computer lose")

       


elif turn =='S':
  while(len(game_num)<21):
        print("Computer's turn")
        num2=random.randint(1,6)
        b=len(game_num)
       
        for i in range (b+1,num2+1+b):
            game_num.append(i)
        print(game_num)  

        if len(game_num)>20:
              print("Computer lose")
        else:
              print("Your Turn")
            
              a=int(input("Enter the number of input you want to give"))
              c=len(game_num)

              for i in range(c+1, a+c+1):
                    game_num.append(i)
              print(game_num)

              if len(game_num)>20:
                    print("You Lose")

            
else:
   print('Invalid Input')
