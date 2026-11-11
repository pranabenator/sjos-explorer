"""
Systemic Denial of Justice (SDoJ) — Interactive Mathematical Explorer (v3.1)

Author identity withheld for double-blind peer review.
Companion dashboard for: Systemic Denial of Justice: A Mathematical Theory
of Institutional Executability and the Rule-of-Law Tax in Digital Governance.

The manuscript reframes the Governance Executability Framework's original
"Systemic Denial of Service" (SDoS) failure class as "Systemic Denial of
Justice" (SDoJ); the underlying mathematical model is unchanged.

Run locally:      streamlit run app_3.py
"""

from __future__ import annotations

import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

# ---------------------------------------------------------------------------
# Page configuration & theme styling
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="SDoJ Theory — Interactive Explorer",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------------------------
# Header and research context (anonymised for double-blind review)
# ---------------------------------------------------------------------------
st.title("Systemic Denial of Justice (SDoJ)")
st.caption(
    "Interactive Mathematical Explorer & Governance Simulator — "
    "Companion to *Systemic Denial of Justice: "
    "A Mathematical Theory of Institutional Executability and the Rule-of-Law Tax in Digital Governance*. "
    "Reframed from the Governance Executability Framework's *Systemic Denial of Service* (SDoS) failure class."
)

with st.sidebar:
    st.subheader("Research Context")
    st.markdown("**Focus:** Digital Governance & Institutional Systems")
    st.markdown("Author identity withheld for double-blind review.")
    st.divider()
    st.subheader("Dashboard Navigation")
    st.markdown(
        "- **Tab 1:** Constraint Saturation (Theorem 4.3)\n"
        "- **Tab 2:** Residual Viability (Theorems 4.6 & 4.7)\n"
        "- **Tab 3:** Defect Recursion (Theorem 4.10)\n"
        "- **Tab 4:** Observability Window (Theorems 4.9 & 4.13)\n"
        "- **Tab 5:** Rule-of-Law Tax (Definition 3.11)"
    )
    st.info("No personal or case data is used. Models closed mathematical forms only.")

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    [
        "1. Constraint Saturation",
        "2. Residual Viability",
        "3. Defect Recursion",
        "4. Observability & Recovery",
        "5. Rule-of-Law Tax",
    ]
)

# ---------------------------------------------------------------------------
# Tab 1 — Constraint Saturation (Theorem 4.3)
# ---------------------------------------------------------------------------
with tab1:
    st.header("Constraint Saturation Threshold (Theorem 4.3)")
    st.markdown(
        "**Scenario:** A litigant faces accumulating filing requirements. Individually reasonable "
        "procedural constraints ($m$) conjunctively eliminate all feasible paths, creating a 'valid but immobile' state."
    )
    
    col1, col2 = st.columns([1, 2])
    with col1:
        N = st.slider(
            "Candidate Paths (N)", 5, 100, 40, 5,
            help="Total alternative routes or legal strategies available to reach disposition."
        )
        phi = st.slider(
            "Constraint Failure Rate (φ)", 0.01, 0.50, 0.15, 0.01,
            help="Probability that a single requirement blocks a given path due to validation errors."
        )
        m_max = st.slider(
            "Max Constraints Evaluated (m)", 5, 50, 30,
            help="Number of cumulative procedural rules along the gateway."
        )

    with col2:
        m_vals = np.arange(0, m_max + 1)
        q = 1.0 - phi
        prob_survival = 1.0 - (1.0 - q ** m_vals) ** N
        
        color_zone = ["Green (Safe)" if p >= 0.7 else "Yellow (Warning)" if p >= 0.3 else "Red (Saturated)" for p in prob_survival]
        df1 = pd.DataFrame({"m": m_vals, "P(feasible path)": prob_survival, "Zone": color_zone})
        
        current_p = prob_survival[-1]
        if current_p >= 0.7:
            st.success(f"🟢 **SAFE ZONE (P = {current_p:.2f}):** Feasible paths survive. System has operational bandwidth.")
        elif current_p >= 0.3:
            st.warning(f"🟡 **WARNING ZONE (P = {current_p:.2f}):** System approaching saturation threshold (m*). Path availability fragile.")
        else:
            st.error(f"🔴 **CRITICAL SATURATION (P = {current_p:.2f}):** Constraint saturation reached. Process is valid but operationally non-executable.")
        
        chart1 = alt.Chart(df1).mark_line(strokeWidth=3).encode(
            x=alt.X("m:Q", title="Number of Constraints (m)"),
            y=alt.Y("P(feasible path):Q", title="P(Feasible Path Exists)", scale=alt.Scale(domain=[0, 1])),
            color=alt.Color("Zone:N", scale=alt.Scale(domain=["Green (Safe)", "Yellow (Warning)", "Red (Saturated)"], range=["#2ca02c", "#ff7f0e", "#d62728"])),
            tooltip=["m", "P(feasible path)", "Zone"]
        ).properties(height=320)
        
        st.altair_chart(chart1, use_container_width=True)

