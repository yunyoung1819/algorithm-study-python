# Chapter 6. 너비 우선 탐색 구현하기

# 알고리즘이 구현되는 방식은 다음과 같다.

# 1. 확인할 사람의 명단을 넣을 큐를 준비한다.
# 2. 큐에서 한 사람을 꺼낸다.
# 3. 이 사람이 망고 판매상인지 확인한다.
# 4-a. 예 -> 작업 완료!
# 4-b. 아니요 -> 그 사람의 이웃을 모두 큐에 추가한다.
# 5. 반복문
# 6. 만약 큐가 비어있으면 네트워크에는 망고 판매상이 없다.

from collections import deque


graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"]= []
graph["jonny"] = []

def person_is_seller(name):
    return name[-1] == 'm'

def search(name):
    search_queue = deque()   # 새 큐를 생성
    search_queue += graph[name]  # 모든 이웃을 탐색 큐에 추가
    searched = []   # 이 배열은 이미 확인한 사람을 추적하기 위한 것

    while search_queue:  # 큐가 비어있지 않는 한 계속 실행
        person = search_queue.popleft() # 큐의 첫번째 사람을 꺼냄
        if not person in searched:   # 이전에 확인하지 않은 사람만 확인
            if person_is_seller(person): # 망고 판매상인지 확인
                print (person + " is a mango seller!")    # 망고 판매상이 맞음
                return True
            else:
                search_queue += graph[person]  # 망고 판매상이 아님. 모든 이웃을 탐색 목록에 추가
                searched.append(person) # 이 사람을 확인한 것으로 표시
    return False    # 여기에 도달했다는 것은 망고 판매상이 아무도 없다는 의미


search("you")
