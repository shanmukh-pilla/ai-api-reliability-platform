# dashboard/app.py

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="AI API Reliability Platform",
    layout="wide"
)

st.title("🤖 AI API Reliability Platform")

st.markdown("Enterprise API Monitoring & Quality Engineering Dashboard")

# ---------------------------------------------------
# KPI Metrics
# ---------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

col1.metric("APIs Monitored", "4")
col2.metric("Tests Passed", "48")
col3.metric("Failures", "2")
col4.metric("Coverage", "92%")

st.divider()

# ---------------------------------------------------
# API Health Table
# ---------------------------------------------------

st.subheader("📊 API Health Status")

api_data = pd.DataFrame({
    "API": ["Users API", "Payments API", "Orders API", "Auth API"],
    "Status": ["Healthy", "Healthy", "Warning", "Healthy"],
    "Response Time (ms)": [120, 180, 850, 95]
})

st.dataframe(api_data, use_container_width=True)

# ---------------------------------------------------
# Performance Chart
# ---------------------------------------------------

st.subheader("⚡ API Performance Monitoring")

fig = px.bar(
    api_data,
    x="API",
    y="Response Time (ms)",
    color="Status",
    title="API Response Time Analysis"
)

st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------
# Quality Gates
# ---------------------------------------------------

st.subheader("🛡 Quality Gates")

st.success("✅ Coverage Threshold Passed")
st.info("Coverage: 92%")
st.info("CI/CD Pipeline Status: SUCCESS")

# ---------------------------------------------------
# AI Alerts
# ---------------------------------------------------

st.subheader("🚨 AI Reliability Alerts")

st.warning("⚠️ Orders API latency increased above threshold")
st.warning("⚠️ Potential flaky behavior detected in API tests")

# ---------------------------------------------------
# Footer
# ---------------------------------------------------

st.divider()

st.caption("Built using Python, Pytest, GitHub Actions, Docker & Streamlit")