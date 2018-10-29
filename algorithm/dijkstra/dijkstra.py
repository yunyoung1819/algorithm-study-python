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
infinity = float("inf")     # 파이썬에서 무한대 표시

costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity
print("갱신 이전 : ", costs)

# 부모 테이블
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None
print("갱신 이전 : ", parents)

# 각 정점은 한번씩만 처리해야 하므로 이미 처리한 정점을 추적하기 위한 배열
processed = []
print("갱신 이전 : ", processed)

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs: # 모든 정점을 확인
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs)  # 아직 처리하지 않은 가장 싼 정점을 찾음
while node is not None: # 모든 정점을 처리하면 반복문 종료
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys(): # 모든 이웃에 대해 반복
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost: # 만약 이 정점을 지나는 것이 가격이 더 싸다면
           costs[n] = new_cost
           parents[n] = node  # 부모를 이 정점으로 새로 설정
    processed.append(node) # 정점을 처리한 사실 기록
    node = find_lowest_cost_node(costs) # 다음으로 처리할 정점을 찾아 반복함


print("갱신 이후 : ", costs)
print("갱신 이후 : ", parents)
print("갱신 이후 : ", processed)
