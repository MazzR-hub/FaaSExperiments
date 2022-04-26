import timeit
import requests
import time
import csv
import json
import numpy as np

INPUT_SIZE = 2000

def call_wf_one(numbers, second):
    url = "https://faasexperimentworkflowone.azurewebsites.net/api/orchestrators/VectorOrchestrator?code=zhsDDnJai0BGeacj0hiELMQPZqgbT3jr/a6AfrNRaUvjlcaephrciQ=="
    data = {"instances": 200, "vector_one": numbers.tolist(), "vector_two": second.tolist()}
    start_time = timeit.default_timer()
    requests.post(url, json=data)
    exec_time = timeit.default_timer() - start_time
    print(f"Workflow one used: {exec_time}")


def call_wf_two(numbers, second):
    url = "https://faasexperimentworkflowtwo.azurewebsites.net/api/orchestrators/WholeVectorOrchestrator?code=0nIhDdk2ZdZf67y5rh1MK06FqTg6jLpzjNjme8LHkTNzWUr5Yl7Rrw=="
    data = {"instances": 200, "vector_one": numbers.tolist(), "vector_two": second.tolist()}
    start_time = timeit.default_timer()
    requests.post(url, json=data)
    exec_time = timeit.default_timer() - start_time
    print(f"Workflow two used: {exec_time}")


def call_wf_three(numbers, second):
    url = "https://faasexperimentworkflowthree.azurewebsites.net/api/orchestrators/VectorOrchestratorMultiPart?code=u962w5909ESLtryoC3ESqHILqv2hwiu750eA2OrHTL0K0EJmHPUu7g=="
    data = {"add_instances": 150, "mult_instances":50, "vector_one": numbers.tolist(), "vector_two": second.tolist()}
    start_time = timeit.default_timer()
    requests.post(url, json=data)
    exec_time = timeit.default_timer() - start_time
    print(f"Workflow three used: {exec_time}")


def call_wf_five(transactions):
    url = "https://faasexperimentworkflowfive.azurewebsites.net/api/orchestrators/FraudDetectionOrchestrator?code=U2NA0BgdTRaBVeRcj986oWVifMjD94p0hKn77/aYKnzOV5XWHIrcag=="
    transactions["top_instances"] = 50
    transactions["sub_instances"] = 4
    start_time = timeit.default_timer()
    requests.post(url, json=transactions)
    exec_time = timeit.default_timer() - start_time
    print(f"Workflow five used: {exec_time}")


def call_wf_six(transactions):
    url = "https://faasexperimentworkflowsix.azurewebsites.net/api/orchestrators/FraudDataOrchestrator?code=yDgfwa6bJN2O93iEbOn2zngy5HukTVKTGydUeeIJteIXvU76Pxd2Bg=="
    transactions["top_instances"] = 50
    transactions["sub_instances"] = 4
    start_time = timeit.default_timer()
    requests.post(url, json=transactions)
    exec_time = timeit.default_timer() - start_time
    print(f"Workflow six used: {exec_time}")


def call_all():
    randnums= np.random.randint(1,100,INPUT_SIZE)
    randnums_sec= np.random.randint(1,100,INPUT_SIZE)

    data = {}
    transactions = []
    id = 1
    i=0
     
    with open("FraudData.csv", encoding='utf-8') as csvf:
        reader = csv.DictReader(csvf)
         
        for rows in reader:
            transactions.append(rows)
            i += 1
            if i >= INPUT_SIZE:
                break
        data["transactions"] = transactions

    print(f"To confirm: {len(randnums)}")

    for i in range(2):
        call_wf_one(randnums, randnums_sec)
        call_wf_two(randnums, randnums_sec)
        call_wf_three(randnums, randnums_sec)
        call_wf_five(data)
        call_wf_six(data)
        time.sleep(360)
        print("------------------")

call_all()