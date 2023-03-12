from io import BytesIO
from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, File, Unset

T = TypeVar("T", bound="CreateTranscriptionRequest")


@attr.s(auto_attribs=True)
class CreateTranscriptionRequest:
    """
    Attributes:
        file (File): The audio file to transcribe, in one of these formats: mp3, mp4, mpeg, mpga, m4a, wav, or webm.
        model (str): ID of the model to use. Only `whisper-1` is currently available.
        prompt (Union[Unset, str]): An optional text to guide the model's style or continue a previous audio segment.
            The [prompt](/docs/guides/speech-to-text/prompting) should match the audio language.
        response_format (Union[Unset, str]): The format of the transcript output, in one of these options: json, text,
            srt, verbose_json, or vtt.
             Default: 'json'.
        temperature (Union[Unset, float]): The sampling temperature, between 0 and 1. Higher values like 0.8 will make
            the output more random, while lower values like 0.2 will make it more focused and deterministic. If set to 0,
            the model will use [log probability](https://en.wikipedia.org/wiki/Log_probability) to automatically increase
            the temperature until certain thresholds are hit.
        language (Union[Unset, str]): The language of the input audio. Supplying the input language in
            [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) format will improve accuracy and latency.
    """

    file: File
    model: str
    prompt: Union[Unset, str] = UNSET
    response_format: Union[Unset, str] = "json"
    temperature: Union[Unset, float] = 0.0
    language: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        file = self.file.to_tuple()

        model = self.model
        prompt = self.prompt
        response_format = self.response_format
        temperature = self.temperature
        language = self.language

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
        if language is not UNSET:
            field_dict["language"] = language

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
        language = (
            self.language if isinstance(self.language, Unset) else (None, str(self.language).encode(), "text/plain")
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
        if language is not UNSET:
            field_dict["language"] = language

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        file = File(payload=BytesIO(d.pop("file")))

        model = d.pop("model")

        prompt = d.pop("prompt", UNSET)

        response_format = d.pop("response_format", UNSET)

        temperature = d.pop("temperature", UNSET)

        language = d.pop("language", UNSET)

        create_transcription_request = cls(
            file=file,
            model=model,
            prompt=prompt,
            response_format=response_format,
            temperature=temperature,
            language=language,
        )

        return create_transcription_request
