import os

do=""
while do!="N":
  
  S = " "*15
  N = "   "
  X = " X "
  O = " O "
  p1 = p2 = p3 = p4 = p5 = p6 = p7 = p8 = p9 = N
  count = 0

  def title():
     print(" _____ _     _____  v1.1   _____ by DHMe\n|_   _(_) __|_   ___ _  __|_   ____   ___\n  | | | |/ __|| |/ _` |/ __|| |/ _ \ / _ \\\n  | | | | (__ | | (_| | (__ | | (_) |  __/\n  |_| |_|\___||_|\__,_|\___||_|\___/ \___|\n")

  def XorO():
    if count % 2 == 0:
      return X
    else:
      return O

  while True:
    os.system("clear")
    title()
    print(f"{S}{chr(95)*11}\n{S}|{p1}{p2}{p3}|\n{S}|{p4}{p5}{p6}|\n{S}|{p7}{p8}{p9}|\n{S}{chr(175)*11}")
    if p1==p2==p3!=N or p4==p5==p6!=N or p7==p8==p9!=N or p1==p4==p7!=N or p2==p5==p8!=N or p3==p6==p9!=N or p1==p5==p9!=N or p1==p4==p7!=N or p3==p5==p7!=N:
      count-=1
      print(f"\nThe winner is {XorO()[1:2]} !\n")
      do=input("Reset? (Y/n): ").upper()
      break
    if p1!=N and p2!=N and p3!=N and p4!=N and p5!=N and p6!=N and p7!=N and p8!=N and p9!=N:
      print("It's a draw!\n")
      do=input("Reset? (Y/n): ").upper()
      break
    user_input=int(input(f"\nChoose a position for {XorO()[1:2]} (1 - 9): "))
    if user_input == 1 and p1==N: p1=XorO(); count+=1
    if user_input == 2 and p2==N: p2=XorO(); count+=1
    if user_input == 3 and p3==N: p3=XorO(); count+=1
    if user_input == 4 and p4==N: p4=XorO(); count+=1
    if user_input == 5 and p5==N: p5=XorO(); count+=1
    if user_input == 6 and p6==N: p6=XorO(); count+=1
    if user_input == 7 and p7==N: p7=XorO(); count+=1
    if user_input == 8 and p8==N: p8=XorO(); count+=1
    if user_input == 9 and p9==N: p9=XorO(); count+=1
