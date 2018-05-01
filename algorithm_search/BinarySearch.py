# 이진탐색은 입력으로는 정렬된 원소 리스트를 받는다.
# 리스트에 원하는 원소가 있으면 그 원소의 위치를 반환하고, 아니면 null 값을 반환
# 1~100 사이의 숫자를 하나 찾을 때 100의 중간, 즉 50부터 시작한다.
# 이진 탐색에서는 매번 남은 숫자 중의 가운데 숫자를 말하고 대답에 따라
# 그보다 큰 숫자 혹은 작은 숫자들을 한꺼번에 없앨 수 있다. 
# 만약 n개의 원소를 가진 리스트에서 이진탐색을 사용하면 최대 log2n번만에 답을 찾을 수 있다
# 단순 탐색이면 최대 n번이 필요할 수도 있다


#이진탐색

def binary_search(list, item):
    low = 0
    high = len(list)-1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]

        if guess == item:       # item을 찾았습니다.
            return mid
        if guess > item:        # 추측한 숫자가 너무 크다
            high = mid - 1
        else:                   # 추측한 숫자가 너무 작다
            low = mid + 1
    return None

my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))
print(binary_search(my_list, -1))
