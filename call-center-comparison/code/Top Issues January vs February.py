import pandas as pd

jan = pd.read_csv("c:\\call-center-comparison\\data\\Call Log - 2026 - January.csv")
feb = pd.read_csv("c:\\call-center-comparison\\data\\Call Log - 2026 - February.csv")


#Adding a month column

jan["Month"] = "January"
feb["Month"] = "February"


#Combine datasets

df=pd.concat([jan, feb])


#compare top issues for each month


monthly_issues = df.groupby(["Month", "Reason"]).size().reset_index(name="Count")

jan_top = monthly_issues[monthly_issues["Month"] == "January"].sort_values("Count", ascending=False).head(5)
feb_top = monthly_issues[monthly_issues["Month"] == "February"].sort_values("Count", ascending=False).head(5)



# Build a graph

import matplotlib.pyplot as plt

jan_top.plot(kind="bar",
                x="Reason",
                color=["blue"],
                title="Top 5 Call Reasons January",
                ylabel="Count",
                figsize=(10,6))

plt.legend().remove()# hides the color legend

feb_top.plot(kind="bar",
                x="Reason",
                color=["red"],
                title="Top 5 Call Reasons February",
                ylabel="Count",
                figsize=(10,6))

plt.legend().remove()
plt.show()


#Interpretation

"""3rd party billing and installation assistance are the only two call reasons which
carried over from the previous month. The amount of installation assistance-related
calls increased, suggesting that more resources should be allocated on the user-end
to assist customers with installation, or that the installation process itself be
simplified."""
