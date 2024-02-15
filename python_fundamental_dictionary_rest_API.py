"""
fundamental dictionary rest API/ JSON
"""

users = {
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
      "street": "Kulas Light",
      "suit":"Apt. 556",
      "city": "Gwenborough",
      "zipecode": "92998-3874",
      "geo": {
          "lat":"-37.3159",
          "lng":"81.1496"
      }
     }

}
print(users)
print(users["name"])
print(users["username"])
print(users["email"])
print(users["address"]["street"])
print(users["address"]["suit"])
print(users["address"]["geo"]["lat"])
print(users["address"]["geo"]["lng"])
