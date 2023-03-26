class MoneyBox:
    def __init__(self, capacity):
        # конструктор с аргументом – вместимость копилки
        self.capacity = capacity
        self.accumulated_coins = 0

    def can_add(self, coins_count):
        # True, если можно добавить coins_count монет, False если монет
        if self.accumulated_coins + coins_count > self.capacity:
            return False
        else:
            return True

    def add(self, coins_count):
        # положить coins_count монет в копилку
        self.accumulated_coins += coins_count
