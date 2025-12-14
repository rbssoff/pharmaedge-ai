from trials_fetch import fetch_trials

trials = fetch_trials("Metformin")

for t in trials:
    print("\nCondition:", t.get("Condition"))
    print("Phase:", t.get("Phase"))
    print("Status:", t.get("OverallStatus"))
