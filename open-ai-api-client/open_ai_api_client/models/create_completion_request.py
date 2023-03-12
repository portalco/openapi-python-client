from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_completion_request_logit_bias import CreateCompletionRequestLogitBias


T = TypeVar("T", bound="CreateCompletionRequest")


@attr.s(auto_attribs=True)
class CreateCompletionRequest:
    """
    Attributes:
        model (str): ID of the model to use. You can use the [List models](/docs/api-reference/models/list) API to see
            all of your available models, or see our [Model overview](/docs/models/overview) for descriptions of them.
        prompt (Union[List[List[int]], List[int], List[str], None, Unset, str]): The prompt(s) to generate completions
            for, encoded as a string, array of strings, array of tokens, or array of token arrays.

            Note that <|endoftext|> is the document separator that the model sees during training, so if a prompt is not
            specified the model will generate as if from the beginning of a new document.
             Default: '<|endoftext|>'.
        suffix (Union[Unset, None, str]): The suffix that comes after a completion of inserted text. Example: test..
        max_tokens (Union[Unset, None, int]): The maximum number of [tokens](/tokenizer) to generate in the completion.

            The token count of your prompt plus `max_tokens` cannot exceed the model's context length. Most models have a
            context length of 2048 tokens (except for the newest models, which support 4096).
             Default: 16. Example: 16.
        temperature (Union[Unset, None, float]): What sampling temperature to use, between 0 and 2. Higher values like
            0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.

            We generally recommend altering this or `top_p` but not both.
             Default: 1.0. Example: 1.
        top_p (Union[Unset, None, float]): An alternative to sampling with temperature, called nucleus sampling, where
            the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens
            comprising the top 10% probability mass are considered.

            We generally recommend altering this or `temperature` but not both.
             Default: 1.0. Example: 1.
        n (Union[Unset, None, int]): How many completions to generate for each prompt.

            **Note:** Because this parameter generates many completions, it can quickly consume your token quota. Use
            carefully and ensure that you have reasonable settings for `max_tokens` and `stop`.
             Default: 1. Example: 1.
        stream (Union[Unset, None, bool]): Whether to stream back partial progress. If set, tokens will be sent as data-
            only [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-
            sent_events#Event_stream_format) as they become available, with the stream terminated by a `data: [DONE]`
            message.
        logprobs (Union[Unset, None, int]): Include the log probabilities on the `logprobs` most likely tokens, as well
            the chosen tokens. For example, if `logprobs` is 5, the API will return a list of the 5 most likely tokens. The
            API will always return the `logprob` of the sampled token, so there may be up to `logprobs+1` elements in the
            response.

            The maximum value for `logprobs` is 5. If you need more than this, please contact us through our [Help
            center](https://help.openai.com) and describe your use case.
        echo (Union[Unset, None, bool]): Echo back the prompt in addition to the completion
        stop (Union[List[str], None, Unset, str]): Up to 4 sequences where the API will stop generating further tokens.
            The returned text will not contain the stop sequence.
        presence_penalty (Union[Unset, None, float]): Number between -2.0 and 2.0. Positive values penalize new tokens
            based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics.

            [See more information about frequency and presence penalties.](/docs/api-reference/parameter-details)
        frequency_penalty (Union[Unset, None, float]): Number between -2.0 and 2.0. Positive values penalize new tokens
            based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line
            verbatim.

            [See more information about frequency and presence penalties.](/docs/api-reference/parameter-details)
        best_of (Union[Unset, None, int]): Generates `best_of` completions server-side and returns the "best" (the one
            with the highest log probability per token). Results cannot be streamed.

            When used with `n`, `best_of` controls the number of candidate completions and `n` specifies how many to return
            – `best_of` must be greater than `n`.

            **Note:** Because this parameter generates many completions, it can quickly consume your token quota. Use
            carefully and ensure that you have reasonable settings for `max_tokens` and `stop`.
             Default: 1.
        logit_bias (Union[Unset, None, CreateCompletionRequestLogitBias]): Modify the likelihood of specified tokens
            appearing in the completion.

            Accepts a json object that maps tokens (specified by their token ID in the GPT tokenizer) to an associated bias
            value from -100 to 100. You can use this [tokenizer tool](/tokenizer?view=bpe) (which works for both GPT-2 and
            GPT-3) to convert text to token IDs. Mathematically, the bias is added to the logits generated by the model
            prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase
            likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant
            token.

            As an example, you can pass `{"50256": -100}` to prevent the <|endoftext|> token from being generated.
        user (Union[Unset, str]): A unique identifier representing your end-user, which can help OpenAI to monitor and
            detect abuse. [Learn more](/docs/guides/safety-best-practices/end-user-ids).
             Example: user-1234.
    """

    model: str
    prompt: Union[List[List[int]], List[int], List[str], None, Unset, str] = "<|endoftext|>"
    suffix: Union[Unset, None, str] = UNSET
    max_tokens: Union[Unset, None, int] = 16
    temperature: Union[Unset, None, float] = 1.0
    top_p: Union[Unset, None, float] = 1.0
    n: Union[Unset, None, int] = 1
    stream: Union[Unset, None, bool] = False
    logprobs: Union[Unset, None, int] = UNSET
    echo: Union[Unset, None, bool] = False
    stop: Union[List[str], None, Unset, str] = UNSET
    presence_penalty: Union[Unset, None, float] = 0.0
    frequency_penalty: Union[Unset, None, float] = 0.0
    best_of: Union[Unset, None, int] = 1
    logit_bias: Union[Unset, None, "CreateCompletionRequestLogitBias"] = UNSET
    user: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        model = self.model
        prompt: Union[List[List[int]], List[int], List[str], None, Unset, str]
        if isinstance(self.prompt, Unset):
            prompt = UNSET
        elif self.prompt is None:
            prompt = None

        elif isinstance(self.prompt, list):
            prompt = UNSET
            if not isinstance(self.prompt, Unset):
                prompt = self.prompt

        elif isinstance(self.prompt, list):
            prompt = UNSET
            if not isinstance(self.prompt, Unset):
                prompt = self.prompt

        elif isinstance(self.prompt, list):
            prompt = UNSET
            if not isinstance(self.prompt, Unset):
                prompt = []
                for prompt_type_3_item_data in self.prompt:
                    prompt_type_3_item = prompt_type_3_item_data

                    prompt.append(prompt_type_3_item)

        else:
            prompt = self.prompt

        suffix = self.suffix
        max_tokens = self.max_tokens
        temperature = self.temperature
        top_p = self.top_p
        n = self.n
        stream = self.stream
        logprobs = self.logprobs
        echo = self.echo
        stop: Union[List[str], None, Unset, str]
        if isinstance(self.stop, Unset):
            stop = UNSET
        elif self.stop is None:
            stop = None

        elif isinstance(self.stop, list):
            stop = UNSET
            if not isinstance(self.stop, Unset):
                stop = self.stop

        else:
            stop = self.stop

        presence_penalty = self.presence_penalty
        frequency_penalty = self.frequency_penalty
        best_of = self.best_of
        logit_bias: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.logit_bias, Unset):
            logit_bias = self.logit_bias.to_dict() if self.logit_bias else None

        user = self.user

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "model": model,
            }
        )
        if prompt is not UNSET:
            field_dict["prompt"] = prompt
        if suffix is not UNSET:
            field_dict["suffix"] = suffix
        if max_tokens is not UNSET:
            field_dict["max_tokens"] = max_tokens
        if temperature is not UNSET:
            field_dict["temperature"] = temperature
        if top_p is not UNSET:
            field_dict["top_p"] = top_p
        if n is not UNSET:
            field_dict["n"] = n
        if stream is not UNSET:
            field_dict["stream"] = stream
        if logprobs is not UNSET:
            field_dict["logprobs"] = logprobs
        if echo is not UNSET:
            field_dict["echo"] = echo
        if stop is not UNSET:
            field_dict["stop"] = stop
        if presence_penalty is not UNSET:
            field_dict["presence_penalty"] = presence_penalty
        if frequency_penalty is not UNSET:
            field_dict["frequency_penalty"] = frequency_penalty
        if best_of is not UNSET:
            field_dict["best_of"] = best_of
        if logit_bias is not UNSET:
            field_dict["logit_bias"] = logit_bias
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.create_completion_request_logit_bias import CreateCompletionRequestLogitBias

        d = src_dict.copy()
        model = d.pop("model")

        def _parse_prompt(data: object) -> Union[List[List[int]], List[int], List[str], None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                prompt_type_1 = cast(List[str], data)

                return prompt_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                prompt_type_2 = cast(List[int], data)

                return prompt_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                prompt_type_3 = UNSET
                _prompt_type_3 = data
                for prompt_type_3_item_data in _prompt_type_3 or []:
                    prompt_type_3_item = cast(List[int], prompt_type_3_item_data)

                    prompt_type_3.append(prompt_type_3_item)

                return prompt_type_3
            except:  # noqa: E722
                pass
            return cast(Union[List[List[int]], List[int], List[str], None, Unset, str], data)

        prompt = _parse_prompt(d.pop("prompt", UNSET))

        suffix = d.pop("suffix", UNSET)

        max_tokens = d.pop("max_tokens", UNSET)

        temperature = d.pop("temperature", UNSET)

        top_p = d.pop("top_p", UNSET)

        n = d.pop("n", UNSET)

        stream = d.pop("stream", UNSET)

        logprobs = d.pop("logprobs", UNSET)

        echo = d.pop("echo", UNSET)

        def _parse_stop(data: object) -> Union[List[str], None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                stop_type_1 = cast(List[str], data)

                return stop_type_1
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset, str], data)

        stop = _parse_stop(d.pop("stop", UNSET))

        presence_penalty = d.pop("presence_penalty", UNSET)

        frequency_penalty = d.pop("frequency_penalty", UNSET)

        best_of = d.pop("best_of", UNSET)

        _logit_bias = d.pop("logit_bias", UNSET)
        logit_bias: Union[Unset, None, CreateCompletionRequestLogitBias]
        if _logit_bias is None:
            logit_bias = None
        elif isinstance(_logit_bias, Unset):
            logit_bias = UNSET
        else:
            logit_bias = CreateCompletionRequestLogitBias.from_dict(_logit_bias)

        user = d.pop("user", UNSET)

        create_completion_request = cls(
            model=model,
            prompt=prompt,
            suffix=suffix,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            n=n,
            stream=stream,
            logprobs=logprobs,
            echo=echo,
            stop=stop,
            presence_penalty=presence_penalty,
            frequency_penalty=frequency_penalty,
            best_of=best_of,
            logit_bias=logit_bias,
            user=user,
        )

        create_completion_request.additional_properties = d
        return create_completion_request

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
