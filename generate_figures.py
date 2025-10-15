"""Generate publication-ready governance figures and tables.

This script produces Figure 1 and Table 1 described in the report:

* Figure 1: Hybrid Governance Stack with Dimensional Oversight
* Table 1: Governance Framework Comparison

Both artefacts are exported as PNG (300 DPI) and PDF versions.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


# Configure Matplotlib for publication-style output
plt.rcParams.update(
    {
        "font.family": "sans-serif",
        "font.size": 10,
        "axes.linewidth": 1.5,
    }
)


def build_hybrid_governance_stack() -> None:
    """Create Figure 1 showing the hybrid governance stack."""

    fig, ax = plt.subplots(figsize=(10, 8), dpi=150)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")

    layer_height = 2.2
    layer_y_positions = [6.8, 4.3, 1.8]
    layer_width = 6.5
    layer_x_start = 0.5

    layers = [
        {
            "title": "COMPETENCE LAYER",
            "content": [
                "• Verification Literacy (evaluate AI outputs)",
                "• Choice Architecture Charter (option construction)",
                "• Decision-Rights Register (approval authority)",
                "• Assurance Case (structured safety argument)",
            ],
            "y": layer_y_positions[0],
        },
        {
            "title": "PROCESS LAYER",
            "content": [
                "• ISO 42001 (Plan-Do-Check-Act certification)",
                "• NIST AI RMF (Govern-Map-Measure-Manage)",
                "• Continuous Auditing (real-time monitoring)",
                "• Adaptive Risk Assessment (dynamic recalibration)",
            ],
            "y": layer_y_positions[1],
        },
        {
            "title": "DESIGN LAYER",
            "content": [
                "• SAGA (cryptographic tokens, Agent Cards)",
                "• ACE (context evolution, Generator/Reflector/Curator)",
                "• DIRF (63 controls, 9 domains, provenance)",
                "• Identity/Signing (Kshetri: signatures, graphs)",
            ],
            "y": layer_y_positions[2],
        },
    ]

    for layer in layers:
        box = FancyBboxPatch(
            (layer_x_start, layer["y"] - layer_height),
            layer_width,
            layer_height,
            boxstyle="round,pad=0.05",
            edgecolor="black",
            facecolor="white",
            linewidth=2,
        )
        ax.add_patch(box)

        ax.text(
            layer_x_start + layer_width / 2,
            layer["y"] - 0.25,
            layer["title"],
            ha="center",
            va="top",
            fontsize=11,
            fontweight="bold",
        )

        for i, item in enumerate(layer["content"]):
            ax.text(
                layer_x_start + 0.2,
                layer["y"] - 0.7 - i * 0.38,
                item,
                ha="left",
                va="top",
                fontsize=9,
            )

    three_as_x = layer_x_start + layer_width + 0.8
    three_as_y = 5
    three_as_width = 2.2
    three_as_height = 3.5

    three_as_box = FancyBboxPatch(
        (three_as_x, three_as_y - three_as_height),
        three_as_width,
        three_as_height,
        boxstyle="round,pad=0.05",
        edgecolor="black",
        facecolor="white",
        linewidth=1.5,
        linestyle="--",
    )
    ax.add_patch(three_as_box)

    ax.text(
        three_as_x + three_as_width / 2,
        three_as_y - 0.2,
        "Dynamic\nRecalibration",
        ha="center",
        va="top",
        fontsize=9,
        fontweight="bold",
    )

    three_as_items = [
        "3As Thresholds:",
        "",
        "Autonomy",
        "(independence)",
        "",
        "Authority",
        "(decision rights)",
        "",
        "Accountability",
        "(liability)",
    ]

    y_offset = three_as_y - 0.9
    for item in three_as_items:
        if item == "":
            y_offset -= 0.15
            continue

        ax.text(
            three_as_x + three_as_width / 2,
            y_offset,
            item,
            ha="center",
            va="top",
            fontsize=9 if item == "3As Thresholds:" else 8,
            fontweight="bold"
            if item in {"Autonomy", "Authority", "Accountability", "3As Thresholds:"}
            else "normal",
        )
        y_offset -= 0.25

    arrows = [
        ((layer_x_start + layer_width + 0.1, 6), (three_as_x - 0.1, 5.5)),
        ((layer_x_start + layer_width + 0.1, 3.5), (three_as_x - 0.1, 2.5)),
    ]
    for start, end in arrows:
        arrow = FancyArrowPatch(start, end, arrowstyle="<->", linewidth=1.5, color="black")
        ax.add_patch(arrow)

    ax.text(
        5,
        9.5,
        "Figure 1: Hybrid Governance Stack with Dimensional Oversight",
        ha="center",
        va="top",
        fontsize=12,
        fontweight="bold",
    )

    caption_text = (
        "The Hybrid Governance Stack integrates three interdependent layers—Design (architectural controls),\n"
        "Process (lifecycle management), and Competence (professional capabilities)—with continuous recalibration\n"
        "hooks tracking dimensional shifts in autonomy, authority, and accountability (3As). This architecture\n"
        "embeds accountability-by-design while maintaining adaptive policy processes and feedback loops."
    )
    ax.text(
        5,
        0.3,
        caption_text,
        ha="center",
        va="top",
        fontsize=8,
        style="italic",
        wrap=True,
    )

    fig.tight_layout()
    fig.savefig("figure1_governance_stack.png", dpi=300, bbox_inches="tight", facecolor="white")
    fig.savefig("figure1_governance_stack.pdf", bbox_inches="tight", facecolor="white")
    plt.close(fig)


def build_governance_framework_table() -> None:
    """Create Table 1 comparing governance frameworks."""

    fig, ax = plt.subplots(figsize=(14, 10), dpi=150)
    ax.axis("tight")
    ax.axis("off")

    frameworks = [
        "SAGA",
        "ACE",
        "TRiSM",
        "ISO 42001",
        "NIST RMF",
        "DIRF",
        "Kshetri",
    ]
    mechanisms = [
        "Cryptographic tokens,\nAgent Cards,\nOne-Time Keys",
        "Dynamic context\nevolution via\nGenerator/Reflector/\nCurator",
        "Lifecycle metrics\n(Component Synergy\nScore, Tool\nUtilisation Efficacy)",
        "Plan-Do-Check-Act\ncertification,\nmanagement-system\nframework",
        "Four functions:\nGovern, Map,\nMeasure, Manage\n(GMMM)",
        "63 controls across\n9 domains for\nidentity clone\ngovernance",
        "Identity-centric\ngovernance via\ndigital signing,\nprovenance graphs",
    ]
    legal_fit = [
        "Strong\n(auditability via\nimmutable trails)",
        "Moderate\n(GDPR Art. 17\nselective\nunlearning)",
        "Strong\n(comprehensive\nlifecycle\ncoverage)",
        "Strong\n(comprehensive,\ninternationally\nrecognized)",
        "Moderate\n(voluntary\nframework, no\nenforcement)",
        "Strong\n(GDPR Art. 17\nright to erasure)",
        "Strong\n(attribution and\nprovenance\ntracking)",
    ]
    ethical_issues = [
        "Centralization risk,\nhonest-but-curious\nparadox",
        "Autonomous rule\nchanges without\nexplicit\nauthorization",
        "Metric gaming,\noptimizing proxy\nmeasures over\ngenuine outcomes",
        "Compliance\ntheatre,\nprocedural\nbox-ticking",
        "Voluntary adoption\nlimits\neffectiveness,\ncompliance gaps",
        "Consent\ncomplexity, user\nburden for\ngranular control",
        "Privacy vs.\ntraceability\ntension, data\nretention risks",
    ]
    pm_artefacts = [
        "Audit trails,\ncryptographic\nsignatures,\ncapability logs",
        "Living\ndocumentation,\nstructured delta\nrecords",
        "Risk registers,\nassurance cases,\nquantitative\nindicators",
        "Management\nsystems,\ncertification\ndocumentation",
        "Risk assessments,\nsocio-technical\nmappings",
        "Provenance logs,\nconsent\nmanagement,\ndeletion trails",
        "Decision trails,\nprovenance\ngraphs, signing\nmechanisms",
    ]
    known_gaps = [
        "Single-point-of-\nfailure risk,\nhierarchical\nre-creation",
        "Accountability for\nautonomous\ngovernance\nevolution",
        "Empirically\nuntested in\npost-deployment\ncontexts",
        "Low adoption\n(<7%), 12-24mo\ncertification,\nprocess overhead",
        "No enforcement\nmechanism, relies\non organizational\ncommitment",
        "Early stage\n(arXiv preprint),\nlimited field\nvalidation",
        "Integration\ncomplexity with\nexisting systems,\nperformance\noverhead",
    ]

    table_data = list(zip(frameworks, mechanisms, legal_fit, ethical_issues, pm_artefacts, known_gaps))
    col_labels = [
        "Framework",
        "Mechanism",
        "Legal Fit\n(Art.14/GDPR)",
        "Ethical Issues",
        "PM Artefacts",
        "Known Gaps",
    ]

    table = ax.table(
        cellText=table_data,
        colLabels=col_labels,
        cellLoc="left",
        loc="center",
        colWidths=[0.10, 0.18, 0.16, 0.18, 0.18, 0.20],
    )

    table.auto_set_font_size(False)
    table.set_fontsize(8)
    table.scale(1, 3.5)

    for col in range(len(col_labels)):
        cell = table[(0, col)]
        cell.set_facecolor("#E8E8E8")
        cell.set_text_props(weight="bold", fontsize=9)
        cell.set_edgecolor("black")
        cell.set_linewidth(2)

    for row in range(1, len(frameworks) + 1):
        for col in range(len(col_labels)):
            cell = table[(row, col)]
            cell.set_edgecolor("black")
            cell.set_linewidth(1)
            if col == 0:
                cell.set_text_props(weight="bold")
            if row % 2 == 0:
                cell.set_facecolor("#F5F5F5")

    fig.text(
        0.5,
        0.98,
        "Table 1: Governance Framework Comparison",
        ha="center",
        va="top",
        fontsize=12,
        fontweight="bold",
    )

    caption_text = (
        "Comparative analysis of governance frameworks for agentic AI systems across six dimensions: framework name, technical mechanism,\n"
        "legal compliance (EU AI Act Article 14, GDPR), ethical considerations, project management artefacts, and known limitations.\n"
        "Frameworks span governance-by-design approaches (SAGA, ACE, TRiSM, DIRF, Kshetri) and governance-by-policy approaches\n"
        "(ISO 42001, NIST RMF), revealing that no single framework addresses all accountability requirements comprehensively."
    )
    fig.text(
        0.5,
        0.02,
        caption_text,
        ha="center",
        va="bottom",
        fontsize=7,
        style="italic",
    )

    fig.savefig("table1_framework_comparison.png", dpi=300, bbox_inches="tight", facecolor="white")
    fig.savefig("table1_framework_comparison.pdf", bbox_inches="tight", facecolor="white")
    plt.close(fig)


def main() -> None:
    build_hybrid_governance_stack()
    build_governance_framework_table()
    print("Figures successfully created: figure1_governance_stack.(png|pdf), table1_framework_comparison.(png|pdf)")


if __name__ == "__main__":
    main()
