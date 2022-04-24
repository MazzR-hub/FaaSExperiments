# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging


def main(vectormult: str) -> str:
    vector = vectormult['vector']
    logging.info(f'Received {vector}')
    multValue = vectormult['operand']

    result = []

    for i in range(len(vector)):
        result.append(vector[i] * multValue)

    return result
