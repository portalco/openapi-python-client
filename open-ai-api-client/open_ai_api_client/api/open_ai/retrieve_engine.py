from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.engine import Engine
from ...types import Response


def _get_kwargs(
    engine_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/engines/{engine_id}".format(client.base_url, engine_id=engine_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Engine]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Engine.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Engine]:
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
) -> Response[Engine]:
    """Retrieves a model instance, providing basic information about it such as the owner and availability.

    Args:
        engine_id (str):  Example: davinci.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Engine]
    """

    kwargs = _get_kwargs(
        engine_id=engine_id,
        client=client,
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
) -> Optional[Engine]:
    """Retrieves a model instance, providing basic information about it such as the owner and availability.

    Args:
        engine_id (str):  Example: davinci.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Engine]
    """

    return sync_detailed(
        engine_id=engine_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    engine_id: str,
    *,
    client: Client,
) -> Response[Engine]:
    """Retrieves a model instance, providing basic information about it such as the owner and availability.

    Args:
        engine_id (str):  Example: davinci.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Engine]
    """

    kwargs = _get_kwargs(
        engine_id=engine_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    engine_id: str,
    *,
    client: Client,
) -> Optional[Engine]:
    """Retrieves a model instance, providing basic information about it such as the owner and availability.

    Args:
        engine_id (str):  Example: davinci.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Engine]
    """

    return (
        await asyncio_detailed(
            engine_id=engine_id,
            client=client,
        )
    ).parsed
