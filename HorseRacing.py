import random
import time
import sys
import os

money = 7500

horsenames = {
  "Names":"Tigre Moon Stallion Vagabond Morning Feet Calua Flight Sparkle Rainstone Hustle Zani Navajo Wallflower Pendragon Icabob Gabriella Kalahari Rage Verdun Jo Sweet Dreams IceDrop Felicity Promise Mistro Shadowfax Penny Kystie Shadow Stallion Nightflash Dawson Shiver Sniper Allegro Toric Apache Roxy Bramble Torch Wild Stallion Lightningheart Applejax Vegas Thunderbird Katareena Juno Thunder Step Licorice Morning Ranger Gallamist Nightmane Quincy Keno Flight Blossom Century Ty Kalita Karana Altair Juniper Haughty Leonardo".split(),
}
def StartScreen(money):
  if money == 0:
    print("You have zero money brokie, take this 2500 as a gift...")
    money = 2500
  print("-----E P I C HorseRacing-----")
  print("Pick A difficulty!")
  print("1 - Easy, 3 horses")
  print("2 - Medium, 5 horses")
  print("3 - Hard, 7 horses")
  print("4 - Extreme, 10 horses")
  print(f"Current money: {money}")
  print("-----------------------------")
  try:
    diffi = int(input("- "))
    print("Just a moment...")
    time.sleep(2)
    os.system('clear')
  except ValueError:
    try:
      print(" ")
      diffi = int(input("Invalid Option, try again- "))
      print("Just a moment...")
      time.sleep(2)
      os.system('clear')
    except ValueError:
      try:
        print(" ")
        diffi = int(input("Last chance, don't mess it up here!!- "))
        print("Just a moment...")
        time.sleep(2)
        os.system('clear')
      except ValueError:
        print(" ")
        print("I warned you, no more game.")
        sys.exit()
  if diffi != 1 and diffi != 2 and diffi != 3 and diffi != 4:
    diffi = int(input("Invalid Option, please try again- "))
    print("Just a moment...")
    time.sleep(2)
    os.system('clear')
  if diffi == 1:
    Diff1(money)
  if diffi == 2:
    Diff2(money)
  if diffi == 3:
    Diff3(money)
  if diffi == 4:
    Diff4(money)


def Diff1(money):
  h1_d = 0
  h2_d = 0
  h3_d = 0
  h1_sp = 2.5
  h2_sp = 2.5
  h3_sp = 2.5
  winner_decided = False
  print("Welcome to the horse race!")
  print(" ")
  time.sleep(1)
  print("We have three horse's racing for you today, now is the prime time to place your bets!!")
  print(" ")
  time.sleep(1.5)
  for i in range(3):
    if i == 0:
      RandomNameIndex = random.randint(0, len(horsenames["Names"]) - 1)
      Horse1 = ([horsenames["Names"][RandomNameIndex]])
      Horse1 = str(Horse1[0])
      Odds1 = random.randint(1, 50)
      
    if i == 1:
      RandomNameIndex = random.randint(0, len(horsenames["Names"]) - 1)
      Horse2 = ([horsenames["Names"][RandomNameIndex]])
      Horse2 = str(Horse2[0])
      Odds2 = random.randint(1, 50)
      
    if i == 2:
      RandomNameIndex = random.randint(0, len(horsenames["Names"]) - 1)
      Horse3 = ([horsenames["Names"][RandomNameIndex]])
      Horse3 = str(Horse3[0])
      Odds3 = random.randint(1, 50)
  
  print("1. " + Horse1)
  print(f"{Odds1}/1")
  print(" ")
  time.sleep(0.75)
  print("2. " + Horse2)
  print(f"{Odds2}/1")
  print(" ")
  time.sleep(0.75)
  print("3. " + Horse3)
  print(f"{Odds3}/1")
  print(" ")
  print(f"Money: {money}")
  horse_bet = int(input("What horse do you want to bet on- "))
  print(" ")
  if horse_bet != 1 and horse_bet != 2 and horse_bet != 3:
    horse_bet = int(input("Invalid input, try again- "))
  if horse_bet == 1:
    chosenhorse = Horse1
  if horse_bet == 2:
    chosenhorse = Horse2
  if horse_bet == 3:
    chosenhorse = Horse3
  if horse_bet == 4:
    chosenhorse = Horse4
  if horse_bet == 5:
    chosenhorse = Horse5
  confirm_bet = input(f"You wish to place a bet on {chosenhorse}, correct? (y/n)- ")
  print(" ")
  if confirm_bet == "n":
    while True:
      horse_bet = int(input("Reselect the horse you wish to bet on- "))
      print(" ")
      if horse_bet == 1:
        chosenhorse = Horse1
        break
      if horse_bet == 2:
        chosenhorse = Horse2
        break
      if horse_bet == 3:
        chosenhorse = Horse3
        break
      if horse_bet == 4:
        chosenhorse = Horse4
        break
      if horse_bet == 5:
        chosenhorse = Horse5
        break
      confirm_bet = input(f"You wish to place a bet on {chosenhorse}, correct? (y/n)- ")
      print(" ")
  money_bet = int(input("How much money do you want to bet- "))
  print(" ")
  if money_bet > money or money_bet < 0:
    print("Invalid Option.")
    print(" ")
    money_bet = int(input("How much money do you want to bet- "))
    print(" ")
  confirm_money_bet = input(f"You wish to place a bet of {money_bet}, correct? (y/n)- ")
  print(" ")
  if confirm_money_bet == "n":
    while True:
      money_bet = int(input("Reselect the money you wish to bet- "))
      print(" ")
      confirm_money_bet = input(f"You wish to place a bet of {money_bet}, correct? (y/n)- ")
      break
  if confirm_money_bet == "y":
    money = money - money_bet
    print(f"Current money: {money}")
    print(" ")
  time.sleep(3)
  os.system('clear')
  print("OK, all bets have been placed! We will now start the races!")
  time.sleep(3)
  os.system('clear')
  print("3")
  time.sleep(1)
  os.system('clear')
  print("2")
  time.sleep(1)
  os.system('clear')
  print("1")
  time.sleep(1)
  os.system('clear')
  print("Go!")
  time.sleep(0.75)
  os.system('clear')
  while winner_decided == False:
    print(f"{Horse1} Distance Traveled:")
    print(f"{h1_d}/100")
    print(" ")
    print(f"{Horse2} Distance Traveled:")
    print(f"{h2_d}/100")
    print(" ")
    print(f"{Horse3} Distance Traveled:")
    print(f"{h3_d}/100")

    h1_d = h1_d + h1_sp
    h2_d = h2_d + h2_sp
    h3_d = h3_d + h3_sp

    if h1_d >= 25:
      h1_sp = random.randint(1, 7)
    elif h1_d >= 50:
      h1_sp = random.randint(1, 7)
    elif h1_d >= 75:
      h1_sp = random.randint(1, 7)
      
    if h2_d >= 25:
      h2_sp = random.randint(1, 7)
    elif h2_d >= 50:
      h2_sp = random.randint(1, 7)
    elif h2_d >= 75:
      h2_sp = random.randint(1, 7)

    if h3_d >= 25:
      h3_sp = random.randint(1, 7)
    elif h3_d >= 50:
      h3_sp = random.randint(1, 7)
    elif h3_d >= 75:
      h3_sp = random.randint(1, 7)

    time.sleep(1)
    os.system('clear')
    
    if h1_d >= 100:
      print(f"{Horse1} is the winner!")
      winner = Horse1
      winner_decided = True
      break
    if h2_d >= 100:
      print(f"{Horse2} is the winner!")
      winner = Horse2
      winner_decided = True
      break
    if h3_d >= 100:
      print(f"{Horse3} is the winner!")
      winner = Horse3
      winner_decided = True
      break
  if chosenhorse == winner:
    print("Your bet won, you  get your bet back at 3x the amount!")
    money = money + (money_bet * 3)
    print(f"Current money: {money}")
  elif chosenhorse != winner:
    print("Sorry, you didn't win, better luck next time.")
    print(" ")

  time.sleep(3)
  os.system('clear')
  print(f"Current money: {money}")
  back_to_menu = input("Do you wish to return to the menu? (y/n)- ")
  if back_to_menu == "y":
    os.system('clear')
    StartScreen(money)
  elif back_to_menu == "n":
    print("See you soon!")
    time.sleep(1)
    sys.exit()


