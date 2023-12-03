import sys
import asyncio

from temporalio.client import Client
from greeting import GreetSomeone


async def main():
    client = await Client.connect("localhost:7233")

    # Execute a workflow via code
    result = await client.execute_workflow(GreetSomeone, sys.argv[2], id=f"test_workflow_{sys.argv[1]}", task_queue='greeting-tasks')
    print(f"Sync Result: {result}")


if __name__ == "__main__":
    asyncio.run(main())
