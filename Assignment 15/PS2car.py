class Car:
    def __init__(self, make, model, stickerPrice):
        self.make = make
        self.model = model
        self.stickerPrice = float(stickerPrice)
        
    def discountPrice(self):
        return self.stickerPrice *0.90
    
    
class Sport(Car):
    def __init__(self, make, model, stickerPrice):
        super().__init__(make, model, stickerPrice)
        self.wheelsOptions =  'N'
        self.enginOption = 'N'
        self.interiorOption = 'N'

    def SportWheels(self, opt):
        self.wheelsOptions = opt.upper()

    def SportEngine(self, opt):
        self.enginOption = opt.upper()

    def SportInterior(self, opt):
        self.interiorOption = opt.upper()
    
    def pricewithoptions(self):
        basePrice = self.discountPrice()
        optionTotal = 0.0

        if self.wheelsOptions == 'Y':
            optionTotal += 1000.00
        if self.enginOption == 'Y':
            optionTotal += 3000.00
        if self.interiorOption == 'Y':
            optionTotal += 2000.00

        return basePrice + optionTotal
   
    def priceWithDisplayPrint(self):
        print("Car make is: ", self.make)
        print("Car model is: ", self.model)
        print("Car Sticker Price is: ", self.stickerPrice)
        print("Discounted Base Price: $", self.discountPrice())
        print("Final Price with Options: $", self.pricewithoptions())

        
make = input("Enter car make ")
model = input("Enter the car model ")
stickerPrice = float(input ("Enter the Sticker Price "))

car1 = Sport(make, model, stickerPrice)

car1.SportWheels(input("Add Sport Weels (Y/N)? "))
car1.SportEngine(input("Add sport Engin (Y/N)? "))
car1.SportInterior(input("Add Sport Interior (Y/N)? "))

car1.priceWithDisplayPrint()


