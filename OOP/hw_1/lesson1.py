class Elements(object):
    zamerzanya = 1537
    plavlenya = 1538
    isparenya = 2862
    t = 0

    def agg_state(self, t):
        celsie = t
        farengeit = (t * 9 / 5) + 32
        celvin = t + 273, 15
        if self.t >= self.plavlenya and self.t < self.isparenya:
            print('plavimsya')
        elif self.t < self.plavlenya:
            print('Tverdeem')
        else:
            print('Mi isparyaemsya')

        print('Цельсий =', celsie, 'Фаренгейт = ', farengeit, 'Кельвин = ', celvin)
    def convertation(self):
        celsie2 = self
        farengeit2 = (self * 9 / 5) + 32
        celvin2 = self + 273,15

        print('Цельсий =', celsie2, 'Фаренгейт = ', farengeit2, 'Кельвин = ', celvin2)


proba1 = Elements()
proba1.t = int(input("Введите температуру металла:"))

proba1.agg_state(proba1.t)


class Iron(Elements):
    pass

    