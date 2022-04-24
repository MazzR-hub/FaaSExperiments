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

    step = len(vec_one) // instances

    for i in range(instances-1):
        # Create the parallel function calls that will then be run
        tasks.append(context.call_activity('MultAndAdd', {"vector_one": vec_one[:step],"vector_two": vec_two[:step]}))
        
        # Remove the data we just passed out to a worker
        vec_one = vec_one[step:]
        vec_two = vec_two[step:]

    # Pass extra elements to the final worker
    tasks.append(context.call_activity('MultAndAdd', {"vector_one":vec_one, "vector_two":vec_two}))

    # Execute all the functions
    results = yield context.task_all(tasks)
    
    # Combine the results back into a flat list
    results = list(chain.from_iterable(results))

    return results

main = df.Orchestrator.create(orchestrator_function)