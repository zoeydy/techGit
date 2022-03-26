import imp


import sys
sys.path.append('')

from mod_class import Car
test = Car("Subaru")
test.set_model("WRX")
test.set_year(1999)


from mod_class import AnimalNew
animal = AnimalNew('dog', "wang...")

if __name__ == "__main__":
    test.get_info()
    animal.greet()  