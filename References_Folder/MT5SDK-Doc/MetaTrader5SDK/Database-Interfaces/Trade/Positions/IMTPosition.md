[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Trade](../../Trade.md) / [Positions](../Positions.md) / IMTPosition

[Previous](../Positions.md) | [Next](IMTPosition/Enumerations.md)

# IMTPosition

The IMTPosition class contains the following methods:

Method | Purpose  
---|---  
[Release](IMTPosition/Release.md) | Deletes the current object.  
[Assign](IMTPosition/Assign.md) | Assigns a passed object to the current one.  
[Clear](IMTPosition/Clear.md) | Clears an object.  
[Print](IMTPosition/Print.md) | Gets the string description of a position.  
[Login](IMTPosition/Login.md) | Gets the login of the client, to whom the trade position belongs.  
[LoginSet](IMTPosition/LoginSet.md) | Sets the login of the client, to whom the trade position belongs.  
[Symbol](IMTPosition/Symbol.md) | Gets and sets the symbol of a trade position.  
[Action](IMTPosition/Action.md) | Gets and sets the type of a position.  
[Digits](IMTPosition/Digits.md) | Gets and sets the number of decimal places in the price of a position.  
[DigitsCurrency](IMTPosition/DigitsCurrency.md) | Gets and sets the number of decimal places the deposit currency of a client who has opened the position.  
[ContractSize](IMTPosition/ContractSize.md) | Gets and sets the contract size of the symbol, for which a position is opened.  
[Position](IMTPosition/Position.md) | Gets the ticket (a unique number) of a trade position in the MetaTrader 5 platform.  
[ExternalID](IMTPosition/ExternalID.md) | Gets and sets the ticket (a unique number) of a position in an external trading system.  
[TimeCreate](IMTPosition/TimeCreate.md) | Gets and sets the position creation time.  
[TimeUpdate](IMTPosition/TimeUpdate.md) | Gets and sets the time of the last modification of a trade position.  
[TimeCreateMsc](IMTPosition/TimeCreateMsc.md) | Gets and sets position creation time in milliseconds.  
[TimeUpdateMsc](IMTPosition/TimeUpdateMsc.md) | Gets and sets the time of the last modification of a trade position in milliseconds.  
[PriceOpen](IMTPosition/PriceOpen.md) | Gets and sets the weighted average open price of a position.  
[PriceCurrent](IMTPosition/PriceCurrent.md) | Gets and sets the current price of the symbol, for which a position has been opened.  
[PriceSL](IMTPosition/PriceSL.md) | Gets and sets the Stop Loss level of a trade position.  
[PriceTP](IMTPosition/PriceTP.md) | Gets and sets the Take Profit level of a trade position.  
[Volume](IMTPosition/Volume.md) | Gets and sets the volume of a trade position.  
[VolumeExt](IMTPosition/VolumeExt.md) | Gets and sets the trade position volume with an extended accuracy.  
[Profit](IMTPosition/Profit.md) | Gets and sets the current profit/loss of a trade position.  
[Storage](IMTPosition/Storage.md) | Gets and sets the swap size for a position.  
[RateProfit](IMTPosition/RateProfit.md) | Gets and sets the exchange rate of the profit currency of a position to the deposit currency of a client group.  
[RateMargin](IMTPosition/RateMargin.md) | Gets and sets the exchange rate of the margin currency of a position to the client's deposit currency.  
[ExpertID](IMTPosition/ExpertID.md) | Gets and sets the ID of the Expert Advisor that has opened the position.  
[ExpertPositionID](IMTPosition/ExpertPositionID.md) | Gets and sets the position ID.  
[Comment](IMTPosition/Comment.md) | Gets and sets a comment to a position.  
[Dealer](IMTPosition/Dealer.md) | Gets and sets the login of a dealer, who has processed the order that opened the position.  
[ActivationMode](IMTPosition/ActivationMode.md) | Gets and sets the position activation type.  
[ActivationTime](IMTPosition/ActivationTime.md) | Gets and sets the position activation time.  
[ActivationPrice](IMTPosition/ActivationPrice.md) | Gets and sets the position activation price.  
[ActivationFlags](IMTPosition/ActivationFlags.md) | Gets and sets position activation flags.  
[ApiDataSet](IMTPosition/ApiDataSet.md) | Sets the custom parameter for a position.  
[ApiDataGet](IMTPosition/ApiDataGet.md) | Gets the value of a custom parameter of a position.  
[ApiDataClear](IMTPosition/ApiDataClear.md) | Clears all custom parameters of positions set by an application.  
[ApiDataClearAll](IMTPosition/ApiDataClearAll.md) | Clears all custom parameters of positions.  
[APIDataUpdate](IMTPosition/APIDataUpdate.md) | Modifies a custom parameter for a position.  
[APIDataNext](IMTPosition/APIDataNext.md) | Gets a custom parameter of a trade position by the parameter position.  
[ModificationFlags](IMTPosition/ModificationFlags.md) | Gets position modification flags.  
[Reason](IMTPosition/Reason.md) | Gets the reason for position opening.  
[ReasonSet](IMTPosition/ReasonSet.md) | Sets the reason for opening a position.  
  
The IMTPosition class contains the following enumerations:

Enumeration | Purpose  
---|---  
[EnPositionAction (#enpositionaction)](IMTPosition/Enumerations.md#enpositionaction) | Position type.  
[EnActivation (#enactivation)](IMTPosition/Enumerations.md#enactivation) | Type of position activation.  
[EnTradeActivationFlags (#entradeactivationflags)](IMTPosition/Enumerations.md#entradeactivationflags) | Flags of position activation.  
[EnTradeModifyFlags (#entrademodifyflags)](IMTPosition/Enumerations.md#entrademodifyflags) | Position modification flags.
