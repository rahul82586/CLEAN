[🏠 Document Start](../../README.md) / [Server API](../README.md) / [Interface of Trade Events](../Interface-of-Trade-Events.md) / HookTradeCommissionOrder

[Previous](HookTradeInterestChargeDeal.md) | [Next](HookTradeCommissionDeal.md)

# IMTTradeSink::HookTradeCommissionOrder

A hook of the calculation of commission, which is blocked on an account during the placing of an order.
    
    
    virtual MTAPIRES  IMTTradeSink::HookTradeCommissionOrder(
       const IMTConCommission*  commission,     // A pointer to the commission object
       const IMTConGroup*       group,          // A pointer to the group object
       const IMTConSymbol*      symbol,         // A pointer to the object of the symbol configuration
       const IMTOrder*          order,          // A pointer to the order object
       const double             original_value, // Initial value
       double&                  new_value       // Update value
       )

### Parameters

**commission**  
[in] A pointer to theobject of commission configuration, in accordance with which the amount to lock is calculated.

**group**  
[in] A pointer to the object of theconfiguration of the groupof a client, for whom the locked commission is calculated.

**symbol**  
[in]The object of the symbol, for which a trade operation whose commission is being calculated, has been requested.

**order**  
[in]The object of the symbol, for which a trade operation whose commission is being calculated, has been requested.

**original_value**  
[in] The initial value of commission that will be locked.

**new_value**  
[out] The modified value of commission that will be locked.

### Return Value

In case of confirmation [MT_RET_OK](../../Return-Codes/Successful-completion.md) should be returned, otherwise, the request will be rejected with a response code returned from the hook. Thus, if the response code is different from MT_RET_OK, the commission will not be blocked.

### Note

Initially, the values of original_value and new_value are equal. If the values are different, then the interest value has been changed (new_value) by one of the previous [hook handlers](../Hooks.md).

  * Once an order is created, a commission is calculated for this order, and IMTTradeSink::HookTradeCommissionOrder is called.
  * The appropriate commission value is blocked on the client's account.
  * A deal is performed based on that order. Commission is recalculated for the actually executed deal (its volume) and IMTTradeSink::HookTradeCommissionDeal is called.
  * The previously blocked commission amount is updated.


