[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTSubscriptionHistory](../IMTSubscriptionHistory.md) / AmountDigits

[Previous](Amount.md) | [Next](AmountDeal.md)

# IMTSubscriptionHistory::AmountDigits

Get the number of decimal places in the subscription payment amount.

C++
    
    
    UINT  IMTSubscriptionHistory::AmountDigits()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTSubscriptionHistory.AmountDigits()

### Return Value

The number of decimal places in the subscription payment amount.

### Note

The payment amount is determined by the [IMTSubscriptionHistory::Amount](Amount.md) property.

# IMTSubscriptionHistory::AmountDigits

Set the number of decimal places in the subscription payment amount.

C++
    
    
    MTAPIRES  IMTSubscriptionHistory::AmountDigits(
       UINT  digits      // The number of decimal places
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTSubscriptionHistory.AmountDigits(
       uint  digits      // The number of decimal places
       )

### Parameters

**digits**  
[in] The number of decimal places in the subscription payment amount.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.

### Note

The payment amount is determined by the [IMTSubscriptionHistory::Amount](Amount.md) property.
