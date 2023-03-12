from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.create_edit_response_choices_item import CreateEditResponseChoicesItem
    from ..models.create_edit_response_usage import CreateEditResponseUsage


T = TypeVar("T", bound="CreateEditResponse")


@attr.s(auto_attribs=True)
class CreateEditResponse:
    """
    Attributes:
        object_ (str):
        created (int):
        choices (List['CreateEditResponseChoicesItem']):
        usage (CreateEditResponseUsage):
    """

    object_: str
    created: int
    choices: List["CreateEditResponseChoicesItem"]
    usage: "CreateEditResponseUsage"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        object_ = self.object_
        created = self.created
        choices = []
        for choices_item_data in self.choices:
            choices_item = choices_item_data.to_dict()

            choices.append(choices_item)

        usage = self.usage.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object": object_,
                "created": created,
                "choices": choices,
                "usage": usage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.create_edit_response_choices_item import CreateEditResponseChoicesItem
        from ..models.create_edit_response_usage import CreateEditResponseUsage

        d = src_dict.copy()
        object_ = d.pop("object")

        created = d.pop("created")

        choices = []
        _choices = d.pop("choices")
        for choices_item_data in _choices:
            choices_item = CreateEditResponseChoicesItem.from_dict(choices_item_data)

            choices.append(choices_item)

        usage = CreateEditResponseUsage.from_dict(d.pop("usage"))

        create_edit_response = cls(
            object_=object_,
            created=created,
            choices=choices,
            usage=usage,
        )

        create_edit_response.additional_properties = d
        return create_edit_response

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
