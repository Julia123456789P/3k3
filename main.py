class Tomato:

    states = {0: 'Отсутствует', 1: 'Цветок', 2: 'Зелёный', 3: 'Красный'}

    def __init__(self, index):
        self.index = index
        self._state = 0

    def grow(self):
        if self._state < 3:
            self._state += 1
            print('Томат {} сейчас {}'.format(self.index, Tomato.states[self._state]))

    def is_ripe(self):
        if self._state == 3:
            return True
        return False

class TomatoBush(Tomato):

    def __init__(self, count):
        self.tomatoes = [Tomato(index) for index in range(1, count + 1)]
        super().__init__(count)

    def grow_all(self):
        for i_tomato in self.tomatoes:
            i_tomato.grow()

    def all_are_ripe(self):
        for i_tomato in self.tomatoes:
            if not i_tomato.is_ripe():
                print('Томат ещё не созрел!\n')
                break
            else:
                print('Все томаты созрели! Можно собирать!\n')

    def give_away_all(self):
        self.tomatoes = []
        #self.tomatoes.clear()


class Gardener:

    __info = 'Рассада', 'Уход', 'Вредители и болезни', 'Сорта и гибриды'

    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print('Садовник работает')
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Собрали весь урожай')
        else:
            print('Не все созрело')

    def knowledge_base():
        print('Cправка по садоводству:')
        return Gardener.__info


print(Gardener.knowledge_base())
tb = TomatoBush(2)
men = Gardener('Ivan', tb)
men.work()
tb.all_are_ripe()
men.work()
men.harvest()
tb.tomatoes = ['g', 'f']




