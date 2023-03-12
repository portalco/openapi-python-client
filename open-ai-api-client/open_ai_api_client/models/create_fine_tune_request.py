from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateFineTuneRequest")


@attr.s(auto_attribs=True)
class CreateFineTuneRequest:
    """
    Attributes:
        training_file (str): The ID of an uploaded file that contains training data.

            See [upload file](/docs/api-reference/files/upload) for how to upload a file.

            Your dataset must be formatted as a JSONL file, where each training
            example is a JSON object with the keys "prompt" and "completion".
            Additionally, you must upload your file with the purpose `fine-tune`.

            See the [fine-tuning guide](/docs/guides/fine-tuning/creating-training-data) for more details.
             Example: file-ajSREls59WBbvgSzJSVWxMCB.
        validation_file (Union[Unset, None, str]): The ID of an uploaded file that contains validation data.

            If you provide this file, the data is used to generate validation
            metrics periodically during fine-tuning. These metrics can be viewed in
            the [fine-tuning results file](/docs/guides/fine-tuning/analyzing-your-fine-tuned-model).
            Your train and validation data should be mutually exclusive.

            Your dataset must be formatted as a JSONL file, where each validation
            example is a JSON object with the keys "prompt" and "completion".
            Additionally, you must upload your file with the purpose `fine-tune`.

            See the [fine-tuning guide](/docs/guides/fine-tuning/creating-training-data) for more details.
             Example: file-XjSREls59WBbvgSzJSVWxMCa.
        model (Union[Unset, None, str]): The name of the base model to fine-tune. You can select one of "ada",
            "babbage", "curie", "davinci", or a fine-tuned model created after 2022-04-21.
            To learn more about these models, see the
            [Models](https://platform.openai.com/docs/models) documentation.
             Default: 'curie'.
        n_epochs (Union[Unset, None, int]): The number of epochs to train the model for. An epoch refers to one
            full cycle through the training dataset.
             Default: 4.
        batch_size (Union[Unset, None, int]): The batch size to use for training. The batch size is the number of
            training examples used to train a single forward and backward pass.

            By default, the batch size will be dynamically configured to be
            ~0.2% of the number of examples in the training set, capped at 256 -
            in general, we've found that larger batch sizes tend to work better
            for larger datasets.
        learning_rate_multiplier (Union[Unset, None, float]): The learning rate multiplier to use for training.
            The fine-tuning learning rate is the original learning rate used for
            pretraining multiplied by this value.

            By default, the learning rate multiplier is the 0.05, 0.1, or 0.2
            depending on final `batch_size` (larger learning rates tend to
            perform better with larger batch sizes). We recommend experimenting
            with values in the range 0.02 to 0.2 to see what produces the best
            results.
        prompt_loss_weight (Union[Unset, None, float]): The weight to use for loss on the prompt tokens. This controls
            how
            much the model tries to learn to generate the prompt (as compared
            to the completion which always has a weight of 1.0), and can add
            a stabilizing effect to training when completions are short.

            If prompts are extremely long (relative to completions), it may make
            sense to reduce this weight so as to avoid over-prioritizing
            learning the prompt.
             Default: 0.01.
        compute_classification_metrics (Union[Unset, None, bool]): If set, we calculate classification-specific metrics
            such as accuracy
            and F-1 score using the validation set at the end of every epoch.
            These metrics can be viewed in the [results file](/docs/guides/fine-tuning/analyzing-your-fine-tuned-model).

            In order to compute classification metrics, you must provide a
            `validation_file`. Additionally, you must
            specify `classification_n_classes` for multiclass classification or
            `classification_positive_class` for binary classification.
        classification_n_classes (Union[Unset, None, int]): The number of classes in a classification task.

            This parameter is required for multiclass classification.
        classification_positive_class (Union[Unset, None, str]): The positive class in binary classification.

            This parameter is needed to generate precision, recall, and F1
            metrics when doing binary classification.
        classification_betas (Union[Unset, None, List[float]]): If this is provided, we calculate F-beta scores at the
            specified
            beta values. The F-beta score is a generalization of F-1 score.
            This is only used for binary classification.

            With a beta of 1 (i.e. the F-1 score), precision and recall are
            given the same weight. A larger beta score puts more weight on
            recall and less on precision. A smaller beta score puts more weight
            on precision and less on recall.
             Example: [0.6, 1, 1.5, 2].
        suffix (Union[Unset, None, str]): A string of up to 40 characters that will be added to your fine-tuned model
            name.

            For example, a `suffix` of "custom-model-name" would produce a model name like `ada:ft-your-org:custom-model-
            name-2022-02-15-04-21-04`.
    """

    training_file: str
    validation_file: Union[Unset, None, str] = UNSET
    model: Union[Unset, None, str] = "curie"
    n_epochs: Union[Unset, None, int] = 4
    batch_size: Union[Unset, None, int] = UNSET
    learning_rate_multiplier: Union[Unset, None, float] = UNSET
    prompt_loss_weight: Union[Unset, None, float] = 0.01
    compute_classification_metrics: Union[Unset, None, bool] = False
    classification_n_classes: Union[Unset, None, int] = UNSET
    classification_positive_class: Union[Unset, None, str] = UNSET
    classification_betas: Union[Unset, None, List[float]] = UNSET
    suffix: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        training_file = self.training_file
        validation_file = self.validation_file
        model = self.model
        n_epochs = self.n_epochs
        batch_size = self.batch_size
        learning_rate_multiplier = self.learning_rate_multiplier
        prompt_loss_weight = self.prompt_loss_weight
        compute_classification_metrics = self.compute_classification_metrics
        classification_n_classes = self.classification_n_classes
        classification_positive_class = self.classification_positive_class
        classification_betas: Union[Unset, None, List[float]] = UNSET
        if not isinstance(self.classification_betas, Unset):
            if self.classification_betas is None:
                classification_betas = None
            else:
                classification_betas = self.classification_betas

        suffix = self.suffix

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "training_file": training_file,
            }
        )
        if validation_file is not UNSET:
            field_dict["validation_file"] = validation_file
        if model is not UNSET:
            field_dict["model"] = model
        if n_epochs is not UNSET:
            field_dict["n_epochs"] = n_epochs
        if batch_size is not UNSET:
            field_dict["batch_size"] = batch_size
        if learning_rate_multiplier is not UNSET:
            field_dict["learning_rate_multiplier"] = learning_rate_multiplier
        if prompt_loss_weight is not UNSET:
            field_dict["prompt_loss_weight"] = prompt_loss_weight
        if compute_classification_metrics is not UNSET:
            field_dict["compute_classification_metrics"] = compute_classification_metrics
        if classification_n_classes is not UNSET:
            field_dict["classification_n_classes"] = classification_n_classes
        if classification_positive_class is not UNSET:
            field_dict["classification_positive_class"] = classification_positive_class
        if classification_betas is not UNSET:
            field_dict["classification_betas"] = classification_betas
        if suffix is not UNSET:
            field_dict["suffix"] = suffix

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        training_file = d.pop("training_file")

        validation_file = d.pop("validation_file", UNSET)

        model = d.pop("model", UNSET)

        n_epochs = d.pop("n_epochs", UNSET)

        batch_size = d.pop("batch_size", UNSET)

        learning_rate_multiplier = d.pop("learning_rate_multiplier", UNSET)

        prompt_loss_weight = d.pop("prompt_loss_weight", UNSET)

        compute_classification_metrics = d.pop("compute_classification_metrics", UNSET)

        classification_n_classes = d.pop("classification_n_classes", UNSET)

        classification_positive_class = d.pop("classification_positive_class", UNSET)

        classification_betas = cast(List[float], d.pop("classification_betas", UNSET))

        suffix = d.pop("suffix", UNSET)

        create_fine_tune_request = cls(
            training_file=training_file,
            validation_file=validation_file,
            model=model,
            n_epochs=n_epochs,
            batch_size=batch_size,
            learning_rate_multiplier=learning_rate_multiplier,
            prompt_loss_weight=prompt_loss_weight,
            compute_classification_metrics=compute_classification_metrics,
            classification_n_classes=classification_n_classes,
            classification_positive_class=classification_positive_class,
            classification_betas=classification_betas,
            suffix=suffix,
        )

        create_fine_tune_request.additional_properties = d
        return create_fine_tune_request

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
