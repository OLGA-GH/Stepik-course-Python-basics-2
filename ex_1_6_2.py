class ExtendedStack(list):
    def sum(self):
        sum = 0
        for _ in range(2):
            sum += self.pop()
        self.append(sum)

    def sub(self):
        sub = 0
        sub = self.pop()
        sub -= self.pop()
        self.append(sub)

    def mul(self):
        mul = 0
        mul = self.pop()
        mul *= self.pop()
        self.append(mul)

    def div(self):
        div = 0
        div = self.pop()
        div = div // self.pop()
        self.append(div)
