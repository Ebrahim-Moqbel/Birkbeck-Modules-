class Product:
    '''
    Class representing a product in an online shopping cart, storing
    description, price and stock level.
    '''

    def __init__(self, description: str, price: float, stock: int):
        # initialise the three private instance variables
        self._description = description
        self._price = price
        self._stock = stock

    # define three getter methods returning their instance variable values
    def getDescription(self):
        return self._description

    def getPrice(self):
        return self._price

    def getStock(self):
        return self._stock

    # define two setter methods updating their respective instance variable values
    def setDescription(self, text):
        self._description = text

    def setPrice(self, amount):
        self._price = amount

    def updateStock(self, amount):
        '''
        Takes a positive or negative value, checks it against the current
        stock, ensuring it will not go below zero, before adding it to the
        stock value. Returns True if stock was updated, False if not.
        '''
        # validate that amount is an integer
        if not isinstance(amount, int):
            raise TypeError('amount must be an integer')

        # update stock only if it won't go below zero
        if self._stock + amount < 0:
            return False
        else:
            self._stock += amount
            return True