def Diff2(money):
  horse1 = ""
  horse2 = ""
  horse3 = ""
  horse4 = ""
  horse5 = ""
  winner = False
  first_place = False
  second_place = False
  third_place = False
  done1 = False
  done2 = False
  done3 = False
  done4 = False
  done5 = False
  h1_d = 0
  h2_d = 0
  h3_d = 0
  h4_d = 0
  h5_d = 0
  h1_sp = 2.5
  h2_sp = 2.5
  h3_sp = 2.5
  h4_sp = 2.5
  h5_sp = 2.5
  winner_decided = False
  print("Welcome to the horse race!")
  print(" ")
  time.sleep(1)
  print("We have five horse's racing for you today, now is the prime time to place your bets!!")
  print(" ")
  time.sleep(1.5)
  for i in range(5):
    if i == 0:
      RandomNameIndex = random.randint(0, len(horsenames["Names"]) - 1)
      Horse1 = ([horsenames["Names"][RandomNameIndex]])
      Horse1 = str(Horse1[0])
      Odds1 = random.randint(1, 50)
      
    if i == 1:
      RandomNameIndex = random.randint(0, len(horsenames["Names"]) - 1)
      Horse2 = ([horsenames["Names"][RandomNameIndex]])
      Horse2 = str(Horse2[0])
      Odds2 = random.randint(1, 50)
      
    if i == 2:
      RandomNameIndex = random.randint(0, len(horsenames["Names"]) - 1)
      Horse3 = ([horsenames["Names"][RandomNameIndex]])
      Horse3 = str(Horse3[0])
      Odds3 = random.randint(1, 50)
      
    if i == 3:
      RandomNameIndex = random.randint(0, len(horsenames["Names"]) - 1)
      Horse4 = ([horsenames["Names"][RandomNameIndex]])
      Horse4 = str(Horse4[0])
      Odds4 = random.randint(1, 50)
    if i == 4:
      RandomNameIndex = random.randint(0, len(horsenames["Names"]) - 1)
      Horse5 = ([horsenames["Names"][RandomNameIndex]])
      Horse5 = str(Horse5[0])
      Odds5 = random.randint(1, 50)
  print("1. " + Horse1)
  print(f"{Odds1}/1")
  print(" ")
  time.sleep(0.75)
  print("2. " + Horse2)
  print(f"{Odds2}/1")
  print(" ")
  time.sleep(0.75)
  print("3. " + Horse3)
  print(f"{Odds3}/1")
  print(" ")
  time.sleep(0.75)
  print("4. " + Horse4)
  print(f"{Odds4}/1")
  print(" ")
  time.sleep(0.75)
  print("5. " + Horse5)
  print(f"{Odds5}/1")
  print(" ")
  print(f"Money: {money}")
  horse_bet = int(input("What horse do you want to bet on- "))
  print(" ")
  if horse_bet != 1 and horse_bet != 2 and horse_bet != 3 and horse_bet != 4 and horse_bet != 5:
    horse_bet = int(input("Invalid input, try again- "))
  if horse_bet == 1:
    chosenhorse = Horse1
  if horse_bet == 2:
    chosenhorse = Horse2
  if horse_bet == 3:
    chosenhorse = Horse3
  if horse_bet == 4:
    chosenhorse = Horse4
  if horse_bet == 5:
    chosenhorse = Horse5
  confirm_bet = input(f"You wish to place a bet on {chosenhorse}, correct? (y/n)- ")
  print(" ")
  if confirm_bet == "n":
    while True:
      horse_bet = int(input("Reselect the horse you wish to bet on- "))
      print(" ")
      if horse_bet == 1:
        chosenhorse = Horse1
        break
      if horse_bet == 2:
        chosenhorse = Horse2
        break
      if horse_bet == 3:
        chosenhorse = Horse3
        break
      if horse_bet == 4:
        chosenhorse = Horse4
        break
      if horse_bet == 5:
        chosenhore = Horse5
        break
      confirm_bet = input(f"You wish to place a bet on {chosenhorse}, correct? (y/n)- ")
      print(" ")
  ask_bet_type = int(input("What type of bet do you want to place, 1.Win, 2.Place- "))
  print(" ")
  if ask_bet_type == 1:
    bet_type = "win"
  elif ask_bet_type == 2:
    bet_type = "place"
  elif ask_bet_type > 2 or ask_bet_type < 0:
    print(" ")
    ask_bet_type = int(input("Inavlid option, What type of bet do you want to place, 1.Win, 2.Place- "))
  money_bet = int(input("How much money do you want to bet- "))
  print(" ")
  if money_bet > money:
    print("Invalid Option, bets must be under current amount of money.")
    print(" ")
    money_bet = int(input("How much money do you want to bet- "))
    print(" ")
  confirm_money_bet = input(f"You wish to place a bet of {money_bet}, correct? (y/n)- ")
  print(" ")
  if confirm_money_bet == "n":
    while True:
      money_bet = int(input("Reselect the money you wish to bet- "))
      print(" ")
      confirm_money_bet = input(f"You wish to place a bet of {money_bet}, correct? (y/n)- ")
      break
  if confirm_money_bet == "y":
    money = money - money_bet
    print(f"Current money: {money}")
    print(" ")
  time.sleep(3)
  os.system('clear')
  print("OK, all bets have been placed! We will now start the races!")
  time.sleep(3)
  os.system('clear')
  print("3")
  time.sleep(1)
  os.system('clear')
  print("2")
  time.sleep(1)
  os.system('clear')
  print("1")
  time.sleep(1)
  os.system('clear')
  print("Go!")
  time.sleep(0.75)
  os.system('clear')
  while winner_decided == False:
    print(f"{Horse1} Distance Traveled:")
    print(f"{h1_d}/100")
    print(" ")
    print(f"{Horse2} Distance Traveled:")
    print(f"{h2_d}/100")
    print(" ")
    print(f"{Horse3} Distance Traveled:")
    print(f"{h3_d}/100")
    print(" ")
    print(f"{Horse4} Distance Traveled:")
    print(f"{h4_d}/100")
    print(" ")
    print(f"{Horse5} Distance Traveled:")
    print(f"{h5_d}/100")

    h1_d = h1_d + h1_sp
    h2_d = h2_d + h2_sp
    h3_d = h3_d + h3_sp
    h4_d = h4_d + h4_sp
    h5_d = h5_d + h5_sp

    if h1_d >= 25:
      h1_sp = random.randint(1, 7)
    elif h1_d >= 50:
      h1_sp = random.randint(1, 7)
    elif h1_d >= 75:
      h1_sp = random.randint(1, 7)
      
    if h2_d >= 25:
      h2_sp = random.randint(1, 7)
    elif h2_d >= 50:
      h2_sp = random.randint(1, 7)
    elif h2_d >= 75:
      h2_sp = random.randint(1, 7)

    if h3_d >= 25:
      h3_sp = random.randint(1, 7)
    elif h3_d >= 50:
      h3_sp = random.randint(1, 7)
    elif h3_d >= 75:
      h3_sp = random.randint(1, 7)
    
    if h4_d >= 25:
      h4_sp = random.randint(1, 7)
    elif h4_d >= 50:
      h4_sp = random.randint(1, 7)
    elif h4_d >= 75:
      h4_sp = random.randint(1, 7)

    if h5_d >= 25:
      h5_sp = random.randint(1, 7)
    elif h5_d >= 50:
      h5_sp = random.randint(1, 7)
    elif h5_d >= 75:
      h5_sp = random.randint(1, 7)

    if winner == False:
      winner_horse = "None"
    if second_place == False:
      second_place_horse = "None"
    if third_place == False:
      third_place_horse = "None"
    print(" ")
    print("---------------------")
    print(f"1st place: {winner_horse}")
    print(f"2nd place: {second_place_horse}")
    print(f"3rd place: {third_place_horse}")
    time.sleep(1)
    os.system('clear')
    

    if h1_d >= 100:
      done1 = True
      h1_sp = 0
      if first_place == False:
        winner = True
        horse1 = "winner"
        first_place = True
        if winner == True and horse1 == "winner":
          winner_horse = Horse1
      elif first_place == True and horse1 != "winner":
        if second_place == False:
          second_place = True
          horse1 = "place2"
          if second_place == True and horse1 == "place2":
            second_place_horse = Horse1
        elif second_place == True and horse1 != "place2":
          if third_place == False:
            third_place = True
            horse1 = "place3"
            if third_place == True and horse1 == "place3":
              third_place_horse = Horse1
            
    
    if h2_d >= 100:
      done2 = True
      h2_sp = 0
      if first_place == False:
        winner = True
        horse2 = "winner"
        first_place = True
        if winner == True and horse2 == "winner":
          winner_horse = Horse2
      elif first_place == True and horse2 != "winner":
        if second_place == False:
          second_place = True
          horse2 = "place2"
          if second_place == True and horse2 == "place2":
            second_place_horse = Horse2
        elif second_place == True and horse2 != "place2":
          if third_place == False:
            third_place = True
            horse2 = "place3"
            if third_place == True and horse2 == "place3":
              third_place_horse = Horse2
          
    if h3_d >= 100:
      done3 = True
      h3_sp = 0
      if first_place == False:
        winner = True
        horse3 = "winner"
        first_place = True
        if winner == True and horse3 == "winner":
          winner_horse = Horse3
      elif first_place == True and horse3 != "winner":
        if second_place == False:
          second_place = True
          horse3 = "place2"
          if second_place == True and horse3 == "place2":
            second_place_horse = Horse3
        elif second_place == True and horse3 != "place2":
          if third_place == False:
            third_place = True
            horse3 = "place3"
            if third_place == True and horse3 == "place3":
              third_place_horse = Horse3
          
    if h4_d >= 100:
      done4 = True
      h4_sp = 0
      if first_place == False:
        winner = True
        horse4 = "winner"
        first_place = True
        if winner == True and horse4 == "winner":
          winner_horse = Horse4
      elif first_place == True and horse4 != "winner":
        if second_place == False:
          second_place = True
          horse4 = "place2"
          if second_place == True and horse4 == "place2":
            second_place_horse = Horse4
        elif second_place == True and horse4 != "place2":
          if third_place == False:
            third_place = True
            horse4 = "place3"
            if third_place == True and horse4 == "place3":
              third_place_horse = Horse4
          
    if h5_d >= 100:
      done5 = True
      h5_sp = 0
      if first_place == False:
        winner = True
        horse5 = "winner"
        first_place = True
        if winner == True and horse5 == "winner":
          winner_horse = Horse5
      elif first_place == True and horse5 != "winner":
        if second_place == False:
          second_place = True
          horse5 = "place2"
          if second_place == True and horse5 == "place2":
            second_place_horse = Horse5
        elif second_place == True and horse5 != "place2":
          if third_place == False:
            third_place = True
            horse5 = "place3"
            if third_place == True and horse5 == "place3":
              third_place_horse = Horse5

    
      
      if done1 == True and done2 == True and done3 == True and done4 == True and done5 == True:
        break
  if horse_bet == 1:
    chosenhorse = horse1
  if horse_bet == 2:
    chosenhorse = horse2
  if horse_bet == 3:
    chosenhorse = horse3
  if horse_bet == 4:
    chosenhorse = horse4
  if horse_bet == 5:
    chosenhorse = horse5
  if bet_type == "win":
    if chosenhorse == "winner":
      print(f"Your horse won! You won {money_bet * 3}!")
      money = money + (money_bet * 3)
      print(f"Current money: {money}")
    else:
      print("Your horse didn't win, better luck next time.")
  if bet_type == "place":
      if chosenhorse == "winner" or chosenhorse == "place2" or chosenhorse == "place3":
        print(f"Your horse placed! You won {money_bet * 2}!")
        money = money + (money_bet * 2)
        print(" ")
        print(f"Current money: {money}")
      else:
        print("Your horse didn't place, better luck next time.")

  time.sleep(3)
  os.system('clear')
  print(f"Current money: {money}")
  back_to_menu = input("Do you wish to return to the menu? (y/n)- ")
  if back_to_menu == "y":
    os.system('clear')
    StartScreen(money)
  elif back_to_menu == "n":
    print("See you soon!")
    time.sleep(1)
    sys.exit()
    
