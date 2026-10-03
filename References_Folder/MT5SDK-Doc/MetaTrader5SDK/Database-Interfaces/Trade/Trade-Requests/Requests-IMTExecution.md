[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Trade](../../Trade.md) / [Trade Requests](../Requests.md) / Requests IMTExecution

[Previous](IMTConfirm/Requests-ExternalRetcode.md) | [Next](IMTExecution/Requests-Enumerations.md)

# IMTExecution

IMTExecution is an interface, through which an external system can manage the MetaTrader 5 trading platform. Using its methods, a trading platform receives the results of the execution of trading orders in the external system.

The IMTExecution class contains the following methods:

Method | Purpose  
---|---  
[Release](IMTExecution/Requests-Release.md) | Delete the current object.  
[Assign](IMTExecution/Requests-Assign.md) | Assign a passed object to the current one.  
[Clear](IMTExecution/Requests-Clear.md) | Clear an object.  
[Print](IMTExecution/Requests-Print.md) | Get a string description of a trade execution.  
[ID](IMTExecution/Requests-ID.md) | Get and set the ID of a trade execution.  
[ExternalID](IMTExecution/Requests-ExternalID.md) | Get and set the ID of a trade execution in an external trading system.  
[ExternalAccount](IMTExecution/Requests-ExternalAccount.md) | Get and set the account number in an external trading system.  
[Action](IMTExecution/Requests-Action.md) | Get and set the type of a trade execution.  
[Datetime](IMTExecution/Requests-Datetime.md) | Get and set the time of the trade execution in an external trading system.  
[DatetimeMsc](IMTExecution/Requests-DatetimeMsc.md) | Get and set the time of the trade execution in an external trading system, in the amount of milliseconds.  
[Login](IMTExecution/Requests-Login.md) | Get and set a client login in the MetaTrader 5 platform.  
[Group](IMTExecution/Requests-Group.md) | Get and set the group in the MetaTrader 5 platform, for the clients of which that execution can be applied.  
[Flags](IMTExecution/Requests-Flags.md) | Get and set additional flags of a trade execution.  
[Symbol](IMTExecution/Requests-Symbol.md) | Get the name of the symbol, for which trade execution is performed.  
[SymbolNew](IMTExecution/Requests-SymbolNew.md) | Get and set the name of a new symbol where position is relocated.  
[Digits](IMTExecution/Requests-Digits.md) | Get and set the number of decimal places in the price of a symbol, for which trade execution is performed.  
[Comment](IMTExecution/Requests-Comment.md) | Get and set a comment to a trade execution.  
[Order](IMTExecution/Requests-Order.md) | Get and set the number of the order in the MetaTrader 5 platform.  
[OrderExternalID](IMTExecution/Requests-OrderExternalID.md) | Get and set the number of the order in an external trading system.  
[OrderType](IMTExecution/Requests-OrderType.md) | Get and set order type.  
[OrderVolume](IMTExecution/Requests-OrderVolume.md) | Get and set the order volume in lots.  
[OrderVolumeExt](IMTExecution/Requests-OrderVolumeExt.md) | Get and set the order volume in lots with an extended accuracy.  
[OrderPrice](IMTExecution/Requests-OrderPrice.md) | Get and set the order price.  
[OrderActivationFlags](IMTExecution/Requests-OrderActivationFlags.md) | Get and set additional conditions of order activation.  
[OrderPriceTrigger](IMTExecution/Requests-OrderPriceTrigger.md) | Get and set the number of activation of a stop-limit order placed in an external trading system.  
[OrderTypeTime](IMTExecution/Requests-OrderTypeTime.md) | Get and set the expiration type of the order placed in an external trading system.  
[OrderTimeExpiration](IMTExecution/Requests-OrderTimeExpiration.md) | Get and set the expiration time of the order placed in an external trading system.  
[OrderTypeFill](IMTExecution/Requests-OrderTypeFill.md) | Get and set the filling type of the order placed in an external trading system.  
[OrderPriceSL](IMTExecution/Requests-OrderPriceSL.md) | Get and set the Stop Loss level specified for the order in an external trading system.  
[OrderPriceTP](IMTExecution/Requests-OrderPriceTP.md) | Get and set the Take Profit level specified for the order in an external trading system.  
[OrderActivationMode](IMTExecution/Requests-OrderActivationMode.md) | Get and set the activation type of the order placed in an external trading system.  
[DealExternalID](IMTExecution/Requests-DealExternalID.md) | Get and set the ID of the deal in an external trading system.  
[DealAction](IMTExecution/Requests-DealAction.md) | Get and set the deal type (direction).  
[DealVolume](IMTExecution/Requests-DealVolume.md) | Get and set the deal volume in lots.  
[DealVolumeExt](IMTExecution/Requests-DealVolumeExt.md) | Get and set the deal volume in lots with an extended accuracy.  
[DealVolumeRemaind](IMTExecution/Requests-DealVolumeRemaind.md) | Get and set the remaining volume in the order.  
[DealVolumeRemaindExt](IMTExecution/Requests-DealVolumeRemaindExt.md) | Get and set the remaining order volume with an extended accuracy.  
[DealPrice](IMTExecution/Requests-DealPrice.md) | Get and set the price of a deal.  
[DealReason](IMTExecution/Requests-DealReason.md) | Get and set the reason for a deal.  
[DealStorage](IMTExecution/Requests-DealStorage.md) | Get and set the swap size of a deal conducted as a result of trade execution.  
[DealCommission](IMTExecution/Requests-DealCommission.md) | Get and set the commission charged when conducting deals via a gateway in an external trading system.  
[Position](IMTExecution/Requests-Position.md) | Get and set a position ticket (unique number) in a MetaTrader 5 platform.  
[PositionBy](IMTExecution/Requests-PositionBy.md) | Get and set the ticket (unique number) of an opposite trade position in a MetaTrader 5 platform.  
[PositionExternalID](IMTExecution/Requests-PositionExternalID.md) | Get and set the ticket (a unique number) of a position in an external trading system.  
[PositionByExternalID](IMTExecution/Requests-PositionByExternalID.md) | Get and set the ticket (unique number) of an opposite trade position in an external trading system.  
[PositionPriceSL](IMTExecution/Requests-PositionPriceSL.md) | Get and set the Stop Loss level specified for a position in an external trading system.  
[PositionPriceTP](IMTExecution/Requests-PositionPriceTP.md) | Get and set the Take Profit level specified for a position in an external trading system.  
[EOSSessionStart](IMTExecution/Requests-EOSSessionStart.md) | Get and set the time of the session beginning.  
[EOSSessionEnd](IMTExecution/Requests-EOSSessionEnd.md) | Get and set the time of the session end.  
[EOSPriceSettlement](IMTExecution/Requests-EOSPriceSettlement.md) | Get and set the settlement (clearing) price of the session.  
[EOSProrfitRateBuy](IMTExecution/Requests-EOSProrfitRateBuy.md) | Get a new rate for recalculating profit/loss for buy deals.  
[EOSProrfitRateSell](IMTExecution/Requests-EOSProrfitRateSell.md) | Get a new rate for recalculating profit/loss for sell deals.  
[EOSProrfitRate](IMTExecution/Requests-EOSProrfitRate.md) | Set a new rate for recalculating profit/loss for the deals performed during the session.  
[EOSTickValue](IMTExecution/Requests-EOSTickValue.md) | Set a new tick price for recalculating profit/loss for the deals performed during the session.  
[EOSRolloverValueLong](IMTExecution/Requests-EOSRolloverValueLong.md) | Get the rollover size accrued by a long position.  
[EOSRolloverValueShort](IMTExecution/Requests-EOSRolloverValueShort.md) | Get the rollover size accrued by a short position.  
[EOSRolloverValue](IMTExecution/Requests-EOSRolloverValue.md) | Set the rollover size for a position.  
[ApiDataSet](IMTExecution/Requests-ApiDataSet.md) | Set a custom parameter for the trade execution.  
[ApiDataGet](IMTExecution/Requests-ApiDataGet.md) | Get the value of a custom parameter of the trade execution.  
[APIDataUpdate](IMTExecution/Requests-APIDataUpdate.md) | Add or update the custom parameter of the trade execution.  
[APIDataNext](IMTExecution/Requests-APIDataNext.md) | Gets the custom parameter of the trade execution by a position.  
[APIDataRawSet](IMTExecution/Requests-APIDataRawSet.md) | Set custom parameters for a trade execution as raw data (memory fragment).  
[APIDataRawGet](IMTExecution/Requests-APIDataRawGet.md) | Get custom parameters for a trade execution as raw data (memory fragment).  
[APIDataRawMax](IMTExecution/Requests-APIDataRawMax.md) | Get the maximum possible size of custom parameters of a trade execution.  
[ApiDataClear](IMTExecution/Requests-ApiDataClear.md) | Clear all custom parameters of trade executions set by an application.  
[ApiDataClearAll](IMTExecution/Requests-ApiDataClearAll.md) | Clear all user settings of trade executions.  
[PriceGateway](IMTExecution/Requests-PriceGateway.md) | Get and set the actual price of a deal conducted via a gateway in an external trading system with no consideration to the gateway price transformation settings.  
[GatewayID](IMTExecution/Requests-GatewayID.md) | Get and set the gateway ID from which the trade execution has been received.  
[ExternalRetcode](IMTExecution/Requests-ExternalRetcode.md) | Get and set the code of response from an external trading system.  
  
