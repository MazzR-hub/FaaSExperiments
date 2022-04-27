# This function is not intended to be invoked directly. Instead it will be
# triggered by an HTTP starter function.
# Before running this sample, please:
# - create a Durable activity function (default name is "Hello")
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import json

import azure.functions as func
import azure.durable_functions as df


def orchestrator_function(context: df.DurableOrchestrationContext):
    data = context.get_input()
    transactions = data["transactions"]
    senders = []
    instances = data['instances']
    logging.info(f"I received this {transactions}")

    loops_required = len(transactions) // instances
    remainder = len(transactions) % instances

    tasks = []

    for i in range(loops_required):
        for j in range(instances):
            index = i * instances + j
            transaction = transactions[index]
            tasks.append(context.call_activity("CompareForSender", transaction))
        yield context.task_all(tasks)
        tasks = []

    for j in range(remainder):
        index = loops_required * instances + j
        transaction = transactions[index]
        tasks.append(context.call_activity("CompareForSender", transaction))
    return []

main = df.Orchestrator.create(orchestrator_function)