pizza = 'Margherita, Four Seasons, Neapolitan, Vegetarian, Spicy'
salad = 'Caesar salad, Green salad, Tuna salad, Fruit salad'
soup = 'Chicken soup, Ramen, Tomato soup, Mushroom cream soup'

order = input()

if order == 'pizza':
    print(pizza)
elif order == 'salad':
    print(salad)
elif order == 'soup':
    print(soup)
else:
    print("Sorry, we don't have it in the menu")
