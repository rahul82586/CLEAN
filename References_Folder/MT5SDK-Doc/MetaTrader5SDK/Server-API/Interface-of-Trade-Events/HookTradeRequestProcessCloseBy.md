[🏠 Document Start](../../README.md) / [Server API](../README.md) / [Interface of Trade Events](../Interface-of-Trade-Events.md) / HookTradeRequestProcessCloseBy

[Previous](HookTradeRequestProcess.md) | [Next](HookTradeRequestRuleFilter.md)

# IMTTradeSink::HookTradeRequestProcessCloseBy

A hook of execution of the [trade request](../../Database-Interfaces/Trade/Trade-Requests/Requests-IMTRequest.md) to close a position by an opposite one (TA_CLOSE_BY or TA_DEALER_CLOSE_BY).
    
    
    virtual MTAPIRES  IMTTradeSink::HookTradeRequestProcessCloseBy(
       const IMTRequest*    request,      // A pointer to the request object
       const IMTConfirm*    confirm,      // A pointer to the confirmation object
       const IMTConGroup*   group,        // A pointer to the group configuration object
       const IMTConSymbol*  symbol,       // A pointer to the symbol configuration object
       IMTPosition*         position,     // A pointer to the position object
       IMTOrder*            order,        // A pointer to the order object
       IMTDeal*             deal,         // A pointer to the deal object to close the source position
       IMTDeal*             deal_by       // A pointer to the deal object to close the opposite position
       )

### Parameters

**request**  
[in] A pointer to the object of atrade request.

**confirm**  
[in] A pointer to the object ofconfirmation of a trade request, as a result of which a deal is executed.

**group**  
[in] A pointer to the object of theconfiguration of the group of a client, for whom the request is being processed.

**symbol**  
[in] A pointer to the object of theconfiguration of a symbol, which request is being processed.

**position**  
[in][out] A pointer to the object of atrade position, which corresponds to the client and symbol, for which a request is being processed.

**order**  
[in][out] A pointer to the object of atrade order, which corresponds to the request being processed: a newly created or modified order.

**deal**  
[in] A pointer to the object of thedealofENTRY_OUT_BYtype, which was executed in order to close the source position.

**deal_by**  
[in] A pointer to the object of thedealofENTRY_OUT_BYtype, which was executed in order to close the opposite position.

### Return Value

In case of confirmation [MT_RET_OK](../../Return-Codes/Successful-completion.md) should be returned, otherwise, the request will be rejected with a response code returned from the hook.

### Note

Note that after the execution of a specified order, a deal and a position will be passed in a recalculated state. Therefore, you should ensure the integrity of the changed data.
