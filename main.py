import random
import time
from decimal import Decimal
def menu():
  challenge = input("[1]VAT\n[2]Darts\n[3]Snake Eyes\n[q]Quit\n ")
  if challenge == "1":
    item = input("Enter the price of an item: ")
    InitVat(item)
  elif challenge == "2":
    InitDarts()
  elif challenge == "3":
    InitSnake()
  elif challenge.lower() == "q":
    return
  else:
    print("Invalid choice, try again.")
    menu()
def InitVat(price):
  tdp = Decimal(10) ** -2
  try:
    price = float(price)
  except Exception:
    print("Invalid price, please try again.")
    menu()
  price = price * 0.2
  price = Decimal(price).quantize(tdp)
  print(f"You must pay £{price} as VAT.")
  menu()
def InitDarts():
  score = 501
  print("New game. Player starts at 501 points.")
  while score != 0:
    total = input("Enter the total from 3 darts: ")
    if total == "q":
      menu()
      return
    try:
      total = int(total)
    except Exception:
      print("Invalid total, please try again.")
      continue

    score = score - total
    if score >= 1:
      print(f"Your score is: {score}")
    elif score == 0:
      print("YOU WIN!")
      menu()
    else:
      print("BUST!")
      score = score + total
  
def roll(player):
  score = random.randint(1,6)
  print(f"Player {player} rolls {score}!")
  return score
def InitSnake():
  try:
    players = int(input("Enter the number of players: "))
  except Exception:
    print("Invalid number, please try again.")
    InitSnake()
  bank = [0]*players
  while [i for i,value in enumerate(bank) if value >= 100] == []:#Every value in bank is compared to 100
    print(bank)#and if it is equal or higher then it means there are no winners
    for i in range(0,len(bank)):
      gamble = "G"
      score = 0
      while gamble.upper() == "G":
        print(bank)
        gamble = "B"
        
        num1 = roll(i+1)
        num2 = roll(i+1)
        print(f"Player {i+1} rolls {num1+num2} in total!")
        if num1 == 1 and num2 ==1:
          print("TOO BAD!\nScore and Bank are now 0.")
          bank[i] = 0
          score = 0
          continue
        elif num1==1 or num2 == 1:
          print("Too bad.\n Score is now 0.")
          score = 0
          continue
        else:
          score += num1 + num2
          print(f"Your score is: {score}")
          gamble = input(f"Does player {i+1} want to:\n [G]Gamble\n [B]Bank\n")
          if gamble.upper() == "G":
            continue
          elif gamble.upper() == "B":
            bank[i] += score
            print(f"Banked points : {bank[i]}")
            if bank[i] >= 100:
              print("The winner is:")
              for i in range(0,3):
                time.sleep(1)
                print("...")
              print(f"PLAYER {i}!!! Score: {bank[i-1]}")
              menu()
              exit()
            continue
          else:
            print("Invalid option, defaulting to bank.")
            bank[i] += score
            print(f"Banked points : {bank[i]}")
            if bank[i] >= 100:
              print("The winner is:")
              for j in range(0,3):
                time.sleep(1)
                print("...")
              print(f"PLAYER {i+1}!!! Score: {bank[i]}")
              menu()
              exit()
            continue

menu()
