import asyncio
import random

async def call_ai(query: str):
    await asyncio.sleep(1)

    # simulate failure
    if random.choice([True, False]):
        return None

    return f"AI Response: {query}"