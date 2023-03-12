from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.open_ai_file_status_details import OpenAIFileStatusDetails


T = TypeVar("T", bound="OpenAIFile")


@attr.s(auto_attribs=True)
class OpenAIFile:
    """
    Attributes:
        id (str):
        object_ (str):
        bytes_ (int):
        created_at (int):
        filename (str):
        purpose (str):
        status (Union[Unset, str]):
        status_details (Union[Unset, None, OpenAIFileStatusDetails]):
    """

    id: str
    object_: str
    bytes_: int
    created_at: int
    filename: str
    purpose: str
    status: Union[Unset, str] = UNSET
    status_details: Union[Unset, None, "OpenAIFileStatusDetails"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        object_ = self.object_
        bytes_ = self.bytes_
        created_at = self.created_at
        filename = self.filename
        purpose = self.purpose
        status = self.status
        status_details: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.status_details, Unset):
            status_details = self.status_details.to_dict() if self.status_details else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "object": object_,
                "bytes": bytes_,
                "created_at": created_at,
                "filename": filename,
                "purpose": purpose,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if status_details is not UNSET:
            field_dict["status_details"] = status_details

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.open_ai_file_status_details import OpenAIFileStatusDetails

        d = src_dict.copy()
        id = d.pop("id")

        object_ = d.pop("object")

        bytes_ = d.pop("bytes")

        created_at = d.pop("created_at")

        filename = d.pop("filename")

        purpose = d.pop("purpose")

        status = d.pop("status", UNSET)

        _status_details = d.pop("status_details", UNSET)
        status_details: Union[Unset, None, OpenAIFileStatusDetails]
        if _status_details is None:
            status_details = None
        elif isinstance(_status_details, Unset):
            status_details = UNSET
        else:
            status_details = OpenAIFileStatusDetails.from_dict(_status_details)

        open_ai_file = cls(
            id=id,
            object_=object_,
            bytes_=bytes_,
            created_at=created_at,
            filename=filename,
            purpose=purpose,
            status=status,
            status_details=status_details,
        )

        open_ai_file.additional_properties = d
        return open_ai_file

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
