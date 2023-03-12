from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.chat_completion_request_message_role import ChatCompletionRequestMessageRole
from ..types import UNSET, Unset

T = TypeVar("T", bound="ChatCompletionRequestMessage")


@attr.s(auto_attribs=True)
class ChatCompletionRequestMessage:
    """
    Attributes:
        role (ChatCompletionRequestMessageRole): The role of the author of this message.
        content (str): The contents of the message
        name (Union[Unset, str]): The name of the user in a multi-user chat
    """

    role: ChatCompletionRequestMessageRole
    content: str
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        role = self.role.value

        content = self.content
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "role": role,
                "content": content,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        role = ChatCompletionRequestMessageRole(d.pop("role"))

        content = d.pop("content")

        name = d.pop("name", UNSET)

        chat_completion_request_message = cls(
            role=role,
            content=content,
            name=name,
        )

        chat_completion_request_message.additional_properties = d
        return chat_completion_request_message

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
