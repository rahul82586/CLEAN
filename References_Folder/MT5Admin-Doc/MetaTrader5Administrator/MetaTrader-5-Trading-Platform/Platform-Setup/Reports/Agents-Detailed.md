[🏠 Document Start](../../../README.md) / [MetaTrader 5 Trading Platform](../../../MetaTrader-5-Trading-Platform.md) / [Platform Setup](../../Platform-Setup.md) / [Reports](../Reports.md) / Agents Detailed

[Previous](Agents.md) | [Next](Credit-Facility.md)

# Agents Detailed Report

Agents Detailed Report is a detailed report on agent commissions. The report reflects deals related to paying commissions [accumulated during a trading day/month (#charge)](../Groups/Commission-Settings.md#charge), as well as client deals, for which the agent received immediate commissions.

## Setup

The following parameters should be specified before requesting a report in the manager terminal:

  * Groups — the report will be generated on accounts listed in these groups.
  * Period — trades performed during this period will be requested for the report.



## Report

Information in the report is presented in blocks for each agent, containing a list of client deals and commission paying operations, as well as the total commission amount.

The following details are shows for deals, for which the client immediately received commission (immediate charge):

  * Deal — the ticket of the deal.
  * Account — the number of the account, at which the deal was performed.
  * Name — account holder's name.
  * Time — time of the deal. The record has a format of YYYY.MM.DD HH:MM (year.month.day hour:minute).
  * Position — the ticket of the position, to which the deal is related.
  * Symbol — the symbol, for which the deal was executed.
  * Volume — deal volume in lots.
  * Action — deal type: buying or selling.
  * Entry — deal direction: market entry (in), market exit (out), position reversal (in/out), closing by an opposite position (out by).
  * Price — the price at which the deal is executed.
  * Commission — [standard commission](../Groups/Commission-Settings.md) for the deal.
  * Group — the group the account belongs to.
  * Type — commission type: instant agent commission, daily agent commission, monthly agent commission.
  * Agents Commission — amount of calculated commission which the agent received for the deal.
  * Currency — commission currency.



The following data is provided for deals related to agent commissions accumulated during a day/month:

  * Account — the number of the account, for which the commission on deals was accumulated.
  * Name — account holder's name.
  * Time — commission charging time. The record has a format of YYYY.MM.DD HH:MM (year.month.day hour:minute).
  * Type — commission type: instant agent commission, daily agent commission, monthly agent commission.
  * Agents Commission — amount of calculated commission to be transferred to the agent.
  * Currency — commission currency.



Information about the agent is given below each block. It includes the agent's login, name and total amount of commission.

The amount of commissions to all agents over the selected period is provided at the end of the table.
