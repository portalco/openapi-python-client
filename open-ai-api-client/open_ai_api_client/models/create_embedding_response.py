from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.create_embedding_response_data_item import CreateEmbeddingResponseDataItem
    from ..models.create_embedding_response_usage import CreateEmbeddingResponseUsage


T = TypeVar("T", bound="CreateEmbeddingResponse")


@attr.s(auto_attribs=True)
class CreateEmbeddingResponse:
    """
    Attributes:
        object_ (str):
        model (str):
        data (List['CreateEmbeddingResponseDataItem']):
        usage (CreateEmbeddingResponseUsage):
    """

    object_: str
    model: str
    data: List["CreateEmbeddingResponseDataItem"]
    usage: "CreateEmbeddingResponseUsage"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        object_ = self.object_
        model = self.model
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()

            data.append(data_item)

        usage = self.usage.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object": object_,
                "model": model,
                "data": data,
                "usage": usage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.create_embedding_response_data_item import CreateEmbeddingResponseDataItem
        from ..models.create_embedding_response_usage import CreateEmbeddingResponseUsage

        d = src_dict.copy()
        object_ = d.pop("object")

        model = d.pop("model")

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = CreateEmbeddingResponseDataItem.from_dict(data_item_data)

            data.append(data_item)

        usage = CreateEmbeddingResponseUsage.from_dict(d.pop("usage"))

        create_embedding_response = cls(
            object_=object_,
            model=model,
            data=data,
            usage=usage,
        )

        create_embedding_response.additional_properties = d
        return create_embedding_response

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
