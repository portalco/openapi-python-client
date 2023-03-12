from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="Model")


@attr.s(auto_attribs=True)
class Model:
    """
    Attributes:
        id (str):
        object_ (str):
        created (int):
        owned_by (str):
    """

    id: str
    object_: str
    created: int
    owned_by: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        object_ = self.object_
        created = self.created
        owned_by = self.owned_by

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "object": object_,
                "created": created,
                "owned_by": owned_by,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        object_ = d.pop("object")

        created = d.pop("created")

        owned_by = d.pop("owned_by")

        model = cls(
            id=id,
            object_=object_,
            created=created,
            owned_by=owned_by,
        )

        model.additional_properties = d
        return model

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
