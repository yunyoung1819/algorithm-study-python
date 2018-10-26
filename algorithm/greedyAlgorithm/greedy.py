# 탐욕 알고리즘 (greedy Algorithm)

# 각 단계에서 국소 최적해(locally optimal solution)을 찾음으로써
# 최종적으로 전역 최적해(globally optimal solution)을 구한다.

# 집합 커버링 문제


# 방송하고자 하는 주의 목록
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])   # 배열을 넣으면 집합이 됨

# 선택된 방송국의 목록
stations = {}
stations["kone"] = set(["id", "nv", "ut"]) # 키는 방송국의 이름이고 값은 그 방송국의 방송을 들을 수 있는 주의 목록
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

# 방문할 방송국의 목록을 저장할 집합
final_stations = set()

while states_needed:    # 방송하고자 하는 주의 목록이 빌 때까지
    best_station = None
    states_covered = set() # 아직 방송되지 않은 주 중에서 해당 방송국이 커버하는 주의 집합
    for station, states in stations.items():
        covered = states_needed & states # states_needed 와 states_for_station에 모두 포함된 주의 집합
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

    states_needed -= states_covered
    final_stations.add(best_station)

print(final_stations)
