# Use a base image
FROM debian:buster-slim

# Set working directory
WORKDIR /app

# Install necessary utilities
RUN apt-get update && \
    apt-get install -y openjdk-11-jre-headless wget curl python3 python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Upgrade pip to the latest version
RUN python3 -m pip install --upgrade pip

# Set Java environment variable
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64
ENV PATH $PATH:$JAVA_HOME/bin

# Install Apache Spark
ENV APACHE_SPARK_VERSION 3.4.4
ENV HADOOP_VERSION 3
RUN curl -L https://dlcdn.apache.org/spark/spark-$APACHE_SPARK_VERSION/spark-$APACHE_SPARK_VERSION-bin-hadoop$HADOOP_VERSION.tgz -o spark.tgz && \
    tar -xzf spark.tgz -C /opt && \
    rm spark.tgz

# Set Spark Home environment variable
ENV SPARK_HOME /opt/spark-$APACHE_SPARK_VERSION-bin-hadoop$HADOOP_VERSION
ENV PATH $PATH:$SPARK_HOME/bin

# Tworzenie folderu store
RUN mkdir -p /app/store

# Set src folder and ENV
COPY src /app/src
ENV PYTHONPATH=/app/src:$PYTHONPATH

# Install requirements using python3 -m pip (safer approach)
COPY requirements.txt /app/
RUN python3 -m pip install --no-cache-dir -r /app/requirements.txt

# Copy main.py into the container
COPY main.py /app/

# Expose Dash port
EXPOSE 8050

# Command to run the Dash application
CMD ["python3", "/app/main.py"]
