#writing a welcome massage 
print('******** Welcome to iShop Calculator ********\n')
#Creating an input to get the number of items 
num_items=int(input('How many items are there in your basket today? '))
print('\n Lets get to count them....')
#creating lists to save the items
items=[]
price=[]
#creating a loop to get the item name and price and appened them to the lists
for y in range (1,num_items+1):
  name_item=input(f' please enter the name of item number {y}')
  items.append(name_item)
  price_item=float(input(f'What is the price of{name_item}?\n$'))
  price.append(price_item)
#asking if the costumer wants to see his basket
see_basket=input('Do you want to see your intire basket items?(yes/no) ').lower()
#printing the results
if see_basket=='yes':
  print(items)
elif see_basket=='no':
  ok=['ok']
else:
  print('i dont get it')
#asking if the costumer wants to see the cost of the items
see_cost=input('Would you like to know how much it will cost? ')
#printing the results
if see_cost=='yes':
  print('\nBuying these items will cost:')
  print(f'${sum(price)}')
elif see_cost=='no':
  ok=['ok']
else:
  print('i dont get it')
  
