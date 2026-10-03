[🏠 Document Start](../../README.md) / [Server API](../README.md) / [Interface of Trade Events](../Interface-of-Trade-Events.md) / HookTradeRequestRoute

[Previous](HookTradeRequestAdd.md) | [Next](HookTradeRequestProcess.md)

# IMTTradeSink::HookTradeRequestRoute

A hook of [trade request](../../Database-Interfaces/Trade/Trade-Requests/Requests-IMTRequest.md) routing in a requests queue.
    
    
    virtual MTAPIRES  IMTTradeSink::HookTradeRequestRoute(
       IMTRequest*          request,      // A pointer to the request object
       IMTConfirm*          confirm,      // A pointer to the confirmation object
       const IMTConGroup*   group,        // Group
       const IMTConSymbol*  symbol,       // Obsolete parameter
       const IMTPosition*   position,     // Obsolete parameter
       const IMTOrder*      order         // A pointer to the order object
       )

### Parameters

**request**  
[in][out] A pointer to the object ofa trade request.

**confirm**  
[in][out] A pointer to the object ofconfirmation of a trade request, as a result of which a deal is executed.

**group**  
[in] A pointer to the object of thegroupto which the client who has send the request belongs.

**symbol**  
[in] This parameter is obsolete. Its value is always NULL.

**position**  
[in] This parameter is obsolete. Its value is always NULL.

**order**  
[in] A pointer to the object of atrade order, which corresponds to the request being processed: a newly created or modified order.

### Return Value

If the response code [MT_RET_REQUEST_DONE](../../Return-Codes/Trade-Requests.md) is returned from the hook, the request will be confirmed without applying routing rules. If [MT_RET_OK](../../Return-Codes/Successful-completion.md) is returned, the request will be processed according to the routing rule. In case any other response code is returned, the request will be rejected with that response code.
