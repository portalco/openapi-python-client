from typing import Any, Dict, List, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="CreateEmbeddingResponseDataItem")


@attr.s(auto_attribs=True)
class CreateEmbeddingResponseDataItem:
    """
    Attributes:
        index (int):
        object_ (str):
        embedding (List[float]):
    """

    index: int
    object_: str
    embedding: List[float]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        index = self.index
        object_ = self.object_
        embedding = self.embedding

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "index": index,
                "object": object_,
                "embedding": embedding,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        index = d.pop("index")

        object_ = d.pop("object")

        embedding = cast(List[float], d.pop("embedding"))

        create_embedding_response_data_item = cls(
            index=index,
            object_=object_,
            embedding=embedding,
        )

        create_embedding_response_data_item.additional_properties = d
        return create_embedding_response_data_item

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
