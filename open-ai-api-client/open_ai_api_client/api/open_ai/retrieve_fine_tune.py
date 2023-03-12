from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.fine_tune import FineTune
from ...types import Response


def _get_kwargs(
    fine_tune_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/fine-tunes/{fine_tune_id}".format(client.base_url, fine_tune_id=fine_tune_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[FineTune]:
    if response.status_code == HTTPStatus.OK:
        response_200 = FineTune.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[FineTune]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    fine_tune_id: str,
    *,
    client: Client,
) -> Response[FineTune]:
    """Gets info about the fine-tune job.

    [Learn more about Fine-tuning](/docs/guides/fine-tuning)

    Args:
        fine_tune_id (str):  Example: ft-AF1WoRqd3aJAHsqc9NY7iL8F.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FineTune]
    """

    kwargs = _get_kwargs(
        fine_tune_id=fine_tune_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    fine_tune_id: str,
    *,
    client: Client,
) -> Optional[FineTune]:
    """Gets info about the fine-tune job.

    [Learn more about Fine-tuning](/docs/guides/fine-tuning)

    Args:
        fine_tune_id (str):  Example: ft-AF1WoRqd3aJAHsqc9NY7iL8F.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FineTune]
    """

    return sync_detailed(
        fine_tune_id=fine_tune_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    fine_tune_id: str,
    *,
    client: Client,
) -> Response[FineTune]:
    """Gets info about the fine-tune job.

    [Learn more about Fine-tuning](/docs/guides/fine-tuning)

    Args:
        fine_tune_id (str):  Example: ft-AF1WoRqd3aJAHsqc9NY7iL8F.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FineTune]
    """

    kwargs = _get_kwargs(
        fine_tune_id=fine_tune_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    fine_tune_id: str,
    *,
    client: Client,
) -> Optional[FineTune]:
    """Gets info about the fine-tune job.

    [Learn more about Fine-tuning](/docs/guides/fine-tuning)

    Args:
        fine_tune_id (str):  Example: ft-AF1WoRqd3aJAHsqc9NY7iL8F.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FineTune]
    """

    return (
        await asyncio_detailed(
            fine_tune_id=fine_tune_id,
            client=client,
        )
    ).parsed
