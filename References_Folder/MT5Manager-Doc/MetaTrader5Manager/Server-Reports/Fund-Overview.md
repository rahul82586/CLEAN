[🏠 Document Start](../README.md) / [Server Reports](README.md) / Fund Overview

[Previous](EMIR.md) | [Next](Risk-Appetite.md)

# Fund Overview

If you are using the MetaTrader 5 platform for the operation of an investment fund, this report will show the key fund performance characteristics, including Assets Under Management and Net Asset Value, as well as information about fund investors and managers.

![The "Fund Overview" report](images/fund_overview_report.png)

## Filters

Data requested for the report can be filtered. Specify the following parameters before requesting a report in the manager terminal:

  * Period — starting and ending date of the period, for which the report will be generated.



## Data in the report

The report provides the following information:

  * Fund Value — Asset Under Management (AUM).
  * Shareholders — the number of the fund shareholders.
  * Fund value (diagram) — Net Asset Value (NAV) dynamics.
  * Trading Accounts Value — current balance and equity on the accounts of fund managers.
  * Investors Volume — the share of each shareholder. The size of the corresponding position (in lots) for the fund symbol is displayed on each shareholder's account.



## Setup in MetaTrader 5 Administrator

The following parameters can be specified in the report configuration in MetaTrader 5 Administrator:

  * Fund name — the name of the fund for which the report is generated. The name can be obtained from the appropriate section of MetaTrader 5 Administrator settings.
  * Currency — the currency in which the amounts are displayed in the report. Conversion to the specified currency is performed in accordance with the current quotes in the platform. For example, EURUSD quotes are used to convert an amount in EUR to USD.


