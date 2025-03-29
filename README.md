# 🟢 Log Analysis - Apache Logs Analyzer

## 📜 Project Description
This project provides a tool for analyzing Apache logs using:
- **Apache Spark** - Big Data processing
- **Databricks Community Edition** - cloud-based data analysis
- **Dash** - interactive data visualization

### 🎯 Project Objective
The goal is to test the functionalities of **Databricks Community Edition**, **Apache Spark**, and **Dash**.  
The dataset used for analysis is a publicly available Apache logs dataset from:  
[Apache Logs Dataset](https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/apache_logs/apache_logs)  

## 🗂️ Project Structure
```bash
log-analysis/
├── Dockerfile                           # Docker image configuration
├── requirements.txt                     # Python dependencies
├── README.md                            # Project documentation
├── main.py                              # Main entry point of the application
├── store/                               # Folder containing data files
│   └── access_log_data.txt              # Sample Apache log file for analysis
└── src/                                 # Source code directory
    ├── databricks/                      # Databricks specific code
    │   └── log_analysis_databricks.dbc  # Databricks notebook for log analysis
    │   └── log_analysis_databricks.html # Databricks notebook for log analysis
    ├── dash/                            # Dash specific code for interactive visualization
    │   ├── data_analysis.py             # Data analysis logic
    │   ├── data_loader.py               # Data loading logic
    │   ├── log_parser.py                # Log parsing logic
    │   └── visualization.py             # Visualization logic for Dash app
```

## 🚀 Running the Application with Docker

1. **Clone the repository**:  
```bash
git clone https://github.com/kamil-scp/log_analysis
cd log_analysis
```
Build the Docker image:
```bash
docker build -t log_analysis .
```
Run the container:
```bash
docker run -p 8050:8050 log_analysis
```
The application will be available at:
http://localhost:8050

## 🟢 Databricks Community Edition Instructions

1. Go to Databricks Community Edition and create a free account.

2. Log in and navigate to the **Clusters** section in the left menu.

3. Click **Create Cluster** and configure it as follows:
    - Cluster Name: `log_analysis_cluster`
    - Databricks Runtime Version: `12.2 LTS (includes Apache Spark 3.3.2, Scala 2.12)`
    - Click **Create Cluster**

4. Go to the **Workspace** section and create a new folder, e.g., `log_analysis`.

5. Click on the three dots next to the `log_analysis` folder and choose **Import**.

6. Select the notebook file from the repository or paste the URL:
    - `https://github.com/kamil-scp/log_analysis/blob/main/src/databricks/log_analysis_databricks.dbc`

7. Click **Import**.

8. Open the imported notebook, attach the cluster (Attach Cluster), and run the cells sequentially.

9. Done! You can now analyze data using Apache Spark on Databricks! 🚀

## 📊 Features
Apache log analysis with:

- Top IP addresses

- HTTP status codes

- HTTP request types

- CSV data export

- Interactive visualizations with Dash

- Handling datasets with Apache Spark

## 🟢 Sample Dash View
The Dash application provides an interactive way to explore analysis results in the browser.
It includes bar charts, line charts, and an option to export data.

## 📢 Requirements
- Docker

- Python 3.8+

- Databricks Community Edition (for cloud analysis)