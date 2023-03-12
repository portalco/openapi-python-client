from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.create_classification_request import CreateClassificationRequest
from ...models.create_classification_response import CreateClassificationResponse
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: CreateClassificationRequest,
) -> Dict[str, Any]:
    url = "{}/classifications".format(client.base_url)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[CreateClassificationResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CreateClassificationResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[CreateClassificationResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: CreateClassificationRequest,
) -> Response[CreateClassificationResponse]:
    """Classifies the specified `query` using provided examples.

    The endpoint first [searches](/docs/api-reference/searches) over the labeled examples
    to select the ones most relevant for the particular query. Then, the relevant examples
    are combined with the query to construct a prompt to produce the final label via the
    [completions](/docs/api-reference/completions) endpoint.

    Labeled examples can be provided via an uploaded `file`, or explicitly listed in the
    request using the `examples` parameter for quick tests and small scale use cases.

    Args:
        json_body (CreateClassificationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateClassificationResponse]
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
    json_body: CreateClassificationRequest,
) -> Optional[CreateClassificationResponse]:
    """Classifies the specified `query` using provided examples.

    The endpoint first [searches](/docs/api-reference/searches) over the labeled examples
    to select the ones most relevant for the particular query. Then, the relevant examples
    are combined with the query to construct a prompt to produce the final label via the
    [completions](/docs/api-reference/completions) endpoint.

    Labeled examples can be provided via an uploaded `file`, or explicitly listed in the
    request using the `examples` parameter for quick tests and small scale use cases.

    Args:
        json_body (CreateClassificationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateClassificationResponse]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: CreateClassificationRequest,
) -> Response[CreateClassificationResponse]:
    """Classifies the specified `query` using provided examples.

    The endpoint first [searches](/docs/api-reference/searches) over the labeled examples
    to select the ones most relevant for the particular query. Then, the relevant examples
    are combined with the query to construct a prompt to produce the final label via the
    [completions](/docs/api-reference/completions) endpoint.

    Labeled examples can be provided via an uploaded `file`, or explicitly listed in the
    request using the `examples` parameter for quick tests and small scale use cases.

    Args:
        json_body (CreateClassificationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateClassificationResponse]
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
    json_body: CreateClassificationRequest,
) -> Optional[CreateClassificationResponse]:
    """Classifies the specified `query` using provided examples.

    The endpoint first [searches](/docs/api-reference/searches) over the labeled examples
    to select the ones most relevant for the particular query. Then, the relevant examples
    are combined with the query to construct a prompt to produce the final label via the
    [completions](/docs/api-reference/completions) endpoint.

    Labeled examples can be provided via an uploaded `file`, or explicitly listed in the
    request using the `examples` parameter for quick tests and small scale use cases.

    Args:
        json_body (CreateClassificationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateClassificationResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
