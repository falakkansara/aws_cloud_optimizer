import streamlit as st
import pandas as pd


import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from audit import ec2_audit
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
     