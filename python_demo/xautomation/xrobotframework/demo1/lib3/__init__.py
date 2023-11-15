""" 包作为lib引入demo

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