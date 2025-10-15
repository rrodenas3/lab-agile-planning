# lab-agile-planning

This repository now includes a small utility for recreating the publication-ready
artefacts referenced in the governance report.

## Generating the figures

Create a virtual environment with Matplotlib available (e.g. `pip install
matplotlib`) and then execute:

```bash
python generate_figures.py
```

The script exports both PNG (300 DPI) and PDF versions of:

* **Figure 1** – Hybrid Governance Stack with Dimensional Oversight
* **Table 1** – Governance Framework Comparison

The resulting files are saved in the repository root:

* `figure1_governance_stack.png`
* `figure1_governance_stack.pdf`
* `table1_framework_comparison.png`
* `table1_framework_comparison.pdf`

These assets match the specifications for submission (grayscale-friendly, print
ready) outlined in the accompanying analysis.
