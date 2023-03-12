from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.create_file_request import CreateFileRequest
from ...models.open_ai_file import OpenAIFile
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    multipart_data: CreateFileRequest,
) -> Dict[str, Any]:
    url = "{}/files".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "files": multipart_multipart_data,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[OpenAIFile]:
    if response.status_code == HTTPStatus.OK:
        response_200 = OpenAIFile.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[OpenAIFile]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    multipart_data: CreateFileRequest,
) -> Response[OpenAIFile]:
    """Upload a file that contains document(s) to be used across various endpoints/features. Currently, the
    size of all the files uploaded by one organization can be up to 1 GB. Please contact us if you need
    to increase the storage limit.

    Args:
        multipart_data (CreateFileRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OpenAIFile]
    """

    kwargs = _get_kwargs(
        client=client,
        multipart_data=multipart_data,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    multipart_data: CreateFileRequest,
) -> Optional[OpenAIFile]:
    """Upload a file that contains document(s) to be used across various endpoints/features. Currently, the
    size of all the files uploaded by one organization can be up to 1 GB. Please contact us if you need
    to increase the storage limit.

    Args:
        multipart_data (CreateFileRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OpenAIFile]
    """

    return sync_detailed(
        client=client,
        multipart_data=multipart_data,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    multipart_data: CreateFileRequest,
) -> Response[OpenAIFile]:
    """Upload a file that contains document(s) to be used across various endpoints/features. Currently, the
    size of all the files uploaded by one organization can be up to 1 GB. Please contact us if you need
    to increase the storage limit.

    Args:
        multipart_data (CreateFileRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OpenAIFile]
    """

    kwargs = _get_kwargs(
        client=client,
        multipart_data=multipart_data,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    multipart_data: CreateFileRequest,
) -> Optional[OpenAIFile]:
    """Upload a file that contains document(s) to be used across various endpoints/features. Currently, the
    size of all the files uploaded by one organization can be up to 1 GB. Please contact us if you need
    to increase the storage limit.

    Args:
        multipart_data (CreateFileRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OpenAIFile]
    """

    return (
        await asyncio_detailed(
            client=client,
            multipart_data=multipart_data,
        )
    ).parsed
