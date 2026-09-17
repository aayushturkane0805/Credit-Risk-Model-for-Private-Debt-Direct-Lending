# How to Run the Project

The project is designed to run in **Google Colab**.

## 1. Open the notebook

Open:

`notebooks/Credit_Risk_Model_Project.ipynb`

You can upload the notebook to Google Colab or open it directly from GitHub.

## 2. Install / verify dependencies

The notebook uses the project's Python dependencies listed in `requirements.txt`.

Core libraries include:

- NumPy
- Pandas
- Matplotlib
- OpenPyXL

SQLite and the SEC/XBRL workflow are also used by the project.

## 3. Run the notebook from top to bottom

Run the main notebook cells in order. The workflow is designed to move through:

1. Environment setup
2. Historical bankruptcy data loading
3. Data cleaning and validation
4. Financial-ratio feature preparation
5. Train / validation / test splitting
6. Logistic Regression training
7. Gradient Boosting training
8. Model evaluation and comparison
9. Public-company financial-data retrieval
10. Borrower feature construction
11. Borrower risk scoring
12. Hypothetical direct-lending analysis
13. Stress testing
14. Output generation
15. Final credit analysis / memo

## 4. Public-company data

The public-company layer is designed around SEC/XBRL financial information. The notebook includes defensive handling for retrieval, compression and validation so that invalid or incomplete responses are not silently treated as usable financial data.

The sample companies are:

- MSFT — Microsoft
- AAPL — Apple
- AMZN — Amazon
- WMT — Walmart

## 5. Review the model results

After execution, review the model metrics and borrower scoring outputs first.

Key files include:

- `model_metrics.csv`
- `borrower_scores.csv`
- `borrower_features.csv`

## 6. Review the underwriting analysis

The direct-lending layer produces:

- Deal analysis
- Facility sizing
- Net leverage
- Interest coverage
- Illustrative pricing
- Expected loss
- Covenant thresholds
- Risk-adjusted yield

The stress-test output can then be reviewed to understand how the underwriting metrics respond to weaker EBITDA and higher interest rates.

## 7. Review the final deliverables

The project can produce:

- CSV analytical outputs
- Charts
- SQLite database
- Saved model artifact
- Excel credit memo

The Excel credit memo is intended to present the analysis in a format closer to a practical credit-underwriting deliverable.

## 8. Recommended execution order for review

For an interviewer or recruiter, the fastest review path is:

**README → notebook → model results → borrower analysis → stress test → credit memo.**

The separate documentation files provide additional detail only when needed.
