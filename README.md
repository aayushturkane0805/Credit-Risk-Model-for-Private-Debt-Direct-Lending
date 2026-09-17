# Credit Risk Model for Private Debt / Direct Lending

## Overview

An end-to-end quantitative credit-risk and private-credit underwriting project. The workflow learns relationships between historical corporate financial ratios and bankruptcy outcomes, produces model-implied Probability of Default (PD) estimates for public-company borrowers, and translates those estimates into a hypothetical direct-lending underwriting framework.

> **Important:** The historical bankruptcy training population and the SEC public-company population are different populations and time periods. The resulting PD should therefore be treated as a **model-implied research estimate**, not a production-calibrated private-credit PD.

## What the project does

```text
Historical corporate financials
            ↓
Financial-ratio feature engineering
            ↓
Credit-event model
     ┌──────┴──────┐
     ↓             ↓
Logistic       Gradient
Regression     Boosting
     └──────┬──────┘
            ↓
Model-implied Probability of Default
            ↓
Public-company borrower scoring
            ↓
Hypothetical direct-lending underwriting
            ↓
Pricing • Facility sizing • Covenants • Expected loss
            ↓
EBITDA / interest-rate stress testing
            ↓
Credit memo + analytical outputs
```

## Companies used

| Ticker | Company | Sector | Role |
|---|---|---|---|
| MSFT | Microsoft Corporation | Technology | Primary detailed borrower |
| AAPL | Apple Inc. | Technology | Comparative borrower |
| AMZN | Amazon.com, Inc. | Consumer / Technology | Comparative borrower |
| WMT | Walmart Inc. | Retail | Comparative borrower |

The historical training data is the UCI Polish Companies Bankruptcy dataset. The public-company layer is designed around SEC/XBRL financial data, with validation and fallback handling in the notebook.

## Quantitative methodology

### Financial features

The model uses profitability, leverage, liquidity, coverage, efficiency and capital-structure ratios, including:

- Net Profit / Total Assets
- Total Liabilities / Total Assets
- Working Capital / Total Assets
- Current Assets / Short-Term Liabilities
- Retained Earnings / Total Assets
- EBIT / Total Assets
- Equity / Total Liabilities
- Sales / Total Assets
- Equity / Total Assets
- Gross Profit / Sales
- Net Profit / Sales
- Operating Profit / Interest Expense
- Working Capital / Fixed Assets
- Log Total Assets
- (Liabilities - Cash) / Sales
- Constant Capital / Total Assets
- Operating Profit / Sales
- Current Assets / Total Liabilities
- Current Liabilities / Total Assets
- Gross Margin
- Long-Term Liabilities / Equity

### Models

**Logistic Regression** provides a simple, interpretable baseline for a binary credit-event outcome.

**Gradient Boosting** adds nonlinear decision rules by combining many weak tree-based learners.

The notebook evaluates model discrimination and probability quality using metrics such as ROC-AUC, PR-AUC, KS, Brier Score and Log Loss where applicable.

## Direct-lending underwriting layer

The model output is connected to an illustrative private-credit deal analysis covering:

- Probability of Default (PD)
- Loss Given Default (LGD)
- Exposure at Default (EAD)
- Expected Loss
- Illustrative interest-rate spread and coupon
- Maximum facility size
- Net leverage
- Interest coverage
- Covenant thresholds
- Risk-adjusted yield
- EBITDA stress testing
- Interest-rate stress testing

The relationship used for simplified expected-loss analysis is:

**Expected Loss = PD × LGD × EAD**

## Visualizations

Only the most decision-useful charts are emphasized:

1. **Model performance / ROC curve** — shows how well the model separates the two outcome classes.
2. **Borrower PD comparison** — shows how model-implied risk differs across the sample public companies.
3. **Stress-test visualization** — shows how underwriting metrics change as operating performance or financing costs deteriorate.

## Repository structure

```text
Credit-Risk-Model-for-Private-Debt-Direct-Lending/
├── README.md
├── notebooks/
│   └── Credit_Risk_Model_Project.ipynb
├── src/
│   └── credit_risk_model.py
├── data/
│   └── README.md
├── outputs/
│   ├── borrower_scores.csv
│   ├── borrower_features.csv
│   ├── model_metrics.csv
│   ├── deal_analysis.csv
│   ├── stress_test.csv
│   └── charts/
├── models/
│   └── final_model.json
├── reports/
│   └── credit_memo.xlsx
├── sql/
│   └── credit_risk.db
├── requirements.txt
└── .gitignore
```

## How to run

The original implementation is designed for Google Colab. Open the notebook, run the main cell from top to bottom, and review the generated outputs. The notebook downloads the historical dataset and attempts to retrieve public-company financial information through SEC endpoints with defensive validation and fallback logic.

## Technologies

- Python
- NumPy
- Pandas
- Matplotlib
- OpenPyXL
- SQLite
- SEC/XBRL data
- Google Colab

## Finance concepts demonstrated

**Probability of Default (PD):** estimated probability of the defined credit event over the model's relevant horizon.

**Default:** failure to meet a contractual debt obligation under the applicable loan terms. It is not synonymous with bankruptcy.

**Loss Given Default (LGD):** proportion of exposure expected to be lost if default occurs, after considering recoveries.

**Exposure at Default (EAD):** amount of credit exposure outstanding when default occurs.

**Leverage:** relationship between debt and operating earnings, commonly expressed as debt / EBITDA in leveraged lending.

**Interest Coverage:** ability of operating earnings to cover interest expense, commonly EBIT or EBITDA divided by interest expense depending on the underwriting definition.

**Covenant:** contractual financial or operational requirement designed to protect lenders and provide early warning of deterioration.

## Key limitation

This is an educational/research underwriting framework. It is not intended to replace a lender's full due diligence, management assessment, industry analysis, legal documentation review, recovery analysis, or a production-grade probability-of-default calibration process.

## Author

Aayush Turkane
