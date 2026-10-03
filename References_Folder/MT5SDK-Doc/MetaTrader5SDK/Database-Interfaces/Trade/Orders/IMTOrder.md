[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Trade](../../Trade.md) / [Orders](../Orders.md) / IMTOrder

[Previous](../Orders.md) | [Next](IMTOrder/Enumerations.md)

# IMTOrder

The IMTOrder class contains the following methods:

Method | Purpose  
---|---  
[Release](IMTOrder/Release.md) | Deletes the current object.  
[Assign](IMTOrder/Assign.md) | Assigns a passed object to the current one.  
[Clear](IMTOrder/Clear.md) | Clears an object.  
[Print](IMTOrder/Print.md) | Gets the string description of an order.  
[Order](IMTOrder/Order.md) | Gets the ticket of an order.  
[OrderSet](IMTOrder/OrderSet.md) | Sets the order ticket.  
[ExternalID](IMTOrder/ExternalID.md) | Gets and sets the order ID in external trading systems.  
[Login](IMTOrder/Login.md) | Gets and sets the login of the client, to whom the order belongs.  
[Dealer](IMTOrder/Dealer.md) | Gets and sets the login of a dealer, who has processed the order.  
[Symbol](IMTOrder/Symbol.md) | Gets and sets the order symbol.  
[Digits](IMTOrder/Digits.md) | Gets and sets the number of decimal places in the price of an order.  
[DigitsCurrency](IMTOrder/DigitsCurrency.md) | Gets and sets the number of decimal places the deposit currency of a client who has placed the order.  
[ContractSize](IMTOrder/ContractSize.md) | Gets and sets the contract size of the symbol, for which an order was placed.  
[State](IMTOrder/State.md) | Gets the current state of an order.  
[StateSet](IMTOrder/StateSet.md) | Sets the order state.  
[Reason](IMTOrder/Reason.md) | Gets the reason for placing an order.  
[ReasonSet](IMTOrder/ReasonSet.md) | Sets the order placing reason.  
[TimeSetup](IMTOrder/TimeSetup.md) | Gets and sets the order placing time.  
[TimeSetupMsc](IMTOrder/TimeSetupMsc.md) | Gets and sets the order placing time in milliseconds.  
[TimeExpiration](IMTOrder/TimeExpiration.md) | Gets and sets the order expiration time.  
[TimeDone](IMTOrder/TimeDone.md) | Gets and sets the order execution time.  
[TimeDoneMsc](IMTOrder/TimeDoneMsc.md) | Gets and sets the order execution time in milliseconds.  
[Type](IMTOrder/Type.md) | Gets and sets the order type.  
[TypeFill](IMTOrder/TypeFill.md) | Gets and sets the order filling type.  
[TypeTime](IMTOrder/TypeTime.md) | Gets and sets the order expiration type.  
[PriceOrder](IMTOrder/PriceOrder.md) | Gets and sets the order price.  
[PriceTrigger](IMTOrder/PriceTrigger.md) | Gets and sets the price, at which a Limit order is placed when the Stop Limit order triggers.  
[PriceCurrent](IMTOrder/PriceCurrent.md) | Gets and sets the current price of the symbol, for which an order has been placed.  
[PriceSL](IMTOrder/PriceSL.md) | Gets and sets the Stop Loss level of an order.  
[PriceTP](IMTOrder/PriceTP.md) | Gets and sets the Take Profit level of an order.  
[VolumeInitial](IMTOrder/VolumeInitial.md) | Gets and sets the initial volume of an order.  
[VolumeInitialExt](IMTOrder/VolumeInitialExt.md) | Gets and sets the initial order volume with an extended accuracy.  
[VolumeCurrent](IMTOrder/VolumeCurrent.md) | Gets and sets the current unfilled volume of an order.  
[VolumeCurrentExt](IMTOrder/VolumeCurrentExt.md) | Gets and sets the current unfilled order volume with an extended accuracy.  
[ExpertID](IMTOrder/ExpertID.md) | Gets and sets the ID of the Expert Advisor, which has placed the order.  
[PositionID](IMTOrder/PositionID.md) | Gets and sets the position ID (ticket) specified in the order.  
[PositionByID](IMTOrder/PositionByID.md) | Gets and sets the ID (ticket) of an opposite position for the order.  
[Comment](IMTOrder/Comment.md) | Gets and sets a comment to an order.  
[ActivationMode](IMTOrder/ActivationMode.md) | Gets the order activation type.  
[ActivationTime](IMTOrder/ActivationTime.md) | Gets the order activation time.  
[ActivationPrice](IMTOrder/ActivationPrice.md) | Gets the price, at which the order was activated.  
[ActivationFlags](IMTOrder/ActivationFlags.md) | Gets order activation flags.  
[ApiDataSet](IMTOrder/ApiDataSet.md) | Sets a custom parameter for a trade order.  
[ApiDataGet](IMTOrder/ApiDataGet.md) | Gets the value of a custom parameter of a trade order.  
[ApiDataClear](IMTOrder/ApiDataClear.md) | Clears all custom parameters of orders set by an application.  
[ApiDataClearAll](IMTOrder/ApiDataClearAll.md) | Clears all custom settings of trade order.  
[APIDataUpdate](IMTOrder/APIDataUpdate.md) | Changes the custom parameter of the trade order.  
[APIDataNext](IMTOrder/APIDataNext.md) | Gets the custom parameter of the trade order by a position.  
[RateMargin](IMTOrder/RateMargin.md) | Gets and sets the conversion rate of the symbol margin currency to the client's deposit currency, which is used for calculating the margin for an order.  
[ModificationFlags](IMTOrder/ModificationFlags.md) | Gets the order modification flags.  
  
The IMTOrder class contains the following enumerations:

Enumeration | Purpose  
---|---  
[EnOrderType (#enordertype)](IMTOrder/Enumerations.md#enordertype) | Types of orders.  
[EnOrderFilling (#enorderfilling)](IMTOrder/Enumerations.md#enorderfilling) | Order filling types.  
[EnOrderTime (#enordertime)](IMTOrder/Enumerations.md#enordertime) | Order expiration types.  
[EnOrderState (#enorderstate)](IMTOrder/Enumerations.md#enorderstate) | Order states.  
[EnOrderActivation (#enorderactivation)](IMTOrder/Enumerations.md#enorderactivation) | Types of order activation.  
[EnOrderReason (#enorderreason)](IMTOrder/Enumerations.md#enorderreason) | Order creation ways.  
[EnTradeActivationFlags (#entradeactivationflags)](IMTOrder/Enumerations.md#entradeactivationflags) | Order activation flags.  
[EnTradeModifyFlags (#entrademodifyflags)](IMTOrder/Enumerations.md#entrademodifyflags) | Order modification flags.
