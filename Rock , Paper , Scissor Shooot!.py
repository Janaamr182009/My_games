#printing a welcome message 
print('welcome to rock,paer,scissors game:')
#asking if the player wants the rules
help_or_complete=input('press Enter to continue or type (help) for the rules').lower()
#printing the rules or continue
if help_or_complete=='help':
  print('''
                    *********Rules*********
                     1)you choose and the computer chooses
                     2)rock smashes scissors-> rock wins
                     3)scissors cut paper-> scissors wins
                     4)paper covers rock-> paper wins''')
else:
  print('lets start')
#writing the choices
choise=['Rock','Paper','Scissors']
#getting the users choices 
users_choise=input('Enter your choise(rock,paper,scissors): ').capitalize()
#checking if it's a real choice
if users_choise not in choise:
  print('Invalid choice please run the program again and choose rock,paper or scissors')
else:
  ok=['ok','right']
#making the system choose randomly
import random
computer_choise=random.choice(choise)
#preparing the choises' asciis
rock_ascii="""
     _______
 ---'   ____)
       (_____)
       (_____)
       (____)
 ---.__(___)
 """
paper_ascii="""
     _______
 ---'   ____)____
           ______)
           _______)
          _______)
 ---.__________)
 """
scissors_ascii="""
     _______
 ---'   ____)____
           ______)
        __________)
       (____)
 ---.__(___)
 """
#printing the user's choice's ascii
if users_choise=='Rock':
  print(f'you chose:\n{rock_ascii}')
elif users_choise=='Paper':
  print(f'you chose:\n{paper_ascii}')
else:
  print(f'you chose:\n{scissors_ascii}')
#printing the systems choice's ascii
if computer_choise=='Rock':
  print(f'computer chose:\n{rock_ascii}')
elif computer_choise=='Paper':
  print(f'computer chose:\n{paper_ascii}')
else:
  print(f'computer chose:\n{scissors_ascii}')
#printing the results
if users_choise=='Paper' and computer_choise=='Rock'or users_choise=='Scissors'and computer_choise== 'Paper' or users_choise=='Rock' and computer_choise=='Scissors':
 print(' you win')
elif users_choise==computer_choise:
  print('its a tie')
else:
  print('you loose')