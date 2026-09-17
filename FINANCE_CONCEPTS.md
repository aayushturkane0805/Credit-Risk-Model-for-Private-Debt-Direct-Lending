# Finance Concepts Covered

This document explains the main credit and lending concepts used in the project and where they appear in the workflow.

## 1. Probability of Default (PD)

PD is the estimated probability of the modeled credit event over the relevant model horizon.

In this project, the historical training target is bankruptcy. Therefore, the model output is a **model-implied research estimate related to the historical event**, rather than a production-calibrated private-credit PD.

**Project use:** borrower scoring and downstream underwriting analysis.

## 2. Default vs. Bankruptcy

**Default** is failure to meet a contractual debt obligation according to the applicable loan terms.

**Bankruptcy** is a formal legal process associated with severe financial distress. A borrower can default without entering bankruptcy, so the two terms are not interchangeable.

**Project use:** the historical dataset uses bankruptcy as the modeled event, while the direct-lending layer uses standard private-credit terminology such as PD, LGD and EAD.

## 3. Loss Given Default (LGD)

LGD represents the proportion of exposure expected to be lost if default occurs after considering recoveries.

**Project use:** incorporated into simplified expected-loss analysis.

## 4. Exposure at Default (EAD)

EAD represents the credit exposure outstanding when default occurs.

**Project use:** used with PD and LGD to estimate expected loss.

## 5. Expected Loss

The simplified relationship used in the project is:

**Expected Loss = PD × LGD × EAD**

This connects the model's risk estimate to an economic loss measure for the hypothetical lending decision.

## 6. Leverage

Leverage measures the relationship between debt and operating earnings or capital.

The project uses **net leverage** in the direct-lending analysis to assess how much debt the hypothetical borrower carries relative to operating earnings.

**Project use:** facility sizing and covenant analysis.

## 7. Interest Coverage

Interest coverage measures the borrower's ability to meet interest expense from operating earnings.

The project's underwriting definition uses operating earnings relative to interest expense.

**Project use:** assessing debt-service capacity and setting covenant thresholds.

## 8. Covenants

Covenants are contractual requirements designed to protect lenders and provide early warning when borrower credit quality deteriorates.

**Project use:** the hypothetical deal translates leverage and coverage analysis into illustrative covenant thresholds.

## 9. Pricing / Interest-Rate Spread

Credit pricing compensates a lender for the cost of capital, credit risk and other deal considerations.

**Project use:** the model output is incorporated into an illustrative interest-rate spread / coupon framework rather than being treated as a standalone prediction.

## 10. Risk-Adjusted Yield

Risk-adjusted yield considers the economics of lending after incorporating an estimate of credit loss or other risk considerations.

**Project use:** connects expected credit risk with the hypothetical deal's return profile.

## 11. Stress Testing

Stress testing examines how underwriting metrics change when important assumptions deteriorate.

The project includes:

- **EBITDA stress** — tests the effect of weaker operating performance.
- **Interest-rate stress** — tests the effect of higher financing costs.

**Project use:** evaluates whether leverage, interest coverage and other deal metrics remain within the illustrative underwriting framework under adverse scenarios.

## 12. Financial Ratio Analysis

The historical model uses ratios covering:

- Profitability
- Leverage and solvency
- Liquidity
- Interest coverage
- Efficiency
- Margins
- Capital structure

Examples include Net Profit / Total Assets, Total Liabilities / Total Assets, Working Capital / Total Assets, Current Assets / Short-Term Liabilities, EBIT / Total Assets, Equity / Total Liabilities, Sales / Total Assets, Operating Profit / Interest Expense, and Long-Term Liabilities / Equity.

## How the concepts connect

```text
Financial Statements
        ↓
Financial Ratios
        ↓
Credit Risk Model
        ↓
PD / Risk Estimate
        ↓
LGD + EAD
        ↓
Expected Loss
        ↓
Leverage + Interest Coverage
        ↓
Facility Size + Pricing + Covenants
        ↓
Stress Testing
        ↓
Credit Underwriting Decision
```
