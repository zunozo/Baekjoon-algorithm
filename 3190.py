from collections import defaultdict,deque
n=int(input())
k=int(input())
apple=defaultdict(int)
for _ in range(k):
    i,j=map(int,input().split())
    apple[i,j]=1
l=int(input())
move_list=deque()
for _ in range(l):
    move_list.append(list(input().split()))

board=[[0] * (n+1) for _ in range(n+1)]
def rotate_move(rotate,c):
    if rotate=='R':
        if c=='L':
            return 'U'
        else:
            return 'D'
    elif rotate=='L':
        if c=='L':
            return 'D'
        else:
            return 'U'
    elif rotate=='U':
        if c=='L':
            return 'L'
        else:
            return 'R'
    else:
        if c=='L':
            return 'R'
        else:
            return 'L'

def move():
    global board,apple
    length=1
    i,j=1,1
    time=0
    rotate='R'
    while 1:
        #move
        if move_list and time==int(move_list[0][0]):
            x,c=move_list.popleft()
            rotate=rotate_move(rotate,c)
        if rotate=='R':
            j+=1
        elif rotate=='L':
            j-=1
        elif rotate=='D':
            i+=1
        else:
            i-=1
        if i<1 or i>n or j<1 or j>n: #벗어난다면
            return time+1
        if board[i][j]>0 and length>3 and length > time-board[i][j]:#자기자신의 몸과 부딪힐때
            return time+1
        time+=1
        board[i][j]=time
        if apple[i,j]:
            apple[i,j]=0
            length+=1
print(move())        

''' 구현 '''
