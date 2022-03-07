


from modClass import Car
test = Car("Subaru")
test.set_model("WRX")
test.set_year(1999)


from modClass import AnimalNew
animal = AnimalNew('dog', "wang...")

if __name__ == "__main__":
    test.get_info()
    animal.greet()  