from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_edit_response_choices_item_logprobs import CreateEditResponseChoicesItemLogprobs


T = TypeVar("T", bound="CreateEditResponseChoicesItem")


@attr.s(auto_attribs=True)
class CreateEditResponseChoicesItem:
    """
    Attributes:
        text (Union[Unset, str]):
        index (Union[Unset, int]):
        logprobs (Union[Unset, None, CreateEditResponseChoicesItemLogprobs]):
        finish_reason (Union[Unset, str]):
    """

    text: Union[Unset, str] = UNSET
    index: Union[Unset, int] = UNSET
    logprobs: Union[Unset, None, "CreateEditResponseChoicesItemLogprobs"] = UNSET
    finish_reason: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        text = self.text
        index = self.index
        logprobs: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.logprobs, Unset):
            logprobs = self.logprobs.to_dict() if self.logprobs else None

        finish_reason = self.finish_reason

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if text is not UNSET:
            field_dict["text"] = text
        if index is not UNSET:
            field_dict["index"] = index
        if logprobs is not UNSET:
            field_dict["logprobs"] = logprobs
        if finish_reason is not UNSET:
            field_dict["finish_reason"] = finish_reason

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.create_edit_response_choices_item_logprobs import CreateEditResponseChoicesItemLogprobs

        d = src_dict.copy()
        text = d.pop("text", UNSET)

        index = d.pop("index", UNSET)

        _logprobs = d.pop("logprobs", UNSET)
        logprobs: Union[Unset, None, CreateEditResponseChoicesItemLogprobs]
        if _logprobs is None:
            logprobs = None
        elif isinstance(_logprobs, Unset):
            logprobs = UNSET
        else:
            logprobs = CreateEditResponseChoicesItemLogprobs.from_dict(_logprobs)

        finish_reason = d.pop("finish_reason", UNSET)

        create_edit_response_choices_item = cls(
            text=text,
            index=index,
            logprobs=logprobs,
            finish_reason=finish_reason,
        )

        create_edit_response_choices_item.additional_properties = d
        return create_edit_response_choices_item

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
