import timeit
import requests
import time
import csv
import json
import numpy as np

INPUT_SIZE = 2000
INSTANCES = 1

def call_wf_one(numbers, second):
    #VectorOrchestrator
    url = "https://experimentworkflowonefaas.azurewebsites.net/api/orchestrators/VectorOrchestrator?code=bkAur1wvfoayK713v7u5KllCSqbF2ozDjSKepTyrqGzKwIIPSjbKkA=="
    data = {"instances": 2, "vector_one": numbers.tolist(), "vector_two": second.tolist()}
    start_time = timeit.default_timer()
    requests.post(url, json=data)
    exec_time = timeit.default_timer() - start_time
    print(f"Workflow one used: {exec_time}")


def call_wf_two(numbers, second):
    #WholeVectorOrchestrator
    url = "https://experimentworkflowtwofaas.azurewebsites.net/api/orchestrators/WholeVectorOrchestrator?code=LX1Da5QTsspBO6DdVAswG/QPWYaKce5kg/PF0YaCgvvm1WapI1Zdxg=="
    data = {"instances": 2, "vector_one": numbers.tolist(), "vector_two": second.tolist()}
    start_time = timeit.default_timer()
    requests.post(url, json=data)
    exec_time = timeit.default_timer() - start_time
    print(f"Workflow two used: {exec_time}")


def call_wf_three(numbers, second):
    #VectorOrchestratorMultiPart
    url = "https://experimentworkflowthreefaas.azurewebsites.net/api/orchestrators/VectorOrchestratorMultiPart?code=cO7aWnpChouu52CLSvUtsAORJSFJtpUyFegjo7R7myR9j/EXBaCuGQ=="
    data = {"add_instances": 2, "mult_instances":1, "vector_one": numbers.tolist(), "vector_two": second.tolist()}
    start_time = timeit.default_timer()
    requests.post(url, json=data)
    exec_time = timeit.default_timer() - start_time
    print(f"Workflow three used: {exec_time}")


def call_wf_five(transactions):
    #FraudDetectionOrchestrator
    url = "https://experimentworkflowsixfaas.azurewebsites.net/api/orchestrators/FraudDetectionOrchestrator?code=PMcHsrY8/NUw71JK1637qOntREc/e/nVMZBJgf7F104IDFAtLiZrQw=="
    transactions["top_instances"] = 2
    transactions["sub_instances"] = 1
    start_time = timeit.default_timer()
    requests.post(url, json=transactions)
    exec_time = timeit.default_timer() - start_time
    print(f"Workflow five used: {exec_time}")


def call_wf_six(transactions):
    #FraudDataOrchestrator
    url = "https://experimentworkflowsevenfaas.azurewebsites.net/api/orchestrators/FraudDataOrchestrator?code=wEni8ij7vvR1aixAjsT9cl3fiGfw0DUpEd0deBOOGaGBvdGaXWAhzQ=="
    transactions["top_instances"] = 2
    transactions["sub_instances"] = 1
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

    print(f"Instances: {INSTANCES}")
    for i in range(3):
        call_wf_one(randnums, randnums_sec)
        call_wf_two(randnums, randnums_sec)
        call_wf_three(randnums, randnums_sec)
        call_wf_five(data)
        call_wf_six(data)
        time.sleep(450)
        print("-------------------------")

call_all()