import asyncio
import aiohttp
import pytest


async def num_mines(x, y):
    await asyncio.sleep(3)
    return x + y


@pytest.mark.asyncio
async def test_get_plus(event_loop):
    result = await num_mines(5, 3)
    assert result == 2


async def valueerror():
    await asyncio.sleep(3)
    value = int("as")
    return int


@pytest.mark.asyncio
async def test_valueerror(event_loop):
    with pytest.raises(ValueError):
        await valueerror()


async def get_code(code):
    url = f"http://numbersapi.com/#{code}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return code


@pytest.mark.asyncio
async def test_get_code():
    code = await get_code(3)
    assert code == 3


asyncio.run(test_get_code())