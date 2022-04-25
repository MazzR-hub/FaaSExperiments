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
    logging.info(f"Data provided was {data}")
    transactions = data["transactions"]
    senders = []
    logging.info(f"I received this {transactions}")

    for transaction in transactions:
        result = yield context.call_activity("CompareForSender", transaction)
        if result == "Fraud":
            yield context.call_activity("WarnForReceiver", transaction)

    return []

main = df.Orchestrator.create(orchestrator_function)