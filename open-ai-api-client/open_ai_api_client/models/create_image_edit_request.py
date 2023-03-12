from io import BytesIO
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

import attr

from ..models.create_image_edit_request_response_format import CreateImageEditRequestResponseFormat
from ..models.create_image_edit_request_size import CreateImageEditRequestSize
from ..types import UNSET, File, FileJsonType, Unset

T = TypeVar("T", bound="CreateImageEditRequest")


@attr.s(auto_attribs=True)
class CreateImageEditRequest:
    """
    Attributes:
        image (File): The image to edit. Must be a valid PNG file, less than 4MB, and square. If mask is not provided,
            image must have transparency, which will be used as the mask.
        prompt (str): A text description of the desired image(s). The maximum length is 1000 characters. Example: A cute
            baby sea otter wearing a beret.
        mask (Union[Unset, File]): An additional image whose fully transparent areas (e.g. where alpha is zero) indicate
            where `image` should be edited. Must be a valid PNG file, less than 4MB, and have the same dimensions as
            `image`.
        n (Union[Unset, None, int]): The number of images to generate. Must be between 1 and 10. Default: 1. Example: 1.
        size (Union[Unset, None, CreateImageEditRequestSize]): The size of the generated images. Must be one of
            `256x256`, `512x512`, or `1024x1024`. Default: CreateImageEditRequestSize.VALUE_2. Example: 1024x1024.
        response_format (Union[Unset, None, CreateImageEditRequestResponseFormat]): The format in which the generated
            images are returned. Must be one of `url` or `b64_json`. Default: CreateImageEditRequestResponseFormat.URL.
            Example: url.
        user (Union[Unset, str]): A unique identifier representing your end-user, which can help OpenAI to monitor and
            detect abuse. [Learn more](/docs/guides/safety-best-practices/end-user-ids).
             Example: user-1234.
    """

    image: File
    prompt: str
    mask: Union[Unset, File] = UNSET
    n: Union[Unset, None, int] = 1
    size: Union[Unset, None, CreateImageEditRequestSize] = CreateImageEditRequestSize.VALUE_2
    response_format: Union[Unset, None, CreateImageEditRequestResponseFormat] = CreateImageEditRequestResponseFormat.URL
    user: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        image = self.image.to_tuple()

        prompt = self.prompt
        mask: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.mask, Unset):
            mask = self.mask.to_tuple()

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
                "image": image,
                "prompt": prompt,
            }
        )
        if mask is not UNSET:
            field_dict["mask"] = mask
        if n is not UNSET:
            field_dict["n"] = n
        if size is not UNSET:
            field_dict["size"] = size
        if response_format is not UNSET:
            field_dict["response_format"] = response_format
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        image = self.image.to_tuple()

        prompt = self.prompt if isinstance(self.prompt, Unset) else (None, str(self.prompt).encode(), "text/plain")
        mask: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.mask, Unset):
            mask = self.mask.to_tuple()

        n = self.n if isinstance(self.n, Unset) else (None, str(self.n).encode(), "text/plain")
        size: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.size, Unset):
            size = (None, str(self.size.value).encode(), "text/plain") if self.size else None

        response_format: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.response_format, Unset):
            response_format = (
                (None, str(self.response_format.value).encode(), "text/plain") if self.response_format else None
            )

        user = self.user if isinstance(self.user, Unset) else (None, str(self.user).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "image": image,
                "prompt": prompt,
            }
        )
        if mask is not UNSET:
            field_dict["mask"] = mask
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
        image = File(payload=BytesIO(d.pop("image")))

        prompt = d.pop("prompt")

        _mask = d.pop("mask", UNSET)
        mask: Union[Unset, File]
        if isinstance(_mask, Unset):
            mask = UNSET
        else:
            mask = File(payload=BytesIO(_mask))

        n = d.pop("n", UNSET)

        _size = d.pop("size", UNSET)
        size: Union[Unset, None, CreateImageEditRequestSize]
        if _size is None:
            size = None
        elif isinstance(_size, Unset):
            size = UNSET
        else:
            size = CreateImageEditRequestSize(_size)

        _response_format = d.pop("response_format", UNSET)
        response_format: Union[Unset, None, CreateImageEditRequestResponseFormat]
        if _response_format is None:
            response_format = None
        elif isinstance(_response_format, Unset):
            response_format = UNSET
        else:
            response_format = CreateImageEditRequestResponseFormat(_response_format)

        user = d.pop("user", UNSET)

        create_image_edit_request = cls(
            image=image,
            prompt=prompt,
            mask=mask,
            n=n,
            size=size,
            response_format=response_format,
            user=user,
        )

        create_image_edit_request.additional_properties = d
        return create_image_edit_request

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