def Diff3(money):
  horse1 = ""
  horse2 = ""
  horse3 = ""
  horse4 = ""
  horse5 = ""
  horse6 = ""
  horse7 = ""
  winner = False
  first_place = False
  second_place = False
  third_place = False
  done1 = False
  done2 = False
  done3 = False
  done4 = False
  done5 = False
  done6 = False
  done7 = False
  h1_d = 0
  h2_d = 0
  h3_d = 0
  h4_d = 0
  h5_d = 0
  h6_d = 0
  h7_d = 0
  h1_sp = 2.5
  h2_sp = 2.5
  h3_sp = 2.5
  h4_sp = 2.5
  h5_sp = 2.5
  h6_sp = 2.5
  h7_sp = 2.5
  winner_decided = False
  print("Welcome to the horse race!")
  print(" ")
  time.sleep(1)
  print("We have seven horse's racing for you today, now is the prime time to place your bets!!")
  print(" ")
  time.sleep(1.5)
  for i in range(7):
    if i == 0:
      RandomNameIndex = random.randint(0, len(horsenames["Names"]) - 1)
      Horse1 = ([horsenames["Names"][RandomNameIndex]])
      Horse1 = str(Horse1[0])
      Odds1 = random.randint(1, 50)
      
    if i == 1:
      RandomNameIndex = random.randint(0, len(horsenames["Names"]) - 1)
      Horse2 = ([horsenames["Names"][RandomNameIndex]])
      Horse2 = str(Horse2[0])
      Odds2 = random.randint(1, 50)
      
    if i == 2:
      RandomNameIndex = random.randint(0, len(horsenames["Names"]) - 1)
      Horse3 = ([horsenames["Names"][RandomNameIndex]])
      Horse3 = str(Horse3[0])
      Odds3 = random.randint(1, 50)
      
    if i == 3:
      RandomNameIndex = random.randint(0, len(horsenames["Names"]) - 1)
      Horse4 = ([horsenames["Names"][RandomNameIndex]])
      Horse4 = str(Horse4[0])
      Odds4 = random.randint(1, 50)
    if i == 4:
      RandomNameIndex = random.randint(0, len(horsenames["Names"]) - 1)
      Horse5 = ([horsenames["Names"][RandomNameIndex]])
      Horse5 = str(Horse5[0])
      Odds5 = random.randint(1, 50)
    if i == 5:
      RandomNameIndex = random.randint(0, len(horsenames["Names"]) - 1)
      Horse6 = ([horsenames["Names"][RandomNameIndex]])
      Horse6 = str(Horse6[0])
      Odds6 = random.randint(1, 50)
    if i == 6:
      RandomNameIndex = random.randint(0, len(horsenames["Names"]) - 1)
      Horse7 = ([horsenames["Names"][RandomNameIndex]])
      Horse7 = str(Horse7[0])
      Odds7 = random.randint(1, 50)
  print("1. " + Horse1)
  print(f"{Odds1}/1")
  print(" ")
  time.sleep(0.75)
  print("2. " + Horse2)
  print(f"{Odds2}/1")
  print(" ")
  time.sleep(0.75)
  print("3. " + Horse3)
  print(f"{Odds3}/1")
  print(" ")
  time.sleep(0.75)
  print("4. " + Horse4)
  print(f"{Odds4}/1")
  print(" ")
  time.sleep(0.75)
  print("5. " + Horse5)
  print(f"{Odds5}/1")
  print(" ")
  time.sleep(0.75)
  print("6. " + Horse6)
  print(f"{Odds6}/1")
  print(" ")
  time.sleep(0.75)
  print("7. " + Horse7)
  print(f"{Odds7}/1")
  print(" ")
  print(f"Money: {money}")
  horse_bet = int(input("What horse do you want to bet on- "))
  print(" ")
  if horse_bet != 1 and horse_bet != 2 and horse_bet != 3 and horse_bet != 4 and horse_bet != 5 and horse_bet != 6 and horse_bet != 7:
    horse_bet = int(input("Invalid input, try again- "))
  if horse_bet == 1:
    chosenhorse = Horse1
  if horse_bet == 2:
    chosenhorse = Horse2
  if horse_bet == 3:
    chosenhorse = Horse3
  if horse_bet == 4:
    chosenhorse = Horse4
  if horse_bet == 5:
    chosenhorse = Horse5
  if horse_bet == 6:
    chosenhorse = Horse6
  if horse_bet == 7:
    chosenhorse = Horse7
  confirm_bet = input(f"You wish to place a bet on {chosenhorse}, correct? (y/n)- ")
  print(" ")
  if confirm_bet == "n":
    while True:
      horse_bet = int(input("Reselect the horse you wish to bet on- "))
      print(" ")
      if horse_bet == 1:
        chosenhorse = Horse1
        break
      if horse_bet == 2:
        chosenhorse = Horse2
        break
      if horse_bet == 3:
        chosenhorse = Horse3
        break
      if horse_bet == 4:
        chosenhorse = Horse4
        break
      if horse_bet == 5:
        chosenhore = Horse5
        break
      if horse_bet == 6:
        chosenhorse = Horse6
        break
      if horse_bet == 7:
        chosenhorse = Horse7
        break
      confirm_bet = input(f"You wish to place a bet on {chosenhorse}, correct? (y/n)- ")
      print(" ")
  ask_bet_type = int(input("What type of bet do you want to place, 1.Win, 2.Place- "))
  print(" ")
  if ask_bet_type == 1:
    bet_type = "win"
  elif ask_bet_type == 2:
    bet_type = "place"
  elif ask_bet_type > 2 or ask_bet_type < 0:
    print(" ")
    ask_bet_type = int(input("Inavlid option, What type of bet do you want to place, 1.Win, 2.Place- "))
  money_bet = int(input("How much money do you want to bet- "))
  print(" ")
  if money_bet > money:
    print("Invalid Option, bets must be under current amount of money.")
    print(" ")
    money_bet = int(input("How much money do you want to bet- "))
    print(" ")
  confirm_money_bet = input(f"You wish to place a bet of {money_bet}, correct? (y/n)- ")
  print(" ")
  if confirm_money_bet == "n":
    while True:
      money_bet = int(input("Reselect the money you wish to bet- "))
      print(" ")
      confirm_money_bet = input(f"You wish to place a bet of {money_bet}, correct? (y/n)- ")
      break
  if confirm_money_bet == "y":
    money = money - money_bet
    print(f"Current money: {money}")
    print(" ")
  time.sleep(3)
  os.system('clear')
  print("OK, all bets have been placed! We will now start the races!")
  time.sleep(3)
  os.system('clear')
  print("3")
  time.sleep(1)
  os.system('clear')
  print("2")
  time.sleep(1)
  os.system('clear')
  print("1")
  time.sleep(1)
  os.system('clear')
  print("Go!")
  time.sleep(0.75)
  os.system('clear')
  while winner_decided == False:
    print(f"{Horse1} Distance Traveled:")
    print(f"{h1_d}/100")
    print(" ")
    print(f"{Horse2} Distance Traveled:")
    print(f"{h2_d}/100")
    print(" ")
    print(f"{Horse3} Distance Traveled:")
    print(f"{h3_d}/100")
    print(" ")
    print(f"{Horse4} Distance Traveled:")
    print(f"{h4_d}/100")
    print(" ")
    print(f"{Horse5} Distance Traveled:")
    print(f"{h5_d}/100")
    print(" ")
    print(f"{Horse6} Distance Traveled:")
    print(f"{h6_d}/100")
    print(" ")
    print(f"{Horse7} Distance Traveled:")
    print(f"{h6_d}/100")

    h1_d = h1_d + h1_sp
    h2_d = h2_d + h2_sp
    h3_d = h3_d + h3_sp
    h4_d = h4_d + h4_sp
    h5_d = h5_d + h5_sp
    h6_d = h6_d + h6_sp
    h7_d = h7_d + h7_sp

    if h1_d >= 25:
      h1_sp = random.randint(1, 7)
    elif h1_d >= 50:
      h1_sp = random.randint(1, 7)
    elif h1_d >= 75:
      h1_sp = random.randint(1, 7)
      
    if h2_d >= 25:
      h2_sp = random.randint(1, 7)
    elif h2_d >= 50:
      h2_sp = random.randint(1, 7)
    elif h2_d >= 75:
      h2_sp = random.randint(1, 7)

    if h3_d >= 25:
      h3_sp = random.randint(1, 7)
    elif h3_d >= 50:
      h3_sp = random.randint(1, 7)
    elif h3_d >= 75:
      h3_sp = random.randint(1, 7)
    
    if h4_d >= 25:
      h4_sp = random.randint(1, 7)
    elif h4_d >= 50:
      h4_sp = random.randint(1, 7)
    elif h4_d >= 75:
      h4_sp = random.randint(1, 7)

    if h5_d >= 25:
      h5_sp = random.randint(1, 7)
    elif h5_d >= 50:
      h5_sp = random.randint(1, 7)
    elif h5_d >= 75:
      h5_sp = random.randint(1, 7)

    if h6_d >= 25:
      h6_sp = random.randint(1, 7)
    elif h6_d >= 50:
      h6_sp = random.randint(1, 7)
    elif h6_d >= 75:
      h6_sp = random.randint(1, 7)

    if h7_d >= 25:
      h7_sp = random.randint(1, 7)
    elif h7_d >= 50:
      h7_sp = random.randint(1, 7)
    elif h7_d >= 75:
      h7_sp = random.randint(1, 7)

    if winner == False:
      winner_horse = "None"
    if second_place == False:
      second_place_horse = "None"
    if third_place == False:
      third_place_horse = "None"
    print(" ")
    print("---------------------")
    print(f"1st place: {winner_horse}")
    print(f"2nd place: {second_place_horse}")
    print(f"3rd place: {third_place_horse}")
    time.sleep(1)
    os.system('clear')
    

    if h1_d >= 100:
      done1 = True
      h1_sp = 0
      if first_place == False:
        winner = True
        horse1 = "winner"
        first_place = True
        if winner == True and horse1 == "winner":
          winner_horse = Horse1
      elif first_place == True and horse1 != "winner":
        if second_place == False:
          second_place = True
          horse1 = "place2"
          if second_place == True and horse1 == "place2":
            second_place_horse = Horse1
        elif second_place == True and horse1 != "place2":
          if third_place == False:
            third_place = True
            horse1 = "place3"
            if third_place == True and horse1 == "place3":
              third_place_horse = Horse1
            
    
    if h2_d >= 100:
      done2 = True
      h2_sp = 0
      if first_place == False:
        winner = True
        horse2 = "winner"
        first_place = True
        if winner == True and horse2 == "winner":
          winner_horse = Horse2
      elif first_place == True and horse2 != "winner":
        if second_place == False:
          second_place = True
          horse2 = "place2"
          if second_place == True and horse2 == "place2":
            second_place_horse = Horse2
        elif second_place == True and horse2 != "place2":
          if third_place == False:
            third_place = True
            horse2 = "place3"
            if third_place == True and horse2 == "place3":
              third_place_horse = Horse2
          
    if h3_d >= 100:
      done3 = True
      h3_sp = 0
      if first_place == False:
        winner = True
        horse3 = "winner"
        first_place = True
        if winner == True and horse3 == "winner":
          winner_horse = Horse3
      elif first_place == True and horse3 != "winner":
        if second_place == False:
          second_place = True
          horse3 = "place2"
          if second_place == True and horse3 == "place2":
            second_place_horse = Horse3
        elif second_place == True and horse3 != "place2":
          if third_place == False:
            third_place = True
            horse3 = "place3"
            if third_place == True and horse3 == "place3":
              third_place_horse = Horse3
          
    if h4_d >= 100:
      done4 = True
      h4_sp = 0
      if first_place == False:
        winner = True
        horse4 = "winner"
        first_place = True
        if winner == True and horse4 == "winner":
          winner_horse = Horse4
      elif first_place == True and horse4 != "winner":
        if second_place == False:
          second_place = True
          horse4 = "place2"
          if second_place == True and horse4 == "place2":
            second_place_horse = Horse4
        elif second_place == True and horse4 != "place2":
          if third_place == False:
            third_place = True
            horse4 = "place3"
            if third_place == True and horse4 == "place3":
              third_place_horse = Horse4
          
    if h5_d >= 100:
      done5 = True
      h5_sp = 0
      if first_place == False:
        winner = True
        horse5 = "winner"
        first_place = True
        if winner == True and horse5 == "winner":
          winner_horse = Horse5
      elif first_place == True and horse5 != "winner":
        if second_place == False:
          second_place = True
          horse5 = "place2"
          if second_place == True and horse5 == "place2":
            second_place_horse = Horse5
        elif second_place == True and horse5 != "place2":
          if third_place == False:
            third_place = True
            horse5 = "place3"
            if third_place == True and horse5 == "place3":
              third_place_horse = Horse5

    
    if h6_d >= 100:
      done6 = True
      h6_sp = 0
      if first_place == False:
        winner = True
        horse6 = "winner"
        first_place = True
        if winner == True and horse6 == "winner":
          winner_horse = Horse6
      elif first_place == True and horse6 != "winner":
        if second_place == False:
          second_place = True
          horse6 = "place2"
          if second_place == True and horse6 == "place2":
            second_place_horse = Horse6
        elif second_place == True and horse6 != "place2":
          if third_place == False:
            third_place = True
            horse6 = "place3"
            if third_place == True and horse6 == "place3":
              third_place_horse = Horse6


    if h7_d >= 100:
      done7 = True
      h7_sp = 0
      if first_place == False:
        winner = True
        horse7 = "winner"
        first_place = True
        if winner == True and horse7 == "winner":
          winner_horse = Horse7
      elif first_place == True and horse7 != "winner":
        if second_place == False:
          second_place = True
          horse7 = "place2"
          if second_place == True and horse7 == "place2":
            second_place_horse = Horse7
        elif second_place == True and horse7 != "place2":
          if third_place == False:
            third_place = True
            horse7 = "place3"
            if third_place == True and horse7 == "place3":
              third_place_horse = Horse7
      if done1 == True and done2 == True and done3 == True and done4 == True and done5 == True and done6 == True and done7 == True:
        break
  if horse_bet == 1:
    chosenhorse = horse1
  if horse_bet == 2:
    chosenhorse = horse2
  if horse_bet == 3:
    chosenhorse = horse3
  if horse_bet == 4:
    chosenhorse = horse4
  if horse_bet == 5:
    chosenhorse = horse5
  if horse_bet == 6:
    chosenhorse = horse6
  if horse_bet == 7:
    chosenhorse = horse7
  if bet_type == "win":
    if chosenhorse == "winner":
      print(f"Your horse won! You won {money_bet * 3}!")
      money = money + (money_bet * 3)
      print(f"Current money: {money}")
    else:
      print("Your horse didn't win, better luck next time.")
  if bet_type == "place":
      if chosenhorse == "winner" or chosenhorse == "place2" or chosenhorse == "place3":
        print(f"Your horse placed! You won {money_bet * 2}!")
        money = money + (money_bet * 2)
        print(" ")
        print(f"Current money: {money}")
      else:
        print("Your horse didn't place, better luck next time.")

  time.sleep(3)
  os.system('clear')
  print(f"Current money: {money}")
  back_to_menu = input("Do you wish to return to the menu? (y/n)- ")
  if back_to_menu == "y":
    os.system('clear')
    StartScreen(money)
  elif back_to_menu == "n":
    print("See you soon!")
    time.sleep(1)
    sys.exit()
    

