from typing import Final


class Discounts():
    def TotalAmount(self, product1, product2, product3):
        subtotal = product1 + product2 + product3
        if subtotal >= 100 and subtotal < 200:
            FinalTotal = self.TotalWithDiscount(subtotal, 0.05)
        elif subtotal >= 200:
            FinalTotal = self.TotalWithDiscount(subtotal, 0.08)
        else:
            FinalTotal = subtotal
        return FinalTotal

    def TotalWithDiscount(self, subtotal, discount):
        FinalTotal = subtotal - (subtotal * discount)
        return FinalTotal


if __name__ == '__main__':
    product1 = int(input("Ingresa el costo del primer producto: "))
    product2 = int(input("Ingresa el costo del segundo producto: "))
    product3 = int(input("Ingresa el costo del tercer producto: "))
    object = Discounts()
    FinalTotal = object.TotalAmount(product1, product2, product3)
    print("El total a pagar con el descuento es: %f" % (FinalTotal))