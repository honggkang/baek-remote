class StudentScoreAndCourseManager:
    def __init__(self):
        scores = {}
        courses = {}
    def get_score(self, student_name, course):
        pass
    def get_courses(self, student_name, course):
        pass


class ScoreManager:
    def __init__(self):
        scores = {}
    def get_score(self, student_name, course):
        pass


class CourseManger:
    def __init__(self):
        courses = {}
    def get_courses(self, student_name):
        pass


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class Circle:
    def __init__(self, radius):
        self.radius = radius


class AreaCalculator:
    def __init__(self):
        self.shapes = shapes

    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.width * shape.height
        return total


shapes = [Rectangle(2,3), Rectangle(1,6)]
calculator = AreaCalculator(shapes)
print("The total area is: ", calculator.total_area())


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14*self.radius**2


class AreaCalculator:
    def __init__(self, shapes):
        self.shapes = shapes

    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.area()
        return total


shapes = [Rectangle(1,6), Rectangle(2,3), Circle(5), Circle(7)]
calculator = AreaCalculator(shapes)

print("The total area is: ", calculator.total_area())


