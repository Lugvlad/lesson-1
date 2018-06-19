def test_even_fucntion():
    """
    Необходимо реализовать функцию even_filter, которая получает неограниченное количество аргументов
    и возвращает из них только четные.
    """

    def even_filter(*args):
        for i in args:
            if i % 2 == 0:
                return i

    assert even_filter(1, 2, 3, 4, 5, 6) == [2, 4, 6]


def test_increment_decorator():
    """
    Необходимо реализовать декоратор increment_derocator, который увеличивает полученное значение на 1 и передает его в
    декрорируемую функцию.
    """
    def increment_derocator(func):
        def wrapper(*i)
            value+=1
            func()
        return wrapper()
    @increment_derocator
    def returner(value):
        return value

    assert returner(1) == 2


def test_point_segment_class():
    """
    Дано: есть класс Point, описывающий точку на плоскости. Необходимо закончить класс Segment, описывающий отрезок,
    принимающий на вход 2 точки и позволяющий посчитать его длину.
    Модуль с математическими функциями называется math, документация по нему находится здесь:
    https://docs.python.org/3/library/math.html?highlight=math#module-math
    """

    class Point():
        def __init__(self, x, y):
            self.x = x
            self.y = y


    class Segment():
        def __init__(self, p1, p2):
            p1.x = x1
            p1.y = y1
            p2.x = x2
            p2.y = y2
        def length(self):
            t = math.hyp(x2-x1,y2-y1)
            return t

    p1 = Point(0, 0)
    p2 = Point(3, 4)
    assert Segment(p1, p2).length() == 5.0
    assert Segment(p2, p1).length() == 5.0
