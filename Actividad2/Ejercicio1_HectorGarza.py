class Convertion():
    def LitersToGallons(self, liters):
        result = liters * 0.2641720524
        print("El resultado de su conversion es: %f galones"%(result))

    def FeetsToMeterts(self, feets):
        result = feets * 0.3048
        print("El resultado de su conversion es: %f metros"%(result))
    
    def InchesToCentimeters(self, inches):
        result = inches * 2.54
        print("El resultado de su conversion es: %f centimetros"%(result))


if __name__ == '__main__':
    while True:
        print("1.- Litros a galones")
        print("2.- Pies a metros")
        print("3.- Pulgadas a centimetros")
        print("4.- Salir")
        option = int(input("Seleccione una opcion: "))
        object = Convertion()

        if option == 1:
            liters = float(input("Ingrese los litros a convertir: "))
            object.LitersToGallons(liters)
        
        elif option == 2:
            feets = float(input("Ingrese los pies a convertir: "))
            object.FeetsToMeterts(feets)

        elif option == 3:
            inches = float(input("Ingrese las pulgadas a convertir: "))
            object.InchesToCentimeters(inches)
            
        elif option == 4:
            break
        else:
            print("Opcion invalida! Intente de nuevo")