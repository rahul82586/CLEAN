[🏠 Document Start](../../README.md) / [Database Interfaces](../README.md) / [ECN](../ECN.md) / IMTHistoryMatching

[Previous](IMTECNProviderArray/IMTProviderArray-SearchRight.md) | [Next](IMTECNHistoryMatching/IMTHistoryMatching-Release.md)

# IMTECNHistoryMatching

This interface provides access to parameters a [matching order from history (#matching-orders)](https://support.metaquotes.net/en/docs/mt5/platform/administration/ecn/ecn_matching_history#matching-orders), which is the trader's source request placed in the ECN. History records store information about original client orders as well as filling orders, which are service orders created within ECN to execute client requests at gateways.

Method | Purpose  
---|---  
[Release](IMTECNHistoryMatching/IMTHistoryMatching-Release.md) | Delete the current object.  
[Assign](IMTECNHistoryMatching/IMTHistoryMatching-Assign.md) | Assign a passed object to the current one.  
[Clear](IMTECNHistoryMatching/IMTHistoryMatching-Clear.md) | Clear an object.  
[Order](IMTECNHistoryMatching/IMTHistoryMatching-Order.md) | Get the ticket of the matching order.  
[Login](IMTECNHistoryMatching/IMTHistoryMatching-Login.md) | Get and set the login of the client, to whom the matching order belongs.  
[Server](IMTECNHistoryMatching/IMTHistoryMatching-Server.md) | Get and set the identifier of the trade server on which the matching order was placed.  
[State](IMTECNHistoryMatching/IMTHistoryMatching-State.md) | Get and set the current state of the matching order.  
[TimeSetupMsc](IMTECNHistoryMatching/IMTHistoryMatching-TimeSetupMsc.md) | Get and set order placing time in the ECN.  
[TimeDoneMsc](IMTECNHistoryMatching/IMTHistoryMatching-TimeDoneMsc.md) | Get and set order execution time in the ECN.  
[TimeExpiration](IMTECNHistoryMatching/IMTHistoryMatching-TimeExpiration.md) | Get and set order expiration time in the ECN.  
[Symbol](IMTECNHistoryMatching/IMTHistoryMatching-Symbol.md) | Get and set the name of the trading symbol, for which the matching order is placed on the ECN side.  
[SymbolClient](IMTECNHistoryMatching/IMTHistoryMatching-SymbolClient.md) | Get and set the name of the trading symbol, for which the matching order is placed on the client side.  
[Type](IMTECNHistoryMatching/IMTHistoryMatching-Type.md) | Get and set the type of the order added into the ECN order book.  
[TypeClient](IMTECNHistoryMatching/IMTHistoryMatching-TypeClient.md) | Get and set the type of the order placed on the client side.  
[TypeFill](IMTECNHistoryMatching/IMTHistoryMatching-TypeFill.md) | Get and set the fill policy used for the matching order.  
[TypeFillClient](IMTECNHistoryMatching/IMTHistoryMatching-TypeFillClient.md) | Get and set the fill policy used in the original client order.  
[TypeTime](IMTECNHistoryMatching/IMTHistoryMatching-TypeTime.md) | Get and set the matching order expiration type.  
[TypeTimeClient](IMTECNHistoryMatching/IMTHistoryMatching-TypeTimeClient.md) | Get and set the expiration type in the original client order.  
[Price](IMTECNHistoryMatching/IMTHistoryMatching-Price.md) | Get and set the price of the order created in the ECN for the filling of the client order.  
[PriceClient](IMTECNHistoryMatching/IMTHistoryMatching-PriceClient.md) | Get and set the price specified in the original client order.  
[Digits](IMTECNHistoryMatching/IMTHistoryMatching-Digits.md) | Get and set the number of decimal places in the price of the symbol, for which an order is placed on the ECN side.  
[DigitsClient](IMTECNHistoryMatching/IMTHistoryMatching-DigitsClient.md) | Get and set the price specified in the original client order.  
[VolumeInitialExt](IMTECNHistoryMatching/IMTHistoryMatching-VolumeInitialExt.md) | Get and set the initial volume of the request created in the ECN for the filling of the client order.  
[VolumeInitialClientExt](IMTECNHistoryMatching/IMTHistoryMatching-VolumeInitialClientExt.md) | Get and set the current filled volume of the request created in the ECN for the filling of the client order.  
[VolumeCurrentExt](IMTECNHistoryMatching/IMTHistoryMatching-VolumeCurrentExt.md) | Get and set the initial volume of the request created by the client.  
[VolumeCurrentClientExt](IMTECNHistoryMatching/IMTHistoryMatching-VolumeCurrentClientExt.md) | Get and set the current filled volume of the request created by the client.
