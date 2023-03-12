from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.fine_tune_event import FineTuneEvent


T = TypeVar("T", bound="ListFineTuneEventsResponse")


@attr.s(auto_attribs=True)
class ListFineTuneEventsResponse:
    """
    Attributes:
        object_ (str):
        data (List['FineTuneEvent']):
    """

    object_: str
    data: List["FineTuneEvent"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        object_ = self.object_
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()

            data.append(data_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object": object_,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fine_tune_event import FineTuneEvent

        d = src_dict.copy()
        object_ = d.pop("object")

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = FineTuneEvent.from_dict(data_item_data)

            data.append(data_item)

        list_fine_tune_events_response = cls(
            object_=object_,
            data=data,
        )

        list_fine_tune_events_response.additional_properties = d
        return list_fine_tune_events_response

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
