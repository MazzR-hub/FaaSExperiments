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
    checks = []
    logging.info(f"Whole data: {transactions}")

    for transaction in transactions:
        logging.info(f"Gave us {transaction}")
        if float(transaction["amount"]) > 10000:
            logging.info("Found transaction")
            if transaction['type'] == "CASH_OUT":
                checks.append(context.call_activity("CompareForSender", transaction))
            else:
                checks.append(context.call_activity("CompareForSender", transaction))
                checks.append(context.call_activity("WarnForReceiver", transaction))
            yield context.task_all(checks)
        else:
            logging.info(f"Did not meet. Amount {transaction['amount']}")
            transaction["isFraud"] = 0
        return []

main = df.Orchestrator.create(orchestrator_function)