Possible types of trade executions are enumerated in [IMTExecution::EnTradeExecutions (#entradeexecutions)](IMTExecution/Requests-Enumerations.md#entradeexecutions). The type of trade execution is chosen according to the type of operation executed in an external system.

> For more information about the formation of trade executions read [Trade Operations in the Gateway API](../../../Gateway-API/Trade-Operations-in.md).

## Execution Processing Peculiarities

The MetaTrader 5 server correctly handles order opening from an external system even if that system has rejected the order earlier. For example, an order is sent to an exchange through a gateway, the exchange rejects the order. On the MetaTrader 5 side, the order is placed to the trade history marked as "Canceled". But later the exchange notifies that the order is placed. In this case, on the MetaTrader 5 side the order will be restored from the trade history with the same ticket.

The verification procedure for the orders received from an external system:

  * Checking if this order is available among open ones. If it is, then operation continues as normal.
  * If the order is found in the trading history (checking if the symbol, volume and direction match), it will be deleted from it. Then an attempt is made to open an order with the ticket matching the deleted order in accordance with the passed trade execution. The following entry is added to the journal: unknown open order #543 in execution, but found in history and will be reopened [added order #543, buy limit 1.00 BR-10.15 at 49.94 [based on order '40190126459']].
  * If the order is not found in the trading history, a new order with a new ticket is opened.


