import requests

# Fetch SonarCloud score (Example API call)
sonar_score = requests.get("https://sonarcloud.io/api/project_badges/measure?project=Lok-Jagruti-Kendra-University_testai&metric=alert_status").json()

# Mock MLflow AI model score (Replace with actual MLflow API call)
mlflow_score = 80  # Assume 80/100 for AI implementation

# Mock DeepSource security check score
deepsource_score = 85  # Assume 85/100 for security best practices

# Final weighted score calculation
final_score = (sonar_score * 0.4) + (mlflow_score * 0.3) + (deepsource_score * 0.3)

print(f"Final Project Score: {final_score}/100")
