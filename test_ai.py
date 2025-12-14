from ai_engine import analyze_data

abstracts = [
    "Metformin has demonstrated potential anti-cancer effects in observational studies."
]

trials = [
    {"Condition": ["Breast Cancer"], "Phase": ["Phase 2"], "OverallStatus": ["Recruiting"]}
]

result = analyze_data("Metformin", abstracts, trials)
print(result)
