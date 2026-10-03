[🏠 Document Start](../../README.md) / [Report API](../README.md) / [Ready-made Examples](../Ready-made-Examples.md) / Daily Server Logs

[Previous](Daily-Detailed.md) | [Next](Daily-Dealing.md)

# Daily Server Logs Report

Daily Server Report is a statistical report on the platform operation for a specified day.

## Setup

The following parameters must be set in the manager terminal before requesting the report:

  * Period — a day, for which the report must be generated.



The report contains several diagrams and tables:

  * Server Messages — total number of entries in the trading server for the day, as well as the number of critical messages for the day;
  * Critical Errors — list of critical errors for the day is displayed in the table. Description and the number of cases are shown for each error.
  * Top Flooders — this diagram shows the users, from whom the server log contains most messages.
  * Manager Connections — list of manager connections to the server for the day is displayed in this table. Manager login and IP address, from which the connection has been performed, are shown.
  * Client Builds — this diagram shows distribution of connections to the server by builds and terminal types: terminal PC version, mobile terminals for iPhone and Android.


