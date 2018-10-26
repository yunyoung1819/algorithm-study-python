fruits = set(["avocado", "tomato", "banana"])
vegetables = set(["beets", "carrots", "tomato"])

print(fruits | vegetables) # 이것은 합집합입니다
print(fruits & vegetables) # 이것은 교집합입니다
print(fruits - vegetables) # 이것은 차집합입니다
print(vegetables - fruits)