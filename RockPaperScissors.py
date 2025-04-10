import random


print("===================")
print("Rock Paper Scissors Lizard Spock")
print("===================")
print("1)✊") 
print("2)✋")
print("3)✌️")
print("4)🦎")
print("5)🖖")

ans = int(input("Pick a number: "))
compchoice = random.randint(1,5)

if ans == 1:
    temp1 = "✊"
elif ans == 2:
   temp1 = "✋"
elif ans == 3:
   temp1 = "✌️"
elif ans == 4:
   temp1 = "🦎"
elif ans == 5:
   temp1 = "🖖"

if compchoice == 1:
    temp2 = "✊"
elif compchoice == 2:
   temp2 = "✋"
elif compchoice == 3:
   temp2 = "✌️"
elif compchoice == 4:
   temp2 = "🦎"
elif compchoice == 5:
   temp2 = "🖖"


print("You chose: ", temp1)
print("Computer chose: ",temp2)

if ans == 1 and (compchoice == 3 or compchoice == 4):
    print("You win")
elif ans == 1 and (compchoice == 2 or compchoice == 5):
    print("Computer wins")

if ans == 2 and (compchoice == 1 or compchoice == 5):
    print("You win")
elif ans == 2 and (compchoice == 3 or compchoice == 4):
    print("Computer wins")

if ans == 3 and (compchoice == 2 or compchoice == 4):
    print("You win")
elif ans == 3 and (compchoice == 1 or compchoice == 5):
    print("Computer wins")

if ans == 4 and (compchoice == 5 or compchoice == 2):
    print("You win")
elif ans == 4 and (compchoice == 1 or compchoice == 3):
    print("Computer wins")

if ans == 5 and (compchoice == 1 or compchoice == 3):
    print("You win")
elif ans == 5 and (compchoice == 2 or compchoice == 4):
    print("Computer wins")

elif ans == compchoice:
    print("It's a tie")