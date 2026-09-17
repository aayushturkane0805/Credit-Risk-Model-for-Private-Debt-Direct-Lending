# Limitations and Interpretation

This document describes the main limitations of the project and how its outputs should be interpreted.

## 1. Historical target is bankruptcy

The historical training dataset uses bankruptcy as the outcome. Bankruptcy and contractual default are related but different events.

Therefore, the model output should be described as a **model-implied research estimate related to historical bankruptcy / credit distress**, not as a production-calibrated private-credit probability of default.

## 2. Different populations and time periods

The historical training population and the public-company population used for the borrower-scoring layer are different populations and time periods.

This means the model is being applied as an analytical research exercise rather than as a formally validated production model for today's private-credit market.

## 3. Public-company data is not private-company underwriting data

The borrower-scoring layer is based on public-company financial information and SEC/XBRL data. A real direct-lending process would normally include much more information, including detailed debt schedules, cash-flow forecasts, liquidity sources, management information and transaction-specific documentation.

## 4. Illustrative underwriting assumptions

The direct-lending layer uses hypothetical assumptions for items such as LGD, EAD, facility sizing, pricing and covenant thresholds.

These assumptions demonstrate how quantitative credit analysis can feed into a lending framework; they are not recommendations for an actual transaction.

## 5. No full recovery analysis

A real LGD analysis would require a detailed assessment of collateral, enterprise value, capital structure, seniority, guarantees, documentation and potential recovery proceeds.

The project's expected-loss calculation is therefore simplified.

## 6. Model calibration

Good discrimination does not automatically mean that predicted probabilities are accurately calibrated to real-world default frequencies.

A production credit model would require appropriate calibration, monitoring, validation and governance using a relevant target population and time period.

## 7. Limited underwriting context

The quantitative model does not replace qualitative credit work such as:

- Management assessment
- Industry and competitive analysis
- Business-model assessment
- Customer / supplier concentration
- Legal documentation review
- Collateral analysis
- Sponsor assessment
- Liquidity and refinancing analysis
- Detailed cash-flow forecasting

## 8. Stress-test scope

The project includes EBITDA and interest-rate stress scenarios. Real underwriting would typically test a broader range of downside cases, including revenue decline, margin compression, working-capital pressure, refinancing risk and liquidity events.

## 9. Educational / research purpose

The project is intended to demonstrate an end-to-end quantitative credit-risk and direct-lending workflow. It should not be used by itself to make an actual lending, investment or credit decision.

## Practical interpretation

The strongest way to interpret the project is as a demonstration of **how financial data and quantitative models can be connected to credit underwriting decisions**.

The value of the project is the workflow:

**financial statements → ratios → model → risk estimate → expected loss → leverage / coverage → pricing / facility sizing → covenants → stress testing → credit memo.**
