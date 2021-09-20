import polygonscan
from aiohttp import ClientSession
from polygonscan.core.base import BaseClient
from polygonscan.enums.fields_enum import FieldsEnum as fields
from polygonscan.utils.parsing import ResponseParser as parser


class AsyncClient(BaseClient):
    async def _build(self):
        for func, v in self._config.items():
            if not func.startswith("_"):  # disabled if _
                attr = getattr(getattr(polygonscan, v["module"]), func)
                setattr(self, func, await self._exec(attr))
        return self

    async def _exec(self, func):
        async def wrapper(*args, **kwargs):
            url = (
                f"{fields.PREFIX}"
                f"{func(*args, **kwargs)}"
                f"{fields.API_KEY}"
                f"{self._api_key}"
            )
            if self._debug:
                print(f"\n{url}\n")
            async with self._session.get(url) as response:
                return parser.parse(await response.json())

        return wrapper

    async def __aenter__(self):
        self._session = ClientSession()
        return await self._build()

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self._session.close()

    @classmethod
    async def from_session(cls, api_key: str, session: ClientSession, **kwargs):
        client = AsyncClient(api_key, **kwargs)
        client._session = session
        return await client._build()