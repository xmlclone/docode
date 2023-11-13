"""
https://lxml.de/apidoc/lxml.etree.html

pip install lxml
"""


import logging
# logging.basicConfig(format="%(lineno)d   %(message)s", level=logging.INFO)

try:
    import lxml.etree as ET
    logging.warning("using lxml")
except ImportError:
    import xml.etree.ElementTree as ET
    logging.warning("using xml.etree")

from pathlib import Path
from typing import Literal
from functools import cached_property





class Suite:
    def __init__(self) -> None:
        self.id: int = None
        self.name: str = None
        self.source: Path = None
        self.parent_id: int = None
    
    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return self.id
    

class Case:
    def __init__(self) -> None:
        self.id: int = None
        self.name: str = None
        self.tags: list[str] = list()
        self.status: Literal["PASS", "FAIL"] = None
        self.parent_id: int = None

    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return self.id
    

class RFXMLParse:
    def __init__(self, xmlfile: Path) -> None:
        self.tree = ET.parse(xmlfile)
        self.root = self.tree.getroot()

    @cached_property
    def cases(self) -> list[Case]:
        return self.__parse_case(self.root)
    
    @cached_property
    def suites(self) -> list[Suite]:
        return self.__parse_suite(self.root)

    def __parse_case(self, root) -> list[Case]:
        cases = []
        for e in root:
            if e.tag == 'test':
                case = Case()
                case.id = e.attrib['id']
                case.name = e.attrib['name']
                case.parent_id = self.getparent(e, self.root).attrib.get('id', root)
                for _e in e:
                    if _e.tag == 'tag': 
                        case.tags.append(_e.text)
                    elif _e.tag == 'status': 
                        case.status = _e.attrib['status']
                cases.append(case)
            elif e.tag == 'suite':
                return self.__parse_case(e)
        return cases

    def __parse_suite(self, root) -> list[Suite]:
        suites = []
        for e in root:
            if e.tag == 'suite':
                suite = Suite()
                suite.id = e.attrib['id']
                suite.name = e.attrib['name']
                suite.source = e.attrib['source']
                suite.parent_id = self.getparent(e, self.root).attrib.get('id', root)
                suites.append(suite)
        return suites
    
    def getparent(self, element, parent):
        try: 
            return element.getparent()
        except AttributeError:
            for e in parent:
                if e is element: 
                    return parent
                result = self.getparent(element, e)
                if result is not None: 
                    return result

    def get_suite_parent(self, suite: Suite) -> list[Suite]:
        for _suite in self.suites:
            if _suite.id == suite.parent_id:
                return [_suite] + (self.get_suite_parent(_suite) or [])

    def get_case_parent(self, case: Case) -> list[Suite]:
        for suite in self.suites:
            if suite.id == case.parent_id:
                return [suite] + (self.get_suite_parent(suite) or [])


xml = RFXMLParse("output.xml")
for suite in xml.suites:
    logging.info(f"{suite.id=}, {suite.name=}, {suite.parent_id=}, {suite.source=}")
    parents = xml.get_suite_parent(suite)
    logging.info(f"{parents=}")
for case in xml.cases:
    logging.info(f"{case.id=}, {case.name=}, {case.parent_id=}, {case.status}")
    parents = xml.get_case_parent(case)
    logging.info(f"{parents=}")
        