from operator import itemgetter


class MetaNode(type):
    @classmethod
    def _validate_fields(cls, base_fields, fields):
        if type(fields) != tuple:
            raise TypeError

        if fields[0:len(base_fields)] != base_fields:
            raise ValueError

        if not all(type(field) == str for field in fields):
            raise TypeError

        if len(set(fields)) != len(fields):
            raise ValueError


    def __new__(cls, name, bases, namespace):
        if len(bases) != 1:
            raise ValueError

        base = bases[0]

        if not issubclass(base, tuple):
            raise TypeError

        fields = namespace.get('__fields__')

        if fields is not None:
            base_fields = getattr(bases[0], '__fields__', ())

            cls._validate_fields(base_fields, fields)

            for field_index, field_name in enumerate(
                    fields[len(base_fields):], len(base_fields)):
                namespace[field_name] = property(itemgetter(field_index))

        return super().__new__(cls, name, bases, namespace)
