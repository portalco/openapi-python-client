from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_answer_request_logit_bias import CreateAnswerRequestLogitBias


T = TypeVar("T", bound="CreateAnswerRequest")


@attr.s(auto_attribs=True)
class CreateAnswerRequest:
    """
    Attributes:
        model (str): ID of the model to use for completion. You can select one of `ada`, `babbage`, `curie`, or
            `davinci`.
        question (str): Question to get answered. Example: What is the capital of Japan?.
        examples (List[List[str]]): List of (question, answer) pairs that will help steer the model towards the tone and
            answer format you'd like. We recommend adding 2 to 3 examples. Example: [['What is the capital of Canada?',
            'Ottawa'], ['Which province is Ottawa in?', 'Ontario']].
        examples_context (str): A text snippet containing the contextual information used to generate the answers for
            the `examples` you provide. Example: Ottawa, Canada's capital, is located in the east of southern Ontario, near
            the city of Montréal and the U.S. border..
        documents (Union[Unset, None, List[str]]): List of documents from which the answer for the input `question`
            should be derived. If this is an empty list, the question will be answered based on the question-answer
            examples.

            You should specify either `documents` or a `file`, but not both.
             Example: ['Japan is an island country in East Asia, located in the northwest Pacific Ocean.', 'Tokyo is the
            capital and most populous prefecture of Japan.'].
        file (Union[Unset, None, str]): The ID of an uploaded file that contains documents to search over. See [upload
            file](/docs/api-reference/files/upload) for how to upload a file of the desired format and purpose.

            You should specify either `documents` or a `file`, but not both.
        search_model (Union[Unset, None, str]): ID of the model to use for [Search](/docs/api-
            reference/searches/create). You can select one of `ada`, `babbage`, `curie`, or `davinci`. Default: 'ada'.
        max_rerank (Union[Unset, None, int]): The maximum number of documents to be ranked by [Search](/docs/api-
            reference/searches/create) when using `file`. Setting it to a higher value leads to improved accuracy but with
            increased latency and cost. Default: 200.
        temperature (Union[Unset, None, float]): What sampling temperature to use, between 0 and 2. Higher values like
            0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.
        logprobs (Union[Unset, None, int]): Include the log probabilities on the `logprobs` most likely tokens, as well
            the chosen tokens. For example, if `logprobs` is 5, the API will return a list of the 5 most likely tokens. The
            API will always return the `logprob` of the sampled token, so there may be up to `logprobs+1` elements in the
            response.

            The maximum value for `logprobs` is 5. If you need more than this, please contact us through our [Help
            center](https://help.openai.com) and describe your use case.

            When `logprobs` is set, `completion` will be automatically added into `expand` to get the logprobs.
        max_tokens (Union[Unset, None, int]): The maximum number of tokens allowed for the generated answer Default: 16.
        stop (Union[List[str], None, Unset, str]): Up to 4 sequences where the API will stop generating further tokens.
            The returned text will not contain the stop sequence.
        n (Union[Unset, None, int]): How many answers to generate for each question. Default: 1.
        logit_bias (Union[Unset, None, CreateAnswerRequestLogitBias]): Modify the likelihood of specified tokens
            appearing in the completion.

            Accepts a json object that maps tokens (specified by their token ID in the GPT tokenizer) to an associated bias
            value from -100 to 100. You can use this [tokenizer tool](/tokenizer?view=bpe) (which works for both GPT-2 and
            GPT-3) to convert text to token IDs. Mathematically, the bias is added to the logits generated by the model
            prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase
            likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant
            token.

            As an example, you can pass `{"50256": -100}` to prevent the <|endoftext|> token from being generated.
        return_metadata (Union[Unset, None, bool]): A special boolean flag for showing metadata. If set to `true`, each
            document entry in the returned JSON will contain a "metadata" field.

            This flag only takes effect when `file` is set.
        return_prompt (Union[Unset, None, bool]): If set to `true`, the returned JSON will include a "prompt" field
            containing the final prompt that was used to request a completion. This is mainly useful for debugging purposes.
        expand (Union[Unset, None, List[Any]]): If an object name is in the list, we provide the full information of the
            object; otherwise, we only provide the object ID. Currently we support `completion` and `file` objects for
            expansion.
        user (Union[Unset, str]): A unique identifier representing your end-user, which can help OpenAI to monitor and
            detect abuse. [Learn more](/docs/guides/safety-best-practices/end-user-ids).
             Example: user-1234.
    """

    model: str
    question: str
    examples: List[List[str]]
    examples_context: str
    documents: Union[Unset, None, List[str]] = UNSET
    file: Union[Unset, None, str] = UNSET
    search_model: Union[Unset, None, str] = "ada"
    max_rerank: Union[Unset, None, int] = 200
    temperature: Union[Unset, None, float] = 0.0
    logprobs: Union[Unset, None, int] = UNSET
    max_tokens: Union[Unset, None, int] = 16
    stop: Union[List[str], None, Unset, str] = UNSET
    n: Union[Unset, None, int] = 1
    logit_bias: Union[Unset, None, "CreateAnswerRequestLogitBias"] = UNSET
    return_metadata: Union[Unset, None, bool] = False
    return_prompt: Union[Unset, None, bool] = False
    expand: Union[Unset, None, List[Any]] = UNSET
    user: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        model = self.model
        question = self.question
        examples = []
        for examples_item_data in self.examples:
            examples_item = examples_item_data

            examples.append(examples_item)

        examples_context = self.examples_context
        documents: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.documents, Unset):
            if self.documents is None:
                documents = None
            else:
                documents = self.documents

        file = self.file
        search_model = self.search_model
        max_rerank = self.max_rerank
        temperature = self.temperature
        logprobs = self.logprobs
        max_tokens = self.max_tokens
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

        n = self.n
        logit_bias: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.logit_bias, Unset):
            logit_bias = self.logit_bias.to_dict() if self.logit_bias else None

        return_metadata = self.return_metadata
        return_prompt = self.return_prompt
        expand: Union[Unset, None, List[Any]] = UNSET
        if not isinstance(self.expand, Unset):
            if self.expand is None:
                expand = None
            else:
                expand = self.expand

        user = self.user

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "model": model,
                "question": question,
                "examples": examples,
                "examples_context": examples_context,
            }
        )
        if documents is not UNSET:
            field_dict["documents"] = documents
        if file is not UNSET:
            field_dict["file"] = file
        if search_model is not UNSET:
            field_dict["search_model"] = search_model
        if max_rerank is not UNSET:
            field_dict["max_rerank"] = max_rerank
        if temperature is not UNSET:
            field_dict["temperature"] = temperature
        if logprobs is not UNSET:
            field_dict["logprobs"] = logprobs
        if max_tokens is not UNSET:
            field_dict["max_tokens"] = max_tokens
        if stop is not UNSET:
            field_dict["stop"] = stop
        if n is not UNSET:
            field_dict["n"] = n
        if logit_bias is not UNSET:
            field_dict["logit_bias"] = logit_bias
        if return_metadata is not UNSET:
            field_dict["return_metadata"] = return_metadata
        if return_prompt is not UNSET:
            field_dict["return_prompt"] = return_prompt
        if expand is not UNSET:
            field_dict["expand"] = expand
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.create_answer_request_logit_bias import CreateAnswerRequestLogitBias

        d = src_dict.copy()
        model = d.pop("model")

        question = d.pop("question")

        examples = []
        _examples = d.pop("examples")
        for examples_item_data in _examples:
            examples_item = cast(List[str], examples_item_data)

            examples.append(examples_item)

        examples_context = d.pop("examples_context")

        documents = cast(List[str], d.pop("documents", UNSET))

        file = d.pop("file", UNSET)

        search_model = d.pop("search_model", UNSET)

        max_rerank = d.pop("max_rerank", UNSET)

        temperature = d.pop("temperature", UNSET)

        logprobs = d.pop("logprobs", UNSET)

        max_tokens = d.pop("max_tokens", UNSET)

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

        n = d.pop("n", UNSET)

        _logit_bias = d.pop("logit_bias", UNSET)
        logit_bias: Union[Unset, None, CreateAnswerRequestLogitBias]
        if _logit_bias is None:
            logit_bias = None
        elif isinstance(_logit_bias, Unset):
            logit_bias = UNSET
        else:
            logit_bias = CreateAnswerRequestLogitBias.from_dict(_logit_bias)

        return_metadata = d.pop("return_metadata", UNSET)

        return_prompt = d.pop("return_prompt", UNSET)

        expand = cast(List[Any], d.pop("expand", UNSET))

        user = d.pop("user", UNSET)

        create_answer_request = cls(
            model=model,
            question=question,
            examples=examples,
            examples_context=examples_context,
            documents=documents,
            file=file,
            search_model=search_model,
            max_rerank=max_rerank,
            temperature=temperature,
            logprobs=logprobs,
            max_tokens=max_tokens,
            stop=stop,
            n=n,
            logit_bias=logit_bias,
            return_metadata=return_metadata,
            return_prompt=return_prompt,
            expand=expand,
            user=user,
        )

        return create_answer_request
