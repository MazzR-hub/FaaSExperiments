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
    amount = float(transaction['amount'])
    newRecord['accountName'] = transaction['nameDest']
    newRecord['amount'] = amount
    newRecord['type'] = transaction['type']
    today = datetime.date.today()
    newRecord['date'] = today.strftime("%d/%m/%Y")

    if amount > 0.1 * float(transaction['oldbalanceOrg']) and amount >= 0.5 * float(transaction['oldbalanceDest']):
        newRecord['warning'] = "Recipient gained more than 50% of their original balance"
        flagReceiver.set(str(newRecord))
        logging.info(f"Should be writing: {newRecord}")
        return "Added message"
    else:
        logging.info(f"Left. Amount was {amount}")
        return "No log"
