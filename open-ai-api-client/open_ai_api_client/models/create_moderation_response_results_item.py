from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.create_moderation_response_results_item_categories import (
        CreateModerationResponseResultsItemCategories,
    )
    from ..models.create_moderation_response_results_item_category_scores import (
        CreateModerationResponseResultsItemCategoryScores,
    )


T = TypeVar("T", bound="CreateModerationResponseResultsItem")


@attr.s(auto_attribs=True)
class CreateModerationResponseResultsItem:
    """
    Attributes:
        flagged (bool):
        categories (CreateModerationResponseResultsItemCategories):
        category_scores (CreateModerationResponseResultsItemCategoryScores):
    """

    flagged: bool
    categories: "CreateModerationResponseResultsItemCategories"
    category_scores: "CreateModerationResponseResultsItemCategoryScores"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        flagged = self.flagged
        categories = self.categories.to_dict()

        category_scores = self.category_scores.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "flagged": flagged,
                "categories": categories,
                "category_scores": category_scores,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.create_moderation_response_results_item_categories import (
            CreateModerationResponseResultsItemCategories,
        )
        from ..models.create_moderation_response_results_item_category_scores import (
            CreateModerationResponseResultsItemCategoryScores,
        )

        d = src_dict.copy()
        flagged = d.pop("flagged")

        categories = CreateModerationResponseResultsItemCategories.from_dict(d.pop("categories"))

        category_scores = CreateModerationResponseResultsItemCategoryScores.from_dict(d.pop("category_scores"))

        create_moderation_response_results_item = cls(
            flagged=flagged,
            categories=categories,
            category_scores=category_scores,
        )

        create_moderation_response_results_item.additional_properties = d
        return create_moderation_response_results_item

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
