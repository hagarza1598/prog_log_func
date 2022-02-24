class Person():
    def __init__(self, name, lastName, secondLastName):
        self.name = name
        self.lastName = lastName
        self.secondLastName = secondLastName

    def FullNameFunction(self):
        return ("%s %s %s" % (self.name, self.lastName, self.secondLastName))

if __name__ == '__main__':
    name = input("Ingresa tu nombre: ")
    lastName = input("Ingresa tu apellido paterno: ")
    secondLastName = input("Ingresa tu apellido materno: ")
    object = Person(name, lastName, secondLastName)
    FullName = object.FullNameFunction()
    print("Tu nombre completo es: %s" % (FullName))