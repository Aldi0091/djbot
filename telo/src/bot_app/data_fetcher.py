import aiohttp
from .local_settings import TOKEN_ENDPOINT

async def save_token(message):
    async with aiohttp.ClientSession() as session:
        async with session.post(TOKEN_ENDPOINT, json={"message": message}) as response:
            return response.text