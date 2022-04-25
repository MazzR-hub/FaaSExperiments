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


def main(transaction: str, flagSender: func.Out[func.QueueMessage], flagReceiver: func.Out[func.QueueMessage]) -> str:
    # Function to determine whether to add the Sender to a list to be checked for fraud in their account.
    logging.info("I'VE GOT HERE")
    newRecord = {}
    amount = float(transaction['amount'])

    newRecord['accountName'] = transaction['nameOrig']
    newRecord['amount'] = amount
    newRecord['type'] = transaction['type']
    today = datetime.date.today()
    newRecord['date'] = today.strftime("%d/%m/%Y")

    if amount >= float(transaction['oldbalanceOrg']):
        newRecord['warning'] = "Balance too high for account"
        newRecord['priority'] = "High"
    elif amount > 0.1 * float(transaction['oldbalanceOrg']):
        newRecord['warning'] = "Over 10% of balance removed"
        newRecord['priority'] = "Medium"
    else:
        logging.info(f"I have not written out to queue {newRecord}")
        return "No Fraud"
    logging.info(f"I have written out to queue {newRecord}")
    flagSender.set(str(newRecord))

    if transaction['type'] != "CASH_OUT":
        nextRecord = newRecord
        nextRecord['accountName'] = transaction['nameDest']
        if amount > 0.1 * float(transaction['oldbalanceOrg']) and amount >= 0.5 * float(transaction['oldbalanceDest']):
            nextRecord['warning'] = "Recipient gained more than 50% of their original balance"
            flagReceiver.set(str(nextRecord))
    return "Fraud"