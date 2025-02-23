import requests

def fetch_sonarcloud_score():
    """Fetch SonarCloud quality metrics."""
    url = "https://sonarcloud.io/api/measures/component"
    params = {
        "component": "Lok-Jagruti-Kendra-University_testai",  # Your SonarCloud project key
        "metric": "coverage,bugs,code_smells"
    }
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        measures = data.get("component", {}).get("measures", [])
        
        # Example: Extracting coverage score
        code_smells = next((m["value"] for m in measures if m["metric"] == "code_smells"), 0)
        return float(code_smells)
    
    return 0  # Default to 0 if request fails

def fetch_mlflow_score():
    """Fetch an example MLflow metric (dummy API, replace with real MLflow API)."""
    url = "http://mlflow-server.example.com/api/2.0/mlflow/metrics/get"
    params = {
        "run_id": "some-run-id",
        "metric_key": "accuracy"
    }
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return float(data.get("metric", {}).get("value", 0)) * 100  # Convert to percentage
    return 0

def fetch_deepsource_score():
    """Fetch DeepSource score (Example API call, replace with actual API)."""
    url = "https://deepsource.io/api/v1/some_project/issues/statistics"
    headers = {"Authorization": "Token YOUR_DEEPSOURCE_API_KEY"}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return 100 - int(data.get("issue_count", 0))  # Assuming fewer issues = better score
    return 0

def aggregate_scores():
    """Aggregate scores from all sources."""
    sonar_score = fetch_sonarcloud_score()
    mlflow_score = 30 #fetch_mlflow_score()
    deepsource_score = 20 #fetch_deepsource_score()

    overall_score = (sonar_score + mlflow_score + deepsource_score) / 3
    return {
        "SonarCloud": sonar_score,
        "MLflow": mlflow_score,
        "DeepSource": deepsource_score,
        "Overall Score": round(overall_score, 2)
    }

if __name__ == "__main__":
    scores = aggregate_scores()
    print("Aggregated Scores:", scores)
