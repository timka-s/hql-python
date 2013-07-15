from .__external__ import Expression, Parameter


class ParameterValue(Expression):
    __fields__ = ('parameter',)


    def __new__(cls, parameter):
        if not isinstance(parameter, Parameter):
            raise TypeError

        return cls._make(parameter)
