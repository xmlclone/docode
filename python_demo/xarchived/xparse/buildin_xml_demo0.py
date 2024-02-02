import logging
import xml.etree.ElementTree as ET

from pathlib import Path
from typing import Literal
from xml.etree.ElementTree import Element


logging.basicConfig(format="%(lineno)d   %(message)s", level=logging.INFO)


class Suite:
    def __init__(self) -> None:
        self.id: int = None
        self.name: str = None
        self.source: Path = None
        self.parent_id: int = None


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
    

def _parse(element: Element) -> list[Case]:
    cases = []
    for e in element:
        if e.tag == 'test':
            case = Case()
            case.id = e.attrib['id']
            case.name = e.attrib['name']
            for _e in e:
                if _e.tag == 'tag':
                    case.tags.append(_e.text)
                elif _e.tag == 'status':
                    case.status = _e.attrib['status']
            cases.append(case)
        elif e.tag == 'suite':
            return _parse(e)
    return cases

def parse(xmlfile: str | Path):
    tree = ET.parse(xmlfile)
    root = tree.getroot()
    for e in root.iter():
        e.get
        logging.info(f"{e.tag=}, {e.find("..")}")
    # logging.info(f"{root=}")
    # return _parse(root)

cases = parse("output.xml")
logging.info(cases)
        