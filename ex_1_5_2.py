class Buffer:
    def __init__(self):
        # конструктор без аргументов
        self.sequence = []

    def add(self, *a):
        # добавить следующую часть последовательности
        if len(self.sequence) < 5:
            for number in [*a]:
                self.sequence.append(number)

        if len(self.sequence) >= 5:
            for chunk in range(len(self.sequence) // 5):
                print(sum(self.sequence[:5]))
                self.sequence = self.sequence[5:]

    def get_current_part(self):
        # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были добавлены
        return self.sequence
