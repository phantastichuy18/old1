import os
import pyfiglet


def end():
  print("\nPlay again?\n")
  while True:
    user_input = (input("(y/N): "))
    user_input = (user_input).lower()
    if user_input == "y":
      print(batdau())
    if user_input == "n":
      exit()
    else:
      print("Please re-enter! y(Yes) or N (No).")


def banner():
  banner = pyfiglet.figlet_format("h6ngmaN2p")
  print(banner)
  print("                                        #made with Python")
  return ""


def batdau():
  os.system('cls' if os.name == 'nt' else 'clear')
  print(banner())
  print(
    "Welcome to H6ngmaN2p! Let's see what you will type.\n\nHow to play? Enter ?inidhelp to see how to play.\n\nYou are player 1!"
  )

  random_tu = input("Type secret word(can't add line spacing): ").replace(
    " ", "")
  random_tu = random_tu.lower()
  if random_tu == "?inidhelp":
    os.system('cls' if os.name == 'nt' else 'clear')
    print(banner())
    print("About information:")
    print(
      "\n  - Made by me Dam Duc Huy on May 25, 2023.\n  - This is just a learning project of mine!\nThis is an upgraded version of the normal hangman game.\n"
    )
    print("How to play?")
    print(
      "Player 1 is the creator of the secret word for player 2 to guess.\nThis is the upgraded version."
    )
    quit()

  sokytu = len(random_tu)

  os.system('cls' if os.name == 'nt' else 'clear')
  print(banner())

  print("Your secret word :", random_tu)
  print(
    "Please enter the number of incorrect guesses to give player 2 chances.\n")

  mang = (input("Enter the number of incorrect guesses: "))
  if mang.isdigit():
    mang = int(mang)

  else:
    print("Only number.")
    quit()
  if mang == 0:
    print("Can't be 0.")
    quit()
  os.system('cls' if os.name == 'nt' else 'clear')
  print(banner())

  print("Your secret word :", random_tu)
  print("Total number of wrong guesses : ", mang, "\n")
  print("If it's too difficult, you can suggest.")
  print("Type not if you don't want to give suggestions .")
  goiy = input("\nGive suggestions or not: ")

  space2 = []

  for i in range(sokytu):
    space2.append('_')

  os.system('cls' if os.name == 'nt' else 'clear')
  print(banner())

  print("It's your turn, player 2!\n\n")
  print("You have", mang, "incorrect guesses left.", "\n")
  print("Your word is...")
  print(' '.join(space2))
  if goiy == "not":
    print("\nNo suggestions at all!")
  else:
    print("\nSuggestion : ", goiy)
  print("""
          ------------
          |          |
          |       -------------------------------
          |       | I'm not good at programming |
          |       -------------------------------
          |
          |        *this is hangman stages lol*
      ------------
      """)
  while ('_' in space2) and (mang > 0):
    # print("see if there is an error: ", random_tu)
    chon = input("\nGuess a letter: ")
    chon = chon.lower()
    os.system('cls' if os.name == 'nt' else 'clear')

    for i, kytu in enumerate(random_tu):
      if chon == kytu:
        space2[i] = kytu
    print(banner())
    print("It's still your turn, player 2!\n\n")
    print(' '.join(space2))
    if goiy == "not":
      print("\nNo suggestions at all!")
    else:
      print("\nSuggestion : ", goiy)

    if chon in random_tu:
      print("\nYes! The letter is part of the secret word")
    else:
      mang -= 1
      print("\nNo! The letter is not part of the secret word")
    print("\n", "You have", mang, "incorrect guesses left.", "\n")
    print("""
          ------------
          |          |
          |       -------------------------------
          |       | I'm not good at programming |
          |       -------------------------------
          |
          |        *this is hangman stages lol*
      ------------
      """)

  if mang == 0:
    print("Player 1 won!")
    print("The secret word: ", random_tu)
  else:
    print("Player 2 won!")
  print(end())


print(batdau())
