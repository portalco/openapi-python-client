from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.create_answer_request import CreateAnswerRequest
from ...models.create_answer_response import CreateAnswerResponse
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: CreateAnswerRequest,
) -> Dict[str, Any]:
    url = "{}/answers".format(client.base_url)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[CreateAnswerResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CreateAnswerResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[CreateAnswerResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: CreateAnswerRequest,
) -> Response[CreateAnswerResponse]:
    """Answers the specified question using the provided documents and examples.

    The endpoint first [searches](/docs/api-reference/searches) over provided documents or files to find
    relevant context. The relevant context is combined with the provided examples and question to create
    the prompt for [completion](/docs/api-reference/completions).

    Args:
        json_body (CreateAnswerRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateAnswerResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    json_body: CreateAnswerRequest,
) -> Optional[CreateAnswerResponse]:
    """Answers the specified question using the provided documents and examples.

    The endpoint first [searches](/docs/api-reference/searches) over provided documents or files to find
    relevant context. The relevant context is combined with the provided examples and question to create
    the prompt for [completion](/docs/api-reference/completions).

    Args:
        json_body (CreateAnswerRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateAnswerResponse]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: CreateAnswerRequest,
) -> Response[CreateAnswerResponse]:
    """Answers the specified question using the provided documents and examples.

    The endpoint first [searches](/docs/api-reference/searches) over provided documents or files to find
    relevant context. The relevant context is combined with the provided examples and question to create
    the prompt for [completion](/docs/api-reference/completions).

    Args:
        json_body (CreateAnswerRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateAnswerResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    json_body: CreateAnswerRequest,
) -> Optional[CreateAnswerResponse]:
    """Answers the specified question using the provided documents and examples.

    The endpoint first [searches](/docs/api-reference/searches) over provided documents or files to find
    relevant context. The relevant context is combined with the provided examples and question to create
    the prompt for [completion](/docs/api-reference/completions).

    Args:
        json_body (CreateAnswerRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateAnswerResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
