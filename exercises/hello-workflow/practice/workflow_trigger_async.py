import sys
import asyncio

from temporalio.client import Client
from greeting import GreetSomeone


async def main():
    client = await Client.connect("localhost:7233")

    # Execute a workflow via code
    handler = client.start_workflow(GreetSomeone, sys.argv[2], id=f"async_workflow_{sys.argv[1]}", task_queue='greeting-tasks')
    print(f"Starting workflow. Workflow ID: {handler.id}, Run ID: {handler.result_run_id}")

    result = await handler.result()

    print(f"Async Result: {result}")


if __name__ == "__main__":
    asyncio.run(main())
