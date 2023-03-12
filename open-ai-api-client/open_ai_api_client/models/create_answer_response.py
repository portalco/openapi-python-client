from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_answer_response_selected_documents_item import CreateAnswerResponseSelectedDocumentsItem


T = TypeVar("T", bound="CreateAnswerResponse")


@attr.s(auto_attribs=True)
class CreateAnswerResponse:
    """
    Attributes:
        object_ (Union[Unset, str]):
        model (Union[Unset, str]):
        search_model (Union[Unset, str]):
        completion (Union[Unset, str]):
        answers (Union[Unset, List[str]]):
        selected_documents (Union[Unset, List['CreateAnswerResponseSelectedDocumentsItem']]):
    """

    object_: Union[Unset, str] = UNSET
    model: Union[Unset, str] = UNSET
    search_model: Union[Unset, str] = UNSET
    completion: Union[Unset, str] = UNSET
    answers: Union[Unset, List[str]] = UNSET
    selected_documents: Union[Unset, List["CreateAnswerResponseSelectedDocumentsItem"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        object_ = self.object_
        model = self.model
        search_model = self.search_model
        completion = self.completion
        answers: Union[Unset, List[str]] = UNSET
        if not isinstance(self.answers, Unset):
            answers = self.answers

        selected_documents: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.selected_documents, Unset):
            selected_documents = []
            for selected_documents_item_data in self.selected_documents:
                selected_documents_item = selected_documents_item_data.to_dict()

                selected_documents.append(selected_documents_item)

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
        if answers is not UNSET:
            field_dict["answers"] = answers
        if selected_documents is not UNSET:
            field_dict["selected_documents"] = selected_documents

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.create_answer_response_selected_documents_item import CreateAnswerResponseSelectedDocumentsItem

        d = src_dict.copy()
        object_ = d.pop("object", UNSET)

        model = d.pop("model", UNSET)

        search_model = d.pop("search_model", UNSET)

        completion = d.pop("completion", UNSET)

        answers = cast(List[str], d.pop("answers", UNSET))

        selected_documents = []
        _selected_documents = d.pop("selected_documents", UNSET)
        for selected_documents_item_data in _selected_documents or []:
            selected_documents_item = CreateAnswerResponseSelectedDocumentsItem.from_dict(selected_documents_item_data)

            selected_documents.append(selected_documents_item)

        create_answer_response = cls(
            object_=object_,
            model=model,
            search_model=search_model,
            completion=completion,
            answers=answers,
            selected_documents=selected_documents,
        )

        create_answer_response.additional_properties = d
        return create_answer_response

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
