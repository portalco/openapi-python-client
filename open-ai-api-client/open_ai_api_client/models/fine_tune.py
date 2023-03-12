from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fine_tune_event import FineTuneEvent
    from ..models.fine_tune_hyperparams import FineTuneHyperparams
    from ..models.open_ai_file import OpenAIFile


T = TypeVar("T", bound="FineTune")


@attr.s(auto_attribs=True)
class FineTune:
    """
    Attributes:
        id (str):
        object_ (str):
        created_at (int):
        updated_at (int):
        model (str):
        organization_id (str):
        status (str):
        hyperparams (FineTuneHyperparams):
        training_files (List['OpenAIFile']):
        validation_files (List['OpenAIFile']):
        result_files (List['OpenAIFile']):
        fine_tuned_model (Optional[str]):
        events (Union[Unset, List['FineTuneEvent']]):
    """

    id: str
    object_: str
    created_at: int
    updated_at: int
    model: str
    organization_id: str
    status: str
    hyperparams: "FineTuneHyperparams"
    training_files: List["OpenAIFile"]
    validation_files: List["OpenAIFile"]
    result_files: List["OpenAIFile"]
    fine_tuned_model: Optional[str]
    events: Union[Unset, List["FineTuneEvent"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        object_ = self.object_
        created_at = self.created_at
        updated_at = self.updated_at
        model = self.model
        organization_id = self.organization_id
        status = self.status
        hyperparams = self.hyperparams.to_dict()

        training_files = []
        for training_files_item_data in self.training_files:
            training_files_item = training_files_item_data.to_dict()

            training_files.append(training_files_item)

        validation_files = []
        for validation_files_item_data in self.validation_files:
            validation_files_item = validation_files_item_data.to_dict()

            validation_files.append(validation_files_item)

        result_files = []
        for result_files_item_data in self.result_files:
            result_files_item = result_files_item_data.to_dict()

            result_files.append(result_files_item)

        fine_tuned_model = self.fine_tuned_model
        events: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.to_dict()

                events.append(events_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "object": object_,
                "created_at": created_at,
                "updated_at": updated_at,
                "model": model,
                "organization_id": organization_id,
                "status": status,
                "hyperparams": hyperparams,
                "training_files": training_files,
                "validation_files": validation_files,
                "result_files": result_files,
                "fine_tuned_model": fine_tuned_model,
            }
        )
        if events is not UNSET:
            field_dict["events"] = events

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fine_tune_event import FineTuneEvent
        from ..models.fine_tune_hyperparams import FineTuneHyperparams
        from ..models.open_ai_file import OpenAIFile

        d = src_dict.copy()
        id = d.pop("id")

        object_ = d.pop("object")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        model = d.pop("model")

        organization_id = d.pop("organization_id")

        status = d.pop("status")

        hyperparams = FineTuneHyperparams.from_dict(d.pop("hyperparams"))

        training_files = []
        _training_files = d.pop("training_files")
        for training_files_item_data in _training_files:
            training_files_item = OpenAIFile.from_dict(training_files_item_data)

            training_files.append(training_files_item)

        validation_files = []
        _validation_files = d.pop("validation_files")
        for validation_files_item_data in _validation_files:
            validation_files_item = OpenAIFile.from_dict(validation_files_item_data)

            validation_files.append(validation_files_item)

        result_files = []
        _result_files = d.pop("result_files")
        for result_files_item_data in _result_files:
            result_files_item = OpenAIFile.from_dict(result_files_item_data)

            result_files.append(result_files_item)

        fine_tuned_model = d.pop("fine_tuned_model")

        events = []
        _events = d.pop("events", UNSET)
        for events_item_data in _events or []:
            events_item = FineTuneEvent.from_dict(events_item_data)

            events.append(events_item)

        fine_tune = cls(
            id=id,
            object_=object_,
            created_at=created_at,
            updated_at=updated_at,
            model=model,
            organization_id=organization_id,
            status=status,
            hyperparams=hyperparams,
            training_files=training_files,
            validation_files=validation_files,
            result_files=result_files,
            fine_tuned_model=fine_tuned_model,
            events=events,
        )

        fine_tune.additional_properties = d
        return fine_tune

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
