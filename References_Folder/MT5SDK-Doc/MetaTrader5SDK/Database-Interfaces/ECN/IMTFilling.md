[🏠 Document Start](../../README.md) / [Database Interfaces](../README.md) / [ECN](../ECN.md) / IMTFilling

[Previous](IMTECNMatchingArray/IMTMatchingArray-SearchRight.md) | [Next](IMTECNFilling/IMTFilling-Release.md)

# IMTECNFilling

This interface provides access to the parameters of a [filling order (#filling-orders-current)](https://support.metaquotes.net/en/docs/mt5/platform/administration/ecn/ecn_matching_history#filling-orders-current), which is a service order created within the ECN for the execution of a client order. 

Method | Purpose  
---|---  
[Release](IMTECNFilling/IMTFilling-Release.md) | Delete the current object.  
[Assign](IMTECNFilling/IMTFilling-Assign.md) | Assign a passed object to the current one.  
[Clear](IMTECNFilling/IMTFilling-Clear.md) | Clear an object.  
[Login](IMTECNFilling/IMTFilling-Login.md) | Get and set the login of the client, whom the filling order belongs to.  
[Order](IMTECNFilling/IMTFilling-Order.md) | Get and set the filling order ticket in the MetaTrader 5 platform.  
[Server](IMTECNFilling/IMTFilling-Server.md) | Get and set the identifier of the trade server on which the filling order was placed.  
[TimeSetupMsc](IMTECNFilling/IMTFilling-TimeSetupMsc.md) | Get and set the time when the filling order was placed in the external system.  
[ExternalID](IMTECNFilling/IMTFilling-ExternalID.md) | Get and set the filling order identifier in the external system.  
[State](IMTECNFilling/IMTFilling-State.md) | Get and set the current state of the filling order.  
[Symbol](IMTECNFilling/IMTFilling-Symbol.md) | Get and set the name of the trading instrument for which the filling order was created.  
[Type](IMTECNFilling/IMTFilling-Type.md) | Get and set the type of the order created for sending to the external system.  
[TypeFill](IMTECNFilling/IMTFilling-TypeFill.md) | Get and set the fill policy used for the filling order.  
[TypeTime](IMTECNFilling/IMTFilling-TypeTime.md) | Get and set the expiration type for the filling order.  
[VolumeInitialExt](IMTECNFilling/IMTFilling-VolumeInitialExt.md) | Get and set the initial volume of the request created in the ECN for the filling of the client order.  
[VolumeCurrentExt](IMTECNFilling/IMTFilling-VolumeCurrentExt.md) | Get and set the current filled volume of the request created in the ECN for the filling of the client order.  
[Price](IMTECNFilling/IMTFilling-Price.md) | Get and set the price of the order created in the ECN for the filling of the client order.  
[Digits](IMTECNFilling/IMTFilling-Digits.md) | Get and set the number of decimal places in the price of the symbol, for which an order is placed on the ECN side.  
[Deviation](IMTECNFilling/IMTFilling-Deviation.md) | Get and set the allowable deviation for the filling order.  
[Provider](IMTECNFilling/IMTFilling-Provider.md) | Get and set the identifier of the provider through which the order is forwarded.  
[Comment](IMTECNFilling/IMTFilling-Comment.md) | Get and set a comment to the filling order.
