[🏠 Document Start](../../README.md) / [Server API](../README.md) / [Interface of Trade Events](../Interface-of-Trade-Events.md) / HookTradeCommissionCharge

[Previous](HookTradeCommissionDeal.md) | [Next](HookTradeExecution.md)

# IMTTradeSink::HookTradeCommissionCharge

Hook of final adding/withdrawal of commissions from an account at the end of a day/month.
    
    
    virtual MTAPIRES  IMTTradeSink::HookTradeCommissionCharge(
       const INT64              period_start,   // Beginning of period
       const INT64              period_end,     // End of period
       const IMTConCommission*  commission,     // A pointer to the commission object
       const IMTConGroup*       group,          // A pointer to the group object
       const IMTUser*           user,           // A pointer to the user object
       const double             original_value, // Initial value
       double&                  new_value       // Update value
       )

### Parameters

**period_start**  
[in] The beginning of the period for which the final commission amount is added/withdrawn, in seconds that have elapsed since 01.01.1970.

**period_end**  
[in] The end of the period for which the final commission amount is added/withdrawn, in seconds that have elapsed since 01.01.1970.

**commission**  
[in] A pointer to thecommission configuration object, in accordance with which the commission amount is added/withdrawn.

**group**  
[in] A pointer to the object of theconfiguration of the groupof a client, for whom the commission is added/withdrawn.

**user**  
[in] A pointer to theobject of the client record, for which the commission is added/withdrawn.

**original_value**  
[in] The initial value of commissions that will be added/withdrawn.

**new_value**  
[out] The modified value of commissions that will be added/withdrawn.

### Return Value

In case of confirmation [MT_RET_OK](../../Return-Codes/Successful-completion.md) should be returned, otherwise, the request will be rejected with a response code returned from the hook. Thus, if the response code is different from MT_RET_OK, the commission is not charged.

### Note

Initially, the values of original_value and new_value are equal. If the values are different, then the interest value has been changed (new_value) by one of the previous [hook handlers](../Hooks.md).
