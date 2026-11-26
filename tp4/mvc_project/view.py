class View:
    def __init__(self):
        pass

    def input(self):
        print("Finding a phone")
        print("Give a name")
        name = input()
        return name

    def output(self, persons):
        print("List of found names")
        print("%d found people" % len(persons))

        for person in persons:
            print(
                person["familyname"],
                person["firstname"],
                person["tel"]
            )

    def input_add(self):
        print("Add a person")

        print("Give a name")
        name = input()

        print("Give a firstname")
        firstname = input()

        print("Give a telephone")
        tel = input()

        return name, firstname, tel,