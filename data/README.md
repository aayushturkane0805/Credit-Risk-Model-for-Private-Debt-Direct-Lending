# Data

The project uses the UCI(University of California, Irvine) Polish Companies Bankruptcy dataset for historical model training and SEC/XBRL financial data for the public-company borrower layer.

Raw datasets are intentionally not committed to this repository. The notebook downloads the historical dataset at runtime and retrieves public-company data through SEC endpoints when available.

The model-implied PD outputs should be treated as research estimates because the historical bankruptcy training population and current public-company population are not identical.
