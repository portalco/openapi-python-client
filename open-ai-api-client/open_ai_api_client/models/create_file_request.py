from io import BytesIO
from typing import Any, Dict, Type, TypeVar

import attr

from ..types import File, Unset

T = TypeVar("T", bound="CreateFileRequest")


@attr.s(auto_attribs=True)
class CreateFileRequest:
    """
    Attributes:
        file (File): Name of the [JSON Lines](https://jsonlines.readthedocs.io/en/latest/) file to be uploaded.

            If the `purpose` is set to "fine-tune", each line is a JSON record with "prompt" and "completion" fields
            representing your [training examples](/docs/guides/fine-tuning/prepare-training-data).
        purpose (str): The intended purpose of the uploaded documents.

            Use "fine-tune" for [Fine-tuning](/docs/api-reference/fine-tunes). This allows us to validate the format of the
            uploaded file.
    """

    file: File
    purpose: str

    def to_dict(self) -> Dict[str, Any]:
        file = self.file.to_tuple()

        purpose = self.purpose

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "file": file,
                "purpose": purpose,
            }
        )

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        file = self.file.to_tuple()

        purpose = self.purpose if isinstance(self.purpose, Unset) else (None, str(self.purpose).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "file": file,
                "purpose": purpose,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        file = File(payload=BytesIO(d.pop("file")))

        purpose = d.pop("purpose")

        create_file_request = cls(
            file=file,
            purpose=purpose,
        )

        return create_file_request
