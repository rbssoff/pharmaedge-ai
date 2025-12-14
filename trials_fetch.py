def fetch_trials(query):
    """
    Fallback clinical trial data.
    Used when live ClinicalTrials.gov API is unavailable.
    """

    mock_trials = [
        {
            "Condition": ["Type 2 Diabetes Mellitus"],
            "Phase": ["Phase 3"],
            "OverallStatus": ["Completed"]
        },
        {
            "Condition": ["Breast Cancer"],
            "Phase": ["Phase 2"],
            "OverallStatus": ["Recruiting"]
        }
    ]

    print("⚠️ Using cached clinical trial data (API unavailable)")
    return mock_trials
