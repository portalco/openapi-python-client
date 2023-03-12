from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateClassificationResponseSelectedExamplesItem")


@attr.s(auto_attribs=True)
class CreateClassificationResponseSelectedExamplesItem:
    """
    Attributes:
        document (Union[Unset, int]):
        text (Union[Unset, str]):
        label (Union[Unset, str]):
    """

    document: Union[Unset, int] = UNSET
    text: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        document = self.document
        text = self.text
        label = self.label

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if document is not UNSET:
            field_dict["document"] = document
        if text is not UNSET:
            field_dict["text"] = text
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        document = d.pop("document", UNSET)

        text = d.pop("text", UNSET)

        label = d.pop("label", UNSET)

        create_classification_response_selected_examples_item = cls(
            document=document,
            text=text,
            label=label,
        )

        create_classification_response_selected_examples_item.additional_properties = d
        return create_classification_response_selected_examples_item

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
