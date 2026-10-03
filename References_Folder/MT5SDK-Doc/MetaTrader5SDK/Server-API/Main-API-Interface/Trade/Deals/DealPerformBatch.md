[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Deals](../Deals.md) / DealPerformBatch

[Previous](DealPerformCloseBy.md) | [Next](DealPerformBatchArray.md)

# IMTServerAPI::DealPerformBatch

Perform multiple deals on the client's account. This method performs market buy or sell operations on the account as if they were performed by the client through the terminal. The only difference is that trade requests and orders are not created to perform the deals, and thus routing rules are not applied to the operations. In all other respects, the behavior the same: deal execution results are applied to positions and to the account trading state; commissions are calculated and charged for the deals in accordance with the relevant account group settings.
    
    
    MTAPIRES  IMTServerAPI::DealPerformBatch(
       IMTDealArray*   deals,         // Array of deals
       MTAPIRES*       results        // Array of results
       )

### Parameters

**deals**  
[in] A pointer to the array of dealsIMTDealArray.

**results**  
[out] An array with deal execution results. The size of the 'results' array must not be less than the size of the 'deals' array.

### Return Value

The [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code indicates that all the specified deals have been executed. The [MT_RET_ERR_PARTIAL](../../../../Return-Codes/Common-errors.md) response code means that only some of the deals have been executed. Analyze the 'results' array for more details on the execution results. This array features the results of execution of each individual deal from the 'deals' array. The result index corresponds to the deal index in the source array.

### Note

Deals can only be performed on the account that is opened on the same server to which the application is connected.

  * [IMTDeal::Login](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Login.md)
  * [IMTDeal::Symbol](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Symbol.md)
  * [IMTDeal::Action](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Action.md) (only IMTDeal::DEAL_BUY and IMTDeal::DEAL_SELL values are allowed)
  * [IMTDeal::Volume](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Volume.md)
  * [IMTDeal::Price](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Price.md)
  * [IMTDeal::PositionID](../../../../Database-Interfaces/Trade/Deals/IMTDeal/PositionID.md) (when closing a position on a hedging account)



You can additionally specify individual margin ([IMTDeal::RateMargin](../../../../Database-Interfaces/Trade/Deals/IMTDeal/RateMargin.md)) and profit ([IMTDeal::RateProfit](../../../../Database-Interfaces/Trade/Deals/IMTDeal/RateProfit.md)) recalculation rates in the deal. If not specified, calculated rates will be used.

If commission ([IMTDeal::Commission](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Commission.md)) is specified in the deal, it will be applied to the client account. However, it does not replace the commission charged in accordance with the trader's group settings ([IMTConGroup::Commission*](../../../../Configuration-Interfaces/Groups/IMTConGroup/CommissionAdd.md)). Therefore, the commission specified in the deal is summed up with the calculated commission. 

The deal profit is always calculated by the server even if you specify it in the [IMTDeal::Profit](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Profit.md) field. If necessary, the server charges the deal commission automatically (in accordance with the [commission settings](../../../../Configuration-Interfaces/Groups/IMTConCommission.md)).

It is not recommended to call the IMTServerAPI::DealPerformBatch method from the [IMTDealSink::OnDealAdd](../../../../Database-Interfaces/Trade/Deals/IMTDealSink/OnDealAdd.md), [IMTDealSink::OnDealUpdate](../../../../Database-Interfaces/Trade/Deals/IMTDealSink/OnDealUpdate.md) and [IMTDealSink::OnDealPerform](../../../../Database-Interfaces/Trade/Deals/IMTDealSink/OnDealPerform.md) handlers.
