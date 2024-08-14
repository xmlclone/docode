def add(a, b, c=1):
    """
    Return a + b + c.

    :param a: value a.
    :type a: int or float
    :param b: value b.
    :type b: int or float
    :param c: optional value c.
    :type c: int or float or None
    :return: sum of a b c.
    :rtype: int or float
    """
    return a + b + c


class Foo:
    """Docstring for class Foo."""

    #: Doc comment for class attribute Foo.bar.
    #: It can have multiple lines.
    bar = 1

    flox = 1.5   #: Doc comment for Foo.flox. One line only.

    baz = 2
    """Docstring for class attribute Foo.baz."""


    def __init__(self):
        self.val = 1
        #: Doc comment for instance attribute qux.
        self.qux = 3

        self.spam = 4
        """Docstring for instance attribute spam."""

    def add(self, a: int, b: int) -> int:
        """
        Return a + b.

        文档注释里面可以通过: :class:`autodoc_demo.Foo` 方式进行跨引用

        :param a: from.
        :type a: int
        :param b: to.
        :type b: int
        :return: sum.
        :rtype: int
        :raises ValueError: exception
        """
        return a + b
    
    @classmethod
    def cls_method(cls):
        """This is class method"""

    @staticmethod
    def sta_method():
        """This is static method"""
    

class Foo1:
    """Docstring for class Foo1."""

    #: Doc comment for class attribute Foo.bar.
    #: It can have multiple lines.
    bar = 1

    flox = 1.5   #: Doc comment for Foo.flox. One line only.

    baz = 2
    """Docstring for class attribute Foo1.baz."""


    def __init__(self):
        self.val = 1
        #: Doc comment for instance attribute qux.
        self.qux = 3

        self.spam = 4
        """Docstring for instance attribute spam."""

    def add(self, a: int, b: int) -> int:
        """
        Return a + b.

        :param a: from.
        :type a: int
        :param b: to.
        :type b: int
        :return: sum.
        :rtype: int
        """
        return a + b
    

#: This is module var
module_var = 1