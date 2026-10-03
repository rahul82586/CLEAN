[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTSubscriptionHistory](../IMTSubscriptionHistory.md) / AmountDeal

[Previous](AmountDigits.md) | [Next](../IMTSubscriptionHistoryArray.md)

# IMTSubscriptionHistory::AmountDeal

Get the ticket of the deal by which the subscription payment was conducted.

C++
    
    
    UINT64  IMTSubscriptionHistory::AmountDeal()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTSubscriptionHistory.AmountDeal()

### Return Value

Deal ticket ([IMTDeal::Deal](../../Trade/Deals/IMTDeal/Deal.md)).

# IMTSubscriptionHistory::AmountDeal

Set the ticket of the deal by which the subscription payment will be made.

C++
    
    
    MTAPIRES  IMTSubscriptionHistory::AmountDeal(
       const UINT64  deal      // Deal ticket
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTSubscriptionHistory.AmountDeal(
       ulong         deal      // Deal ticket
       )

### Parameters

**deal**  
[in] Deal ticket (IMTDeal::Deal).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.
