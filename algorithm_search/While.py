# 큰 상자 속에 작은 상자들이 있고, 그 작은 상자들 안에는 더 작은 상자들이 있다.
# 열쇠는 그 상자 속 어딘가에 있다.
# 열쇠를 찾는 방법은 무엇일까?

# 1. 내부를 확인할 상자를 쌓아놓는다
# 2. 상자를 하나 집어서 내부를 살핀다
# 3. 만약 안에 상자가 있다면 꺼내어 나중에 확인할 상자 더미에 놓는다
# 4. 만약 열쇠가 있으면 작업 종료!
# 5. 반복한다


def look_for_key(main_box):
    pile = main_box.make_a_pile_to_look_through()
    while pile is not empty:
        box = pile.grab_a_box()
        for item in box:
            if item.is_a_box():
                pile.append(item)
            elif item.is_a_key():
                print ("열쇠를 찾았어요!")