[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Orders](../Orders.md) / OrderReopen

[Previous](OrderBackupRestore.md) | [Next](HistoryRequest.md)

# IMTAdminAPI::OrderReopen

Reopens a pending order from the client history.

C++
    
    
    MTAPIRES  IMTAdminAPI::OrderReopen(
       const UINT64  ticket      // The ticket of an order
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.OrderReopen(
       ulong         ticket      // The ticket of an order
       )

Python
    
    
    AdminAPI.OrderReopen(
       int           ticket      # The ticket of an order
       )

### Parameters

**ticket**  
[in] Ticket of an order to be reopened.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

Only [Limit, Stop and Stop Limit orders can be reopened (#enordertype)](../../../../Database-Interfaces/Trade/Orders/IMTOrder/Enumerations.md#enordertype). The order you want to reopen must exist in the client's history.

  * Changes the order status to Placed ([IMTOrder::State](../../../../Database-Interfaces/Trade/Orders/IMTOrder/State.md))
  * Removes the execution date ([IMTOrder::TimeDone](../../../../Database-Interfaces/Trade/Orders/IMTOrder/TimeDone.md), [IMTOrder::TimeDoneMsc](../../../../Database-Interfaces/Trade/Orders/IMTOrder/TimeDoneMsc.md))
  * Removes the execution price ([IMTOrder::PriceTrigger](../../../../Database-Interfaces/Trade/Orders/IMTOrder/PriceTrigger.md))
  * Sets the current volume ([IMTOrder::VolumeCurrent](../../../../Database-Interfaces/Trade/Orders/IMTOrder/VolumeCurrent.md)) to the initial one ([IMTOrder::VolumeInitial](../../../../Database-Interfaces/Trade/Orders/IMTOrder/VolumeInitial.md))
  * Resets the [IMTOrder::PositionID](../../../../Database-Interfaces/Trade/Orders/IMTOrder/PositionID.md) field to zero
  * Clears activation signs: [IMTOrder::ActivationTime](../../../../Database-Interfaces/Trade/Orders/IMTOrder/ActivationTime.md), [IMTOrder::ActivationPrice](../../../../Database-Interfaces/Trade/Orders/IMTOrder/ActivationPrice.md) and [IMTOrder::ActivationMode](../../../../Database-Interfaces/Trade/Orders/IMTOrder/ActivationMode.md)


  * Delete the [trade](../../../../Database-Interfaces/Trade/Deals/IMTDeal.md), which was opened in accordance with the order. If several trades were performed in connection with the order, delete all of them.
  * Fix the client's positions ([IMTAdminAPI::PositionFix](../Positions/PositionFix.md)).
  * Fix the client's balance ([IMTAdminAPI::UserBalanceCheck](../../Users/UserBalanceCheck.md)).


