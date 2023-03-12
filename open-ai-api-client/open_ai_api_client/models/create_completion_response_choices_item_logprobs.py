from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_completion_response_choices_item_logprobs_top_logprobs_item import (
        CreateCompletionResponseChoicesItemLogprobsTopLogprobsItem,
    )


T = TypeVar("T", bound="CreateCompletionResponseChoicesItemLogprobs")


@attr.s(auto_attribs=True)
class CreateCompletionResponseChoicesItemLogprobs:
    """
    Attributes:
        tokens (Union[Unset, List[str]]):
        token_logprobs (Union[Unset, List[float]]):
        top_logprobs (Union[Unset, List['CreateCompletionResponseChoicesItemLogprobsTopLogprobsItem']]):
        text_offset (Union[Unset, List[int]]):
    """

    tokens: Union[Unset, List[str]] = UNSET
    token_logprobs: Union[Unset, List[float]] = UNSET
    top_logprobs: Union[Unset, List["CreateCompletionResponseChoicesItemLogprobsTopLogprobsItem"]] = UNSET
    text_offset: Union[Unset, List[int]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tokens: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tokens, Unset):
            tokens = self.tokens

        token_logprobs: Union[Unset, List[float]] = UNSET
        if not isinstance(self.token_logprobs, Unset):
            token_logprobs = self.token_logprobs

        top_logprobs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.top_logprobs, Unset):
            top_logprobs = []
            for top_logprobs_item_data in self.top_logprobs:
                top_logprobs_item = top_logprobs_item_data.to_dict()

                top_logprobs.append(top_logprobs_item)

        text_offset: Union[Unset, List[int]] = UNSET
        if not isinstance(self.text_offset, Unset):
            text_offset = self.text_offset

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tokens is not UNSET:
            field_dict["tokens"] = tokens
        if token_logprobs is not UNSET:
            field_dict["token_logprobs"] = token_logprobs
        if top_logprobs is not UNSET:
            field_dict["top_logprobs"] = top_logprobs
        if text_offset is not UNSET:
            field_dict["text_offset"] = text_offset

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.create_completion_response_choices_item_logprobs_top_logprobs_item import (
            CreateCompletionResponseChoicesItemLogprobsTopLogprobsItem,
        )

        d = src_dict.copy()
        tokens = cast(List[str], d.pop("tokens", UNSET))

        token_logprobs = cast(List[float], d.pop("token_logprobs", UNSET))

        top_logprobs = []
        _top_logprobs = d.pop("top_logprobs", UNSET)
        for top_logprobs_item_data in _top_logprobs or []:
            top_logprobs_item = CreateCompletionResponseChoicesItemLogprobsTopLogprobsItem.from_dict(
                top_logprobs_item_data
            )

            top_logprobs.append(top_logprobs_item)

        text_offset = cast(List[int], d.pop("text_offset", UNSET))

        create_completion_response_choices_item_logprobs = cls(
            tokens=tokens,
            token_logprobs=token_logprobs,
            top_logprobs=top_logprobs,
            text_offset=text_offset,
        )

        create_completion_response_choices_item_logprobs.additional_properties = d
        return create_completion_response_choices_item_logprobs

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