# ---------------------------------------------------------------------------
# Tab 2 — Residual Viability (Theorems 4.6 & 4.7)
# ---------------------------------------------------------------------------
with tab2:
    st.header("Residual Viability & Heavy-Tailed Latency (Theorems 4.6 & 4.7)")
    st.markdown(
        "**Scenario:** Delay is an active executioner of rights. As elapsed latency ($l$) consumes the deadline ($T$), "
        "residual viability $R(l)$ falls to zero, destroying relief."
    )
    
    col1, col2 = st.columns([1, 2])
    with col1:
        alpha = st.slider(
            "Tail Index (α, Pareto Heavy-Tail)", 0.1, 3.0, 1.5, 0.1,
            help="Controls severity of heavy-tailed latency bottlenecks (α < 1 indicates severe long-tail delay)."
        )
        k_exp = st.slider(
            "Exponential Decay Rate (k)", 0.5, 5.0, 3.0, 0.5,
            help="Baseline exponential decay rate of remedy viability over time."
        )

    with col2:
        l_ratio = np.linspace(0.0, 0.999, 200)
        r_heavy = 1.0 - l_ratio ** alpha
        r_exp = (np.exp(-k_exp * l_ratio) - np.exp(-k_exp)) / (1.0 - np.exp(-k_exp))
        
        df2 = pd.DataFrame(
            {
                "Elapsed Fraction (l/T)": l_ratio,
                "Heavy-Tailed (Pareto)": r_heavy,
                "Exponential": r_exp,
            }
        ).melt("Elapsed Fraction (l/T)", var_name="Regime", value_name="Viability R(l)")
        
        latest_r_heavy = r_heavy[int(len(r_heavy)*0.75)]
        if latest_r_heavy >= 0.6:
            st.success(f"🟢 **HIGH VIABILITY:** At 75% elapsed time, residual viability is {latest_r_heavy:.2f}.")
        elif latest_r_heavy >= 0.25:
            st.warning(f"🟡 **DEGRADED VIABILITY:** At 75% elapsed time, viability drops to {latest_r_heavy:.2f}. Remedy at risk.")
        else:
            st.error(f"🔴 **EXPIRED REMEDY:** At 75% elapsed time, viability plunged to {latest_r_heavy:.2f}. Delay has consumed the right.")

        chart2 = alt.Chart(df2).mark_line(strokeWidth=2.5).encode(
            x=alt.X("Elapsed Fraction (l/T):Q", title="Elapsed Fraction of Deadline (l/T)"),
            y=alt.Y("Viability R(l):Q", title="Residual Viability R(l)", scale=alt.Scale(domain=[0, 1])),
            color=alt.Color("Regime:N", scale=alt.Scale(range=["#1f77b4", "#d62728"])),
            tooltip=["Regime", "Elapsed Fraction (l/T)", "Viability R(l)"]
        ).properties(height=320)
        
        st.altair_chart(chart2, use_container_width=True)

# ---------------------------------------------------------------------------
# Tab 3 — Defect Recursion (Theorem 4.10)
# ---------------------------------------------------------------------------
with tab3:
    st.header("The Defect Recursion Engine (Theorem 4.10)")
    st.markdown(
        "**Scenario:** Compliance begets new defects. When the recursion rate $\\nu \\ge 1.0$, compliance fails "
        "to clear defects, locking the filing in an infinite obstruction cycle."
    )
    
    col1, col2 = st.columns([1, 2])
    with col1:
        nu = st.slider(
            "Recursion Rate (ν)", 0.2, 2.0, 1.1, 0.1,
            help="Defect regeneration multiplier per cycle. ν ≥ 1.0 means compliance generates more defects than it cures."
        )
        b = st.number_input(
            "Exogenous Defect Inflow (b)", min_value=0.0, value=1.0, step=0.5,
            help="New administrative errors injected per compliance iteration."
        )
        cycles = st.slider(
            "Procedural Cycles (n)", 1, 20, 10,
            help="Number of compliance attempts made by the litigant."
        )

    with col2:
        u = np.zeros(cycles + 1)
        u[0] = 1.0
        for n in range(cycles):
            u[n + 1] = nu * u[n] + b
        
        df3 = pd.DataFrame({"Cycle (n)": np.arange(cycles + 1), "Defect Load (u_n)": u})
        
        if nu < 1.0:
            fixed_point = b / (1.0 - nu)
            st.success(f"🟢 **STABLE RECURSION (ν = {nu:.1f} < 1.0):** Defect load clears to a bounded fixed point ({fixed_point:.1f}).")
        elif nu == 1.0:
            st.warning(f"🟡 **LINEAR ACCUMULATION (ν = 1.0):** Defect load grows linearly with every compliance cycle.")
        else:
            st.error(f"🔴 **SELF-SUSTAINING RECURSION (ν = {nu:.1f} ≥ 1.0):** Defect load explodes geometrically. Compliance cannot clear the docket.")

        chart3 = alt.Chart(df3).mark_bar().encode(
            x=alt.X("Cycle (n):O", title="Compliance Cycle (n)"),
            y=alt.Y("Defect Load (u_n):Q", title="Accumulated Defect Load (u_n)"),
            color=alt.value("#d62728" if nu >= 1.0 else "#2ca02c"),
            tooltip=["Cycle (n)", "Defect Load (u_n)"]
        ).properties(height=320)
        
        st.altair_chart(chart3, use_container_width=True)

