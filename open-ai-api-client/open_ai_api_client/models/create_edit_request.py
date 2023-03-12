from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateEditRequest")


@attr.s(auto_attribs=True)
class CreateEditRequest:
    """
    Attributes:
        model (str): ID of the model to use. You can use the `text-davinci-edit-001` or `code-davinci-edit-001` model
            with this endpoint.
        instruction (str): The instruction that tells the model how to edit the prompt. Example: Fix the spelling
            mistakes..
        input_ (Union[Unset, None, str]): The input text to use as a starting point for the edit. Default: ''. Example:
            What day of the wek is it?.
        n (Union[Unset, None, int]): How many edits to generate for the input and instruction. Default: 1. Example: 1.
        temperature (Union[Unset, None, float]): What sampling temperature to use, between 0 and 2. Higher values like
            0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.

            We generally recommend altering this or `top_p` but not both.
             Default: 1.0. Example: 1.
        top_p (Union[Unset, None, float]): An alternative to sampling with temperature, called nucleus sampling, where
            the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens
            comprising the top 10% probability mass are considered.

            We generally recommend altering this or `temperature` but not both.
             Default: 1.0. Example: 1.
    """

    model: str
    instruction: str
    input_: Union[Unset, None, str] = ""
    n: Union[Unset, None, int] = 1
    temperature: Union[Unset, None, float] = 1.0
    top_p: Union[Unset, None, float] = 1.0
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        model = self.model
        instruction = self.instruction
        input_ = self.input_
        n = self.n
        temperature = self.temperature
        top_p = self.top_p

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "model": model,
                "instruction": instruction,
            }
        )
        if input_ is not UNSET:
            field_dict["input"] = input_
        if n is not UNSET:
            field_dict["n"] = n
        if temperature is not UNSET:
            field_dict["temperature"] = temperature
        if top_p is not UNSET:
            field_dict["top_p"] = top_p

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        model = d.pop("model")

        instruction = d.pop("instruction")

        input_ = d.pop("input", UNSET)

        n = d.pop("n", UNSET)

        temperature = d.pop("temperature", UNSET)

        top_p = d.pop("top_p", UNSET)

        create_edit_request = cls(
            model=model,
            instruction=instruction,
            input_=input_,
            n=n,
            temperature=temperature,
            top_p=top_p,
        )

        create_edit_request.additional_properties = d
        return create_edit_request

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
