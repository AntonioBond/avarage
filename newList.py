class NewList(list):
    def arithmetic(self):
        average_arithm = sum(self) / len(self)
        print(average_arithm)

    def geometric(self):
        multi = 1
        for i in self:
            multi *= i
        average_geom = multi ** (1 / len(self))
        print(average_geom)
