import random
import json

thisweek = []
meals = list(open("text/meals.txt", "r"))
for y in range(len(meals)):
    meals[y] = meals[y].strip('\n')
lastweek = list(open("text/history.txt", "r"))
for j in range(7):
    lastweek[j] = lastweek[j].strip('\n')
options = []

#make list without last week's options: list comprehension
options = [x for x in meals if x not in lastweek]

# do the strip thing
for u in range(len(options)):
    options[u] = options[u].strip('\n')

#pick random names
for i in range(7):
    newmeal = (random.choice(options))
    # check that this meal already in isn't in this week's meals
    while newmeal in thisweek:
        newmeal = (random.choice(options))
    thisweek.append(newmeal)

for j in range(7):
    thisweek[j] = thisweek[j].strip('\n')

#check what we have
print("last week:")
print(lastweek)
print("this week:")
print(thisweek)

#write last week's history
with open('text/history.txt', 'w') as history:
    for meal in thisweek:
        history.write(str(meal))
        history.write("\n")
