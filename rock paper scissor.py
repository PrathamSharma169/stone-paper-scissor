import random as r
import time
def rps():
    n=int(input("how many rounds do you want ?\n"))
    user=0
    computer=0
    for i in range(n):
        time.sleep(1)
        print(f'here start round {i+1} ')
        time.sleep(1)
        print("rock , paper , scissor..........\n")
        s=input("choose any one you prefer \n")
        time.sleep(1)
        list=['rock' , 'paper' , 'scissor']
        c=r.choice(list)
        time.sleep(1)
        print(c)
        if s=='rock' and c=='scissor':
            print('congrats you win :)')
            user=user+1
        elif s=='paper' and c=='rock':
            print('congrats you win :)')
            user=user+1
        elif s=='scissor' and c=='paper' :
            print('congrats you win :)')
            user=user+1
        elif c=='rock' and s=='scissor' :
            print('you lost :(')
            computer=computer+1
        elif c=='paper' and s=='rock' :
            print('you lost :(')
            computer=computer+1
        elif c=='scissor' and s=='paper' :
            print('you lost :(')
            computer=computer+1
        elif s==c:
            print('there is a tie')
        
    print('final scorecard :-')
    time.sleep(1)
    print(f'score of user is -------------> {user}\nscore of computer is ------------->{computer}')
    print('result ->')
    time.sleep(1)
    if user>computer :
        print('congrats you win :)')
    elif computer>user:
        print('you lost :(')
    else :
        print('there is a tie ')
print('welcome to the epic rock , paper , scissor game introduced to you by one and only Pratham Sharma ')
rps()



