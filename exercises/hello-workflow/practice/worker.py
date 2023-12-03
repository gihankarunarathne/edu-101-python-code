import asyncio

from temporalio.client import Client
from temporalio.worker import Worker

from greeting import GreetSomeone

# Start worker with `python worker.py`. This'll stuck in the a long poll.
# Whatever the Workflows scheduled by Temporal will be executed via these workers.

# To init a Workflow via terminal:
# $ temporal workflow start \
#     --type <WorkflowDefinition> \
#     --task-queue <TaskQueueName> \
#     --workflow-id <WorkflowID> \
#     --input '"Mason"'
# E.g.
# temporal workflow start --type GreetSomeone --task-queue greeting-tasks --workflow-id=cli_workflow_1 --input='"Gihan"'

# $ temporal workflow show --workflow-id <WorkflowID>

async def main():
    client = await Client.connect("localhost:7233", namespace="default")
    # Run the worker
    worker = Worker(
        client,
        task_queue="greeting-tasks",
        workflows=[GreetSomeone],
    )
    print("Starting worker...")
    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
