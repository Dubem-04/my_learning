class CashRegister:
    """A simulated cash register that tracks the item count and the total amount due."""

    def __init__(self):
        self._cart = []

    def addItem(self, price: float) -> list:
        """Adds an item to this cash register"""
        self._cart.append(price)

    def addItems(self, quantity: int, price: float) -> list:
        """Adds multiple instances of an item"""
        for _ in range(quantity):
            self.addItem(price)

    def getTotal(self) -> float:
        """Gets the price of all items in the current sale"""
        return sum(self._cart)

    def getCount(self) -> int:
        """Gets the number of items in the current sale"""
        return len(self._cart)

    def getDollar(self) -> int:
        """Rounds the total value to the nearest dollar"""
        return round(self.getTotal())

    def giveChange(self, payment: float) -> float:
        if payment < self.getTotal():
            print("Insufficient Funds")
        else:
            balance = f"#{payment - self.getTotal()}"
            self.clear()
            return balance

    def clear(self) -> list:
        """Clears the item count and the total"""
        self._cart.clear()