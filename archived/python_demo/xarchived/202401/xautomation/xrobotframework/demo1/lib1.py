"""
模块作为lib

通过 Library   lib1.py 直接引入

模块内部的函数就可以作为Keywords正常使用


- Formatting with **bold** and *italic*.
- URLs like http://example.com are turned to links.
- Custom links like reStructuredText__ are supported.
- Linking to \`Lib1 Func1\` works but requires backtics to be escaped.

__ http://docutils.sourceforge.net

.. code:: robotframework

    *** Test Cases ***
    Example
        Lib1 Func1    1    2    # How cool is this!!?!!?!1!!
"""

ROBOT_LIBRARY_DOC_FORMAT = "reST"
ROBOT_LIBRARY_VERSION = "0.0.1"
ROBOT_LIBRARY_SCOPE = "GLOBAL"

def lib1_func1(arg1: int, arg2: int) -> int:
    """lib1 func1 doc
    
    Examples:

    .. code:: robotframework

        *** Test Cases ***
        Example
            Lib1 Func1    1    2    # How cool is this!!?!!?!1!!
    """
    return arg1 + arg2