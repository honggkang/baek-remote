from abc import * # abstract class


class Character(metaclass=ABCMeta):
    def __init__(self, name='yourname', health=100, strike=3, defense=3):
        self.name = name
        self.health = health
        self.strike = strike
        self.defense = defense

    def get_info(self):
        print(self.name, self.health_point, self.strike, self.defense)

    @abstractmethod
    def attack(self, second):
        pass

    @abstractmethod
    def attacked(self):
        pass

    @abstractmethod
    def special(self):
        pass


class Character(metaclass=ABCMeta):
    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def eat(self):
        pass

class Elf(Character):
    def attack(self):
        print("bow")

    def move(self):
        print("fly")

    def eat(self):
        print("no eat")  # no use


class Human(Character):
    def attack(self):
        print("punch")

    def move(self):
        print("run")

    def eat(self):
        print("eat foods")


class AttackingWay(metaclass=ABCMeta):
    @abstractmethod
    def attack(self):
        pass

class MovingWay(metaclass=ABCMeta):
    @abstractmethod
    def move(self):
        pass

class EatingWay(metaclass=ABCMeta):
    @abstractmethod
    def eat(self):
        pass


class AbstractHumanCharacter(AttackingWay, MovingWay, EatingWay):
    pass


class Elf(AttackingWay, MovingWay):
    def attack(self):
        print("bow")

    def move(self):
        print("fly")


class Human(AttackingWay, MovingWay, EatingWay):
    def attack(self):
        print("fist")

    def move(self):
        print('run')

    def eat(self):
        print('eat foods')


class Character(metaclass=ABCMeta):
    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Elf(Character):
    def attack(self):
        print('bow')

    def move(self):
        print('fly')


class Human(Character):
    def attack(self):
        print('fist')

    def move(self):
        print('run')

    def eat(self):
        print('eat foods')


class BubbleSort:
    def bubble_sort(self):
        pass


class SortManager:
    def __init__(self):
        self.sort_method = BubbleSort()
        # SortManager는 BubbleSort에 의존적
    def begin_sort(self):
        self.sort_method.bubble_sort()
        # BubbleSort의 bubble_sort 메서드에 의존적


class BubbleSort:  # method 변경
    def sort(self):
        print('bubble sort')
        pass

sortmanager = SortManager()
sortmanager.begin_sort()  # SortManage 도 변경해야 함

class SortManager:
    def __init__(self, sort_method):
        self.set_sort_method(sort_method)

    def set_sort_method(self, sort_method):
        self.sort_method = sort_method

    def begin_sort(self):
        self.sort_method.sort()  # 하부 class 바뀌어도 동일한 코드 활용 가능

class QuickSort:
    def sort(self):
        print('quick sort')
        pass

bubble_sort1 = BubbleSort()
quick_sort1 = QuickSort()

sorting1 = SortManager(bubble_sort1)
sorting1.begin_sort()

sorting2 = SortManager(quick_sort1)
sorting2.begin_sort()