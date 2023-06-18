import random
import os


def sieunhangao():

  def get_hangman_stage(mang):
    max_attempts = 7
    stages = [
      """
          ------
          |
          |
          |
          |
          |
          |
      ------------
      """, """
          ------
          |    |
          |
          |
          |
          |
          |
      ------------
      """, """
          ------
          |    |
          |    O
          |
          |
          |
          |
      ------------
      """, """
          ------
          |    |
          |    O
          |    |
          |    |
          |
          |
      ------------
      """, """
          ------
          |    |
          |    O
          |  --|
          |    |
          |
          |
      ------------
      """, """
          ------
          |    |
          |    O
          |  --|--
          |    |
          |
          |
      ------------
      """, """
          ------
          |    |
          |    O
          |  --|--
          |    |
          |   / 
          |
      ------------
      """, """
          ------
          |    |
          |    O
          |  --|--
          |    |
          |   / \\
          |
      ------------
      """
    ]
    return stages[max_attempts - mang]

  os.system('cls' if os.name == 'nt' else 'clear')
  danh_sach_tu = [
    "banana", "apple", "orange", "grapefruit", "strawberry", "watermelon",
    "mango", "pineapple", "kiwi", "pear", "peach", "cherry", "blueberry",
    "raspberry", "plum", "lemon", "lime", "coconut", "pomegranate", "avocado",
    "fig", "grapes", "apricot", "blackberry", "cranberry", "guava", "papaya",
    "passionfruit", "dragonfruit", "melon"
  ]
  random_tu = random.choice(danh_sach_tu)

  def banner():
    print("""
 _                 __ _                    
| |_   __ _  _ _  / _` | _ __   __ _  _ _  
|   \ / _` || ' \ \__. || '  \ / _` || ' \ 
|_||_|\__/_||_||_||___/ |_|_|_|\__/_||_||_|

""")
    print("                                        # made with python")
    return ""

  def batdau():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(banner())
    print("Welcome to Hangman! Let's see if you can guess this word!\n")

    sokytu = len(random_tu)
    mang = 7
    space2 = []

    for i in range(sokytu):
      space2.append('_')

    print("You have", mang, "incorrect guesses left.", "\n")
    print("Your word is...")
    print(' '.join(space2))

    print(get_hangman_stage(7))

    while ('_' in space2) and (mang > 0):
      # print("see if there is an error: ", random_tu)
      chon = input("\nGuess a letter: ")
      chon = chon.lower()
      os.system('cls' if os.name == 'nt' else 'clear')

      for i, kytu in enumerate(random_tu):
        if chon == kytu:
          space2[i] = kytu
      print(banner())
      print(' '.join(space2))

      if len(chon) == 1 and chon == chon.lower():
        if chon in random_tu:
          print("\nYes! The letter", chon, "is part of the secret word.")
        else:
          mang -= 1
          print("\nNo! The letter", chon, "is not part of the secret word.")
      else:
        print("\nPlease input 1 letter.")

      print("\nYou have", mang, "incorrect guesses left.")
      print(get_hangman_stage(mang))

    if mang == 0:
      print("You lost!")
      print("The secret word: ", random_tu)
      print(end())
    else:
      print("You won!")
      print(end())
    return ""

  def end():
    print("\nPlay again?\n")
    while True:
      user_input = (input("(y/N): "))
      user_input = (user_input).lower()
      if user_input == "y":
        print(sieunhangao())
      if user_input == "n":
        exit()
      else:
        print("Please re-enter! y(Yes) or N (No).")

  print(batdau())


print(sieunhangao())
