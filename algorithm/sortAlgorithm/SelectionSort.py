# 선택 정렬 (Selection sort)
# 여러분의 컴퓨터에 음악이 많이 저장되어 있다고 가정하자.
# 가수별로 몇 곡이 들었는지 기록되어 있다.
# 이 목록을 가장 많이 들은 것부터 가장 적게 들은 것 순서로 정렬하여
# 가장 좋아하는 가수 순위를 알고 싶다면??
# 한 가지 방법은 리스트의 모든 항목을 살펴보고 가장 많이 연주된 가수를 찾아
# 새로운 리스트에 기록하는 것이다.
# 그 다음으로 많이 들은 가수를 찾아서 반복한다.
# 이런 식으로 반복하다보면 정렬된 목록을 얻을 수 있다.

# 연주 횟수가 가장 많은 가수를 찾기 위해서는 목록의 모든 항목을 점검해야 한다.
# 이때는 O(n) 시간이 걸린다. 여기서 O(n) 실행 시간이 걸리는 연산을 n번 해야한다.
# 즉 모두 합해서 O(n x n) 시간, 즉 O(n^2) 시간이 걸린다.

# 예제코드
# 배열을 작은 정수에서 큰 정수 순서로 정렬하는 코드
# 우선 배열에서 가장 작은 원소를 찾는 함수를 작성

def findSmallest(arr):
    smallest = arr[0]       #가장 작은 정수를 저장
    smallest_index = 0      #가장 작은 정수의 인덱스를 저장
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


print (selectionSort([5, 3, 6, 2, 10]))