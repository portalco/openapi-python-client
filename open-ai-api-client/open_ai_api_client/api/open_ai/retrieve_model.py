from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.model import Model
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
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Model]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Model.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Model]:
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
) -> Response[Model]:
    """Retrieves a model instance, providing basic information about the model such as the owner and
    permissioning.

    Args:
        model (str):  Example: text-davinci-001.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Model]
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
) -> Optional[Model]:
    """Retrieves a model instance, providing basic information about the model such as the owner and
    permissioning.

    Args:
        model (str):  Example: text-davinci-001.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Model]
    """

    return sync_detailed(
        model=model,
        client=client,
    ).parsed


async def asyncio_detailed(
    model: str,
    *,
    client: Client,
) -> Response[Model]:
    """Retrieves a model instance, providing basic information about the model such as the owner and
    permissioning.

    Args:
        model (str):  Example: text-davinci-001.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Model]
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
) -> Optional[Model]:
    """Retrieves a model instance, providing basic information about the model such as the owner and
    permissioning.

    Args:
        model (str):  Example: text-davinci-001.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Model]
    """

    return (
        await asyncio_detailed(
            model=model,
            client=client,
        )
    ).parsed
