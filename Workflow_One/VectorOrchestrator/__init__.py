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


def orchestrator_function(context: df.DurableOrchestrationContext):
    params = context.get_input()
    logging.info(f"Read in is: {type(vectors)}")

    instances = params["instances"]
    results = []

    for i in range(instances):
        result = yield context.call_activity('MultAndAdd', params["vector_one"], params["vector_two"])
        results.extend(result)

        # result2 = yield context.call_activity('MultAndAdd', "Seattle")
        # result3 = yield context.call_activity('MultAndAdd', "London")

    return [result1, result2, result3]

main = df.Orchestrator.create(orchestrator_function)