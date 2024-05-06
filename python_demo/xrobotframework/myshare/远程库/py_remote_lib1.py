# pip install robotremoteserver

# $ python -m robotremoteserver test
# Remote server running at http://127.0.0.1:8270.
# $ python -m robotremoteserver test http://10.0.0.42:57347
# No remote server running at http://10.0.0.42:57347.

# python -m robot.libdoc Remote::http://127.0.0.1:8270 list
# python -m robot.libdoc Remote::http://127.0.0.1:8270 MyLibrary.html


import requests
from typing import Any
from robotremoteserver import RobotRemoteServer


class DemoLibrary(object):
    def get(self, url: str) -> Any:
        ret = requests.get(url)
        return ret.json()
    

if __name__ == '__main__':
    RobotRemoteServer(DemoLibrary())
