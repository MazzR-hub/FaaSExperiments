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
    transaction = context.get_input()
    checks = []

    if transaction["amount"] > 10000:
        if transaction['type'] == "CASH_OUT":
            checks.append(context.call_activity("CompareForSender", transaction))

        else:
            checks.append(context.call_activity("CompareForSender", transaction))
            checks.append(context.call_activity("WarnForReceiver", transaction))
    else:
        transaction["isFraud"] = 0
    return []

main = df.Orchestrator.create(orchestrator_function)