def generate_insights(df, monthly_df):

    worst_month = monthly_df.sort_values("margin_loss", ascending=False).iloc[0]
    worst_customer = df.groupby("customer_id")["margin_loss"].sum().idxmax()

    summary = f"""
📊 Margin Intelligence Report

🔴 Highest Loss Month: {worst_month['month']}
   Margin Loss: {round(worst_month['margin_loss'],2)}

👤 Most Impacted Customer: {worst_customer}

📉 Key Trends:
- Margin erosion is driven by increasing PPV
- Higher tariff exposure leads to declining profitability

💡 Recommendations:
- Reprice contracts for high PPV customers
- Diversify sourcing to reduce cost volatility
- Monitor quarterly margin trends closely
"""

    return summary
