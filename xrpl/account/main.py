"""High-level methods to obtain information about accounts."""

import asyncio
from typing import Dict, Union

from xrpl.asyncio.account import main
from xrpl.clients.sync_client import SyncClient
from xrpl.models.response import Response


def does_account_exist(address: str, client: SyncClient) -> bool:
    """
    Query the ledger for whether the account exists.

    Args:
        address: the account to query.
        client: the network client used to make network calls.

    Returns:
        Whether the account exists on the ledger.

    Raises:
        XRPLRequestFailureException: if the transaction fails.
    """
    return asyncio.run(main.does_account_exist(address, client))


def get_next_valid_seq_number(address: str, client: SyncClient) -> int:
    """
    Query the ledger for the next available sequence number for an account.

    Args:
        address: the account to query.
        client: the network client used to make network calls.

    Returns:
        The next valid sequence number for the address.
    """
    return asyncio.run(main.get_next_valid_seq_number(address, client))


def get_balance(address: str, client: SyncClient) -> int:
    """
    Query the ledger for the balance of the given account.

    Args:
        address: the account to query.
        client: the network client used to make network calls.

    Returns:
        The balance of the address.
    """
    return asyncio.run(main.get_balance(address, client))


def get_account_root(address: str, client: SyncClient) -> Dict[str, Union[int, str]]:
    """
    Query the ledger for the AccountRoot object associated with a given address.

    Args:
        address: the account to query.
        client: the network client used to make network calls.

    Returns:
        The AccountRoot dictionary for the address.
    """
    return asyncio.run(main.get_account_root(address, client))


def get_account_info(address: str, client: SyncClient) -> Response:
    """
    Query the ledger for account info of given address.

    Args:
        address: the account to query.
        client: the network client used to make network calls.

    Returns:
        The account info for the address.

    Raises:
        XRPLRequestFailureException: if the rippled API call fails.
    """
    return asyncio.run(main.get_account_info(address, client))


def get_account_lines(address: str, client: SyncClient) -> Response:
    """
    Query the ledger for account lines of given address.

    Args:
        address: the account to query.
        client: the network client used to make network calls.

    Returns:
        The account lines for the address.

    Raises:
        XRPLRequestFailureException: if the rippled API call fails.
    """
    return asyncio.run(main.get_account_lines(address, client))
