from io import BytesIO
from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, File, Unset

T = TypeVar("T", bound="CreateTranslationRequest")


@attr.s(auto_attribs=True)
class CreateTranslationRequest:
    """
    Attributes:
        file (File): The audio file to translate, in one of these formats: mp3, mp4, mpeg, mpga, m4a, wav, or webm.
        model (str): ID of the model to use. Only `whisper-1` is currently available.
        prompt (Union[Unset, str]): An optional text to guide the model's style or continue a previous audio segment.
            The [prompt](/docs/guides/speech-to-text/prompting) should be in English.
        response_format (Union[Unset, str]): The format of the transcript output, in one of these options: json, text,
            srt, verbose_json, or vtt.
             Default: 'json'.
        temperature (Union[Unset, float]): The sampling temperature, between 0 and 1. Higher values like 0.8 will make
            the output more random, while lower values like 0.2 will make it more focused and deterministic. If set to 0,
            the model will use [log probability](https://en.wikipedia.org/wiki/Log_probability) to automatically increase
            the temperature until certain thresholds are hit.
    """

    file: File
    model: str
    prompt: Union[Unset, str] = UNSET
    response_format: Union[Unset, str] = "json"
    temperature: Union[Unset, float] = 0.0

    def to_dict(self) -> Dict[str, Any]:
        file = self.file.to_tuple()

        model = self.model
        prompt = self.prompt
        response_format = self.response_format
        temperature = self.temperature

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "file": file,
                "model": model,
            }
        )
        if prompt is not UNSET:
            field_dict["prompt"] = prompt
        if response_format is not UNSET:
            field_dict["response_format"] = response_format
        if temperature is not UNSET:
            field_dict["temperature"] = temperature

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        file = self.file.to_tuple()

        model = self.model if isinstance(self.model, Unset) else (None, str(self.model).encode(), "text/plain")
        prompt = self.prompt if isinstance(self.prompt, Unset) else (None, str(self.prompt).encode(), "text/plain")
        response_format = (
            self.response_format
            if isinstance(self.response_format, Unset)
            else (None, str(self.response_format).encode(), "text/plain")
        )
        temperature = (
            self.temperature
            if isinstance(self.temperature, Unset)
            else (None, str(self.temperature).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "file": file,
                "model": model,
            }
        )
        if prompt is not UNSET:
            field_dict["prompt"] = prompt
        if response_format is not UNSET:
            field_dict["response_format"] = response_format
        if temperature is not UNSET:
            field_dict["temperature"] = temperature

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        file = File(payload=BytesIO(d.pop("file")))

        model = d.pop("model")

        prompt = d.pop("prompt", UNSET)

        response_format = d.pop("response_format", UNSET)

        temperature = d.pop("temperature", UNSET)

        create_translation_request = cls(
            file=file,
            model=model,
            prompt=prompt,
            response_format=response_format,
            temperature=temperature,
        )

        return create_translation_request
