import operator

from .__external__ import Visitor


class PythonLambda(Visitor):
    class Record():
        def __init__(self, ns):
            self.__dict__.update(dict(sorted(ns.items())))


        def __repr__(self):
            return '<%s %s>' % (self.__class__.__name__, self.__dict__)


    def visit_Constant(self, node):
        data = node.data

        return lambda parameter_map, alias_map: data


    def visit_Attribute(self, node):
        output = self.visit(node.expression)
        key = node.name

        return lambda parameter_map, alias_map: \
            getattr(output(parameter_map, alias_map), key)


    def visit_AliasValue(self, node):
        key = node.alias.name

        return lambda parameter_map, alias_map: alias_map[key]


    def visit_ParameterValue(self, node):
        key = node.parameter.name

        return lambda parameter_map, alias_map: parameter_map[key]


    def function_bool(self, kwarg_assignment_set):
        output = {
            kwarg_assignment.kwarg.name:
                self.visit(kwarg_assignment.expression)
            for kwarg_assignment in kwarg_assignment_set
        }

        return lambda parameter_map, alias_map: \
            bool(**{
                key: data_output(parameter_map, alias_map)
                for key, data_output in output.items()
            })


    def visit_FunctionCall(self, node):
        method_name = 'function_%s' % node.name

        if not hasattr(self, method_name):
            raise NotImplementedError

        return getattr(self, method_name)(node.kwarg_assignment_set)


    def visit_Verity(self, node):
        output = self.visit(node.predicate)

        return lambda parameter_map, alias_map: \
            output(parameter_map, alias_map)


    def visit_TRUE(self, node):
        return lambda parameter_map, alias_map: True


    def visit_FALSE(self, node):
        return lambda parameter_map, alias_map: False


    def visit_Not(self, node):
        output = self.visit(node.predicate)

        return lambda parameter_map, alias_map: \
            not(output(parameter_map, alias_map))


    def visit_And(self, node):
        output_set = tuple(map(self.visit, node.predicate_set))

        return lambda parameter_map, alias_map: \
            all(output(parameter_map, alias_map) for output in output_set)


    def visit_Or(self, node):
        output_set = tuple(map(self.visit, node.predicate_set))

        return lambda parameter_map, alias_map: \
            any(output(parameter_map, alias_map) for output in output_set)


    _comparison_operators = {
        '!=': operator.ne,
        '==': operator.eq,
        '>': operator.gt,
        '>=': operator.ge,
        '<=': operator.le,
        '<': operator.lt,
    }


    def visit_Compare(self, node):
        comparison_operator = self._comparison_operators.get(node.comparison)

        if not comparison_operator:
            raise NotImplementedError

        output_left = self.visit(node.left)
        output_right = self.visit(node.right)

        return lambda parameter_map, alias_map: \
            comparison_operator(
                output_left(parameter_map, alias_map),
                output_right(parameter_map, alias_map)
            )


    def visit_DataAccordance(self, node):
        key = node.alias_assignment.alias.name
        data_output = self.visit(node.alias_assignment.expression)
        predicate_output = self.visit(node.predicate)

        return lambda parameter_map, alias_map: \
            predicate_output(
                parameter_map,
                dict(
                    alias_map,
                    **{key: data_output(parameter_map, alias_map)}
                )
            )


    _quantifier_operators = {
        'any': any,
        'all': all
    }


    def visit_SequenceAccordance(self, node):
        quantifier_operator = self._quantifier_operators.get(node.quantifier)

        if not quantifier_operator:
            raise NotImplementedError

        key = node.iteration.alias.name
        data_output = self.visit(node.iteration.expression)
        predicate_output = self.visit(node.predicate)

        return lambda parameter_map, alias_map: \
            quantifier_operator(
                predicate_output(
                    parameter_map,
                    dict(alias_map, **{key: data})
                ) for data in data_output(parameter_map, alias_map)
            )


    def visit_CheckValue(self, node):
        output = self.visit(node.expression)

        return lambda parameter_map, alias_map: \
            bool(output(parameter_map, alias_map))


    def visit_Condition(self, node):
        return self.visit(node.predicate)


    def visit_Source(self, node):
        if len(node.iteration_set) != 1:
            raise NotImplementedError

        key = node.iteration_set[0].alias.name
        data_output = self.visit(node.iteration_set[0].expression)

        return lambda parameter_map, alias_map: \
            (
                dict(alias_map, **{key: data})
                for data in data_output(parameter_map, alias_map)
            )


    def visit_Declaration(self, node):
        record_cls = self.Record

        field_assignment_set_output = {
            field_assignment.field.name:
                self.visit(field_assignment.expression)
            for field_assignment in node.field_assignment_set
        }

        return lambda parameter_map, alias_map: \
            record_cls({
                key: data_output(parameter_map, alias_map)
                for key, data_output in field_assignment_set_output.items()
            })


    def visit_Select(self, node):
        declaration_output = self.visit(node.declaration)

        source_output = \
            self.visit(node.source) if node.source is not None \
            else lambda parameter_map, alias_map: None

        condition_output = \
            self.visit(node.condition) if node.condition is not None \
            else lambda parameter_map, alias_map: True

        return lambda parameter_map: \
            [
                declaration_output(parameter_map, alias_map)
                for alias_map in source_output(parameter_map, {})
                if condition_output(parameter_map, alias_map)
            ]
