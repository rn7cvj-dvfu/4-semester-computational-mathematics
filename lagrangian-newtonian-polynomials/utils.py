

class Point:

    index : int
    value : float

    def __init__(self , index : int , value : float):
        self.index = index
        self.value = value

def dividedDifference2(x1, x2, f):
    return (f(x2) - f(x1)) / (x2 - x1)


def dividedDifference3(x1, x2, x3, f):
    return (dividedDifference2(x2, x3, f) - dividedDifference2(x1, x2, f)) / (x3 - x1)



def getNearestPoints(points : list[float] , pointValue : float , h : float) -> list[Point]:

    for i in range(len(points) - 1):

        if not (pointValue >= points[i] and pointValue <= points[i + 1]):
            continue
        
        previous : Point = Point(i - 1 , points[max( i - 1 , 0)])

        if (i == 0):
            previous.value -= h

        current : Point = Point(i , points[i])

        next : Point = Point(i + 1 , points[i + 1])

        return [previous , current , next]
