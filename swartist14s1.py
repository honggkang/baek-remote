# SW ARTist 14 Session 1 OOP practice

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '{}.{}'.format(self.x, self.y)

    def __add__(self, pt):
        new_x = self.x + pt.x
        new_y = self.y + pt.y
        return Point(new_x, new_y)


class ComplexNumber:
    def __init__(self, x, y):
        self.re = x
        self.im = y

    def __str__(self):
        if self.im < 0:
            return '{} - {}j'.format(self.re, -self.im)
        else:
            return '{} + {}j'.format(self.re, self.im)

    def __add__(self, other):
        res_re = self.re + other.re
        res_im = self.im + other.im
        return ComplexNumber(res_re, res_im)

    def __sub__(self, other):
        res_re = self.re - other.re
        res_im = self.im - other.im
        return ComplexNumber(res_re, res_im)

    def __mul__(self, other):
        if isinstance(other, ComplexNumber):
            res_re = self.re * other.re - self.im * other.im
            res_im = self.re * other.im + self.im * other.re
            return ComplexNumber(res_re, res_im)
        else:
            return ComplexNumber(self.re * other, self.im * other)

    def __abs__(self):
        return (self.re ** 2 + self.im ** 2) ** (1 / 2)

    def __eq__(self, other):
        if self.re == other.re and self.im == other.im:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.re == other.re and self.im == other.im:
            return False
        else:
            return True


a = ComplexNumber(1, 2)
b = ComplexNumber(2, 3)
dash = '--------'
print(a)
print(dash)
print(a+b)
print(a-b)
print(a*3)
print(a*b)
print(dash)
print(abs(a))
print(dash)
print(a==b)
print(a!=b)
