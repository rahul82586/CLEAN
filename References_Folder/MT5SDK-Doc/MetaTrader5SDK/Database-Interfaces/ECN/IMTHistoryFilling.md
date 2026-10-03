[🏠 Document Start](../../README.md) / [Database Interfaces](../README.md) / [ECN](../ECN.md) / IMTHistoryFilling

[Previous](IMTECNHistoryMatchingArray/IMTHistoryMatchingArray-SearchRight.md) | [Next](IMTECNHistoryFilling/IMTHistoryFilling-Release.md)

# IMTECNHistoryFilling

This interface provides access to the parameters of a [filling order in history (#filling-orders)](https://support.metaquotes.net/en/docs/mt5/platform/administration/ecn/ecn_matching_history#filling-orders), which is a service order created within the ECN for the execution of a client order. 

Method | Purpose  
---|---  
[Release](IMTECNHistoryFilling/IMTHistoryFilling-Release.md) | Delete the current object.  
[Assign](IMTECNHistoryFilling/IMTHistoryFilling-Assign.md) | Assign a passed object to the current one.  
[Clear](IMTECNHistoryFilling/IMTHistoryFilling-Clear.md) | Clear an object.  
[Order](IMTECNHistoryFilling/IMTHistoryFilling-Order.md) | Get and set the order ticket in the MetaTrader 5 platform.  
[OrderMatching](IMTECNHistoryFilling/IMTHistoryFilling-OrderMatching.md) | Get and set the ticket of the matching orders used for the execution of the current order.  
[OrderGateway](IMTECNHistoryFilling/IMTHistoryFilling-OrderGateway.md) | Get and set the ticket of the filling order (used within the ECN).  
[Login](IMTECNHistoryFilling/IMTHistoryFilling-Login.md) | Get and set the login of the client, whom the filling order belongs to.  
[LoginMatching](IMTECNHistoryFilling/IMTHistoryFilling-LoginMatching.md) | Get and set the login of the client who has placed the opposite order which is used to match the current order.  
[Server](IMTECNHistoryFilling/IMTHistoryFilling-Server.md) | Get and set the identifier of the trade server on which the filling order was placed.  
[TimeSetupMsc](IMTECNHistoryFilling/IMTHistoryFilling-TimeSetupMsc.md) | Get and set order creation time in the ECN.  
[TimeDoneMsc](IMTECNHistoryFilling/IMTHistoryFilling-TimeDoneMsc.md) | Get and set order execution time in the ECN.  
[ExternalID](IMTECNHistoryFilling/IMTHistoryFilling-ExternalID.md) | Get and set the filling order identifier in the external system.  
[Symbol](IMTECNHistoryFilling/IMTHistoryFilling-Symbol.md) | Get and set the name of the trading instrument for which the filling order was created.  
[Type](IMTECNHistoryFilling/IMTHistoryFilling-Type.md) | Get and set the type of the order created for sending to the external system.  
[TypeFill](IMTECNHistoryFilling/IMTHistoryFilling-TypeFill.md) | Get and set the fill policy used for the filling order.  
[TypeTime](IMTECNHistoryFilling/IMTHistoryFilling-TypeTime.md) | Get and set the expiration type for the filling order.  
[VolumeInitialExt](IMTECNHistoryFilling/IMTHistoryFilling-VolumeInitialExt.md) | Get and set the initial volume of the request created in the ECN for the filling of the client order.  
[VolumeCurrentExt](IMTECNHistoryFilling/IMTHistoryFilling-VolumeCurrentExt.md) | Get and set the current filled volume of the request created in the ECN for the filling of the client order.  
[Price](IMTECNHistoryFilling/IMTHistoryFilling-Price.md) | Get and set the price of the order created in the ECN for the filling of the client order.  
[Digits](IMTECNHistoryFilling/IMTHistoryFilling-Digits.md) | Get and set the number of decimal places in the price of the symbol, for which an order is placed on the ECN side.  
[Deviation](IMTECNHistoryFilling/IMTHistoryFilling-Deviation.md) | Get and set the allowable deviation for the filling order.  
[Provider](IMTECNHistoryFilling/IMTHistoryFilling-Provider.md) | Get and set the identifier of the provider through which the order is forwarded.  
[Comment](IMTECNHistoryFilling/IMTHistoryFilling-Comment.md) | Get and set a comment to the filling order.
