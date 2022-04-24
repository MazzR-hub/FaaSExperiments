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
    vectors = vectors.replace(' ','')
    vectors = vectors.split(';')
    vectors[0] = vectors[0][1:-1].split(',')
    vectors[0] = list(map(int, vectors[0]))
    vectors[1] = vectors[1][1:-1].split(',')
    vectors[1] = list(map(int, vectors[1]))

    result = []
    
    for i in range(len(vectors[0])):
        result.append(vectors[0][i] + vectors[1][i])

    return result
