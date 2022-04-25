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
    instances = data["instances"]
    checks = []
    logging.info(f"Whole data: {transactions}")
    loops_required = len(transactions) // instances
    remainder = len(transactions) % instances

    for i in range(loops_required):
        for j in range(instances):
            index = i * instances + j
            transaction = transactions[index]
            logging.info(f"Gave us {transaction}")
            if float(transaction["amount"]) > 10000:
                logging.info("Found transaction")
                if transaction['type'] == "CASH_OUT":
                    checks.append(context.call_activity("CompareForSender", transaction))
                else:
                    checks.append(context.call_activity("CompareForSender", transaction))
                    checks.append(context.call_activity("WarnForReceiver", transaction))
            else:
                logging.info(f"Did not meet criteria. Amount {transaction['amount']}")
        yield context.task_all(checks)
        checks = []

    for j in range(remainder):
        index = loops_required * instances + j
        transaction = transactions[index]
        if float(transaction["amount"]) > 10000:
            logging.info("Found transaction")
            if transaction['type'] == "CASH_OUT":
                checks.append(context.call_activity("CompareForSender", transaction))
            else:
                checks.append(context.call_activity("CompareForSender", transaction))
                checks.append(context.call_activity("WarnForReceiver", transaction))
        else:
            logging.info(f"Did not meet criteria. Amount {transaction['amount']}")

    yield context.task_all(checks)

    return []

main = df.Orchestrator.create(orchestrator_function)