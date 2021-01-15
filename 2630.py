n=int(input())
papers=[list(map(int,list(input().split()))) for _ in range(n)]
white_count=0
blue_count=0
def find_path(i,j,size):
    global blue_count,white_count
    one_count=0
    zero_count=0
    if size==1:
        if papers[i][j]:
            blue_count+=1
        else:
            white_count+=1
        return
    tok=0
    for x in range(i,i+size):
        for y in range(j,j+size):
            if papers[x][y]:
                one_count+=1
            else:
                zero_count+=1
    
    if zero_count==size**2:
        white_count+=1
        return
    elif one_count==size**2:
        blue_count+=1
        return
    find_path(i,j,size//2)
    find_path(i+size//2,j,size//2)
    find_path(i,j+size//2,size//2)
    find_path(i+size//2,j+size//2,size//2)
        
find_path(0,0,n)
print(white_count)
print(blue_count)
