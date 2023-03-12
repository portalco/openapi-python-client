from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="FineTuneEvent")


@attr.s(auto_attribs=True)
class FineTuneEvent:
    """
    Attributes:
        object_ (str):
        created_at (int):
        level (str):
        message (str):
    """

    object_: str
    created_at: int
    level: str
    message: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        object_ = self.object_
        created_at = self.created_at
        level = self.level
        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object": object_,
                "created_at": created_at,
                "level": level,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        object_ = d.pop("object")

        created_at = d.pop("created_at")

        level = d.pop("level")

        message = d.pop("message")

        fine_tune_event = cls(
            object_=object_,
            created_at=created_at,
            level=level,
            message=message,
        )

        fine_tune_event.additional_properties = d
        return fine_tune_event

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
