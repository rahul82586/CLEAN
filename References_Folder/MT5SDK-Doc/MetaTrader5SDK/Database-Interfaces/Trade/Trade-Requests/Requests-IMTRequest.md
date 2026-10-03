[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Trade](../../Trade.md) / [Trade Requests](../Requests.md) / Requests IMTRequest

[Previous](../Requests.md) | [Next](IMTRequest/Requests-Enumerations.md)

# IMTRequest

The IMTRequest class contains the following methods:

Method | Description  
---|---  
[Release](IMTRequest/Requests-Release.md) | Delete the current object.  
[Assign](IMTRequest/Requests-Assign.md) | Assign a passed object to the current one.  
[Clear](IMTRequest/Requests-Clear.md) | Clear an object.  
[Print](IMTRequest/Requests-Print.md) | Get a string description of a trade request.  
[ID number](IMTRequest/Requests-ID.md) | Get the request ID.  
[Login](IMTRequest/Requests-Login.md) | Get and set a client login in a request.  
[ExternalAccount](IMTRequest/Requests-ExternalAccount.md) | Get and set a client's account in an external trading system.  
[Group](IMTRequest/Requests-Group.md) | Get the group of the client who has sent the request.  
[Symbol](IMTRequest/Requests-Symbol.md) | Get and set a symbol in a request.  
[SymbolOriginal](IMTRequest/Requests-SymbolOriginal.md) | Get and set the original symbol in a trade request received by the Gateway API.  
[Digits](IMTRequest/Requests-Digits.md) | Get the number of decimal places in the trade request price.  
[DigitsSet](IMTRequest/Requests-DigitsSet.md) | Set the number of decimal places in the trade request price.  
[Action](IMTRequest/Requests-Action.md) | Get and set the type of action to which the trade request belongs.  
[TimeExpiration](IMTRequest/Requests-TimeExpiration.md) | Get and set the expiration time in a trade request.  
[Type](IMTRequest/Requests-Type.md) | Get and set the order type in a request.  
[TypeFill](IMTRequest/Requests-TypeFill.md) | Get and set the order filling type in a request.  
[TypeTime](IMTRequest/Requests-TypeTime.md) | Get and set the order expiration type in a request.  
[Flags](IMTRequest/Requests-Flags.md) | Get and set additional flags of a trade request.  
[Volume](IMTRequest/Requests-Volume.md) | Get and set the operation volume in a request.  
[VolumeExt](IMTRequest/Requests-VolumeExt.md) | Get and set the operation volume in a request, with an extended accuracy.  
[VolumeCurrent](IMTRequest/Requests-VolumeCurrent.md) | Get and set the current unfilled (remaining) order volume in the request.  
[VolumeCurrentExt](IMTRequest/Requests-VolumeCurrentExt.md) | Get and set the current unfilled (remaining) order volume in the request as an increased-precision value.  
[Order](IMTRequest/Requests-Order.md) | Get and set the ticket of an order in a trade request.  
[OrderExternalID](IMTRequest/Requests-OrderExternalID.md) | Get the order ID in external trading systems.  
[PriceOrder](IMTRequest/Requests-PriceOrder.md) | Get and set the price of an order in a trade request.  
[PriceTrigger](IMTRequest/Requests-PriceTrigger.md) | Get and set the price, at which a Limit order is placed when the Stop Limit order triggers.  
[PriceSL](IMTRequest/Requests-PriceSL.md) | Get and set the Stop Loss level in a trade request.  
[PriceTP](IMTRequest/Requests-PriceTP.md) | Get and set the Take Profit level in a trade request.  
[PriceDeviation](IMTRequest/Requests-PriceDeviation.md) | Get and set the maximum allowed deviation of the execution price from the price requested in an order.  
[PriceDeviationTop](IMTRequest/Requests-PriceDeviationTop.md) | Get the allowed price deviation in the increase direction.  
[PriceDeviationBottom](IMTRequest/Requests-PriceDeviationBottom.md) | Get the allowed price deviation in the decrease direction.  
[SpreadDiff](IMTRequest/Requests-SpreadDiff.md) | Get and set the difference between the symbol spread for the group to which the trader belongs and the current symbol spread (price markup for the group).  
[SpreadDiffBalance](IMTRequest/Requests-SpreadDiffBalance.md) | Get and set the spread difference balance in a trade request.  
[Comment](IMTRequest/Requests-Comment.md) | Get and set a comment to a trade request.  
[ResultRetcode](IMTRequest/Requests-ResultRetcode.md) | Get the current state of a trade request.  
[ResultDealer](IMTRequest/Requests-ResultDealer.md) | Get the login of the dealer processing the request.  
[ResultDeal](IMTRequest/Requests-ResultDeal.md) | Get the number of the deal formed as a result of request execution.  
[ResultOrder](IMTRequest/Requests-ResultOrder.md) | Get the number of the order formed as a result of request execution.  
[ResultVolume](IMTRequest/Requests-ResultVolume.md) | Get the deal volume confirmed by a dealer for this request.  
[ResultVolumeExt](IMTRequest/Requests-ResultVolumeExt.md) | Get the extended accuracy deal volume confirmed by a dealer for this request.  
[ResultPrice](IMTRequest/Requests-ResultPrice.md) | Get the price used by a dealer to confirm a request.  
[ResultDealerBid](IMTRequest/Requests-ResultDealerBid.md) | Get the Bid price confirmed by a dealer for this request.  
[ResultDealerAsk](IMTRequest/Requests-ResultDealerAsk.md) | Get the Ask price confirmed by a dealer for this request.  
[ResultDealerLast](IMTRequest/Requests-ResultDealerLast.md) | Get the Last price confirmed by a dealer for this request.  
[ResultMarketBid](IMTRequest/Requests-ResultMarketBid.md) | Get the market Bid price when a request is processed by the server.  
[ResultMarketAsk](IMTRequest/Requests-ResultMarketAsk.md) | Get the market Ask price when a request is processed by the server.  
[ResultMarketLast](IMTRequest/Requests-ResultMarketLast.md) | Get the market Last price when a request is processed by the server.  
[ResultComment](IMTRequest/Requests-ResultComment.md) | Get the comment added by a dealer after confirming the request.  
[IDClient](IMTRequest/Requests-IDClient.md) | Get the request ID on the side of the client who has sent the request.  
[IP](IMTRequest/Requests-IP.md) | Get and set the IP address the request is sent from.  
[SourceLogin](IMTRequest/Requests-SourceLogin.md) | Get and set the login of the dealer, on whose behalf the request is performed.  
[Position](IMTRequest/Requests-Position.md) | Get and set a position ticket (unique number) in a MetaTrader 5 platform.  
[PositionBy](IMTRequest/Requests-PositionBy.md) | Get and set the ticket (unique number) of an opposite trade position in a MetaTrader 5 platform.  
[PositionExternalID](IMTRequest/Requests-PositionExternalID.md) | Get and set the ticket (a unique number) of a position in an external trading system.  
[PositionByExternalID](IMTRequest/Requests-PositionByExternalID.md) | Get and set the ticket (unique number) of an opposite trade position in an external trading system.  
[Reason](IMTRequest/Requests-Reason.md) | Get and set the reason for creating the request.  
[ApiDataSet](IMTRequest/Requests-ApiDataSet.md) | Set the custom parameter for a trade request.  
[ApiDataGet](IMTRequest/Requests-ApiDataGet.md) | Get the value of a custom parameter of a trade request.  
[APIDataUpdate](IMTRequest/Requests-APIDataUpdate.md) | Change the custom parameter of a trade request.  
[APIDataNext](IMTRequest/Requests-APIDataNext.md) | Get the custom parameter of a trade request by a position.  
[APIDataRaw](IMTRequest/Requests-APIDataRaw.md) | Get custom parameters of a trade request as raw data (memory fragment).  
[APIDataRawMax](IMTRequest/Requests-APIDataRawMax.md) | Get the maximum possible size of custom parameters of a trade request.  
[ApiDataClear](IMTRequest/Requests-ApiDataClear.md) | Clear all custom parameters of requests set by an application.  
[ApiDataClearAll](IMTRequest/Requests-ApiDataClearAll.md) | Clear all user settings of trade requests.  
  
The IMTRequest class contains the following enumerations:

Enumeration | Purpose  
---|---  
[EnTradeActions](IMTRequest/Requests-Enumerations.md) | Type of a trade operation.  
[EnTradeActionFlags (#entradeactionflags)](IMTRequest/Requests-Enumerations.md#entradeactionflags) | Additional flags of trade requests.
