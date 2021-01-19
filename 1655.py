import heapq

#중앙값 기준으로 작은 값 = left, 큰 값 = right
left, right=[],[]

n= int(input())
for _ in range(n):
    num = int(input())
    if len(left) == len(right):
        #max_heap
        heapq.heappush(left,(-num,num))
    else:
        heapq.heappush(right,(num,num))

    # 오른쪽 값에 원소가 있으면서,
    # 왼쪽 값이 오른쪽 값보다 큰 경우 조건에 위배
    if right and left[0][1] > right[0][1] : #left[0][1]이 항상 중앙값.
        left_value = heapq.heappop(left)[1]
        right_value = heapq.heappop(right)[1]
        heapq.heappush(right, (left_value, left_value))
        heapq.heappush(left, (-right_value, right_value))

    print(left[0][1])
'''
나도 문제에서 heap을 이용해야한다고 생각은했지만, 처음부터 마지막까지 계속 정렬되있는 queue가 없기때문에,
위와같이 중간값을 특정한 부분에 있다 설계하고, left는 중간값보다 항상 작은값, right는 중간값보다 항상 큰값을 넣어서
조건에 위배되지않게 만들어주면, 문제에서 설계하고자 하는 바대로 중간값을 O(nlogn)으로 찾을수있다.
heap을 이용하는 방법.

'''
