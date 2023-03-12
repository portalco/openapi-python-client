from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_classification_response_selected_examples_item import (
        CreateClassificationResponseSelectedExamplesItem,
    )


T = TypeVar("T", bound="CreateClassificationResponse")


@attr.s(auto_attribs=True)
class CreateClassificationResponse:
    """
    Attributes:
        object_ (Union[Unset, str]):
        model (Union[Unset, str]):
        search_model (Union[Unset, str]):
        completion (Union[Unset, str]):
        label (Union[Unset, str]):
        selected_examples (Union[Unset, List['CreateClassificationResponseSelectedExamplesItem']]):
    """

    object_: Union[Unset, str] = UNSET
    model: Union[Unset, str] = UNSET
    search_model: Union[Unset, str] = UNSET
    completion: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    selected_examples: Union[Unset, List["CreateClassificationResponseSelectedExamplesItem"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        object_ = self.object_
        model = self.model
        search_model = self.search_model
        completion = self.completion
        label = self.label
        selected_examples: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.selected_examples, Unset):
            selected_examples = []
            for selected_examples_item_data in self.selected_examples:
                selected_examples_item = selected_examples_item_data.to_dict()

                selected_examples.append(selected_examples_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if model is not UNSET:
            field_dict["model"] = model
        if search_model is not UNSET:
            field_dict["search_model"] = search_model
        if completion is not UNSET:
            field_dict["completion"] = completion
        if label is not UNSET:
            field_dict["label"] = label
        if selected_examples is not UNSET:
            field_dict["selected_examples"] = selected_examples

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.create_classification_response_selected_examples_item import (
            CreateClassificationResponseSelectedExamplesItem,
        )

        d = src_dict.copy()
        object_ = d.pop("object", UNSET)

        model = d.pop("model", UNSET)

        search_model = d.pop("search_model", UNSET)

        completion = d.pop("completion", UNSET)

        label = d.pop("label", UNSET)

        selected_examples = []
        _selected_examples = d.pop("selected_examples", UNSET)
        for selected_examples_item_data in _selected_examples or []:
            selected_examples_item = CreateClassificationResponseSelectedExamplesItem.from_dict(
                selected_examples_item_data
            )

            selected_examples.append(selected_examples_item)

        create_classification_response = cls(
            object_=object_,
            model=model,
            search_model=search_model,
            completion=completion,
            label=label,
            selected_examples=selected_examples,
        )

        create_classification_response.additional_properties = d
        return create_classification_response

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
