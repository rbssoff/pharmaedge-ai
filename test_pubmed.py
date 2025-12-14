from pubmed_fetch import fetch_pubmed

data = fetch_pubmed("Metformin cancer")

for i, abstract in enumerate(data, start=1):
    print(f"\n--- Abstract {i} ---\n")
    print(abstract)
