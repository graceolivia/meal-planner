import random
import json
thisweek = []
meals = list(open("meals.txt", "r"))
# print(meals)

#pick 3 randoms
for i in range(7):
    newmeal = (random.choice(meals))
    # check that this meal isn't in this week's meals
    while newmeal in thisweek:
        newmeal = (random.choice(meals))
    thisweek.append(newmeal)

for j in range(7):
    thisweek[j] = thisweek[j].strip('\n')
    print thisweek[j]

print("next")

y = {
    "name":"Coconut Lentils",
    "tag":"beans",
    "link":"",
    "ingredients":[
      "lentils",
      "coconut milk",
      "curry powder",
      "garlic",
      "ginger"
    ]
}


with open('recipes.json', 'a') as file:
    # ther = json.load(write)
    for m in meals:
        json.dump(str({
            "name":m,
            "tag":"",
            "link":"",
            "ingredients":""
        }), file)


# print(json.dumps(ther, indent = 4, sort_keys=True))




# for r in ther:
#     print ("Recipe name: {} \n Ingredients: ".format(r["name"]))
#     for ingred in r["ingredients"]:
#         print(ingred)
