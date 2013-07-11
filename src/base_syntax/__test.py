import pytest

from .serializer import Serializer
from .parser import Parser
from .serializer__test import completeness_node


def test_conformity(completeness_node):
    parser = Parser(debug=True)

    completeness_string = Serializer(completeness_node).output
    node = parser.parse(completeness_string, debug=True)
    string = Serializer(node).output

    assert node == completeness_node
    assert string == completeness_string
