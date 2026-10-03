[🏠 Document Start](../../README.md) / [Database Interfaces](../README.md) / [ECN](../ECN.md) / IMTMatching

[Previous](../ECN.md) | [Next](IMTECNMatching/IMTMatching-Enumerations.md)

# IMTECNMatching

This interface provides access to parameters a [matching order (#matching-orders-current)](https://support.metaquotes.net/en/docs/mt5/platform/administration/ecn/ecn_matching_history#matching-orders-current), which is the trader's source request placed in the ECN.

Method | Purpose  
---|---  
[Release](IMTECNMatching/IMTMatching-Release.md) | Delete the current object.  
[Assign](IMTECNMatching/IMTMatching-Assign.md) | Assign a passed object to the current one.  
[Clear](IMTECNMatching/IMTMatching-Clear.md) | Clear an object.  
[Order](IMTECNMatching/IMTMatching-Order.md) | Get the ticket of the matching order.  
[Login](IMTECNMatching/IMTMatching-Login.md) | Get and set the login of the client, to whom the matching order belongs.  
[Server](IMTECNMatching/IMTMatching-Server.md) | Get and set the identifier of the trade server on which the matching order was placed.  
[Group](IMTECNMatching/IMTMatching-Group.md) | Get and set the group of the client who has placed the matching order.  
[State](IMTECNMatching/IMTMatching-State.md) | Get and set the current state of the matching order.  
[Flags](IMTECNMatching/IMTMatching-Flags.md) | Get and set matching order flags.  
[TimeSetupMsc](IMTECNMatching/IMTMatching-TimeSetupMsc.md) | Get and set order placing time in the ECN.  
[TimeExpiration](IMTECNMatching/IMTMatching-TimeExpiration.md) | Get and set order expiration time in the ECN.  
[Symbol](IMTECNMatching/IMTMatching-Symbol.md) | Get and set the name of the trading symbol, for which the matching order is placed on the ECN side.  
[SymbolClient](IMTECNMatching/IMTMatching-SymbolClient.md) | Get and set the name of the trading symbol, for which the matching order is placed on the client side.  
[Type](IMTECNMatching/IMTMatching-Type.md) | Get and set the type of the order added into the ECN order book.  
[TypeFill](IMTECNMatching/IMTMatching-TypeFill.md) | Get and set the fill policy used for the matching order.  
[TypeTime](IMTECNMatching/IMTMatching-TypeTime.md) | Get and set the matching order expiration type.  
[Price](IMTECNMatching/IMTMatching-Price.md) | Get and set the price of the order created in the ECN for the filling of the client order.  
[PriceClient](IMTECNMatching/IMTMatching-PriceClient.md) | Get and set the price specified in the original client order.  
[Digits](IMTECNMatching/IMTMatching-Digits.md) | Get and set the number of decimal places in the price of the symbol, for which an order is placed on the ECN side.  
[DigitsClient](IMTECNMatching/IMTMatching-DigitsClient.md) | Get and set the price specified in the original client order.  
[VolumeInitialExt](IMTECNMatching/IMTMatching-VolumeInitialExt.md) | Get and set the initial volume of the request created in the ECN for the filling of the client order.  
[VolumeCurrentExt](IMTECNMatching/IMTMatching-VolumeCurrentExt.md) | Get and set the current filled volume of the request created in the ECN for the filling of the client order.  
[VolumeInitialClientExt](IMTECNMatching/IMTMatching-VolumeInitialClientExt.md) | Get and set the initial volume of the request created by the client.  
[VolumeCurrentClientExt](IMTECNMatching/IMTMatching-VolumeCurrentClientExt.md) | Get and set the current filled volume of the request created by the client.  
  
The IMTECNMatching class contains the following enumerations:

Enumeration | Description  
---|---  
[ENCMatchingState (#encmatchingstate)](IMTECNMatching/IMTMatching-Enumerations.md#encmatchingstate) | Possible order states.  
[EnECNMatchingOrderFlags (#enecnmatchingorderflags)](IMTECNMatching/IMTMatching-Enumerations.md#enecnmatchingorderflags) | Additional order flags.
