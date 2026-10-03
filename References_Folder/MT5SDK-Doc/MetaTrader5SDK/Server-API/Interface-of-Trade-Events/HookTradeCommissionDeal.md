[🏠 Document Start](../../README.md) / [Server API](../README.md) / [Interface of Trade Events](../Interface-of-Trade-Events.md) / HookTradeCommissionDeal

[Previous](HookTradeCommissionOrder.md) | [Next](HookTradeCommissionCharge.md)

# IMTTradeSink::HookTradeCommissionDeal

A hook of the calculation of commission, which is charged during the execution of a deal. It is called before the calculation and charging/blocking commission on the account, allowing to use an individual commission calculation algorithm.
    
    
    virtual MTAPIRES  IMTTradeSink::HookTradeCommissionDeal(
       const IMTConCommission*  commission,     // A pointer to the commission object
       const IMTConGroup*       group,          // A pointer to the group object
       const IMTConSymbol*      symbol,         // A pointer to the object of the symbol configuration
       const IMTDeal*           deal,           // A pointer to the deal object
       const double             original_value, // Initial value
       double&                  new_value       // Update value
       )

### Parameters

**commission**  
[in] A pointer to theobject of commission configuration, in accordance with which the amount of commission to charge is calculated.

**group**  
[in] A pointer to the object of theconfiguration of the groupof a client, for whom the commission is calculated.

**symbol**  
[in]The object of the symbol, for which a trade operation whose commission is being calculated, has been requested.

**deal**  
[in]The object of the deal, for which the amount of commission to charge is being calculated.

**original_value**  
[in] The initial value of commission that will be charged.

**new_value**  
[out] The modified value of commission that will be charged.

### Return Value

In case of confirmation [MT_RET_OK](../../Return-Codes/Successful-completion.md) should be returned, otherwise, the request will be rejected with a response code returned from the hook. Thus, if the response code is different from MT_RET_OK, the interest is not added.

### Note

Initially, the values of original_value and new_value are equal. If the values are different, then the interest value has been changed (new_value) by one of the previous [hook handlers](../Hooks.md).

  * Once an order is created, a commission is calculated for this order, and IMTTradeSink::HookTradeCommissionOrder is called.
  * The appropriate commission value is blocked on the client's account.
  * A deal is performed based on that order. Commission is recalculated for the actually executed deal (its volume) and IMTTradeSink::HookTradeCommissionDeal is called.
  * The previously blocked commission amount is updated.


