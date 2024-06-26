import random
friends = {}
print('Enter the number of friends joining (including you):')
num = int(input())
if num >0:
    print('Enter the name of every friend (including you), each on a new line:')
    for i in range(0,num):
        name= input()
        friends[name] = 0
    print('Enter the total bill value:')
    bill = int(input())
    split = round(bill/num,2)
    for key in friends:
        friends[key] = split
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    choice = input()
    if choice == 'Yes':
        lucky = random.choice(list(friends.keys()))
        print(f'{lucky} is the lucky one!')
        split = round(bill / (num-1), 2)
        for key in friends:
            friends[key] = split
        friends[lucky] = 0
        print(friends)
    else:
        print('No one is going to be lucky')
        print(friends)
    #print(friends)
elif num<=0:
    print('No one is joining for the party')