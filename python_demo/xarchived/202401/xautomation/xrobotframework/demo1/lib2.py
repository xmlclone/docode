from robot.api import logger


class lib2(object):
    """如果模块内的类名和模块名一致，也可以直接引入使用

    - Formatting with **bold** and *italic*.
    - URLs like http://example.com are turned to links.
    - Custom links like reStructuredText__ are supported.
    - Linking to \`Get Name\` works but requires backtics to be escaped.

    __ http://docutils.sourceforge.net

    .. code:: robotframework

        *** Test Cases ***
        Example
            Get Name    # How cool is this!!?!!?!1!!
    """
    
    # ROBOT_LIBRARY_SCOPE = "SUITE"
    # ROBOT_LIBRARY_SCOPE = "GLOBAL"
    # ROBOT_LIBRARY_SCOPE = "TEST" # 就是在有使用这个库的case时，会被实例化一次(如果没有用到的case，是不会去实例化的)，其它作用域类似
    ROBOT_LIBRARY_VERSION = "0.0.1"
    # __version__ = "0.0.1"  也可以通过__version__指定在类属性或者模块里面
    ROBOT_LIBRARY_DOC_FORMAT = "reST"

    def __init__(self, name=None, age=None):
        """"""
        self.name = name
        self.age = age
        print('*WARN* Warning from a library.')
        logger.info("info logger", also_console=True)


    def get_name(self) -> str:
        """Nothing more to see here.
        
        Examples:

        .. code:: robotframework

            *** Test Cases ***
            Example
                Get Name    # How cool is this!!?!!?!1!!
        """
        return self.name