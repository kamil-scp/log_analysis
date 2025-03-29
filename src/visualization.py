import os
import flask
import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

external_stylesheets = [
    "https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600&display=swap"
]

def limit_categories(df, column, max_categories=30):
    """Limits the number of categories displayed on a chart.
       Remaining values are grouped as 'Other'."""
    if len(df) > max_categories:
        top_values = df.nlargest(max_categories, "count")
        other_sum = df["count"].sum() - top_values["count"].sum()
        other_row = pd.DataFrame([{column: "Other", "count": other_sum}])
        df = pd.concat([top_values, other_row], ignore_index=True)
    return df

def truncate_request_column(df, column, max_length=30):
    """Truncates the values in the specified column to the given maximum length."""
    df[column] = df[column].apply(lambda x: x[:max_length] if isinstance(x, str) else x)
    return df

def save_csv(df, filename):
    """Saves DataFrame to a CSV file in the 'exported_csv' folder."""
    os.makedirs('exported_csv', exist_ok=True)  # Create the 'exported_csv' folder if it doesn't exist
    path = os.path.join('exported_csv', filename)
    df.to_csv(path, index=False)
    return path

def create_dashboard(df_ip_init, df_status_init, df_request_init):
    """Creates a simple Dash dashboard."""
    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

    # Truncate the 'request' column in df_request to 30 characters
    df_request = truncate_request_column(df_request_init, "request", max_length=50)

    df_ip = limit_categories(df_ip_init, "ip")
    df_status = limit_categories(df_status_init, "status")
    df_request = limit_categories(df_request, "request")
    
    # Create the figures
    fig_ip = px.bar(df_ip, x="ip", y="count", title="Top IP Addresses")
    fig_ip.update_xaxes(tickangle=45)  # Rotate X axis labels by 45 degrees
    
    fig_status = px.bar(df_status, x="count", y="status", title="Requests per Status Code", orientation='h')
    fig_status.update_yaxes(tickangle=45)  # Rotate Y axis labels by 45 degrees for horizontal bar chart
    
    fig_request = px.line(df_request, x="request", y="count", title="Request Frequency")
    fig_request.update_xaxes(tickangle=45)  # Rotate X axis labels by 45 degrees

    app.layout = html.Div(style={
        "font-family": "Montserrat, sans-serif",
        "background": "#F8F8F8",  
        "padding": "20px",
        "text-align": "center"
    }, children=[
        html.H1("Log Analysis Dashboard", style={"font-weight": "600", "color": "#333"}),

        html.Div([
            dcc.Graph(figure=fig_ip),
            html.A("📥 Download IP Data", href="/download/ip_requests.csv", className="download-button")
        ], style={"margin-bottom": "20px"}),

        html.Div([
            dcc.Graph(figure=fig_status),
            html.A("📥 Download Status Codes", href="/download/status_codes.csv", className="download-button")
        ], style={"margin-bottom": "20px"}),

        html.Div([
            dcc.Graph(figure=fig_request, style={"height": "600px", "margin-bottom": "20px"}),
            html.A("📥 Download Request Data", href="/download/request_types.csv", className="download-button")
        ])
    ])

    @app.server.route('/download/<filename>')
    def download_file(filename):
        """Handles file download from server."""
        if filename == "ip_requests.csv":
            path = save_csv(df_ip_init, filename)
        elif filename == "status_codes.csv":
            path = save_csv(df_status_init, filename)
        elif filename == "request_types.csv":
            path = save_csv(df_request_init, filename)
        
        # Use os.path.join to create the full path to the file
        return flask.send_from_directory(directory=os.path.abspath('exported_csv'), path=filename)

    return app
