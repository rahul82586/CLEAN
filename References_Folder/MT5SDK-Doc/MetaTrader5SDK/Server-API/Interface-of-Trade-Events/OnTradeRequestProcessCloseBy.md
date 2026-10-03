[🏠 Document Start](../../README.md) / [Server API](../README.md) / [Interface of Trade Events](../Interface-of-Trade-Events.md) / OnTradeRequestProcessCloseBy

[Previous](OnTradeRequestProcess.md) | [Next](OnTradeRequestRefuse.md)

# IMTTradeSink::OnTradeRequestProcessCloseBy

A handler of the successful execution of a [trade request](../../Database-Interfaces/Trade/Trade-Requests/Requests-IMTRequest.md) to close a position by an opposite one (TA_CLOSE_BY or TA_DEALER_CLOSE_BY).
    
    
    virtual void  IMTTradeSink::OnTradeRequestProcessCloseBy(
       const IMTRequest*    request,      // A pointer to the request object
       const IMTConfirm*    confirm,      // A pointer to the confirmation object
       const IMTConGroup*   group,        // A pointer to the group configuration object
       const IMTConSymbol*  symbol,       // A pointer to the symbol configuration object
       const IMTPosition*   position,     // A pointer to the position object
       const IMTOrder*      order,        // A pointer to the order object
       const IMTDeal*       deal,         // A pointer to the deal object to close the source position
       const IMTDeal*       deal_by       // A pointer to the deal object to close the opposite position
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
[in] A pointer to the object of atrade order, which corresponds to the request being processed: a newly created or modified order.

**deal**  
[in] A pointer to the object of thedealofENTRY_OUT_BYtype, which was executed in order to close the source position.

**deal_by**  
[in] A pointer to the object of thedealofENTRY_OUT_BYtype, which was executed in order to close the opposite position.

### Note

This method notifies that the corresponding request has been filled and provides additional information.
