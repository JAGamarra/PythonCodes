class NotExistItemError(Exception):
    pass

class Item:

    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

    
    def __str__(self) -> str:
        return self.name

class ShoppingCart:

    def __init__(self) -> None:
        self.items = []

    
    def add_item(self, item) -> None:
        self.items.append(item)


    def remove_item(self, item) -> None:
        self.items.remove(item)

    
    def contains(self) -> bool:
        return len(self.items) > 0


    def get_item(self, item):
        if item not in self.items:
            raise NotExistItemError("Item does not exist.")
        else:
            return self.items[ self.items.index(item) - 1 ]