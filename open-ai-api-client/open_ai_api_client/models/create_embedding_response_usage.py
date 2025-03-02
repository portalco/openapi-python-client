from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="CreateEmbeddingResponseUsage")


@attr.s(auto_attribs=True)
class CreateEmbeddingResponseUsage:
    """
    Attributes:
        prompt_tokens (int):
        total_tokens (int):
    """

    prompt_tokens: int
    total_tokens: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        prompt_tokens = self.prompt_tokens
        total_tokens = self.total_tokens

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "prompt_tokens": prompt_tokens,
                "total_tokens": total_tokens,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        prompt_tokens = d.pop("prompt_tokens")

        total_tokens = d.pop("total_tokens")

        create_embedding_response_usage = cls(
            prompt_tokens=prompt_tokens,
            total_tokens=total_tokens,
        )

        create_embedding_response_usage.additional_properties = d
        return create_embedding_response_usage

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
