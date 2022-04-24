# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging


from typing import List

def main(vectors: str) -> List[int]:
    # Convert the string parameter back into the list of integers easiest for manipulation.
    logging.info(f'Received {vectors}')
    vec_one = vectors['vector_one']
    vec_two = vectors['vector_two']

    result = []
    
    for i in range(len(vec_one)):
        mult_one = vec_one[i] * 351154
        mult_two = vec_two[i] * 85412
        result.append(mult_one + mult_two)

    return result
