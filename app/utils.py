import asyncio
from typing import Dict

cache: Dict[str, str] = {}

async def transformer_function(string: str) -> str:
    # Check if the result is already cached
    if string in cache:
        return cache[string]
    
    # if not cached hit external service and cache the string
    # simulate hit external service 1 second
    await asyncio.sleep(1)
    transformed_string = string.upper()

    cache[string] = transformed_string
    return transformed_string

def interleave_lists(list1, list2):
    return [item for pair in zip(list1, list2) for item in pair]
