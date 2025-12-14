import streamlit as st
from pubmed_fetch import fetch_pubmed
from trials_fetch import fetch_trials
from ai_engine import analyze_data
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from textwrap import wrap

def summarize_abstracts(abstracts):
    """Summarize abstracts into bullet points."""
    if not abstracts:
        return []
    # Return first 5 abstracts as summaries, or customize as needed
    return abstracts[:5] if isinstance(abstracts, list) else [abstracts]


def generate_pdf(drug, insights, abstract_summary):
    # ✅ SAFETY NORMALIZATION (MANDATORY)
    if isinstance(insights, str):
        insights = [
            line.strip("•- ").strip()
            for line in insights.split("\n")
            if line.strip()
        ]
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    x_margin = 50
    y = height - 50

    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(x_margin, y, "PHARMAEDGE AI – Drug Repurposing Report")

    # Drug name
    y -= 40
    c.setFont("Helvetica", 12)
    c.drawString(x_margin, y, f"Drug / Disease Analyzed: {drug}")

    # Section header
    y -= 35
    c.setFont("Helvetica-Bold", 14)
    c.drawString(x_margin, y, "AI-Generated Insights")

    y -= 25
    c.setFont("Helvetica", 11)

    for insight in insights:
        wrapped_lines = wrap(insight, 90)

        for line in wrapped_lines:
            if y < 80:
                c.showPage()
                y = height - 50
                c.setFont("Helvetica", 11)

            c.drawString(x_margin + 10, y, f"• {line}")
            y -= 18

        y -= 10  # Space between insights
    # Abstract Summary section
    y -= 20
    c.setFont("Helvetica-Bold", 14)
    c.drawString(x_margin, y, "Literature Abstract Summary")

    y -= 25
    c.setFont("Helvetica", 11)

    for point in abstract_summary:
        wrapped_lines = wrap(point, 90)

        for line in wrapped_lines:
            if y < 80:
                c.showPage()
                y = height - 50
                c.setFont("Helvetica", 11)

            c.drawString(x_margin, y, line)
            y -= 18

        y -= 10

    c.save()
    buffer.seek(0)
    return buffer



st.set_page_config(page_title="PHARMAEDGE AI", layout="wide")

st.title("💊 PHARMAEDGE AI")
st.subheader("Agentic AI for Drug Repurposing")

drug = st.text_input("Enter Drug or Disease Name", placeholder="e.g. Metformin")

if st.button("Analyze"):
    if not drug:
        st.warning("Please enter a drug or disease name.")
    else:
        with st.spinner("Fetching biomedical literature..."):
            abstracts = fetch_pubmed(drug)

        with st.spinner("Fetching clinical trial data..."):
            trials = fetch_trials(drug)

        with st.spinner("Analyzing using AI reasoning..."):
            insights = analyze_data(drug, abstracts, trials)
            abstract_summary = summarize_abstracts(abstracts)
            pdf = generate_pdf(drug, insights, abstract_summary)
               

            st.download_button(
                label="Download PDF Report",
                data=pdf,
                file_name=f"{drug}_report.pdf",
                mime="application/pdf"
            )

        st.subheader("🧪 AI-Generated Insights")
        for point in insights:
            st.markdown(f"- {point}")
        

        st.header("📚 Literature Evidence (PubMed)")
        for i, abs_text in enumerate(abstracts, start=1):
            with st.expander(f"Abstract {i}"):
                st.write(abs_text)
