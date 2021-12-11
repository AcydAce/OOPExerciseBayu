class theShopList:
    # initializer method
    def __init__(self, foodName, foodAmount): # 2 parameters
        self.__foodName = foodName                      #
        self.__foodAmount = foodAmount                  #
        self.__foodPrice = self.__Price()               # Attributes
        self.__calculator = self.calcshoplist()         #

    # private method stores list
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

    # public method calculates
    def calcshoplist(self):
        self.__calculator = self.__foodAmount * self.__foodPrice
        return (self.__calculator)

    #accessors
    def getNameBH(self):
        return self.__foodName

    def getPriceBH(self):
        return self.__foodPrice

    def getAmountBH(self):
        return self.__foodAmount

    def getCalcBH(self):
        return self.__calculator