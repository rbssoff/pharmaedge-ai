def analyze_data(drug, abstracts, trials):
    """
    Rule-based AI simulation (no paid API)
    """

    insights = [
        f"{drug} shows strong existing safety data due to long-term clinical use.",
        "Literature suggests potential efficacy beyond original indication.",
        "Clinical trials indicate activity across Phase 2 and Phase 3 studies.",
        "Mechanism of action aligns with unmet clinical needs in related diseases.",
        "Repurposing opportunity identified with reduced development risk.",
        "Further validation recommended through targeted preclinical studies."
    ]

    return insights


def summarize_abstracts(abstracts, max_points=4):
    """
    Simple heuristic-based summarization of abstracts
    """

    if not abstracts:
        return ["No abstracts available for summarization."]

    summary_points = []

    for abstract in abstracts[:max_points]:
        # Take first meaningful sentence
        sentences = abstract.split(".")
        if len(sentences) > 1:
            summary_points.append(sentences[0].strip() + ".")
        else:
            summary_points.append(abstract[:200] + "...")

    return summary_points
