[🏠 Document Start](../../README.md) / [Server API](../README.md) / [Interface of Trade Events](../Interface-of-Trade-Events.md) / HookTradeExecution

[Previous](HookTradeCommissionCharge.md) | [Next](HookTradeSplit.md)

# IMTTradeSink::HookTradeExecution

A hook of applying a trade execution.
    
    
    virtual MTAPIRES  IMTTradeSink::HookTradeExecution(
       const IMTConGateway* gateway,      // A pointer to the gateway configuration
       const IMTExecution*  execution,    // A pointer to the trade execution object
       const IMTConGroup*   group,        // A pointer to the group configuration object
       const IMTConSymbol*  symbol,       // A pointer to the symbol configuration object
       IMTPosition*         position,     // A pointer to the position object
       IMTOrder*            order,        // A pointer to the order object
       IMTDeal*             deal          // A pointer to the deal object
       )

### Parameters

**gateway**  
[in] A pointer to the object of agateway configurationthe trade execution is received from. This parameter is not used and is always equal to NULL.

**execution**  
[in] A pointer to the object of thetrade executionreceived.

**group**  
[in] A pointer to the object of theconfiguration of the groupof a client, for whom the trade execution is being processed.

**symbol**  
[in][out] A pointer to the object of theconfiguration of a symbol, for which the trade execution is being processed.

**position**  
[in][out] A pointer to the object of atrade position, which corresponds to the client and symbol, for which the trade execution is being processed.

**order**  
[in][out] A pointer to the object of atrade order, which corresponds to the trade execution being processed.

**deal**  
[in][out] A pointer to the object of atrade dealcreated as a result of applying the trade execution.

### Return Value

In case of confirmation [MT_RET_OK](../../Return-Codes/Successful-completion.md) should be returned, otherwise, the trade execution be rejected with a response code returned from the hook. Thus, if the response code is different from MT_RET_OK, the trade execution will not be applied.

### Note

Depending on the request type, parameters symbol, position and order can be equal to NULL.
