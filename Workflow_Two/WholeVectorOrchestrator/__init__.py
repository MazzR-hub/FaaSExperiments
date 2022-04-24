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

from itertools import chain

def orchestrator_function(context: df.DurableOrchestrationContext):
    params = context.get_input()

    instances = params["instances"]
    tasks = []

    vec_one = params["vector_one"]
    vec_two = params["vector_two"]
    half = len(vec_one) // 2
    halfinst = instances // 2
    
    half_vectors = {"instances": halfinst, "vector_one": vec_one[:half], "vector_two": vec_two[:half]}
    first_half = context.call_sub_orchestrator("SplitVectorOrchestrator", half_vectors)

    half_vectors = {"instances": (instances - halfinst), "vector_one": vec_one[half:], "vector_two": vec_two[half:]}
    second_half = context.call_sub_orchestrator("SplitVectorOrchestrator", half_vectors)

    orch_tasks = [first_half, second_half]
    results = yield context.task_all(orch_tasks)
    results = list(chain.from_iterable(results))

    return results

main = df.Orchestrator.create(orchestrator_function)