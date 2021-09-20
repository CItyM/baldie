from dataclasses import dataclass
from .layer import Layer


@dataclass
class Attribute:
    # base part name, also works as an id
    name: str
    # layers of the given base part
    layers: list[Layer]

    def __eq__(self, o: object) -> bool:
        return self.name == o.name
