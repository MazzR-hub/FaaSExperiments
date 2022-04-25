# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import os
import pandas as pd
import azure.functions as func
from io import StringIO
from azure.storage.blob import BlobClient, StorageStreamDownloader

def main(name: str, input: func.InputStream) -> StorageStreamDownloader:
    conn = os.getenv("MyStorageConnectionAppSetting")
    blob_client = BlobClient.from_connection_string(conn_str=conn, container_name="payment-data-container",blob_name="Fraud_Detection_Dataset.csv")
    data_downloader = blob_client.download_blob()
    results = pd.read_csv(StringIO(data_downloader.content_as_text()))
    results = results.to_json()
    logging.info(f"Received {results[50]}")

    return 
