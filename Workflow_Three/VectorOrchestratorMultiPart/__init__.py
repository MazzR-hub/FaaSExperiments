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

    add_instances = params["add_instances"]
    mult_instances = params["mult_instances"]
    tasks = []
    tasks_second = []


    # Perform the multiplication step
    vec_one = params["vector_one"]
    vec_two = params["vector_two"]

    # Since instances are split between the two arrays, an odd number of instances will be rounded down.
    loops = mult_instances // 2
    mult_step = len(vec_one) // loops

    for i in range(loops-1):
        # Create the parallel function calls that will then be run
        tasks.append(context.call_activity('VectorMult', {"vector": vec_one[:mult_step],"operand": 351154}))
        tasks_second.append(context.call_activity('VectorMult', {"vector": vec_two[:mult_step],"operand": 85412}))
        
        # Remove the data we just passed out to a worker
        vec_one = vec_one[mult_step:]
        vec_two = vec_two[mult_step:]

    # Includes any extra elements at the end of the array
    tasks.append(context.call_activity('VectorMult', {"vector": vec_one[:mult_step],"operand": 351154}))
    tasks_second.append(context.call_activity('VectorMult', {"vector": vec_two[:mult_step],"operand": 85412}))

    vec_one = yield context.task_all(tasks)
    vec_one = list(chain.from_iterable(vec_one))

    vec_two = yield context.task_all(tasks_second)
    vec_two = list(chain.from_iterable(vec_two))

    logging.info(f"After multiplication is {vec_one} and {vec_two}")

    # Now perform the addition step
    tasks = []
    step = len(vec_one) // add_instances

    for i in range(add_instances-1):
        # Create the parallel function calls that will then be run
        tasks.append(context.call_activity('VectorAdd', {"vector_one": vec_one[:step],"vector_two": vec_two[:step]}))
        
        # Remove the data we just passed out to a worker
        vec_one = vec_one[step:]
        vec_two = vec_two[step:]

    # Pass extra elements to the final worker
    tasks.append(context.call_activity('VectorAdd', {"vector_one": vec_one[:step],"vector_two": vec_two[:step]}))

    # Execute all the functions
    results = yield context.task_all(tasks)
    
    # Combine the results back into a flat list
    results = list(chain.from_iterable(results))
    logging.info(f"Finished with {results}")
    return results

main = df.Orchestrator.create(orchestrator_function)