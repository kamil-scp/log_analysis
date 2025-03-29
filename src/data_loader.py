# Databricks notebook source
# src/data_loader.py
import os
import requests

def load_file(url_log_path, file_store_path, file_name):
    # Download file to the folder
    response = requests.get(url_log_path)
    
    x = os.getcwd()

    if response.status_code == 200:
        with open(os.path.join(file_store_path, file_name), 'wb') as file:
            file.write(response.content)
        msg = 'Log file downloaded correctly!'
    else:
        msg = 'Problem with downloading the log file'
    # Check if the file is in the folder
    return msg

