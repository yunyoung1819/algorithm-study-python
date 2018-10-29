## 다익스트라 알고리즘 (dijkstra algorithm)

graph = {}

# 이웃 정점과 함께 그 이웃의 가격도 저장해야함

graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}  # 도착점에는 이웃이 없다.

# 출발점의 모든 이웃값 출력하기
# print(graph["start"].keys())

# 가격 테이블
infinity = float("inf") # 파이썬에서 무한대 표시

costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# 부모 테이블
parent = {}
parent["a"] = "start"
parent["b"] = "start"
parent["fin"] = None

# 각 정점은 한번씩만 처리해야 하므로 이미 처리한 정점을 추적하기 위한 배열
processed = []





