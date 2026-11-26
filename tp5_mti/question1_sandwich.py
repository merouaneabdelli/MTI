class Sandwich:

    def __init__(self):
        self.ingredients = []

    def add(self, ingredient):
        self.ingredients.append(ingredient)

    def show(self):
        print("Sandwich ingredients:")
        for ingredient in self.ingredients:
            print("-", ingredient)


class SandwichBuilder:

    def __init__(self):
        self.sandwich = Sandwich()

    def add_bread(self):
        self.sandwich.add("Bread")

    def add_meat(self):
        self.sandwich.add("Ground meat")

    def add_chicken(self):
        self.sandwich.add("Chicken")

    def add_omelet(self):
        self.sandwich.add("Omelet")

    def add_salad(self):
        self.sandwich.add("Salad")

    def add_sauce(self):
        self.sandwich.add("Sauce")


class SandwichDirector:

    def make_shawarma(self, builder):
        builder.add_bread()
        builder.add_chicken()
        builder.add_salad()
        builder.add_sauce()

    def make_ground_meat(self, builder):
        builder.add_bread()
        builder.add_meat()
        builder.add_salad()

    def make_omelet_sandwich(self, builder):
        builder.add_bread()
        builder.add_omelet()
        builder.add_salad()


if __name__ == "__main__":

    builder = SandwichBuilder()
    director = SandwichDirector()

    director.make_shawarma(builder)

    sandwich = builder.sandwich
    sandwich.show()