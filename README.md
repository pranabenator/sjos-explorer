# sdos-explorer

Interactive mathematical explorer for the **Systemic Denial of Justice (SDoJ)** framework — the legal reframing of the Governance Executability Framework's *Systemic Denial of Service* (SDoS) failure class.

The repository and folder name `sdos-explorer` are retained for continuity with the original release. The application, manuscript, and documentation use **SDoJ** as the operative term; the underlying mathematical model and theorems are unchanged.

## What it does

A five-tab Streamlit dashboard that visualises the closed-form results of the companion manuscript:

1. **Constraint saturation** — the threshold beyond which conjunctive procedural requirements eliminate every feasible path.
2. **Residual viability** — how elapsed latency consumes the deadline under heavy-tailed and exponential completion times.
3. **Defect recursion** — the recursion rate at which compliance regenerates defects instead of clearing them.
4. **Observability and recovery** — the detection window beyond which a stalled flow becomes absorbing.
5. **Rule-of-law tax** — the compliance, latency, and legitimacy costs of non-executable procedure.

All values are generated from the analytical expressions in the manuscript. The application uses no personal or case data.

## Run locally

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
# source .venv/bin/activate

pip install -r requirements.txt
streamlit run app_3.py
```

The app opens at `http://localhost:8501`.

## Deploy

On Streamlit Community Cloud, point the deployment at `app_3.py` and keep `requirements.txt` at the repository root.

## Terminology

The Governance Executability Framework introduced the failure class as **Systemic Denial of Service (SDoS)** to emphasise its systems-theoretic structure. The manuscript adopts **Systemic Denial of Justice (SDoJ)** for the same structural condition when it operates through an adjudicatory or entitlement-bearing gateway, because the consequence is the denial of a remedy rather than merely the interruption of a service. See the manuscript's terminology note for the full rationale.

## Companion manuscript

*Systemic Denial of Justice: A Mathematical Theory of Institutional Executability and the Rule-of-Law Tax in Digital Governance.*

## Attribution

Author identity withheld for double-blind peer review. Attribution will be restored in the published version.
