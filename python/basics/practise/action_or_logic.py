#method 1 without using if condition 
animal = "crocodile"
for i in range(0, len(animal), 2):
        print(animal[i])

#method 2 witho using if condition
mammal = "bluewhale"
for i in range(len(mammal)):
        if i % 2 == 0:
                print(mammal[i])
