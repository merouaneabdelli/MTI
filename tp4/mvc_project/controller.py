from model import Model
from view import View

class Controller:
    def __init__(self):
        self.data_model = Model()
        self.viewer = View()

    def search(self):
        name = self.viewer.input()

        persons = self.data_model.search(name)

        self.viewer.output(persons)

    def show_all(self):
        persons = self.data_model.get_all()
        self.viewer.output(persons)

    def add(self):
        name, firstname, tel = self.viewer.input_add()

        self.data_model.add(name, firstname, tel)

        persons = self.data_model.get_all()
        self.viewer.output(persons)


if __name__ == "__main__":
    control = Controller()
    control.search()