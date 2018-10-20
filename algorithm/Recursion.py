# 재귀
# 재귀란 함수가 자기 자신을 호출하는 것

def look_for_key(box):
    for item in box:
        if item.is_a_box():
            look_for_key(item) #반복
        elif item.is_a_key():
            print("열쇠를 찾았어요!")