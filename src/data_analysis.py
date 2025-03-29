# Databricks notebook source
# src/data_analysis.py
from pyspark.sql.functions import to_date, to_timestamp, desc

def transform_data(df_parsed):
    # Change column types
    df_parsed = df_parsed.withColumn("date", to_date("timestamp", "dd/MMM/yyyy"))
    df_parsed = df_parsed.withColumn("timestamp", to_timestamp("timestamp", "dd/MMM/yyyy:HH:mm:ss Z"))
    return df_parsed

def analyze_data(df_parsed):
    # Grouping and aggregating data for analysis (example)
    analysis_dict = {}
    analysis_list = ["ip", "request", "status"]
    
    for analysis_item in analysis_list:
        analysis_dict[analysis_item] = df_parsed.groupBy(analysis_item).count().orderBy(desc("count"))
    
    return analysis_dict
