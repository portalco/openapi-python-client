from typing import Any, Dict, List, Optional, Type, TypeVar

import attr

T = TypeVar("T", bound="Engine")


@attr.s(auto_attribs=True)
class Engine:
    """
    Attributes:
        id (str):
        object_ (str):
        ready (bool):
        created (Optional[int]):
    """

    id: str
    object_: str
    ready: bool
    created: Optional[int]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        object_ = self.object_
        ready = self.ready
        created = self.created

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "object": object_,
                "ready": ready,
                "created": created,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        object_ = d.pop("object")

        ready = d.pop("ready")

        created = d.pop("created")

        engine = cls(
            id=id,
            object_=object_,
            ready=ready,
            created=created,
        )

        engine.additional_properties = d
        return engine

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
