from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.delete_model_response import DeleteModelResponse
from ...types import Response


def _get_kwargs(
    model: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/models/{model}".format(client.base_url, model=model)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[DeleteModelResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DeleteModelResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[DeleteModelResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    model: str,
    *,
    client: Client,
) -> Response[DeleteModelResponse]:
    """Delete a fine-tuned model. You must have the Owner role in your organization.

    Args:
        model (str):  Example: curie:ft-acmeco-2021-03-03-21-44-20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteModelResponse]
    """

    kwargs = _get_kwargs(
        model=model,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    model: str,
    *,
    client: Client,
) -> Optional[DeleteModelResponse]:
    """Delete a fine-tuned model. You must have the Owner role in your organization.

    Args:
        model (str):  Example: curie:ft-acmeco-2021-03-03-21-44-20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteModelResponse]
    """

    return sync_detailed(
        model=model,
        client=client,
    ).parsed


async def asyncio_detailed(
    model: str,
    *,
    client: Client,
) -> Response[DeleteModelResponse]:
    """Delete a fine-tuned model. You must have the Owner role in your organization.

    Args:
        model (str):  Example: curie:ft-acmeco-2021-03-03-21-44-20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteModelResponse]
    """

    kwargs = _get_kwargs(
        model=model,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    model: str,
    *,
    client: Client,
) -> Optional[DeleteModelResponse]:
    """Delete a fine-tuned model. You must have the Owner role in your organization.

    Args:
        model (str):  Example: curie:ft-acmeco-2021-03-03-21-44-20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteModelResponse]
    """

    return (
        await asyncio_detailed(
            model=model,
            client=client,
        )
    ).parsed
