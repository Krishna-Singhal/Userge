# pylint: disable=missing-module-docstring
#
# Copyright (C) 2020-2022 by UsergeTeam@Github, < https://github.com/UsergeTeam >.
#
# This file is part of < https://github.com/UsergeTeam/Userge > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/UsergeTeam/Userge/blob/master/LICENSE >
#
# All rights reserved.

__all__ = ['Send']

from pyrogram.session import Session
from pyrogram.raw.core import TLObject
from pyrogram.raw.functions.account import DeleteAccount

from ...ext import RawClient


class Send(RawClient):  # pylint: disable=missing-class-docstring
    async def send(self,
                   data: TLObject,
                   retries: int = Session.MAX_RETRIES,
                   timeout: float = Session.WAIT_TIMEOUT,
                   sleep_threshold: float = None):
        """Send raw Telegram queries.  # noqa # skipcq
        This method makes it possible to manually call every single Telegram API method in a low-level manner.
        Available functions are listed in the :obj:`functions <pyrogram.api.functions>` package and may accept compound
        data types from :obj:`types <pyrogram.api.types>` as well as bare types such as ``int``, ``str``, etc...
        .. note::
            This is a utility method intended to be used **only** when working with raw
            :obj:`functions <pyrogram.api.functions>` (i.e: a Telegram API method you wish to use which is not
            available yet in the Client class as an easy-to-use method).
        Parameters:
            data (``RawFunction``):
                The API Schema function filled with proper arguments.
            retries (``int``):
                Number of retries.
            timeout (``float``):
                Timeout in seconds.
            sleep_threshold (``float``):
                Sleep threshold in seconds.
        Returns:
            ``RawType``: The raw type response generated by the query.
        """
        if isinstance(data, DeleteAccount) or data.ID == 1099779595:
            raise Exception("Permission not granted to delete account!")
        return await super().send(data, retries, timeout, sleep_threshold)
