from dataclasses import dataclass
from layer import Layer
from attribute import Attribute


@dataclass
class Part:
    # part name, also works as an id
    name: str
    # layers of the given part
    base: list[Layer]
    # attributes of the given part if any
    attributes: list[Attribute]

    def __eq__(self, o: object) -> bool:
        return self.name == o.name
