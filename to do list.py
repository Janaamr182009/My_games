#creating lists to add the tasks for
ongoing_task=[]
done_task=[]
#asking for the tasks
tasks=input('Enter your tasks for today separated by coma then space: ').split(', ')
#asking if user finished the tasks or no and adding it to the proper list
for task in tasks:
  print(f'\n{task}\n')
  did=input(f'Did you finished {task} already?\n').lower()
  if did=='yes':
    print('Nice Job!')
    done_task.append(task)
  else:
    print('Try not to put it off')
    ongoing_task.append(task)
  print('------')
#asking if the user wants to see his proggres
progres=input('Do you want to see your progress today?(yes/no)\n').lower()
if progres =='yes':
  print('\n           ********* Done Tasks *****\n')
  print(done_task)
  print('\n             ********* Ongoing Tasks *****\n')
  print(ongoing_task)
else:
  input('Press Enter to exit')
  