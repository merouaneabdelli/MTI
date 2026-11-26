class Model:
    def __init__(self):
        self.directory = [
            {"firstname": "Ahmed", "familyname": "Mahdi", "tel": "0778787887"},
            {"firstname": "Mohamed", "familyname": "Mahdi", "tel": "0778787887"},
            {"firstname": "Mounir", "familyname": "Katibi", "tel": "0778787887"},
            {"firstname": "Noui", "familyname": "Brahimi", "tel": "0778787887"}
        ]

    def search(self, nom):
        persons = []

        for person in self.directory:
            if person["familyname"] == nom:
                persons.append(person)

        return persons

    def get_all(self):
        persons = []

        for person in self.directory:
            persons.append(person)

        return persons

    def add(self, name, firstname, tel):
        person = {
            "familyname": name,
            "firstname": firstname,
            "tel": tel
        }

        self.directory.append(person)