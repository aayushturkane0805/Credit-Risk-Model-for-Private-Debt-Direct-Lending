# Credit Risk Model for Private Debt / Direct Lending

## What this project is

This project builds a quantitative credit-risk framework that connects **financial statement analysis → credit-event prediction → direct-lending underwriting**.

The core question is:

> **Given a company's financial profile, how can a lender estimate credit risk and translate that risk into a lending decision?**

The project learns from historical corporate financials and bankruptcy outcomes, applies the resulting model to a sample of public companies, and converts the model output into an illustrative private-credit underwriting analysis.

## How it works

```text
Historical corporate financials
        ↓
Financial-ratio feature engineering
        ↓
Credit-event modeling
   ┌────┴─────┐
   ↓          ↓
Logistic   Gradient
Regression Boosting
   └────┬─────┘
        ↓
Model-implied credit risk
        ↓
Public-company borrower scoring
        ↓
Direct-lending underwriting
        ↓
PD • LGD • EAD • Expected Loss
        ↓
Facility Size • Leverage • Coverage • Pricing
        ↓
Covenants + Stress Testing
        ↓
Credit Memo + Analytical Outputs
```

## The models

### 1. Logistic Regression

A transparent baseline model for a binary credit event. It estimates how the financial features relate to the probability of the modeled outcome and provides an interpretable benchmark.

### 2. Gradient Boosting

A nonlinear model built from multiple decision-stump learners. It can capture relationships between financial ratios that a simple linear model may not capture.

Both models are trained and evaluated using measures such as **ROC-AUC, PR-AUC, KS, Brier Score and Log Loss** where applicable. Their validation performance is compared before selecting the model used in the downstream analysis.

## Financial analysis

The feature set covers the main areas a credit analyst would examine:

- **Profitability** — earnings relative to assets, sales and capital
- **Leverage / solvency** — liabilities, equity and capital structure
- **Liquidity** — working capital and current-asset coverage
- **Coverage** — operating earnings relative to interest expense
- **Efficiency** — sales and operating performance relative to assets
- **Margins** — gross, operating and net profitability

## From model output to lending decision

The project goes beyond predicting credit risk. It uses the model output in a hypothetical direct-lending deal to show how quantitative risk can be incorporated into underwriting decisions.

The analysis includes:

- **PD, LGD and EAD**
- **Expected Loss = PD × LGD × EAD**
- Maximum facility sizing
- Net leverage
- Interest coverage
- Illustrative pricing / interest-rate spread
- Covenant thresholds
- Risk-adjusted yield
- EBITDA stress testing
- Interest-rate stress testing

This creates a link between **statistical modeling and practical credit underwriting** rather than treating the model as a standalone machine-learning exercise.

## Sample borrowers

The public-company application uses:

| Ticker | Company | Role |
|---|---|---|
| MSFT | Microsoft Corporation | Primary detailed borrower |
| AAPL | Apple Inc. | Comparative borrower |
| AMZN | Amazon.com, Inc. | Comparative borrower |
| WMT | Walmart Inc. | Comparative borrower |

Historical training data comes from the **UCI Polish Companies Bankruptcy dataset**, while the public-company layer is designed around SEC/XBRL financial data.

## Key outputs

The notebook produces decision-oriented outputs including:

- Model performance metrics
- Borrower feature data
- Model-implied borrower risk scores
- Deal analysis
- Stress-test results
- Decision-useful charts
- SQLite analytical database
- Professional Excel credit memo

## What the lender gets from the analysis

The final output is designed to give a lender a structured view of the borrower before committing capital. The lender can assess the company's **model-implied credit risk, expected loss, leverage, interest coverage, facility capacity and risk-adjusted economics**, while also seeing how those metrics change under downside scenarios.

This information supports the key underwriting questions: **How much should we lend? At what pricing? What leverage and coverage levels should we require? What covenants should protect the lender? How resilient is the borrower under stress? And, ultimately, does the proposed risk and return fit the lender's underwriting requirements?**

The project therefore connects quantitative analysis to the practical decision process of **evaluating a borrower, structuring a facility, setting terms and determining whether the proposed lending opportunity meets the lender's requirements.**

## Why this project matters

This project combines **credit analysis, financial modeling and quantitative methods** in one workflow.

It demonstrates how a lender or credit investor could move from:

**financial statements → ratios → risk model → borrower risk assessment → leverage and coverage analysis → pricing → covenants → stress testing → credit memo.**

The framework is relevant to workflows in **private credit, direct lending, credit hedge funds, commercial banking and corporate credit analysis**.

## Documentation

- [Finance Concepts](FINANCE_CONCEPTS.md) — definitions and how the project applies the key credit concepts.
- [Limitations](LIMITATIONS.md) — a concise summary of the project's main limitations.

## Repository structure

```text
Credit-Risk-Model-for-Private-Debt-Direct-Lending/
├── README.md
├── FINANCE_CONCEPTS.md
├── LIMITATIONS.md
├── notebooks/
│   └── Credit_Risk_Model_Project.ipynb
├── src/
│   └── credit_risk_model.py
├── data/
│   └── README.md
├── outputs/
├── models/
├── reports/
├── sql/
├── requirements.txt
└── .gitignore
```

## Technologies

**Python • NumPy • Pandas • Matplotlib • OpenPyXL • SQLite • SEC/XBRL • Google Colab**

## Author

**Aayush Turkane**
