from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="DeleteModelResponse")


@attr.s(auto_attribs=True)
class DeleteModelResponse:
    """
    Attributes:
        id (str):
        object_ (str):
        deleted (bool):
    """

    id: str
    object_: str
    deleted: bool
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        object_ = self.object_
        deleted = self.deleted

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "object": object_,
                "deleted": deleted,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        object_ = d.pop("object")

        deleted = d.pop("deleted")

        delete_model_response = cls(
            id=id,
            object_=object_,
            deleted=deleted,
        )

        delete_model_response.additional_properties = d
        return delete_model_response

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
