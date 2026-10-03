[🏠 Document Start](../README.md) / Return Codes

[Previous](../Journal-Constants/README.md) | [Next](Successful-completion.md)

# Return Codes

The vast majority of functions in the MetaTrader 5 API return a special code to notify of the results of their implementation To develop high-quality, stable applications, a programmer should check the return codes of functions of called API methods.

Return codes are contained in the EnMTAPIRetcode enumeration, in file MT5APIConstants.h and are divided into several groups:

Group of codes | Range of values | Description  
[Successful completion](Successful-completion.md) | 0-1 | Codes that are returned with the successful completion of an operation.  
[Common errors](Common-errors.md) | 2-999 | Codes returned when common errors occur.  
[Authentication](Authentication.md) | 1000-1999 | Codes returned during the authentication of users.  
[Configuration management](Configuration-Management.md) | 2000-2999 | Codes that are returned when changing configurations.  
[User management](User-management.md) | 3000-3999 | The codes returned when working with the database of users.  
[Trade management](Trade-management.md) | 4000-4999 | The codes returned when working with the trading database.  
[Report Generation](Report-Generation.md) | 5000-5999 | Codes that are returned when generating reports.  
[Price Data](Price-Data.md) | 6000-6999 | Codes that are returned when working with price data.  
[Trade Requests](Trade-Requests.md) | 10000-10999 | Codes returned while processing trade requests.  
[Dealer](Dealer.md) | 11000-11999 | Codes returned during the work of a dealer.  
[API](API.md) | 12000-12999 | Codes related to the operation of API.  
[Instant messengers](Messengers.md) | 14000-14999 | Codes related to message sending via instant messengers.  
[Subscriptions](Subscriptions.md) | 15000-15999 | Codes related to the operation of the [Subscriptions](https://support.metaquotes.net/en/docs/mt5/platform/administration/subscriptions) service.
