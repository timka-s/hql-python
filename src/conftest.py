import pytest

from . import tree


@pytest.fixture(scope='module')
def tester_visitor_completeness():
    def tester(test_cls, skip_set):
        base_cls = tree.Node

        tree_attrs = [getattr(tree, attr_name) for attr_name in dir(tree)]

        can_implement = [
            value.__name__ for value in tree_attrs
            if isinstance(value, type) and issubclass(value, base_cls)
        ]

        must_implement = [
            cls_name for cls_name in can_implement
            if cls_name not in skip_set
        ]

        not_implemented = [
            cls_name for cls_name in must_implement
            if not hasattr(test_cls, 'visit_%s' % cls_name)
        ]

        assert len(not_implemented) == 0

        return True

    return tester


@pytest.fixture(scope='module')
def tester_visitor_sufficiency():
    def tester(test_cls):
        implemented = [
            attr_name.replace('visit_', '', 1) for attr_name in dir(test_cls)
            if attr_name.startswith('visit_')
        ]

        not_presents = [
            cls_name for cls_name in implemented
            if not hasattr(tree, cls_name)
        ]

        assert len(not_presents) == 0

        return True

    return tester
