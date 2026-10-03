[🏠 Document Start](../../../README.md) / [MetaTrader 5 Trading Platform](../../../MetaTrader-5-Trading-Platform.md) / [Platform Setup](../../Platform-Setup.md) / [Reports](../Reports.md) / Accounts Lifetime by Countries

[Previous](Accounts-Growth.md) | [Next](Agents.md)

# Accounts Lifetime by Countries

The report shows the duration for which your traders remain active after opening their accounts. The information is presented by country. The lifetime is calculated from the account creation date to the date of the [last connection](../Accounts/Editing-Account.md).

![Accounts Lifetime by Countries](images/report_accounts_lifetime_country.png)

## Configuration in MetaTrader 5 Manager

The following parameters should be configures in the Manager terminal before requesting the report:

  * Groups — groups for which account reports should be generated. You can specify one or several accounts separated by commas.
  * Period — the start and end dates of the period for which the report will be generated.



## Information in the report

Information on the lifetime of trading accounts is presented in the form of an interactive map. It is followed by a table with more detailed information on the top 1000 accounts with the longest lifetime:

  * Login — account number.
  * Name — account holder's name.
  * Lifetime — account lifetime in days.
  * Registration — account creation date.
  * Last Access — date of the last connection to the account.
  * Country — client's country of residence.
  * Group — group the account belongs to.
  * Account Comment — comment to the accounts.


