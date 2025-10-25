class Inventory:

    def __init__(self, __capacity: int):
        self.__capacity = __capacity
        self.items = []

    def add_item(self,item: str):
        if len(self.items) < self.__capacity:
            self.items.append(item)
        return "not enough room in the inventory"

    def get_capacity(self):
        capacity = self.__capacity
        return capacity

    def __repr__(self):
        items =", ".join(self.items)
        left_capacity = self.__capacity - len(self.items)
        return f"Items: {items}.\nCapacity left: {left_capacity}"

