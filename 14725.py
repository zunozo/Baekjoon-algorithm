class Node(object):
    def __init__(self,key):
        self.key=key
        self.child={}
    

class Trie(object):
    def __init__(self):
        self.head=Node(None)

    def insert(self, string):
        curr_node=self.head
        for char in string:
            if char not in curr_node.child:
                curr_node.child[char]=Node(char)
            curr_node=curr_node.child[char]

    def printStructure(self, L, curr_node):
        if L == 0:
            curr_node = self.head

        for ch in sorted(curr_node.child.keys()):
            print('--' * L, ch, sep='')
            self.printStructure(L+1, curr_node.child[ch])

    

n = int(input())
t=Trie()
for _ in range(n):
    k=list(input().split())[1:]
    t.insert(k)

t.printStructure(0,None)
'''
Trie문제
처음에 배웠던구조와는 다르지만, string자체로 trie를 연결하여서 structure를 출력하는 문제,
printstructure는 dfs로 자기자신의 child에 대해서 재귀적으로 함수를 실행할 수 있도록 하였다.
'''
