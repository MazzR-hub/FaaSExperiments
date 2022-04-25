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
    transactions = input['records']

    tasks = []

    for i in range(len(transactions),__step=instances):
        tasks.append(context.call_sub_orchestrator("TransactionProcessOrchestrator", transactions[i]))
        yield context.task_all(tasks)
        tasks = []
        
    return []

main = df.Orchestrator.create(orchestrator_function)