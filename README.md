# Capstone_DA_Web-Scraping
Capstone Project Data Analytic Algoritma: Web Scraping
This project was developed as one of the capstone projects of the Algorithm Academy in the _Data Analytics_ specialty. The expected deliverables from this project are doing simple web scraping to get information. I will also use a simple Flask dashboard to display _scrap_ results and visualizations.

# Case Study: US Dollar to Rupiah exchange rate (https://www.exchange-rates.org/exchange-rate-history/usd-idr)

## Background
The exchange rate between the US Dollar (USD) and the Indonesian Rupiah (IDR) is a critical economic indicator that affects various sectors of Indonesia's economy, including import-export trade, foreign investment inflows, and the overall economic stability of the country. Fluctuations in this exchange rate can significantly impact businesses and investors who engage in international transactions.

Given the importance of the USD to IDR exchange rate, **How do fluctuations in the USD to IDR exchange rate impact financial forecasting and decision-making for businesses involved in international trade with Indonesia?** Understanding these dynamics is crucial for financial planners, investors, and business leaders who rely on accurate predictions of currency movements to mitigate risks and maximize returns.

Web scraping is required because historical exchange rate data is typically not available in a ready-to-use format for analysis. By scraping this data from financial websites that track and record daily exchange rates, we can obtain a comprehensive dataset that allows for a detailed time-series analysis.

The web scraping will provide:
- Daily USD to IDR exchange rates over a specified historical period.
- Dates corresponding to each exchange rate, allowing for time-series analysis.

This data will be used to:
- Plot the historical trends of the exchange rate.
- Identify any patterns, anomalies, or significant fluctuations in the exchange rate.
- Calculate statistical metrics that can help in forecasting future rates.
- Business Implications of the Results

The results from this analysis can be used by businesses and investors to:
- Enhance financial planning by understanding the trends and patterns in exchange rate fluctuations.
- Improve risk management strategies by identifying potential periods of high volatility.
- Make informed decisions regarding timing for currency exchange, investments, or pricing of products and services in international markets.

By leveraging the insights gained from the historical data analysis, businesses can position themselves more favorably in the international market, optimizing their operations in response to currency trends.

# Dependencies

- beautifulsoup4==4.12.3
- Flask==3.0.2
- Jinja2==3.1.3
- Werkzeug==3.0.1
- pandas==2.2.1

Or you can install the packages using `requirements.txt` by running the following command:

```python
pip install -r requirements. txt
```

### Implementing my webscrapping to the flask dashboard

- Copy paste all of your web scrapping process to the desired position on the `app.py`
- Change the title of the dashboard in `index.html`

## Analysis
The chart shows the USD to IDR exchange rate over approximately a six-month period from November 2023 to April 2024. The following observations and analysis can be drawn from the trend in the chart:

- Overall Upward Trend: There is a clear upward trend in the exchange rate, indicating a depreciation of the IDR against the USD over the observed period. This trend could be indicative of a wider economic trend, such as inflation within Indonesia or strengthening of the USD in global markets.
- Volatility: There are periods of increased volatility, notably at the start of the period (around November 2023) and towards the end (around April 2024). Such volatility can be a concern for businesses that rely on stable exchange rates for cost planning and pricing strategies.
- Sharp Increases: Particularly in April 2024, there's a sharp increase in the exchange rate. Such movements may be attributed to economic events or policy changes and can significantly impact businesses with exposure to IDR.

## Conclusion
- Financial Planning: Businesses engaged in trade with Indonesia need to account for a possible continued depreciation of the IDR. Long-term contracts priced in USD may become more costly for Indonesian partners, and this should be factored into any new agreements or financial forecasts.
- Risk Management: The observed volatility underscores the need for robust risk management strategies. Businesses might consider hedging techniques such as forward contracts to mitigate the risk posed by fluctuations in the exchange rate.
- Decision-Making: For companies involved in import-export with Indonesia, this data suggests a careful review of pricing and cost strategies. Importers in Indonesia might find their costs rising and may need to adjust prices accordingly. Exporters to Indonesia might experience increased demand as their products become relatively cheaper for Indonesian buyers.
- Market Opportunities: Investors may see opportunities in market movements like this. For instance, a strengthening USD could attract foreign investment into Indonesian assets, assuming investors expect the IDR to stabilize or appreciate in the future.
- Operational Adjustments: Companies might also need to adjust operations, possibly sourcing more goods locally within Indonesia to avoid currency risk or diversifying the currency exposure in their financial operations.

In light of this analysis, it is advisable for stakeholders to stay informed of macroeconomic indicators and to remain agile, adjusting financial strategies to the dynamic currency landscape. Business leaders should closely monitor not just the exchange rates but also the underlying factors that could be influencing these trends, such as Indonesia's central bank policies, inflation rates, and global economic conditions.
