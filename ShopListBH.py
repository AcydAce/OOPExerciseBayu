class theShopList:
    def __init__(self, foodName, foodAmount):
        self.__foodName = foodName
        self.__foodAmount = foodAmount
        self.__foodPrice = self.__Price()
        self.__calculator = self.calcshoplist()

    def __Price(self):
        if self.__foodName == "Dry Cured Iberian Ham":
            self.__foodPrice = 177.80
        elif self.__foodName == "Wagyu Steaks ":
            self.__foodPrice = 450.00
        elif self.__foodName == "Matsutake Mushrooms":
            self.__foodPrice = 272.00
        elif self.__foodName == "Kopi Luwak Cofee":
            self.__foodPrice = 306.50
        elif self.__foodName == 'Moose Cheese':
            self.__foodPrice = 487.20
        elif self.__foodName == 'White Truffles':
            self.__foodPrice = 3600.00
        elif self.__foodName == 'Blue Fin Tuna':
            self.__foodPrice = 3603.30
        elif self.__foodName == 'Le Bonnotte Potatoes':
            self.__foodPrice = 270.81
        else:
            self.__foodPrice = 0.00

        return self.__foodPrice

    def calcshoplist(self):
        self.__calculator = self.__foodAmount * self.__foodPrice
        return (self.__calculator)

    def getName(self):
        return self.__foodName

    def getPrice(self):
        return self.__foodPrice

    def getAmount(self):
        return self.__foodAmount

    def getcalc(self):
        return self.__calculator