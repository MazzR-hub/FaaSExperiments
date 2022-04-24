# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging


def main(vectors: str) -> str:
    logging.info(f'Received {vectors}')
    vec_one = vectors['vector_one']
    vec_two = vectors['vector_two']

    result = []

    for i in range(len(vec_one)):
        result.append(vec_one[i] + vec_two[i])

    return result

