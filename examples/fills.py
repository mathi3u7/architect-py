import asyncio
import os
from architect_py.client import Client
from architect_py.graphql_client.exceptions import GraphQLClientHttpError
from .common import create_client

async def main():
    c: Client = create_client()
    try:
        stream = c.subscribe_fills()
        async for item in stream:
            print(item)
    except GraphQLClientHttpError as e:
        print(e.status_code)
        print(e.response.json())

asyncio.run(main())