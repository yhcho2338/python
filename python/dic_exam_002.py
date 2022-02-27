dictionary = {
    "name": "맛나 딸기잼",
    "type": "가공식품",
    "ingredient": ["딸기", "설탕", "식용색소"],
    "origin": "미국"

}

print("name: ", dictionary["name"])
print("typr: ", dictionary["type"])
print("ingredient: ", dictionary["ingredient"])



dictionary["name"] = "존맛나 딸기잼"
print("name:", dictionary["name"])