import math


class Polynomial:
    degree = -1
    __coefficients = {}

    # multiplies two polynomials
    def __mul__(self, other):
        to_add = []
        to_return = Polynomial(0, {})
        for i in range(other.degree + 1):
            to_add.append(self.mul_single_power(other.get_coefficient(i), i))
        for i in to_add:
            to_return = to_return + i
            print(i)
        to_return.trim()
        return to_return

    # returns sum of two polynomials
    def __add__(self, other):
        co = {}
        largest = max(self.degree, other.degree)
        for i in range(largest + 1):
            co[i] = other.get_coefficient(i) + self.get_coefficient(i)
        to_return = Polynomial(largest, co)
        to_return.trim()
        return to_return

    # returns polynomial 1 - polynomial 2
    def __sub__(self, other):
        co = {}
        largest = max(self.degree, other.degree)
        for i in range(largest + 1):
            co[i] = self.get_coefficient(i) - other.get_coefficient(i)
        to_return = Polynomial(largest, co)
        to_return.trim()
        return to_return

    def __init__(self, degree: int, co: dict):
        self.degree = degree
        self.coefficients = co

    def __str__(self):
        string = ""
        if self.degree < 0:
            return "empty polynomial"

        # runs through all powers backwards,
        # adding each one to the string unless it is 0
        for i in range(self.degree + 1):
            j = self.degree - i
            co = self.get_coefficient(j)
            if co == 0:
                continue
            string = string + " + " + str(co) + "x^" + str(j)

        # just takes off the first +
        return string[3:]

    # returns the numeric value of the polynomial
    def val(self, x):
        total = 0
        for i in range(self.degree):
            total += pow(x, i) * self.get_coefficient(i)
        return total

    # checks if the degree of the polynomial is correct
    def __trim(self):
        if self.get_coefficient(self.degree) == 0:
            for i in range(self.degree + 1):
                j = self.degree - 1
                if self.get_coefficient(i) != 0:
                    self.degree = j

    # multiplies the polynomial by a single power of x and it's coefficient
    def mul_single_power(self, coefficient, power):
        co = {}
        for i in range(self.degree + 1):
            co[power + i] = self.get_coefficient(i) * coefficient
        return Polynomial(self.degree + power, co)

    # returns the coefficient of a power, if it doesn't exist, returns 0
    def get_coefficient(self, power: int):
        if power < 0:
            raise Exception("Power can not be lower than 0")
        try:
            return self.coefficients[power]
        except KeyError:
            self.coefficients[power] = 0
            return 0

    def solve(self):
        if self.degree == 0:
            return self.get_coefficient(0)
        elif self.degree == 1:
            return self.linearSolution()
        elif self.degree == 2:
            return self.quadraticSolution()
        elif self.degree > 2:
            raise ValueError("Na")

    def linearSolution(self):
        return (-self.get_coefficient(0))/self.get_coefficient(1)

    def quadraticSolution(self):
        a = self.get_coefficient(2)
        b = self.get_coefficient(1)
        c = self.get_coefficient(0)
        determinant = (b ** 2) - (4 * a * c)
        if determinant < 0:
            return
        else:
            return (-b + (math.sqrt(determinant))) / 2 * a, (-b - (math.sqrt(determinant))) / 2 * a
