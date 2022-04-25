# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import datetime
import azure.functions as func


def main(transaction: str, flagReceiver: func.Out[func.QueueMessage]) -> str:
    # Function to write out for a queue to investigate recipients of suspicious payments.
    newRecord = {}
    newRecord['accountName'] = transaction['nameDest']
    newRecord['amount'] = transaction['amount']
    newRecord['type'] = transaction['type']
    newRecord['date'] = datetime.datetime.today()

    if transaction['amount'] >= 0.5 * transaction['oldBalanceDest']:
        newRecord['warning'] = "Recipient gained more than 50% of their original balance"
        flagReceiver.set(newRecord)
        return "Added message"
    else:
        return "No log"
