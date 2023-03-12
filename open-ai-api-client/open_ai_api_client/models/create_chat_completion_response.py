from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_chat_completion_response_choices_item import CreateChatCompletionResponseChoicesItem
    from ..models.create_chat_completion_response_usage import CreateChatCompletionResponseUsage


T = TypeVar("T", bound="CreateChatCompletionResponse")


@attr.s(auto_attribs=True)
class CreateChatCompletionResponse:
    """
    Attributes:
        id (str):
        object_ (str):
        created (int):
        model (str):
        choices (List['CreateChatCompletionResponseChoicesItem']):
        usage (Union[Unset, CreateChatCompletionResponseUsage]):
    """

    id: str
    object_: str
    created: int
    model: str
    choices: List["CreateChatCompletionResponseChoicesItem"]
    usage: Union[Unset, "CreateChatCompletionResponseUsage"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        object_ = self.object_
        created = self.created
        model = self.model
        choices = []
        for choices_item_data in self.choices:
            choices_item = choices_item_data.to_dict()

            choices.append(choices_item)

        usage: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.usage, Unset):
            usage = self.usage.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "object": object_,
                "created": created,
                "model": model,
                "choices": choices,
            }
        )
        if usage is not UNSET:
            field_dict["usage"] = usage

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.create_chat_completion_response_choices_item import CreateChatCompletionResponseChoicesItem
        from ..models.create_chat_completion_response_usage import CreateChatCompletionResponseUsage

        d = src_dict.copy()
        id = d.pop("id")

        object_ = d.pop("object")

        created = d.pop("created")

        model = d.pop("model")

        choices = []
        _choices = d.pop("choices")
        for choices_item_data in _choices:
            choices_item = CreateChatCompletionResponseChoicesItem.from_dict(choices_item_data)

            choices.append(choices_item)

        _usage = d.pop("usage", UNSET)
        usage: Union[Unset, CreateChatCompletionResponseUsage]
        if isinstance(_usage, Unset):
            usage = UNSET
        else:
            usage = CreateChatCompletionResponseUsage.from_dict(_usage)

        create_chat_completion_response = cls(
            id=id,
            object_=object_,
            created=created,
            model=model,
            choices=choices,
            usage=usage,
        )

        create_chat_completion_response.additional_properties = d
        return create_chat_completion_response

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
