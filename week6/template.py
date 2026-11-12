"""
RECORD CHECK  -  my version
===========================

Name  :  Mugabo Gloire Salvy
Lane  :  Cyber
Date  :  11/11/2026

Run it:   python template.py
"""

import pandas as pd
import matplotlib.pyplot as plt

# ==================================================================== LOAD
df = pd.read_csv("records_sample.csv")


# ================================================================= PROCESS
df["percent"] = (df["value"] / df["limit"]) * 100
df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else ("WARNING" if p >= 90 else "OK")
)


# ================================================================== OUTPUT
print(df)
print(df[df["status"] != "OK"])
counts = df.groupby("status")["label"].count()
print(counts)
df.to_csv("records_report.csv", index=False)
counts.plot(kind="bar")
plt.title("Records per status")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("status_chart.png")


# ==========================================================================
# 4. Before you finish:
#    [x] Run it and check the percent/status columns by hand for one row
#    [x] Check you used & (not "and") if you combined more than one condition
#    [x] Check every column your code refers to actually exists - watch case
