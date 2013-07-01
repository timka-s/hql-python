from .__external__ import Expression, Predicate


class Compare(Predicate):
    __fields__ = ('comparison', 'left', 'right')
    __comparisons__ = ('!=', '==', '>=', '>', '<=', '<')


    def __new__(cls, comparison, left, right):
        if comparison not in cls.__comparisons__:
            raise ValueError

        if not isinstance(left, Expression):
            raise TypeError

        if not isinstance(right, Expression):
            raise TypeError

        return cls._make(comparison, left, right)


    def __str__(self):
        return '%s %s %s' % (
            str(self.left), self.comparison, str(self.right))