def Diff4(money):
  horse1 = ""
  horse2 = ""
  horse3 = ""
  horse4 = ""
  horse5 = ""
  horse6 = ""
  horse7 = ""
  horse8 = ""
  horse9 = ""
  horse10 = ""
  winner = False
  first_place = False
  second_place = False
  third_place = False
  done1 = False
  done2 = False
  done3 = False
  done4 = False
  done5 = False
  done6 = False
  done7 = False
  done8 = False
  done9 = False
  done10 = False
  h1_d = 0
  h2_d = 0
  h3_d = 0
  h4_d = 0
  h5_d = 0
  h6_d = 0
  h7_d = 0
  h8_d = 0
  h9_d = 0
  h10_d = 0
  h1_sp = 2.5
  h2_sp = 2.5
  h3_sp = 2.5
  h4_sp = 2.5
  h5_sp = 2.5
  h6_sp = 2.5
  h7_sp = 2.5
  h8_sp = 2.5
  h9_sp = 2.5
  h10_sp = 2.5
  winner_decided = False
  print("Welcome to the horse race!")
  print(" ")
  time.sleep(1)
  print("We have ten horse's racing for you today, now is the prime time to place your bets!!")
  print(" ")
  time.sleep(1.5)
  for i in range(10):
    if i == 0:
      RandomNameIndex = random.randint(0, len(horsenames["Names"]) - 1)
      Horse1 = ([horsenames["Names"][RandomNameIndex]])
      Horse1 = str(Horse1[0])
      Odds1 = random.randint(1, 50)
      
    if i == 1:
      RandomNameIndex = random.randint(0, len(horsenames["Names"]) - 1)
      Horse2 = ([horsenames["Names"][RandomNameIndex]])
      Horse2 = str(Horse2[0])
      Odds2 = random.randint(1, 50)
      
    if i == 2:
      RandomNameIndex = random.randint(0, len(horsenames["Names"]) - 1)
      Horse3 = ([horsenames["Names"][RandomNameIndex]])
      Horse3 = str(Horse3[0])
      Odds3 = random.randint(1, 50)
      
    if i == 3:
      RandomNameIndex = random.randint(0, len(horsenames["Names"]) - 1)
      Horse4 = ([horsenames["Names"][RandomNameIndex]])
      Horse4 = str(Horse4[0])
      Odds4 = random.randint(1, 50)
    if i == 4:
      RandomNameIndex = random.randint(0, len(horsenames["Names"]) - 1)
      Horse5 = ([horsenames["Names"][RandomNameIndex]])
      Horse5 = str(Horse5[0])
      Odds5 = random.randint(1, 50)
    if i == 5:
      RandomNameIndex = random.randint(0, len(horsenames["Names"]) - 1)
      Horse6 = ([horsenames["Names"][RandomNameIndex]])
      Horse6 = str(Horse6[0])
      Odds6 = random.randint(1, 50)
    if i == 6:
      RandomNameIndex = random.randint(0, len(horsenames["Names"]) - 1)
      Horse7 = ([horsenames["Names"][RandomNameIndex]])
      Horse7 = str(Horse7[0])
      Odds7 = random.randint(1, 50)
    if i == 7:
      RandomNameIndex = random.randint(0, len(horsenames["Names"]) - 1)
      Horse8 = ([horsenames["Names"][RandomNameIndex]])
      Horse8 = str(Horse8[0])
      Odds8 = random.randint(1, 50)
    if i == 8:
      RandomNameIndex = random.randint(0, len(horsenames["Names"]) - 1)
      Horse9 = ([horsenames["Names"][RandomNameIndex]])
      Horse9 = str(Horse9[0])
      Odds9 = random.randint(1, 50)
    if i == 9:
      RandomNameIndex = random.randint(0, len(horsenames["Names"]) - 1)
      Horse10 = ([horsenames["Names"][RandomNameIndex]])
      Horse10 = str(Horse10[0])
      Odds10 = random.randint(1, 50)
  print("1. " + Horse1)
  print(f"{Odds1}/1")
  print(" ")
  time.sleep(0.75)
  print("2. " + Horse2)
  print(f"{Odds2}/1")
  print(" ")
  time.sleep(0.75)
  print("3. " + Horse3)
  print(f"{Odds3}/1")
  print(" ")
  time.sleep(0.75)
  print("4. " + Horse4)
  print(f"{Odds4}/1")
  print(" ")
  time.sleep(0.75)
  print("5. " + Horse5)
  print(f"{Odds5}/1")
  print(" ")
  time.sleep(0.75)
  print("6. " + Horse6)
  print(f"{Odds6}/1")
  print(" ")
  time.sleep(0.75)
  print("7. " + Horse7)
  print(f"{Odds7}/1")
  print(" ")
  time.sleep(0.75)
  print("8. " + Horse8)
  print(f"{Odds8}/1")
  print(" ")
  time.sleep(0.75)
  print("9. " + Horse9)
  print(f"{Odds9}/1")
  print(" ")
  time.sleep(0.75)
  print("10. " + Horse10)
  print(f"{Odds10}/1")
  print(" ")
  time.sleep(0.75)
  print(f"Money: {money}")
  horse_bet = int(input("What horse do you want to bet on- "))
  print(" ")
  if horse_bet != 1 and horse_bet != 2 and horse_bet != 3 and horse_bet != 4 and horse_bet != 5 and horse_bet != 6 and horse_bet != 7 and horse_bet != 8 and horse_bet != 9 and horse_bet != 10:
    horse_bet = int(input("Invalid input, try again- "))
  if horse_bet == 1:
    chosenhorse = Horse1
  if horse_bet == 2:
    chosenhorse = Horse2
  if horse_bet == 3:
    chosenhorse = Horse3
  if horse_bet == 4:
    chosenhorse = Horse4
  if horse_bet == 5:
    chosenhorse = Horse5
  if horse_bet == 6:
    chosenhorse = Horse6
  if horse_bet == 7:
    chosenhorse = Horse7
  if horse_bet == 8:
    chosenhorse = Horse8
  if horse_bet == 9:
    chosenhorse = Horse9
  if horse_bet == 10:
    chosenhorse = Horse10
  confirm_bet = input(f"You wish to place a bet on {chosenhorse}, correct? (y/n)- ")
  print(" ")
  if confirm_bet == "n":
    while True:
      horse_bet = int(input("Reselect the horse you wish to bet on- "))
      print(" ")
      if horse_bet == 1:
        chosenhorse = Horse1
        break
      if horse_bet == 2:
        chosenhorse = Horse2
        break
      if horse_bet == 3:
        chosenhorse = Horse3
        break
      if horse_bet == 4:
        chosenhorse = Horse4
        break
      if horse_bet == 5:
        chosenhore = Horse5
        break
      if horse_bet == 6:
        chosenhorse = Horse6
        break
      if horse_bet == 7:
        chosenhorse = Horse7
        break
      if horse_bet == 8:
        chosenhorse = Horse8
        break
      if horse_bet == 9:
        chosenhorse = Horse9
        break
      if horse_bet == 10:
        chosenhorse = Horse10
        break
      confirm_bet = input(f"You wish to place a bet on {chosenhorse}, correct? (y/n)- ")
      print(" ")
  ask_bet_type = int(input("What type of bet do you want to place, 1.Win, 2.Place- "))
  print(" ")
  if ask_bet_type == 1:
    bet_type = "win"
  elif ask_bet_type == 2:
    bet_type = "place"
  elif ask_bet_type > 2 or ask_bet_type < 0:
    print(" ")
    ask_bet_type = int(input("Inavlid option, What type of bet do you want to place, 1.Win, 2.Place- "))
  money_bet = int(input("How much money do you want to bet- "))
  print(" ")
  if money_bet > money:
    print("Invalid Option, bets must be under current amount of money.")
    print(" ")
    money_bet = int(input("How much money do you want to bet- "))
    print(" ")
  confirm_money_bet = input(f"You wish to place a bet of {money_bet}, correct? (y/n)- ")
  print(" ")
  if confirm_money_bet == "n":
    while True:
      money_bet = int(input("Reselect the money you wish to bet- "))
      print(" ")
      confirm_money_bet = input(f"You wish to place a bet of {money_bet}, correct? (y/n)- ")
      break
  if confirm_money_bet == "y":
    money = money - money_bet
    print(f"Current money: {money}")
    print(" ")
  time.sleep(3)
  os.system('clear')
  print("OK, all bets have been placed! We will now start the races!")
  time.sleep(3)
  os.system('clear')
  print("3")
  time.sleep(1)
  os.system('clear')
  print("2")
  time.sleep(1)
  os.system('clear')
  print("1")
  time.sleep(1)
  os.system('clear')
  print("Go!")
  time.sleep(0.75)
  os.system('clear')
  while winner_decided == False:
    print(f"{Horse1} Distance Traveled:")
    print(f"{h1_d}/100")
    print(" ")
    print(f"{Horse2} Distance Traveled:")
    print(f"{h2_d}/100")
    print(" ")
    print(f"{Horse3} Distance Traveled:")
    print(f"{h3_d}/100")
    print(" ")
    print(f"{Horse4} Distance Traveled:")
    print(f"{h4_d}/100")
    print(" ")
    print(f"{Horse5} Distance Traveled:")
    print(f"{h5_d}/100")
    print(" ")
    print(f"{Horse6} Distance Traveled:")
    print(f"{h6_d}/100")
    print(" ")
    print(f"{Horse7} Distance Traveled:")
    print(f"{h6_d}/100")
    print(" ")
    print(f"{Horse8} Distance Traveled:")
    print(f"{h8_d}/100")
    print(" ")
    print(f"{Horse9} Distance Traveled:")
    print(f"{h9_d}/100")
    print(" ")
    print(f"{Horse10} Distance Traveled:")
    print(f"{h10_d}/100")
    print(" ")

    h1_d = h1_d + h1_sp
    h2_d = h2_d + h2_sp
    h3_d = h3_d + h3_sp
    h4_d = h4_d + h4_sp
    h5_d = h5_d + h5_sp
    h6_d = h6_d + h6_sp
    h7_d = h7_d + h7_sp
    h8_d = h8_d + h8_sp
    h9_d = h9_d + h9_sp
    h10_d = h10_d + h10_sp

    if h1_d >= 25:
      h1_sp = random.randint(1, 7)
    elif h1_d >= 50:
      h1_sp = random.randint(1, 7)
    elif h1_d >= 75:
      h1_sp = random.randint(1, 7)
      
    if h2_d >= 25:
      h2_sp = random.randint(1, 7)
    elif h2_d >= 50:
      h2_sp = random.randint(1, 7)
    elif h2_d >= 75:
      h2_sp = random.randint(1, 7)

    if h3_d >= 25:
      h3_sp = random.randint(1, 7)
    elif h3_d >= 50:
      h3_sp = random.randint(1, 7)
    elif h3_d >= 75:
      h3_sp = random.randint(1, 7)
    
    if h4_d >= 25:
      h4_sp = random.randint(1, 7)
    elif h4_d >= 50:
      h4_sp = random.randint(1, 7)
    elif h4_d >= 75:
      h4_sp = random.randint(1, 7)

    if h5_d >= 25:
      h5_sp = random.randint(1, 7)
    elif h5_d >= 50:
      h5_sp = random.randint(1, 7)
    elif h5_d >= 75:
      h5_sp = random.randint(1, 7)

    if h6_d >= 25:
      h6_sp = random.randint(1, 7)
    elif h6_d >= 50:
      h6_sp = random.randint(1, 7)
    elif h6_d >= 75:
      h6_sp = random.randint(1, 7)

    if h7_d >= 25:
      h7_sp = random.randint(1, 7)
    elif h7_d >= 50:
      h7_sp = random.randint(1, 7)
    elif h7_d >= 75:
      h7_sp = random.randint(1, 7)

    if h8_d >= 25:
      h8_sp = random.randint(1, 7)
    elif h8_d >= 50:
      h8_sp = random.randint(1, 7)
    elif h8_d >= 75:
      h8_sp = random.randint(1, 7)

    if h9_d >= 25:
      h9_sp = random.randint(1, 7)
    elif h9_d >= 50:
      h9_sp = random.randint(1, 7)
    elif h9_d >= 75:
      h9_sp = random.randint(1, 7)

    if h10_d >= 25:
      h10_sp = random.randint(1, 7)
    elif h10_d >= 50:
      h10_sp = random.randint(1, 7)
    elif h10_d >= 75:
      h10_sp = random.randint(1, 7)
      
    if winner == False:
      winner_horse = "None"
    if second_place == False:
      second_place_horse = "None"
    if third_place == False:
      third_place_horse = "None"
    print(" ")
    print("---------------------")
    print(f"1st place: {winner_horse}")
    print(f"2nd place: {second_place_horse}")
    print(f"3rd place: {third_place_horse}")
    time.sleep(1)
    os.system('clear')
    

    if h1_d >= 100:
      done1 = True
      h1_sp = 0
      if first_place == False:
        winner = True
        horse1 = "winner"
        first_place = True
        if winner == True and horse1 == "winner":
          winner_horse = Horse1
      elif first_place == True and horse1 != "winner":
        if second_place == False:
          second_place = True
          horse1 = "place2"
          if second_place == True and horse1 == "place2":
            second_place_horse = Horse1
        elif second_place == True and horse1 != "place2":
          if third_place == False:
            third_place = True
            horse1 = "place3"
            if third_place == True and horse1 == "place3":
              third_place_horse = Horse1
            
    
    if h2_d >= 100:
      done2 = True
      h2_sp = 0
      if first_place == False:
        winner = True
        horse2 = "winner"
        first_place = True
        if winner == True and horse2 == "winner":
          winner_horse = Horse2
      elif first_place == True and horse2 != "winner":
        if second_place == False:
          second_place = True
          horse2 = "place2"
          if second_place == True and horse2 == "place2":
            second_place_horse = Horse2
        elif second_place == True and horse2 != "place2":
          if third_place == False:
            third_place = True
            horse2 = "place3"
            if third_place == True and horse2 == "place3":
              third_place_horse = Horse2
          
    if h3_d >= 100:
      done3 = True
      h3_sp = 0
      if first_place == False:
        winner = True
        horse3 = "winner"
        first_place = True
        if winner == True and horse3 == "winner":
          winner_horse = Horse3
      elif first_place == True and horse3 != "winner":
        if second_place == False:
          second_place = True
          horse3 = "place2"
          if second_place == True and horse3 == "place2":
            second_place_horse = Horse3
        elif second_place == True and horse3 != "place2":
          if third_place == False:
            third_place = True
            horse3 = "place3"
            if third_place == True and horse3 == "place3":
              third_place_horse = Horse3
          
    if h4_d >= 100:
      done4 = True
      h4_sp = 0
      if first_place == False:
        winner = True
        horse4 = "winner"
        first_place = True
        if winner == True and horse4 == "winner":
          winner_horse = Horse4
      elif first_place == True and horse4 != "winner":
        if second_place == False:
          second_place = True
          horse4 = "place2"
          if second_place == True and horse4 == "place2":
            second_place_horse = Horse4
        elif second_place == True and horse4 != "place2":
          if third_place == False:
            third_place = True
            horse4 = "place3"
            if third_place == True and horse4 == "place3":
              third_place_horse = Horse4
          
    if h5_d >= 100:
      done5 = True
      h5_sp = 0
      if first_place == False:
        winner = True
        horse5 = "winner"
        first_place = True
        if winner == True and horse5 == "winner":
          winner_horse = Horse5
      elif first_place == True and horse5 != "winner":
        if second_place == False:
          second_place = True
          horse5 = "place2"
          if second_place == True and horse5 == "place2":
            second_place_horse = Horse5
        elif second_place == True and horse5 != "place2":
          if third_place == False:
            third_place = True
            horse5 = "place3"
            if third_place == True and horse5 == "place3":
              third_place_horse = Horse5

    
    if h6_d >= 100:
      done6 = True
      h6_sp = 0
      if first_place == False:
        winner = True
        horse6 = "winner"
        first_place = True
        if winner == True and horse6 == "winner":
          winner_horse = Horse6
      elif first_place == True and horse6 != "winner":
        if second_place == False:
          second_place = True
          horse6 = "place2"
          if second_place == True and horse6 == "place2":
            second_place_horse = Horse6
        elif second_place == True and horse6 != "place2":
          if third_place == False:
            third_place = True
            horse6 = "place3"
            if third_place == True and horse6 == "place3":
              third_place_horse = Horse6


    if h7_d >= 100:
      done7 = True
      h7_sp = 0
      if first_place == False:
        winner = True
        horse7 = "winner"
        first_place = True
        if winner == True and horse7 == "winner":
          winner_horse = Horse7
      elif first_place == True and horse7 != "winner":
        if second_place == False:
          second_place = True
          horse7 = "place2"
          if second_place == True and horse7 == "place2":
            second_place_horse = Horse7
        elif second_place == True and horse7 != "place2":
          if third_place == False:
            third_place = True
            horse7 = "place3"
            if third_place == True and horse7 == "place3":
              third_place_horse = Horse7

    if h8_d >= 100:
      done8 = True
      h8_sp = 0
      if first_place == False:
        winner = True
        horse8 = "winner"
        first_place = True
        if winner == True and horse8 == "winner":
          winner_horse = Horse8
      elif first_place == True and horse8 != "winner":
        if second_place == False:
          second_place = True
          horse8 = "place2"
          if second_place == True and horse8 == "place2":
            second_place_horse = Horse8
        elif second_place == True and horse8 != "place2":
          if third_place == False:
            third_place = True
            horse8 = "place3"
            if third_place == True and horse8 == "place3":
              third_place_horse = Horse8

    if h9_d >= 100:
      done9 = True
      h9_sp = 0
      if first_place == False:
        winner = True
        horse9 = "winner"
        first_place = True
        if winner == True and horse9 == "winner":
          winner_horse = Horse9
      elif first_place == True and horse9 != "winner":
        if second_place == False:
          second_place = True
          horse7 = "place2"
          if second_place == True and horse9 == "place2":
            second_place_horse = Horse9
        elif second_place == True and horse9 != "place2":
          if third_place == False:
            third_place = True
            horse9 = "place3"
            if third_place == True and horse9 == "place3":
              third_place_horse = Horse9

    if h10_d >= 100:
      done10 = True
      h10_sp = 0
      if first_place == False:
        winner = True
        horse10 = "winner"
        first_place = True
        if winner == True and horse10 == "winner":
          winner_horse = Horse10
      elif first_place == True and horse10 != "winner":
        if second_place == False:
          second_place = True
          horse7 = "place2"
          if second_place == True and horse10 == "place2":
            second_place_horse = Horse10
        elif second_place == True and horse10 != "place2":
          if third_place == False:
            third_place = True
            horse7 = "place3"
            if third_place == True and horse10 == "place3":
              third_place_horse = Horse10
            
      if done1 == True and done2 == True and done3 == True and done4 == True and done5 == True and done6 == True and done7 == True and done8 == True and done9 == True and done10 == True:
        break
  if horse_bet == 1:
    chosenhorse = horse1
  if horse_bet == 2:
    chosenhorse = horse2
  if horse_bet == 3:
    chosenhorse = horse3
  if horse_bet == 4:
    chosenhorse = horse4
  if horse_bet == 5:
    chosenhorse = horse5
  if horse_bet == 6:
    chosenhorse = horse6
  if horse_bet == 7:
    chosenhorse = horse7
  if horse_bet == 8:
    chosenhorse = horse8
  if horse_bet == 9:
    chosenhorse = horse9
  if horse_bet == 10:
    chosenhorse = horse10
  if bet_type == "win":
    if chosenhorse == "winner":
      print(f"Your horse won! You won {money_bet * 3}!")
      money = money + (money_bet * 3)
      print(f"Current money: {money}")
    else:
      print("Your horse didn't win, better luck next time.")
  if bet_type == "place":
      if chosenhorse == "winner" or chosenhorse == "place2" or chosenhorse == "place3":
        print(f"Your horse placed! You won {money_bet * 2}!")
        money = money + (money_bet * 2)
        print(" ")
        print(f"Current money: {money}")
      else:
        print("Your horse didn't place, better luck next time.")

  time.sleep(3)
  os.system('clear')
  print(f"Current money: {money}")
  back_to_menu = input("Do you wish to return to the menu? (y/n)- ")
  if back_to_menu == "y":
    os.system('clear')
    StartScreen(money)
  elif back_to_menu == "n":
    print("See you soon!")
    time.sleep(1)
    sys.exit()



def Restart():
  ask = input("Do you want to restart? (y/n)- ")
  ask.lower()
  if ask == "y":
    StartScreen(money)
  elif ask == "n":
    sys.exit()

StartScreen(money)