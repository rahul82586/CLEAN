[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Trade](../../Trade.md) / [Deals](../Deals.md) / IMTDeal

[Previous](../Deals.md) | [Next](IMTDeal/Enumerations.md)

# IMTDeal

The IMTDeal class contains the following methods:

Method | Purpose  
---|---  
[Release](IMTDeal/Release.md) | Delete the current object.  
[Assign](IMTDeal/Assign.md) | Assigns a passed object to the current one.  
[Clear](IMTDeal/Clear.md) | Clear an object.  
[Print](IMTDeal/Print.md) | Get the string description of a deal.  
[Deal](IMTDeal/Deal.md) | Get the ticket of a deal.  
[DealSet](IMTDeal/DealSet.md) | Set the ticket of a deal.  
[ExternalID](IMTDeal/ExternalID.md) | Get and set the deal ID in external trading systems.  
[Login](IMTDeal/Login.md) | Get and set the login of the client, to whom the deal belongs.  
[Dealer](IMTDeal/Dealer.md) | Get and set the login of a dealer, who has processed a deal.  
[Order](IMTDeal/Order.md) | Get and set the ticket of the order, as a result of which a deal was executed.  
[Action](IMTDeal/Action.md) | Get and set the type of action performed with a deal.  
[Entry](IMTDeal/Entry.md) | Get and set the deal direction.  
[Digits](IMTDeal/Digits.md) | Get and set the number of decimal places in the price of a deal.  
[DigitsCurrency](IMTDeal/DigitsCurrency.md) | Get and set the number of decimal places the deposit currency of a client who has executed the deal.  
[ContractSize](IMTDeal/ContractSize.md) | Get and set the contract size of the symbol, for which a deal is executed.  
[Time](IMTDeal/Time.md) | Get and set the time of a deal.  
[Symbol](IMTDeal/Symbol.md) | Get and set the symbol, for which a deal is executed.  
[Price](IMTDeal/Price.md) | Get and set the price of a deal.  
[PriceSL](IMTDeal/PriceSL.md) | Get and set the Stop Loss level of a deal.  
[PriceTP](IMTDeal/PriceTP.md) | Get and set the Take Profit level of a deal.  
[Volume](IMTDeal/Volume.md) | Get and set the deal volume.  
[VolumeExt](IMTDeal/VolumeExt.md) | Get and set the deal volume with an extended accuracy.  
[VolumeClosed](IMTDeal/VolumeClosed.md) | Get and set the position volume that was closed by the deal.  
[VolumeClosedExt](IMTDeal/VolumeClosedExt.md) | Get and set the extended accuracy volume of a position that was closed by this deal.  
[Profit](IMTDeal/Profit.md) | Get and set the value of the profit from the deal execution.  
[Value](IMTDeal/Value.md) | Get and set the deal value in client deposit currency.  
[Storage](IMTDeal/Storage.md) | Get and set the swap size for a deal.  
[Commission](IMTDeal/Commission.md) | Get and set the amount of commission charged for a deal.  
[Fee](IMTDeal/Fee.md) | Get and set the fee amount per deal.  
[RateProfit](IMTDeal/RateProfit.md) | Get and set the exchange rate of the profit currency of a deal to the deposit currency of a client group.  
[RateMargin](IMTDeal/RateMargin.md) | Get and set the exchange rate of the margin currency of a deal to the client's deposit currency.  
[ExpertID](IMTDeal/ExpertID.md) | Get and set the ID of the Expert Advisor that has executed a deal.  
[PositionID](IMTDeal/PositionID.md) | Get and set the position ID (ticket) for a deal.  
[Comment](IMTDeal/Comment.md) | Get and set a comment to a deal.  
[ApiDataSet](IMTDeal/ApiDataSet.md) | Set a custom parameter for a deal.  
[APIDataUpdate](IMTDeal/APIDataUpdate.md) | Change the custom parameter of a deal.  
[APIDataNext](IMTDeal/APIDataNext.md) | Get the custom parameter of a deal by a position.  
[ApiDataGet](IMTDeal/ApiDataGet.md) | Get the value of a custom parameter of a deal.  
[ApiDataClear](IMTDeal/ApiDataClear.md) | Clear all custom parameters of deals set by an application.  
[ApiDataClearAll](IMTDeal/ApiDataClearAll.md) | Clear all custom parameters of deals.  
[ProfitRaw](IMTDeal/ProfitRaw.md) | Get and set the value of profit/loss resulting from the deal execution. The profit/loss is expressed in the profit currency of the symbol, for which a deal is executed.  
[PricePosition](IMTDeal/PricePosition.md) | Get and set the price of the position closed by the deal.  
[TickValue](IMTDeal/TickValue.md) | Get and set the tick price for a deal.  
[TickSize](IMTDeal/TickSize.md) | Get and set the tick size for a deal.  
[Flags](IMTDeal/Flags.md) | Get and set the common flags of a deal.  
[TimeMsc](IMTDeal/TimeMsc.md) | Get and set the time of a deal execution in milliseconds.  
[Reason](IMTDeal/Reason.md) | Get the reason for placing an order.  
[ReasonSet](IMTDeal/ReasonSet.md) | Set the reason for a deal.  
[Gateway](IMTDeal/Gateway.md) | Get the ID of a trade gateway, using which the deal was executed.  
[PriceGatewaySet](IMTDeal/PriceGatewaySet.md) | Set the ID of a trade gateway, using which the deal was executed.  
[PriceGateway](IMTDeal/PriceGateway.md) | Get the actual price of a deal executed via a gateway in an external trading system, not taking into account the gateway price transformation settings.  
[PriceGatewaySet](IMTDeal/PriceGatewaySet.md) | Set the actual price of a deal executed via a gateway in an external trading system.  
[MarketBid](IMTDeal/MarketBid.md) | Get the market Bid price as at the time of deal execution by the server.  
[MarketAsk](IMTDeal/MarketAsk.md) | Get the market Ask price as at the time of deal execution by the server.  
[MarketLast](IMTDeal/MarketLast.md) | Get the market Last price as at the time of deal execution by the server.  
[ModificationFlags](IMTDeal/ModificationFlags.md) | Get deal modification flags.  
  
The IMTDeal class contains the following enumerations:

Enumeration | Purpose  
---|---  
[EnDealAction (#endealaction)](IMTDeal/Enumerations.md#endealaction) | Deal type.  
[EnDealEntry (#endealentry)](IMTDeal/Enumerations.md#endealentry) | Deal direction.  
[EnDealReason (#endealreason)](IMTDeal/Enumerations.md#endealreason) | Reason for deal execution.  
[EnTradeModifyFlags (#endealreason)](IMTDeal/Enumerations.md#endealreason) | Deal modification flags.
