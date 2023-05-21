import os; import random; import platform

def title(): print(" _____ _     _____  v1.3   _____ by DHMe\n|_   _(_) __|_   ___ _  __|_   ____   ___\n  | | | |/ __|| |/ _` |/ __|| |/ _ \ / _ \\\n  | | | | (__ | | (_| | (__ | | (_) |  __/\n  |_| |_|\___||_|\__,_|\___||_|\___/ \___|\n")

def board(): print(f"{' '*15}{chr(95)*11}\n{' '*15}|{p1}{p2}{p3}|\n{' '*15}|{p4}{p5}{p6}|\n{' '*15}|{p7}{p8}{p9}|\n{' '*15}{chr(175)*11}")

def XorO():
  if count % 2 == 0:
    return X
  else:
    return O

if platform.system() == "Windows":
  def clear(): os.system("cls")
else:
  def clear(): os.system("clear")

N = "   "
X = " X "
O = " O "

while True:
  clear()
  
  if 'do' in locals() and do == "N": del count
  
  if not 'count' in locals():
    title()
    choice = input("Welcome to TicTacToe!\n [1] Play vs Player\n [2] Play vs Bot\n [3] Exit\n  ")
  
  p1 = p2 = p3 = p4 = p5 = p6 = p7 = p8 = p9 = N
  
  if choice == "1":
    count = 0
    while True:
      clear()
      title()
      board()
      if p1==p2==p3!=N or p4==p5==p6!=N or p7==p8==p9!=N or p1==p4==p7!=N or p2==p5==p8!=N or p3==p6==p9!=N or p1==p5==p9!=N or p1==p4==p7!=N or p3==p5==p7!=N:
        count-=1
        print(f"\nThe winner is {XorO()[1:2]} !\n")
        do=input("Reset? (Y/n): ").upper()
        break
      if p1!=N and p2!=N and p3!=N and p4!=N and p5!=N and p6!=N and p7!=N and p8!=N and p9!=N:
        print("It's a draw!\n")
        do=input("Reset? (Y/n): ").upper()
        break
      num=int(input(f"\nChoose a position for {XorO()[1:2]} (1 - 9): "))
      if num == 1 and p1==N: p1=XorO(); count+=1
      if num == 2 and p2==N: p2=XorO(); count+=1
      if num == 3 and p3==N: p3=XorO(); count+=1
      if num == 4 and p4==N: p4=XorO(); count+=1
      if num == 5 and p5==N: p5=XorO(); count+=1
      if num == 6 and p6==N: p6=XorO(); count+=1
      if num == 7 and p7==N: p7=XorO(); count+=1
      if num == 8 and p8==N: p8=XorO(); count+=1
      if num == 9 and p9==N: p9=XorO(); count+=1
  
  elif choice == "2":
    count = 0
    while True:
      clear()
      title()
      board()
      if p1==p2==p3!=N or p4==p5==p6!=N or p7==p8==p9!=N or p1==p4==p7!=N or p2==p5==p8!=N or p3==p6==p9!=N or p1==p5==p9!=N or p1==p4==p7!=N or p3==p5==p7!=N:
        count-=1
        if XorO()[1:2] == "X": print("\nYou win!\n")
        if XorO()[1:2] == "O": print("\nYou lose!\n")
        do=input("Reset? (Y/n): ").upper()
        break
      if p1!=N and p2!=N and p3!=N and p4!=N and p5!=N and p6!=N and p7!=N and p8!=N and p9!=N:
        print("It's a draw!\n")
        do=input("Reset? (Y/n): ").upper()
        break
      if XorO()[1:2] == "X":
        num=int(input(f"\nChoose a position (1 - 9): "))
      if XorO()[1:2] == "O":
        num = random.randint(1,9)
      if num == 1 and p1==N: p1=XorO(); count+=1
      if num == 2 and p2==N: p2=XorO(); count+=1
      if num == 3 and p3==N: p3=XorO(); count+=1
      if num == 4 and p4==N: p4=XorO(); count+=1
      if num == 5 and p5==N: p5=XorO(); count+=1
      if num == 6 and p6==N: p6=XorO(); count+=1
      if num == 7 and p7==N: p7=XorO(); count+=1
      if num == 8 and p8==N: p8=XorO(); count+=1
      if num == 9 and p9==N: p9=XorO(); count+=1
  
  elif choice == "3": exit()
