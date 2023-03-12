from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="CreateModerationResponseResultsItemCategories")


@attr.s(auto_attribs=True)
class CreateModerationResponseResultsItemCategories:
    """
    Attributes:
        hate (bool):
        hatethreatening (bool):
        self_harm (bool):
        sexual (bool):
        sexualminors (bool):
        violence (bool):
        violencegraphic (bool):
    """

    hate: bool
    hatethreatening: bool
    self_harm: bool
    sexual: bool
    sexualminors: bool
    violence: bool
    violencegraphic: bool
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hate = self.hate
        hatethreatening = self.hatethreatening
        self_harm = self.self_harm
        sexual = self.sexual
        sexualminors = self.sexualminors
        violence = self.violence
        violencegraphic = self.violencegraphic

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hate": hate,
                "hate/threatening": hatethreatening,
                "self-harm": self_harm,
                "sexual": sexual,
                "sexual/minors": sexualminors,
                "violence": violence,
                "violence/graphic": violencegraphic,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        hate = d.pop("hate")

        hatethreatening = d.pop("hate/threatening")

        self_harm = d.pop("self-harm")

        sexual = d.pop("sexual")

        sexualminors = d.pop("sexual/minors")

        violence = d.pop("violence")

        violencegraphic = d.pop("violence/graphic")

        create_moderation_response_results_item_categories = cls(
            hate=hate,
            hatethreatening=hatethreatening,
            self_harm=self_harm,
            sexual=sexual,
            sexualminors=sexualminors,
            violence=violence,
            violencegraphic=violencegraphic,
        )

        create_moderation_response_results_item_categories.additional_properties = d
        return create_moderation_response_results_item_categories

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
