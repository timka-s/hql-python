from .__external__ import Visitor


class Serializer(Visitor):
    def visit_Alias(self, node):
        return '@%s' % str(node.name)


    def visit_Parameter(self, node):
        return '%%%s' % str(node.name)


    def visit_Field(self, node):
        return '%s' % str(node.name)


    def visit_Kwarg(self, node):
        return '%s' % str(node.name)


    def visit_AliasAssignment(self, node):
        expression = self.visit(node.expression)
        alias = self.visit(node.alias)

        return '%s AS %s' % (expression, alias)


    def visit_Iteration(self, node):
        alias = self.visit(node.alias)
        expression = self.visit(node.expression)

        return '%s FROM %s' % (alias, expression)


    def visit_FieldAssignment(self, node):
        field = self.visit(node.field)
        expression = self.visit(node.expression)

        return '%s = %s' % (field, expression)


    def visit_KwargAssignment(self, node):
        kwarg = self.visit(node.kwarg)
        expression = self.visit(node.expression)

        return '%s = %s' % (kwarg, expression)


    def visit_Constant(self, node):
        data = node.data

        if isinstance(data, str):
            data = '"%s"' % data.replace('"', '\\"')
        else:
            data = str(data)

        return data


    def visit_Attribute(self, node):
        expression = self.visit(node.expression)

        return '%s.%s' % (expression, node.name)


    def visit_AliasValue(self, node):
        return self.visit(node.alias)


    def visit_ParameterValue(self, node):
        return self.visit(node.parameter)


    def visit_FunctionCall(self, node):
        kwarg_assignment_set = ', '.join(
            self.visit(kwarg_assignment)
            for kwarg_assignment in node.kwarg_assignment_set
        )

        return '%s(%s)' % (node.name, kwarg_assignment_set)


    def visit_Verity(self, node):
        predicate = self.visit(node.predicate)

        return '{%s}' % (predicate)


    def visit_TRUE(self, node):
        return 'TRUE'


    def visit_FALSE(self, node):
        return 'FALSE'


    def visit_Not(self, node):
        return 'NOT %s' % self.visit(node.predicate)


    def visit_And(self, node):
        predicate_set = '\n     && '.join(
            self.visit(predicate).replace('\n', '\n        ')
            for predicate in node.predicate_set
        )

        return '(\n        %s\n)' % predicate_set


    def visit_Or(self, node):
        predicate_set = '\n     || '.join(
            self.visit(predicate).replace('\n', '\n        ')
            for predicate in node.predicate_set
        )

        return '(\n        %s\n)' % predicate_set


    def visit_Compare(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)

        return '(%s %s %s)' % (left, node.comparison, right)


    def visit_DataAccordance(self, node):
        alias_assignment = self.visit(node.alias_assignment)
        predicate = self.visit(node.predicate)

        return '(%s ACCORD %s)' % (alias_assignment, predicate)


    def visit_SequenceAccordance(self, node):
        iteration = self.visit(node.iteration)
        predicate = self.visit(node.predicate)

        return '(%s %s ACCORD %s)' % (
            node.quantifier.upper(), iteration, predicate)


    def visit_CheckValue(self, node):
        expression = self.visit(node.expression)

        return '{%s}' % (expression)


    def visit_Origin(self, node):
        return self.visit(node.iteration)


    def visit_Filter(self, node):
        source = self.visit(node.source)
        predicate = self.visit(node.predicate)

        return 'SUCH %s\nWHERE %s' % (source, predicate)


    def visit_Combination(self, node):
        source_set = '\n    '.join(
            self.visit(source).replace('\n', '\n        ')
            for source in node.source_set
        )

        return 'COMBINATION\n    %s' % source_set


    def visit_Declaration(self, node):
        field_assignment_set = '\n    '.join(
            self.visit(field_assignment).replace('\n', '\n        ')
            for field_assignment in node.field_assignment_set
        )

        return 'GET\n    %s\n' % field_assignment_set


    def visit_Input(self, node):
        source = self.visit(node.source)

        return 'USING %s\n' % source


    def visit_Select(self, node):
        def prepare():
            yield self.visit(node.declaration)

            if node.input:
                yield self.visit(node.input)

        return ''.join(prepare())
