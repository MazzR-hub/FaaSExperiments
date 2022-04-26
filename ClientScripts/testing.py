# Workflow One. FunctionName: VectorOrchestrator
# {"instances": 2,"vector_one": [1,2,3,4], "vector_two": [5,6,7,8]}

# Workflow Two FunctionName: WholeVectorOrchestrator
# {"instances": 2,"vector_one": [1,2,3,4], "vector_two": [5,6,7,8]}

# Workflow Three FunctionName: VectorOrchestratorMultiPart
# {"add_instances": 2,"mult_instances":3,"vector_one": [1,2,3,4], "vector_two": [5,6,7,8]}

# Workflow Five (Called Six in second) FunctionName: FraudDetectionOrchestrator
# Workflow Six (Seven) FunctionName: FraudDataOrchestrator
# {
#     "top_instances": 5,
#     "sub_instances": 2,
#     "transactions": [
#         {
#             "step": "1",
#             "type": "PAYMENT",
#             "amount": "9839.64",
#             "nameOrig": "C1231006815",
#             "oldbalanceOrg": "170136.0",
#             "newbalanceOrig": "160296.36",
#             "nameDest": "M1979787155",
#             "oldbalanceDest": "0.0",
#             "newbalanceDest": "0.0",
#             "isFraud": "0",
#             "isFlaggedFraud": "0"
#         },
#         {
#             "step": "1",
#             "type": "PAYMENT",
#             "amount": "1864.28",
#             "nameOrig": "C1666544295",
#             "oldbalanceOrg": "21249.0",
#             "newbalanceOrig": "19384.72",
#             "nameDest": "M2044282225",
#             "oldbalanceDest": "0.0",
#             "newbalanceDest": "0.0",
#             "isFraud": "0",
#             "isFlaggedFraud": "0"
#         },
#         {
#             "step": "1",
#             "type": "TRANSFER",
#             "amount": "181.0",
#             "nameOrig": "C1305486145",
#             "oldbalanceOrg": "181.0",
#             "newbalanceOrig": "0.0",
#             "nameDest": "C553264065",
#             "oldbalanceDest": "0.0",
#             "newbalanceDest": "0.0",
#             "isFraud": "1",
#             "isFlaggedFraud": "0"
#         },
#         {
#             "step": "1",
#             "type": "CASH_OUT",
#             "amount": "181.0",
#             "nameOrig": "C840083671",
#             "oldbalanceOrg": "181.0",
#             "newbalanceOrig": "0.0",
#             "nameDest": "C38997010",
#             "oldbalanceDest": "21182.0",
#             "newbalanceDest": "0.0",
#             "isFraud": "1",
#             "isFlaggedFraud": "0"
#         },
#         {
#             "step": "1",
#             "type": "PAYMENT",
#             "amount": "11668.14",
#             "nameOrig": "C2048537720",
#             "oldbalanceOrg": "41554.0",
#             "newbalanceOrig": "29885.86",
#             "nameDest": "M1230701703",
#             "oldbalanceDest": "0.0",
#             "newbalanceDest": "0.0",
#             "isFraud": "0",
#             "isFlaggedFraud": "0"
#         },
#         {
#             "step": "1",
#             "type": "PAYMENT",
#             "amount": "7817.71",
#             "nameOrig": "C90045638",
#             "oldbalanceOrg": "53860.0",
#             "newbalanceOrig": "46042.29",
#             "nameDest": "M573487274",
#             "oldbalanceDest": "0.0",
#             "newbalanceDest": "0.0",
#             "isFraud": "0",
#             "isFlaggedFraud": "0"
#         },
#         {
#             "step": "1",
#             "type": "PAYMENT",
#             "amount": "7107.77",
#             "nameOrig": "C154988899",
#             "oldbalanceOrg": "183195.0",
#             "newbalanceOrig": "176087.23",
#             "nameDest": "M408069119",
#             "oldbalanceDest": "0.0",
#             "newbalanceDest": "0.0",
#             "isFraud": "0",
#             "isFlaggedFraud": "0"
#         },
#         {
#             "step": "1",
#             "type": "PAYMENT",
#             "amount": "7861.64",
#             "nameOrig": "C1912850431",
#             "oldbalanceOrg": "176087.23",
#             "newbalanceOrig": "168225.59",
#             "nameDest": "M633326333",
#             "oldbalanceDest": "0.0",
#             "newbalanceDest": "0.0",
#             "isFraud": "0",
#             "isFlaggedFraud": "0"
#         },
#         {
#             "step": "1",
#             "type": "PAYMENT",
#             "amount": "4024.36",
#             "nameOrig": "C1265012928",
#             "oldbalanceOrg": "2671.0",
#             "newbalanceOrig": "0.0",
#             "nameDest": "M1176932104",
#             "oldbalanceDest": "0.0",
#             "newbalanceDest": "0.0",
#             "isFraud": "0",
#             "isFlaggedFraud": "0"
#         },
#         {
#             "step": "1",
#             "type": "DEBIT",
#             "amount": "5337.77",
#             "nameOrig": "C712410124",
#             "oldbalanceOrg": "41720.0",
#             "newbalanceOrig": "36382.23",
#             "nameDest": "C195600860",
#             "oldbalanceDest": "41898.0",
#             "newbalanceDest": "40348.79",
#             "isFraud": "0",
#             "isFlaggedFraud": "0"
#         },
#         {
#             "step": "1",
#             "type": "DEBIT",
#             "amount": "9644.94",
#             "nameOrig": "C1900366749",
#             "oldbalanceOrg": "4465.0",
#             "newbalanceOrig": "0.0",
#             "nameDest": "C997608398",
#             "oldbalanceDest": "10845.0",
#             "newbalanceDest": "157982.12",
#             "isFraud": "0",
#             "isFlaggedFraud": "0"
#         },
#         {
#             "step": "1",
#             "type": "PAYMENT",
#             "amount": "3099.97",
#             "nameOrig": "C249177573",
#             "oldbalanceOrg": "20771.0",
#             "newbalanceOrig": "17671.03",
#             "nameDest": "M2096539129",
#             "oldbalanceDest": "0.0",
#             "newbalanceDest": "0.0",
#             "isFraud": "0",
#             "isFlaggedFraud": "0"
#         },
#         {
#             "step": "1",
#             "type": "PAYMENT",
#             "amount": "2560.74",
#             "nameOrig": "C1648232591",
#             "oldbalanceOrg": "5070.0",
#             "newbalanceOrig": "2509.26",
#             "nameDest": "M972865270",
#             "oldbalanceDest": "0.0",
#             "newbalanceDest": "0.0",
#             "isFraud": "0",
#             "isFlaggedFraud": "0"
#         },
#         {
#             "step": "1",
#             "type": "PAYMENT",
#             "amount": "11633.76",
#             "nameOrig": "C1716932897",
#             "oldbalanceOrg": "10127.0",
#             "newbalanceOrig": "0.0",
#             "nameDest": "M801569151",
#             "oldbalanceDest": "0.0",
#             "newbalanceDest": "0.0",
#             "isFraud": "0",
#             "isFlaggedFraud": "0"
#         },
#         {
#             "step": "1",
#             "type": "PAYMENT",
#             "amount": "4098.78",
#             "nameOrig": "C1026483832",
#             "oldbalanceOrg": "503264.0",
#             "newbalanceOrig": "499165.22",
#             "nameDest": "M1635378213",
#             "oldbalanceDest": "0.0",
#             "newbalanceDest": "0.0",
#             "isFraud": "0",
#             "isFlaggedFraud": "0"
#         },
#         {
#             "step": "1",
#             "type": "CASH_OUT",
#             "amount": "229133.94",
#             "nameOrig": "C905080434",
#             "oldbalanceOrg": "15325.0",
#             "newbalanceOrig": "0.0",
#             "nameDest": "C476402209",
#             "oldbalanceDest": "5083.0",
#             "newbalanceDest": "51513.44",
#             "isFraud": "0",
#             "isFlaggedFraud": "0"
#         }
#     ]
# }