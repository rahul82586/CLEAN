[🏠 Document Start](../../README.md) / [Server API](../README.md) / [Interface of Trade Events](../Interface-of-Trade-Events.md) / OnTradeRequestProcess

[Previous](OnTradeRequestDelete.md) | [Next](OnTradeRequestProcessCloseBy.md)

# IMTTradeSink::OnTradeRequestProcess

A handler of the event of a successful execution of a [trade request](../../Database-Interfaces/Trade/Trade-Requests/Requests-IMTRequest.md).
    
    
    virtual void  IMTTradeSink::OnTradeRequestProcess(
       const IMTRequest*    request,      // A pointer to the request object
       const IMTConfirm*    confirm,      // A pointer to the confirmation object
       const IMTConGroup*   group,        // A pointer to the group configuration object
       const IMTConSymbol*  symbol,       // A pointer to the symbol configuration object
       const IMTPosition*   position,     // A pointer to the position object
       const IMTOrder*      order,        // A pointer to the order object
       const IMTDeal*       deal          // A pointer to the deal object
       )

### Parameters

**request**  
[in] A pointer to the object of atrade request.

**confirm**  
[in] A pointer to the object ofconfirmation of a trade request, as a result of which a deal is executed.

**group**  
[in] A pointer to the object of theconfiguration of the groupof a client, for whom the request is being processed.

**symbol**  
[in] A pointer to the object of theconfiguration of a symbol, which request is being processed.

**position**  
[in] A pointer to the object of atrade position, which corresponds to the client and symbol, for which a request is being processed.

**order**  
[in] A pointer to the object of atrade order, which corresponds to the request being processed: a newly created or modified order. Please note that the method passes the current order state, not the future one as after its execution. For example, if the handler triggered during the execution of the order modification request, you will receive information about the initial order state and not about the modified one.

**deal**  
[in][ A pointer to the object of atrade dealcreated as a result of the execution of a trade request.

### Note

This method notifies that the corresponding request has been filled and provides additional information.
