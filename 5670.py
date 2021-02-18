import sys

class Node():
    def __init__(self, key, data=None):
        self.key=key
        self.data=data
        self.child={}

class Trie():
    def __init__(self):
        self.head=Node(None)

    def insert(self,string):
        curr_node=self.head
        for char in string:
            if char not in curr_node.child:
                curr_node.child[char]=Node(char)
            curr_node=curr_node.child[char]
        curr_node.data=string

    def count(self,string):
        curr_node=self.head.child[string[0]]
        i,cnt,str_len=1,1,len(string)
        while i<str_len:
            if len(curr_node.child.keys())!=1 or curr_node.data:
                cnt+=1
            curr_node=curr_node.child[string[i]]
            i+=1
        return cnt

while True:
    try:
        n=int(sys.stdin.readline())
    except :
        break
    t=Trie()
    string=[]
    for _ in range(n):
        ch=input()
        string.append(ch)
        t.insert(ch)
    summ=0
    for char in string:
        summ+=t.count(char)
    print("{0:0.2f}".format(summ/len(string)))

'''
Trie 구현
알게된점
format 형식
"{내가원하는 형태}".format(변수)
{0:0.2f}로 하면, 0은 모두, 소수점은 2자리까지.
{1:0.3f}로 하면, 정수 1자리, 소수점은 3자리까지.

EOF까지 입력받는법
sys.stdin.readline으로 try를 이용해서 입력받다가
except에 EOFError가 걸리면 break로 빠져나가면된다.
'''
