dictionary = {
    "name": "맛나 딸기잼",
    "type": "가공식품",
    "ingredient": ["딸기", "설탕", "식용색소"],
    "origin": "미국"

}

print("요소 제거 이전: ", dictionary)



del dictionary["name"]
del dictionary["origin"]


print("요소 제거 이후: ", dictionary)