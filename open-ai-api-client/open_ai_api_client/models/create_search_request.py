from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateSearchRequest")


@attr.s(auto_attribs=True)
class CreateSearchRequest:
    """
    Attributes:
        query (str): Query to search against the documents. Example: the president.
        documents (Union[Unset, None, List[str]]): Up to 200 documents to search over, provided as a list of strings.

            The maximum document length (in tokens) is 2034 minus the number of tokens in the query.

            You should specify either `documents` or a `file`, but not both.
             Example: ['White House', 'hospital', 'school'].
        file (Union[Unset, None, str]): The ID of an uploaded file that contains documents to search over.

            You should specify either `documents` or a `file`, but not both.
        max_rerank (Union[Unset, None, int]): The maximum number of documents to be re-ranked and returned by search.

            This flag only takes effect when `file` is set.
             Default: 200.
        return_metadata (Union[Unset, None, bool]): A special boolean flag for showing metadata. If set to `true`, each
            document entry in the returned JSON will contain a "metadata" field.

            This flag only takes effect when `file` is set.
        user (Union[Unset, str]): A unique identifier representing your end-user, which can help OpenAI to monitor and
            detect abuse. [Learn more](/docs/guides/safety-best-practices/end-user-ids).
             Example: user-1234.
    """

    query: str
    documents: Union[Unset, None, List[str]] = UNSET
    file: Union[Unset, None, str] = UNSET
    max_rerank: Union[Unset, None, int] = 200
    return_metadata: Union[Unset, None, bool] = False
    user: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        query = self.query
        documents: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.documents, Unset):
            if self.documents is None:
                documents = None
            else:
                documents = self.documents

        file = self.file
        max_rerank = self.max_rerank
        return_metadata = self.return_metadata
        user = self.user

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query": query,
            }
        )
        if documents is not UNSET:
            field_dict["documents"] = documents
        if file is not UNSET:
            field_dict["file"] = file
        if max_rerank is not UNSET:
            field_dict["max_rerank"] = max_rerank
        if return_metadata is not UNSET:
            field_dict["return_metadata"] = return_metadata
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        query = d.pop("query")

        documents = cast(List[str], d.pop("documents", UNSET))

        file = d.pop("file", UNSET)

        max_rerank = d.pop("max_rerank", UNSET)

        return_metadata = d.pop("return_metadata", UNSET)

        user = d.pop("user", UNSET)

        create_search_request = cls(
            query=query,
            documents=documents,
            file=file,
            max_rerank=max_rerank,
            return_metadata=return_metadata,
            user=user,
        )

        create_search_request.additional_properties = d
        return create_search_request

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
