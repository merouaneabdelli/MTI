
directory = [
    {"firstname": "Ahmed", "familyname": "Mahdi", "tel": "0778787887"},
    {"firstname": "Mohamed", "familyname": "Mahdi", "tel": "0778787887"},
    {"firstname": "Mounir", "familyname": "Katibi", "tel": "0778787887"},
    {"firstname": "Noui", "familyname": "Brahimi", "tel": "0778787887"}
]

def main():
    print("Finding a telephone")
    print("Give a name")

    familyname = input()

    nb_found = 0

    for person in directory:
        if person["familyname"] == familyname:
            print(familyname, person["firstname"], person["tel"])
            nb_found += 1

    if not nb_found:
        print("This familyname %s doesn't exist" % familyname)

if __name__ == "__main__":
    main()