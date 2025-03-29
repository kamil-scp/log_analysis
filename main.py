import os
from pyspark.sql import SparkSession
from src.log_parser import parse_logs
from src.data_loader import load_file
from src.data_analysis import transform_data, analyze_data
from src.visualization import create_dashboard

# Ustawienia ścieżek do plików
url_log_path = "https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/apache_logs/apache_logs"
file_store_path = "store"
file_name = "access_log_data.log"

# Pobranie pliku z logami
print(f"Getting logs from: {url_log_path}...")
load_file(url_log_path, file_store_path, file_name)

# Uruchomienie SparkSession
spark = SparkSession.builder.appName("LogAnalysis").getOrCreate()

# Wczytanie logów do DataFrame
df = spark.read.text(os.path.join(file_store_path, file_name))

# Przetwarzanie logów
df_parsed = parse_logs(df)
df_parsed = transform_data(df_parsed)
analysis_dict = analyze_data(df_parsed)

# Konwersja do Pandas DataFrame
df_ip = analysis_dict["ip"].toPandas()
df_status = analysis_dict["status"].toPandas()
df_request = analysis_dict["request"].toPandas()

# Tworzenie i uruchomienie aplikacji Dash
app = create_dashboard(df_ip, df_status, df_request)

if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8050, debug=True)
