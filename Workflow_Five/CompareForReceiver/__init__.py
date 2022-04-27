# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import azure.functions as func

def main(transaction: str, flagReceiver: func.Out[func.QueueMessage]) -> str:
    # Function to determine whether to add the Receiver to a list to be checked for fraud in their account.
    # Used for Cash withdrawal payment records
    newRecord = {}
    newRecord['accountName'] = transaction['nameOrig']
    newRecord['amount'] = transaction['amount']
    newRecord['type'] = transaction['type']

    if transaction['amount'] >= transaction['oldBalanceOrg']:
        newRecord['warning'] = "Balance too high for account"
        newRecord['priority'] = "High"
    elif transaction['amount'] > 0.1 * transaction['oldBalanceOrg']:
        newRecord['warning'] = "Over 10% of balance removed in cash"
        newRecord['priority'] = "Medium"
    else:
        return "No log"
    flagReceiver.set(newRecord)
    return "Added message"
