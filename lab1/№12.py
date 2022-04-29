money = 0
class MoneyBox:
    def __init__(self, capacity):
        self.capacity = int(capacity)
    def can_add(self, v):
        current_value = self.capacity - money
        if int(v) < current_value:
            return True
        else:
            return False
    def add(self, v):
        self.v = int(v)
        global money
        money += self.v
        print(money)
box1 = MoneyBox(100)
print(box1.can_add(50))
print(box1.can_add(1000))
box1.add(6)
box1.add(6)
box1.add(6)
print(box1.can_add(50))
print(box1.can_add(90))