# ============================================================
# DOWNLOAD ONLY THE 2 REMAINING GITHUB FILES
# ============================================================

from pathlib import Path
import shutil
import zipfile
from google.colab import files

# ------------------------------------------------------------
# 1. Locate the existing project
# ------------------------------------------------------------

if "PROJECT_ROOT" in globals():
    project_root = Path(PROJECT_ROOT)
else:
    project_root = Path.cwd() / "credit-risk-direct-lending"

if not project_root.exists():
    raise FileNotFoundError(
        f"Project folder not found: {project_root}\n"
        "Please run the main credit-risk project cell first."
    )

# ------------------------------------------------------------
# 2. Create required GitHub folders
# ------------------------------------------------------------

src_dir = project_root / "src"
reports_dir = project_root / "reports"

src_dir.mkdir(parents=True, exist_ok=True)
reports_dir.mkdir(parents=True, exist_ok=True)

# ------------------------------------------------------------
# 3. Get the main project code from the executed Colab cell
# ------------------------------------------------------------

main_code = None

try:
    # Search executed IPython/Colab cells for the main project code
    ipython_inputs = get_ipython().user_ns.get("In", [])

    for cell_code in reversed(ipython_inputs):
        if (
            "CREDIT RISK MODEL FOR PRIVATE DEBT / DIRECT LENDING" in cell_code
            and "PROJECT_ROOT" in cell_code
            and "OUTPUT_DIR" in cell_code
        ):
            main_code = cell_code
            break

except Exception:
    pass

# Fallback: look for an ipynb file in /content
if main_code is None:
    import json

    notebook_candidates = list(Path("/content").rglob("*.ipynb"))

    for notebook_path in notebook_candidates:

        try:
            with open(notebook_path, "r", encoding="utf-8") as f:
                notebook = json.load(f)

            for cell in notebook.get("cells", []):

                cell_code = "".join(cell.get("source", []))

                if (
                    "CREDIT RISK MODEL FOR PRIVATE DEBT / DIRECT LENDING"
                    in cell_code
                    and "PROJECT_ROOT" in cell_code
                    and "OUTPUT_DIR" in cell_code
                ):
                    main_code = cell_code
                    break

            if main_code is not None:
                break

        except Exception:
            continue

if main_code is None:
    raise RuntimeError(
        "I could not find the main project code. "
        "Please run your main project cell once and then run this export cell again."
    )

# ------------------------------------------------------------
# 4. Create the source file
# ------------------------------------------------------------

src_file = src_dir / "credit_risk_model.py"

src_file.write_text(
    main_code,
    encoding="utf-8"
)

# ------------------------------------------------------------
# 5. Copy the existing credit memo into reports/
# ------------------------------------------------------------

possible_credit_memo_paths = [
    project_root / "outputs" / "credit_memo.xlsx",
    Path("/content/credit_memo.xlsx"),
]

credit_memo_source = None

for candidate in possible_credit_memo_paths:

    if candidate.exists():
        credit_memo_source = candidate
        break

if credit_memo_source is None:

    # Search project directory as a fallback
    matches = list(project_root.rglob("credit_memo.xlsx"))

    if matches:
        credit_memo_source = matches[0]

if credit_memo_source is None:
    raise FileNotFoundError(
        "credit_memo.xlsx could not be found."
    )

credit_memo_destination = reports_dir / "credit_memo.xlsx"

shutil.copy2(
    credit_memo_source,
    credit_memo_destination
)

# ------------------------------------------------------------
# 6. Create a ZIP containing ONLY the two remaining files
# ------------------------------------------------------------

zip_path = Path(
    "/content/Credit_Risk_Remaining_GitHub_Files.zip"
)

if zip_path.exists():
    zip_path.unlink()

with zipfile.ZipFile(
    zip_path,
    "w",
    zipfile.ZIP_DEFLATED
) as zipf:

    zipf.write(
        src_file,
        arcname="src/credit_risk_model.py"
    )

    zipf.write(
        credit_memo_destination,
        arcname="reports/credit_memo.xlsx"
    )

# ------------------------------------------------------------
# 7. Verify
# ------------------------------------------------------------

print("=" * 70)
print("REMAINING GITHUB FILES READY")
print("=" * 70)

print("\nFiles in ZIP:")

with zipfile.ZipFile(zip_path, "r") as zipf:

    for name in zipf.namelist():
        print(" -", name)

print("\nZIP:")
print(zip_path)

print("\nDownloading...")
files.download(str(zip_path))