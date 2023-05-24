import random
import os
import pyfiglet

os.system('cls' if os.name == 'nt' else 'clear')
danh_sach_tu = [
  "kiwi", "mango", "pineapple", "peach", "papaya", "avocado", "watermelon",
  "grapefruit", "passionfruit", "dragonfruit", "pomegranate", "guava",
  "lychee", "jackfruit", "orange", "strawberry", "apple"
]
banner = pyfiglet.figlet_format("hangman")
print(banner)
print(
  "                                        #made by Đàm Đức Huy\n")  # hello
print("Welcome to Hangman! Let's see if you can guess this word!\n")

random_tu = random.choice(danh_sach_tu)

sokytu = len(random_tu)
mang = 7
space2 = []

for i in range(sokytu):
  space2.append('_')

print("Your remaining lives:", mang, "!\n")
print("Your word is...")
print(space2)


def get_hangman_stage(mang):
  max_attempts = 7
  stages = [
    """
        |
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


print(get_hangman_stage(7))
while ('_' in space2) and (mang > 0):
  # print("see if there is an error: ", random_tu)
  chon = input("\nGuess a letter: ")
  os.system('cls' if os.name == 'nt' else 'clear')
  ketqua = ''

  for i, kytu in enumerate(random_tu):
    if chon == kytu:
      space2[i] = kytu
  print(banner)
  print("                                        #made by Đàm Đức Huy\n")
  print(' '.join(space2))

  if chon in random_tu:
    print("\nYes! The letter is part of the secret word")
  else:
    mang -= 1
    print("\nNo! The letter is not part of the secret word")
  print("\nYour remaining lives:", mang, "!")
  print(get_hangman_stage(mang))

if mang == 0:
  print("You lost!")
else:
  print("You won!")
