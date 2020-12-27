pasta = "tomato, basil, garlic, salt, pasta, olive oil"
apple_pie = "apple, sugar, salt, cinnamon, flour, egg, butter"
ratatouille = "aubergine, carrot, onion, tomato, garlic, olive oil, pepper, salt"
chocolate_cake = "chocolate, sugar, salt, flour, coffee, butter"
omelette = "egg, milk, bacon, tomato, salt, pepper"
word = input()
list_ = [pasta, apple_pie,ratatouille, chocolate_cake, omelette]
dish = ['pasta', 'apple pie', 'ratatouille', 'chocolate cake', 'omelette']
dict_ = dict(zip(dish,list_))
for ele, ingredient in list(dict_.items()):
    if word in ingredient:
        print(ele + " time!")
