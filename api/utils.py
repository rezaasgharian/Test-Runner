from enum import Enum
from typing import List, Tuple


class ExtendedEnum(Enum):
    @classmethod
    def get_as_tuple(cls) -> List[Tuple]:
        #  return str representation of value to allow for objects as values
        return [(item.name, str(item.value)) for item in cls]
