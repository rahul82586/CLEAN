[🏠 Document Start](../../README.md) / [Server API](../README.md) / [Interface of Trade Events](../Interface-of-Trade-Events.md) / HookTradeInterest

[Previous](HookTradeRollover.md) | [Next](HookTradeInterestCharge.md)

# IMTTradeSink::HookTradeInterest

A hook of adding of calculating interest on available funds.
    
    
    virtual MTAPIRES  IMTTradeSink::HookTradeInterest(
       const INT64         datetime,           // Time of interest adding
       const IMTConGroup*  group,              // A pointer to the confirmation object
       const IMTAccount*   account,            // A pointer to the object of a trade account
       const double        original_value,     // Initial value
       double&             new_value           // Changed value
       )

### Parameters

**datetime**  
[in] The time of interest calculation in seconds that have elapsed since 01.01.1970.

**group**  
[in] A pointer to the object of theconfiguration of the groupof a client, for whom the interest is added.

**account**  
[in] A pointer to the object of atrading account, on which interest is added.

**original_value**  
[in] The initial value of interest calculated by the server.

**new_value**  
[out] The new value of annual interest.

### Return Value

In case of confirmation [MT_RET_OK](../../Return-Codes/Successful-completion.md) should be returned, otherwise, the request will be rejected with a response code returned from the hook. Thus, if the response code is different from MT_RET_OK, the interest is not added.

### Note

Initially, the values of original_value and new_value are equal. If the values are different, then the interest value has been changed (new_value) by one of the previous [hook handlers](../Hooks.md).
