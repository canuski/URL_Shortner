def make_chocolate_sauce():
    return print('Wat heb je nodig:\nJe zal: ¾ cup white sugar, ½ cup unsweetened cocoa powder, 1 ½ tablespoons all-purpose flour, 1 ¼ cups milk, 2 tablespoons butter, ½ teaspoon vanilla extract, or more to taste en 1 tiny pinch salt nodig hebben \nDirections:\n-Place sugar, cocoa powder, and flour into a bowl. Whisk together to remove lumps\n-Heat milk, butter, and vanilla extract in a saucepan over medium heat until butter melts.\n-Whisk dry ingredients into the milk mixture a little at a time. Increase heat to medium-high until mixture comes to a simmer.\n-Cook, stirring constantly, for 6 minutes, then turn off the heat. Whisk in a pinch of salt.\nNow on to the donut making!')

def make_caramel():
    return print('Wat heb je nodig:\nUse high quality butter, Never leave your caramel sauce unattended, Dont forget the salt! ½1 \nDirections:\n-Place the sugar in a heavy bottomed saucepan over medium heat\n-Keep an eye on the sugar, stirring it every few minutes until it melts.\n-Remove from heat. Add butter to the melted sugar and stir to combine.\n-Pour in the cream and salt, and stir until completely combined.\nNow on to the donut making!')

def make_donut(sauce_function):
    print("Wat heb je nodig voor de donut:")
    print("- 1 cup all-purpose flour")
    print("- 1/2 cup sugar")
    print("- 1/4 cup milk")
    print("- 1/4 cup vegetable oil")
    print("- 1/2 teaspoon vanilla extract")
    print("- 1/2 teaspoon baking powder")
    print("- 1/4 teaspoon salt")
    print("Directions:")
    print("- Preheat your oven to 350 degrees F (175 degrees C). Grease a donut pan.")
    print("- In a large bowl, mix flour, sugar, baking powder, and salt.")
    print("- Stir in milk, oil, and vanilla extract until well combined.")
    print("- Fill each donut cup about 3/4 full.")
    print("- Bake in the preheated oven until a toothpick inserted into the center comes out clean, about 12 minutes.")
    print("- Let cool in the pan for 10 minutes, then transfer to a wire rack to cool completely.")
    print("- Now, let's make the sauce for the donut:")
    sauce_function()

#chocoladedonut
make_donut(make_chocolate_sauce)

#carameldonut
make_donut(make_caramel)