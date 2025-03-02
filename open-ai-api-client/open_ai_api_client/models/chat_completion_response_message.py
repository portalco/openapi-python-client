from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.chat_completion_response_message_role import ChatCompletionResponseMessageRole

T = TypeVar("T", bound="ChatCompletionResponseMessage")


@attr.s(auto_attribs=True)
class ChatCompletionResponseMessage:
    """
    Attributes:
        role (ChatCompletionResponseMessageRole): The role of the author of this message.
        content (str): The contents of the message
    """

    role: ChatCompletionResponseMessageRole
    content: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        role = self.role.value

        content = self.content

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "role": role,
                "content": content,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        role = ChatCompletionResponseMessageRole(d.pop("role"))

        content = d.pop("content")

        chat_completion_response_message = cls(
            role=role,
            content=content,
        )

        chat_completion_response_message.additional_properties = d
        return chat_completion_response_message

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
