import requests
import pandas as pd
from bs4 import BeautifulSoup

def fetch_sonarcloud_score():
    """Fetch SonarCloud quality metrics."""
    url = "https://sonarcloud.io/api/measures/component"
    params = {
        "component": "Lok-Jagruti-Kendra-University_testai",  # Your SonarCloud project key
        "branch":"main",
        "metricKeys": "coverage,bugs,code_smells"
    }
    response = requests.get(url, params=params)
    # Debugging output
    
    print("Response Status Code:", response.status_code)
    print("Response Content:", response.text)  
    
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
    deepsource_score = 30 #fetch_deepsource_score()
    return sonar_score
    overall_score = (sonar_score + mlflow_score + deepsource_score) / 3
    return {
        "SonarCloud": sonar_score,
        "MLflow": mlflow_score,
        "DeepSource": deepsource_score,
        "Overall Score": round(overall_score, 2)
    }


# SonarCloud Summary Page URL
SONARCLOUD_URL = "https://sonarcloud.io/summary/overall?id=Lok-Jagruti-Kendra-University_testai&branch=main"

def fetch_sonarcloud_summary():
    """Fetch and extract SonarCloud summary data."""
    response = requests.get(SONARCLOUD_URL)

    if response.status_code != 200:
        print("Failed to fetch data from SonarCloud")
        return None

    # Parse HTML content
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Extract metrics (example: Bugs, Code Smells, Vulnerabilities)
    metrics = {}
    
    # Example: Extracting bugs count (Modify selectors based on SonarCloud changes)
    bugs_element = soup.find("div", class_="metric-label", text="Bugs")
    if bugs_element:
        bugs_value = bugs_element.find_next_sibling("div").text.strip()
        metrics["Bugs"] = bugs_value

    # Example: Extracting Code Smells
    code_smells_element = soup.find("div", class_="metric-label", text="Code Smells")
    if code_smells_element:
        code_smells_value = code_smells_element.find_next_sibling("div").text.strip()
        metrics["Code Smells"] = code_smells_value

    # Example: Extracting Vulnerabilities
    vulnerabilities_element = soup.find("div", class_="metric-label", text="Vulnerabilities")
    if vulnerabilities_element:
        vulnerabilities_value = vulnerabilities_element.find_next_sibling("div").text.strip()
        metrics["Vulnerabilities"] = vulnerabilities_value

    return metrics

def save_to_excel(data):
    """Save extracted data to an Excel file."""
    if not data:
        print("No data to save")
        return

    df = pd.DataFrame([data])  # Convert dictionary to DataFrame
    df.to_excel("sonarcloud_summary.xlsx", index=False)  # Save to Excel
    print("SonarCloud summary saved to sonarcloud_summary.xlsx")

if __name__ == "__main__":
    summary_data = fetch_sonarcloud_summary()
    save_to_excel(summary_data)

    scores = aggregate_scores()
    print("Aggregated Scores:", scores)