# ---------------------------------------------------------------------------
# Tab 4 — Observability & Recovery (Theorems 4.9 & 4.13)
# ---------------------------------------------------------------------------
with tab4:
    st.header("Observability Detection Window (Theorems 4.9 & 4.13)")
    st.markdown(
        "**Scenario:** Opaque status displays delay stall detection ($\delta$). Past the detection window ($W$), "
        "corrective efficacy $\kappa(\delta)$ vanishes, trapping the flow in an absorbing failure state."
    )
    
    col1, col2 = st.columns([1, 2])
    with col1:
        W = st.slider(
            "Detection Window Boundary (W)", 5, 30, 14,
            help="Maximum elapsed days before a stalled flow becomes unrecoverable."
        )
        beta = st.slider(
            "Observability Recovery Rate (β)", 0.01, 0.5, 0.10, 0.01,
            help="Speed at which status notifications reach the participant."
        )

    with col2:
        delta = np.linspace(0, 40, 200)
        kappa = np.where(delta < W, np.exp(-beta * delta), 0.0)
        
        df4 = pd.DataFrame({"Detection Latency (δ)": delta, "Recovery Efficacy κ(δ)": kappa})
        
        st.info(f"💡 **WINDOW STATUS:** Stalls detected after **W = {W} days** enter an absorbing failure state ($\kappa = 0$).")

        chart4 = alt.Chart(df4).mark_area(opacity=0.7).encode(
            x=alt.X("Detection Latency (δ):Q", title="Detection Latency (δ in days)"),
            y=alt.Y("Recovery Efficacy κ(δ):Q", title="Corrective Efficacy κ(δ)", scale=alt.Scale(domain=[0, 1])),
            color=alt.value("#008080"),
            tooltip=["Detection Latency (δ)", "Recovery Efficacy κ(δ)"]
        ).properties(height=320)
        
        st.altair_chart(chart4, use_container_width=True)

# ---------------------------------------------------------------------------
# Tab 5 — Rule-of-Law Tax (Definition 3.11)
# ---------------------------------------------------------------------------
with tab5:
    st.header("Aggregate Rule-of-Law Tax Ledger (Definition 3.11)")
    st.markdown(
        "**Scenario:** Quantifying the total cost ($\mathcal{T}(f)$) imposed on citizens by digital non-executability: "
        "direct compliance effort, latency loss, and legitimacy decay ($\lambda_l$)."
    )
    
    col1, col2 = st.columns([1, 2])
    with col1:
        effort = st.slider("Compliance Effort (Hours)", 1, 100, 25, help="Hours spent re-filing or seeking support.")
        latency_days = st.slider("Days Delayed", 1, 365, 120, help="Total calendar days lost in administrative limbo.")
        legitimacy_weight = st.slider("Legitimacy Decay Penalty (λ_l)", 100, 5000, 1500, help="Weighting parameter for institutional trust erosion.")
        executability = st.slider("System Executability Capacity E_T(f)", 0.0, 1.0, 0.2, help="Probability of successful completion before deadline.")

    with col2:
        c_c = 50.0
        cost_compliance = effort * c_c
        cost_latency = latency_days * 10.0
        cost_legitimacy = legitimacy_weight * (1.0 - executability)
        total_tax = cost_compliance + cost_latency + cost_legitimacy

        if executability >= 0.7:
            st.success(f"🟢 **LOW SYSTEMIC TAX:** Total Tax = ${total_tax:,.2f}. High executability preserves trust.")
        elif executability >= 0.3:
            st.warning(f"🟡 **MODERATE TAX:** Total Tax = ${total_tax:,.2f}. Significant latency and compliance burden.")
        else:
            st.error(f"🔴 **SEVERE LEGITIMACY DEFICIT:** Total Tax = ${total_tax:,.2f}. System absorbs full legitimacy penalty.")

        df5 = pd.DataFrame(
            {
                "Component": ["Compliance Effort", "Latency Loss", "Legitimacy Deficit"],
                "Cost": [cost_compliance, cost_latency, cost_legitimacy],
            }
        )
        
        chart5 = alt.Chart(df5).mark_bar().encode(
            x=alt.X("Component:N", sort=None, title="Tax Component"),
            y=alt.Y("Cost:Q", title="Cost Burden ($)"),
            color=alt.Color("Component:N", scale=alt.Scale(domain=["Compliance Effort", "Latency Loss", "Legitimacy Deficit"], range=["#2ca02c", "#ff7f0e", "#d62728"])),
            tooltip=["Component", "Cost"]
        ).properties(height=300)
        
        st.altair_chart(chart5, use_container_width=True)

st.divider()
st.caption("Companion interactive application for SDoJ Theory research. Author identity withheld for double-blind review.")