from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_search_response_data_item import CreateSearchResponseDataItem


T = TypeVar("T", bound="CreateSearchResponse")


@attr.s(auto_attribs=True)
class CreateSearchResponse:
    """
    Attributes:
        object_ (Union[Unset, str]):
        model (Union[Unset, str]):
        data (Union[Unset, List['CreateSearchResponseDataItem']]):
    """

    object_: Union[Unset, str] = UNSET
    model: Union[Unset, str] = UNSET
    data: Union[Unset, List["CreateSearchResponseDataItem"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        object_ = self.object_
        model = self.model
        data: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()

                data.append(data_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if model is not UNSET:
            field_dict["model"] = model
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.create_search_response_data_item import CreateSearchResponseDataItem

        d = src_dict.copy()
        object_ = d.pop("object", UNSET)

        model = d.pop("model", UNSET)

        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = CreateSearchResponseDataItem.from_dict(data_item_data)

            data.append(data_item)

        create_search_response = cls(
            object_=object_,
            model=model,
            data=data,
        )

        create_search_response.additional_properties = d
        return create_search_response

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
