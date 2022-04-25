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
    input = context.get_input()
    instances = input['instances']
    transactions = input['transactions']

    tasks = []
    j=0

    for i in range(len(transactions)):
        tasks.append(context.call_sub_orchestrator("TransactionProcessOrchestrator", transactions[i]))
        j += 1

        if j >= i:
            yield context.task_all(tasks)
            tasks = []
            j=0

    return []

main = df.Orchestrator.create(orchestrator_function)