from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ImagesResponseDataItem")


@attr.s(auto_attribs=True)
class ImagesResponseDataItem:
    """
    Attributes:
        url (Union[Unset, str]):
        b64_json (Union[Unset, str]):
    """

    url: Union[Unset, str] = UNSET
    b64_json: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        b64_json = self.b64_json

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if b64_json is not UNSET:
            field_dict["b64_json"] = b64_json

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url", UNSET)

        b64_json = d.pop("b64_json", UNSET)

        images_response_data_item = cls(
            url=url,
            b64_json=b64_json,
        )

        images_response_data_item.additional_properties = d
        return images_response_data_item

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
