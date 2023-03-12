from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.create_image_request_response_format import CreateImageRequestResponseFormat
from ..models.create_image_request_size import CreateImageRequestSize
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateImageRequest")


@attr.s(auto_attribs=True)
class CreateImageRequest:
    """
    Attributes:
        prompt (str): A text description of the desired image(s). The maximum length is 1000 characters. Example: A cute
            baby sea otter.
        n (Union[Unset, None, int]): The number of images to generate. Must be between 1 and 10. Default: 1. Example: 1.
        size (Union[Unset, None, CreateImageRequestSize]): The size of the generated images. Must be one of `256x256`,
            `512x512`, or `1024x1024`. Default: CreateImageRequestSize.VALUE_2. Example: 1024x1024.
        response_format (Union[Unset, None, CreateImageRequestResponseFormat]): The format in which the generated images
            are returned. Must be one of `url` or `b64_json`. Default: CreateImageRequestResponseFormat.URL. Example: url.
        user (Union[Unset, str]): A unique identifier representing your end-user, which can help OpenAI to monitor and
            detect abuse. [Learn more](/docs/guides/safety-best-practices/end-user-ids).
             Example: user-1234.
    """

    prompt: str
    n: Union[Unset, None, int] = 1
    size: Union[Unset, None, CreateImageRequestSize] = CreateImageRequestSize.VALUE_2
    response_format: Union[Unset, None, CreateImageRequestResponseFormat] = CreateImageRequestResponseFormat.URL
    user: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        prompt = self.prompt
        n = self.n
        size: Union[Unset, None, str] = UNSET
        if not isinstance(self.size, Unset):
            size = self.size.value if self.size else None

        response_format: Union[Unset, None, str] = UNSET
        if not isinstance(self.response_format, Unset):
            response_format = self.response_format.value if self.response_format else None

        user = self.user

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "prompt": prompt,
            }
        )
        if n is not UNSET:
            field_dict["n"] = n
        if size is not UNSET:
            field_dict["size"] = size
        if response_format is not UNSET:
            field_dict["response_format"] = response_format
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        prompt = d.pop("prompt")

        n = d.pop("n", UNSET)

        _size = d.pop("size", UNSET)
        size: Union[Unset, None, CreateImageRequestSize]
        if _size is None:
            size = None
        elif isinstance(_size, Unset):
            size = UNSET
        else:
            size = CreateImageRequestSize(_size)

        _response_format = d.pop("response_format", UNSET)
        response_format: Union[Unset, None, CreateImageRequestResponseFormat]
        if _response_format is None:
            response_format = None
        elif isinstance(_response_format, Unset):
            response_format = UNSET
        else:
            response_format = CreateImageRequestResponseFormat(_response_format)

        user = d.pop("user", UNSET)

        create_image_request = cls(
            prompt=prompt,
            n=n,
            size=size,
            response_format=response_format,
            user=user,
        )

        create_image_request.additional_properties = d
        return create_image_request

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
