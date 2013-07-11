from .__external__ import Obtainment, Parameter


class ParameterValue(Obtainment):
    __fields__ = ('parameter',)


    def __new__(cls, parameter):
        if not isinstance(parameter, Parameter):
            raise TypeError

        return cls._make(parameter)
