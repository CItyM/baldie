from dataclasses import dataclass
from PIL import Image


@dataclass
class Layer:
    # layer id
    id: int
    # layer content
    img: Image

    def __eq__(self, o: object) -> bool:
        return self.id == o.id
