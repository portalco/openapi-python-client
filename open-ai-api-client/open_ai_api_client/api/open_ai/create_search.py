from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.create_search_request import CreateSearchRequest
from ...models.create_search_response import CreateSearchResponse
from ...types import Response


def _get_kwargs(
    engine_id: str,
    *,
    client: Client,
    json_body: CreateSearchRequest,
) -> Dict[str, Any]:
    url = "{}/engines/{engine_id}/search".format(client.base_url, engine_id=engine_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[CreateSearchResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CreateSearchResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[CreateSearchResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    engine_id: str,
    *,
    client: Client,
    json_body: CreateSearchRequest,
) -> Response[CreateSearchResponse]:
    """The search endpoint computes similarity scores between provided query and documents. Documents can
    be passed directly to the API if there are no more than 200 of them.

    To go beyond the 200 document limit, documents can be processed offline and then used for efficient
    retrieval at query time. When `file` is set, the search endpoint searches over all the documents in
    the given file and returns up to the `max_rerank` number of documents. These documents will be
    returned along with their search scores.

    The similarity score is a positive score that usually ranges from 0 to 300 (but can sometimes go
    higher), where a score above 200 usually means the document is semantically similar to the query.

    Args:
        engine_id (str):  Example: davinci.
        json_body (CreateSearchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateSearchResponse]
    """

    kwargs = _get_kwargs(
        engine_id=engine_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    engine_id: str,
    *,
    client: Client,
    json_body: CreateSearchRequest,
) -> Optional[CreateSearchResponse]:
    """The search endpoint computes similarity scores between provided query and documents. Documents can
    be passed directly to the API if there are no more than 200 of them.

    To go beyond the 200 document limit, documents can be processed offline and then used for efficient
    retrieval at query time. When `file` is set, the search endpoint searches over all the documents in
    the given file and returns up to the `max_rerank` number of documents. These documents will be
    returned along with their search scores.

    The similarity score is a positive score that usually ranges from 0 to 300 (but can sometimes go
    higher), where a score above 200 usually means the document is semantically similar to the query.

    Args:
        engine_id (str):  Example: davinci.
        json_body (CreateSearchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateSearchResponse]
    """

    return sync_detailed(
        engine_id=engine_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    engine_id: str,
    *,
    client: Client,
    json_body: CreateSearchRequest,
) -> Response[CreateSearchResponse]:
    """The search endpoint computes similarity scores between provided query and documents. Documents can
    be passed directly to the API if there are no more than 200 of them.

    To go beyond the 200 document limit, documents can be processed offline and then used for efficient
    retrieval at query time. When `file` is set, the search endpoint searches over all the documents in
    the given file and returns up to the `max_rerank` number of documents. These documents will be
    returned along with their search scores.

    The similarity score is a positive score that usually ranges from 0 to 300 (but can sometimes go
    higher), where a score above 200 usually means the document is semantically similar to the query.

    Args:
        engine_id (str):  Example: davinci.
        json_body (CreateSearchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateSearchResponse]
    """

    kwargs = _get_kwargs(
        engine_id=engine_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    engine_id: str,
    *,
    client: Client,
    json_body: CreateSearchRequest,
) -> Optional[CreateSearchResponse]:
    """The search endpoint computes similarity scores between provided query and documents. Documents can
    be passed directly to the API if there are no more than 200 of them.

    To go beyond the 200 document limit, documents can be processed offline and then used for efficient
    retrieval at query time. When `file` is set, the search endpoint searches over all the documents in
    the given file and returns up to the `max_rerank` number of documents. These documents will be
    returned along with their search scores.

    The similarity score is a positive score that usually ranges from 0 to 300 (but can sometimes go
    higher), where a score above 200 usually means the document is semantically similar to the query.

    Args:
        engine_id (str):  Example: davinci.
        json_body (CreateSearchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateSearchResponse]
    """

    return (
        await asyncio_detailed(
            engine_id=engine_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
