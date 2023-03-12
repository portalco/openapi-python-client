from enum import Enum


class CreateImageRequestResponseFormat(str, Enum):
    URL = "url"
    B64_JSON = "b64_json"

    def __str__(self) -> str:
        return str(self.value)
