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
    instances = input['top_instances']
    transactions = input['transactions']
    sub_instances = input['sub_instances']

    to_process = []

    for transaction in transactions:
        if float(transaction['amount']) > 10000:
            to_process.append(transaction)

    tasks = []

    number_per_instance = len(to_process) // instances
    if number_per_instance < 1:
        instances = len(to_process)
        number_per_instance = 1

    for i in range(instances - 1):
        sub_transactions = {"instances": sub_instances, "transactions": to_process[:number_per_instance]}
        tasks.append(context.call_sub_orchestrator("HighAmountOrchestrator", sub_transactions))
        transactions = to_process[number_per_instance:]

    sub_transactions = {"instances": sub_instances, "transactions": to_process}
    tasks.append(context.call_sub_orchestrator("HighAmountOrchestrator", sub_transactions))
    
    yield context.task_all(tasks)

    return []

main = df.Orchestrator.create(orchestrator_function)