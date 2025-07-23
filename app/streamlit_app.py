import streamlit as st
import pandas as pd
from audit.ec2_audit import get_ec2_report

st.title("AWS EC2 Optimization Report")

with st.spinner("Collecting data..."):
    report = get_ec2_report()
    df = pd.DataFrame(report)

if df.empty:
    st.warning("No data found or no running instances.")
else:
    st.dataframe(df)

    low_cpu = df[df["avg_cpu"] < 10]
    if not low_cpu.empty:
        st.subheader("Underutilized Instances")
        st.dataframe(low_cpu)