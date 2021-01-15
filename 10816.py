from collections import defaultdict
n=int(input())
card_dic=defaultdict(int)
card=list(input().split(' '))
card=list(map(int,card))
for i in card:
    card_dic[i]+=1
m=int(input())
m_list=list(input().split(' '))
m_list=list(map(int,m_list))
for i in range(m):
    if i==m-1:
        print(card_dic[m_list[i]])
    else:
        print(card_dic[m_list[i]], end=' ')
