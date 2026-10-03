[🏠 Document Start](../../README.md) / [Server API](../README.md) / [Interface of Trade Events](../Interface-of-Trade-Events.md) / HookTradeRollover

[Previous](HookTradeRequestRuleApply.md) | [Next](HookTradeInterest.md)

# IMTTradeSink::HookTradeRollover

A hook of rollover charging.
    
    
    virtual MTAPIRES  IMTTradeSink::HookTradeRollover(
       const INT64          datetime,           // Time of charging
       const IMTConGroup*   group,              // A pointer to the group object
       const IMTConSymbol*  symbol,             // A pointer to the object of the symbol configuration
       const IMTPosition*   position,           // A pointer to the position object
       const double         original_value,     // Initial value
       double&              new_value           // Modified value
       )

### Parameters

**datetime**  
[in] The time of rollover charging in seconds that have elapsed since 01.01.1970.

**group**  
[in] A pointer to the object of theconfiguration of the group, for which rollover is charged.

**symbol**  
[in] A pointer to the object of theconfiguration of a symbol, for which rollover is charged.

**position**  
[in] A pointer to the object of atrade position, which corresponds to the group and financial instrument, for which rollover is charged.

**original_value**  
[in] The initial rollover value calculated by the server.

**new_value**  
[in][out] The new value of the rollover.

### Return Value

In case of confirmation [MT_RET_OK](../../Return-Codes/Successful-completion.md) should be returned, otherwise, the request will be rejected with a response code returned from the hook. Thus, if the response code is different from MT_RET_OK, the rollover is not charged.

### Note

Initially, the values of original_value and new_value are equal. If the values are different, then the rollover value has been changed (new_value) by one of the previous [hook handlers](../Hooks.md).
