# Databricks notebook source
# src/log_parser.py
from pyspark.sql.functions import regexp_extract, col

def parse_logs(df):
    log_pattern = r'(\S+) - - \[(.*?)\] "(.*?)" (\d{3}) (\d+) "(.*?)" "(.*?)"'
    aliases_list = ["ip", "timestamp", "request", "status", "size", "referer", "user_agent"]
    
    columns = [
        regexp_extract(col("value"), log_pattern, index + 1).alias(alias_name)
        for index, alias_name in enumerate(aliases_list)
    ]
    
    df_parsed = df.select(*columns)
    return df_parsed
