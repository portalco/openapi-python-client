from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chat_completion_response_message import ChatCompletionResponseMessage


T = TypeVar("T", bound="CreateChatCompletionResponseChoicesItem")


@attr.s(auto_attribs=True)
class CreateChatCompletionResponseChoicesItem:
    """
    Attributes:
        index (Union[Unset, int]):
        message (Union[Unset, ChatCompletionResponseMessage]):
        finish_reason (Union[Unset, str]):
    """

    index: Union[Unset, int] = UNSET
    message: Union[Unset, "ChatCompletionResponseMessage"] = UNSET
    finish_reason: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        index = self.index
        message: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.message, Unset):
            message = self.message.to_dict()

        finish_reason = self.finish_reason

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if index is not UNSET:
            field_dict["index"] = index
        if message is not UNSET:
            field_dict["message"] = message
        if finish_reason is not UNSET:
            field_dict["finish_reason"] = finish_reason

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.chat_completion_response_message import ChatCompletionResponseMessage

        d = src_dict.copy()
        index = d.pop("index", UNSET)

        _message = d.pop("message", UNSET)
        message: Union[Unset, ChatCompletionResponseMessage]
        if isinstance(_message, Unset):
            message = UNSET
        else:
            message = ChatCompletionResponseMessage.from_dict(_message)

        finish_reason = d.pop("finish_reason", UNSET)

        create_chat_completion_response_choices_item = cls(
            index=index,
            message=message,
            finish_reason=finish_reason,
        )

        create_chat_completion_response_choices_item.additional_properties = d
        return create_chat_completion_response_choices_item

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
