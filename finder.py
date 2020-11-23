import random
thisweek = []
meals = list(open("meals.txt", "r"))
# print(meals)

#pick 3 randoms
for i in range(7):
    thisweek.append((random.choice(meals)))

for j in range(7):
    thisweek[j] = thisweek[j].strip('\n')
    print thisweek[j]
