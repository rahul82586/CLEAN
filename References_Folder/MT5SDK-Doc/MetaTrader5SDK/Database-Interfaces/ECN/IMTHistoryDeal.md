[🏠 Document Start](../../README.md) / [Database Interfaces](../README.md) / [ECN](../ECN.md) / IMTHistoryDeal

[Previous](IMTECNHistoryFillingArray/IMTHistoryFillingArray-SearchRight.md) | [Next](IMTECNHistoryDeal/IMTHistoryDeal-Release.md)

# IMTECNHistoryDeal

This interface provides access to the parameters of [deals (#deals)](https://support.metaquotes.net/en/docs/mt5/platform/administration/ecn/ecn_matching_history#deals) performed as a result of order execution at gateways. These deals contain execution data at the corresponding gateway and client order execution parameters, taking into account slippage settings.

Method | Purpose  
---|---  
[Release](IMTECNHistoryDeal/IMTHistoryDeal-Release.md) | Delete the current object.  
[Assign](IMTECNHistoryDeal/IMTHistoryDeal-Assign.md) | Assign a passed object to the current one.  
[Clear](IMTECNHistoryDeal/IMTHistoryDeal-Clear.md) | Clear an object.  
[Order](IMTECNHistoryDeal/IMTHistoryDeal-Order.md) | Get and set the ticket of the original client order in the MetaTrader 5 platform.  
[OrderGateway](IMTECNHistoryDeal/IMTHistoryDeal-OrderGateway.md) | Get and set the internal ticket of the filling order (which is used within the ECN for internal purposes).  
[DealGateway](IMTECNHistoryDeal/IMTHistoryDeal-DealGateway.md) | Get and set the internal ticket of the deal (used within the ECN for internal purposes).  
[Login](IMTECNHistoryDeal/IMTHistoryDeal-Login.md) | Get and set the login of the client, to whom the original order belongs.  
[Server](IMTECNHistoryDeal/IMTHistoryDeal-Server.md) | Get and set the identifier of the trade server on which the original order was placed.  
[ExternalID](IMTECNHistoryDeal/IMTHistoryDeal-ExternalID.md) | Get and set the deal identifier in an external system.  
[TimeMsc](IMTECNHistoryDeal/IMTHistoryDeal-TimeMsc.md) | Get and set deal execution time at the gateway.  
[Symbol](IMTECNHistoryDeal/IMTHistoryDeal-Symbol.md) | Get and set the name of the trading symbol for which the deal was executed.  
[Action](IMTECNHistoryDeal/IMTHistoryDeal-Action.md) | Get and set the deal type.  
[VolumeExt](IMTECNHistoryDeal/IMTHistoryDeal-VolumeExt.md) | Get and set the deal volume.  
[Price](IMTECNHistoryDeal/IMTHistoryDeal-Price.md) | Get and set the price at which the deal was executed on the platform side.  
[PriceGateway](IMTECNHistoryDeal/IMTHistoryDeal-PriceGateway.md) | Get and set the price at which the deal was actually executed on the external system side.  
[Digits](IMTECNHistoryDeal/IMTHistoryDeal-Digits.md) | Get and set the number of decimal places in the price of the symbol, for which the deal was executed, on the trading platform side.  
[DigitsGateway](IMTECNHistoryDeal/IMTHistoryDeal-DigitsGateway.md) | Get and set the number of decimal places in the price of the symbol, for which the deal was executed, on the external system side.  
[Commission](IMTECNHistoryDeal/IMTHistoryDeal-Commission.md) | Get and set the commission charged by an external system for the deal.  
[Provider](IMTECNHistoryDeal/IMTHistoryDeal-Provider.md) | Get and set the identifier of the provider through which the deal was executed.
