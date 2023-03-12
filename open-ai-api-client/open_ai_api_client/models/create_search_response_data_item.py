from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateSearchResponseDataItem")


@attr.s(auto_attribs=True)
class CreateSearchResponseDataItem:
    """
    Attributes:
        object_ (Union[Unset, str]):
        document (Union[Unset, int]):
        score (Union[Unset, float]):
    """

    object_: Union[Unset, str] = UNSET
    document: Union[Unset, int] = UNSET
    score: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        object_ = self.object_
        document = self.document
        score = self.score

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if document is not UNSET:
            field_dict["document"] = document
        if score is not UNSET:
            field_dict["score"] = score

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        object_ = d.pop("object", UNSET)

        document = d.pop("document", UNSET)

        score = d.pop("score", UNSET)

        create_search_response_data_item = cls(
            object_=object_,
            document=document,
            score=score,
        )

        create_search_response_data_item.additional_properties = d
        return create_search_response_data_item

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
