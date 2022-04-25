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
    number_per_instance = len(transactions) // instances

    for i in range(instances - 1):
        sub_transactions = {"transactions": transactions[:number_per_instance]}
        tasks.append(context.call_sub_orchestrator("TransactionProcessOrchestrator", sub_transactions))
        transactions = transactions[number_per_instance:]

    sub_transactions = {"transactions": transactions[:number_per_instance]}
    tasks.append(context.call_sub_orchestrator("TransactionProcessOrchestrator", sub_transactions))
    
    yield context.task_all(tasks)

    return []

main = df.Orchestrator.create(orchestrator_function)