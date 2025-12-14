from Bio import Entrez

# Required by NCBI (can be any email)
Entrez.email = "pharmaedge@student.com"

def fetch_pubmed(query, max_results=3):
    search = Entrez.esearch(
        db="pubmed",
        term=query,
        retmax=max_results
    )

    result = Entrez.read(search)
    id_list = result["IdList"]

    abstracts = []

    for pid in id_list:
        fetch = Entrez.efetch(
            db="pubmed",
            id=pid,
            rettype="abstract",
            retmode="text"
        )
        abstracts.append(fetch.read())

    return abstracts
