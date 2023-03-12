from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateEmbeddingRequest")


@attr.s(auto_attribs=True)
class CreateEmbeddingRequest:
    """
    Attributes:
        model (str): ID of the model to use. You can use the [List models](/docs/api-reference/models/list) API to see
            all of your available models, or see our [Model overview](/docs/models/overview) for descriptions of them.
        input_ (Union[List[List[int]], List[int], List[str], str]): Input text to get embeddings for, encoded as a
            string or array of tokens. To get embeddings for multiple inputs in a single request, pass an array of strings
            or array of token arrays. Each input must not exceed 8192 tokens in length.
             Example: The quick brown fox jumped over the lazy dog.
        user (Union[Unset, str]): A unique identifier representing your end-user, which can help OpenAI to monitor and
            detect abuse. [Learn more](/docs/guides/safety-best-practices/end-user-ids).
             Example: user-1234.
    """

    model: str
    input_: Union[List[List[int]], List[int], List[str], str]
    user: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        model = self.model
        input_: Union[List[List[int]], List[int], List[str], str]

        if isinstance(self.input_, list):
            input_ = self.input_

        elif isinstance(self.input_, list):
            input_ = self.input_

        elif isinstance(self.input_, list):
            input_ = []
            for input_type_3_item_data in self.input_:
                input_type_3_item = input_type_3_item_data

                input_.append(input_type_3_item)

        else:
            input_ = self.input_

        user = self.user

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "model": model,
                "input": input_,
            }
        )
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        model = d.pop("model")

        def _parse_input_(data: object) -> Union[List[List[int]], List[int], List[str], str]:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                input_type_1 = cast(List[str], data)

                return input_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                input_type_2 = cast(List[int], data)

                return input_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                input_type_3 = UNSET
                _input_type_3 = data
                for input_type_3_item_data in _input_type_3:
                    input_type_3_item = cast(List[int], input_type_3_item_data)

                    input_type_3.append(input_type_3_item)

                return input_type_3
            except:  # noqa: E722
                pass
            return cast(Union[List[List[int]], List[int], List[str], str], data)

        input_ = _parse_input_(d.pop("input"))

        user = d.pop("user", UNSET)

        create_embedding_request = cls(
            model=model,
            input_=input_,
            user=user,
        )

        return create_embedding_request
