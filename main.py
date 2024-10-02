from replit import clear
from game_data import data
import random
from art import logo,vs

print(logo)
def rand_generator():
  dice=random.randint(0,50)
  return dice
      
  
score = 0
a=rand_generator()
A = f"Compare A : {data[a]['name']}, a {data[a]['description']}, from {data[a]['country']}"
print(A)
print(vs)
b=rand_generator()
while(a==b):
  if(a==b):
    b=rand_generator()
B = f"Against B : {data[b]['name']}, a {data[b]['description']}, from {data[b]['country']}"
print(B)
again = True
while(again):
  Option = input("Who has more followers. Type 'A' or 'B': ")
  clear()
  print(logo)
  #compare(a,b,score,Option,again)
  if(Option == 'A'):
    if(data[a]['follower_count']>data[b]['follower_count']):
      #count(score)
      score+=1
      print(f"You are right! Current Score : {score}")
      a=b
      again=True
    else:
      again=False
      clear()
      print(logo)
      print(f"Sorry that's wrong. Final Score : {score}")
  else:
    if(data[a]['follower_count']<data[b]['follower_count']):
      score+=1
      print(f"You are right! Current Score : {score}")
      a=b
      again = True
    else:
      again = False
      clear()
      print(logo)
      print(f"Sorry that's wrong. Final Score : {score}")
  
  if(again==True):
    A = f"Compare A : {data[a]['name']}, a {data[a]['description']}, from {data[a]['country']}"
    print(A)
    print(vs)
    b=rand_generator()
    while(a==b):
      if(a==b):
        b=rand_generator()
    B = f"Against B : {data[b]['name']}, a {data[b]['description']}, from {data[b]['country']}"
    print(B)
    
  
  

