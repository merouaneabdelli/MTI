class FileSingleton:

    instance = None

    def __new__(cls):

        if cls.instance is None:
            cls.instance = super().__new__(cls)

        return cls.instance

    def write_file(self, filename, text):

        with open(filename, "a", encoding="utf-8") as file:
            file.write(text + "\n")


if __name__ == "__main__":

    file1 = FileSingleton()
    file2 = FileSingleton()

    print(file1 is file2)

    file1.write_file("test.txt", "Hello Python")
    file2.write_file("test.txt", "Singleton Pattern")

    print("Writing completed") 
   