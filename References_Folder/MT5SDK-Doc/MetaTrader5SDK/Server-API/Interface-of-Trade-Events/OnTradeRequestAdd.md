[🏠 Document Start](../../README.md) / [Server API](../README.md) / [Interface of Trade Events](../Interface-of-Trade-Events.md) / OnTradeRequestAdd

[Previous](../Interface-of-Trade-Events.md) | [Next](OnTradeRequestUpdate.md)

# IMTTradeSink::OnTradeRequestAdd

A handler of the event of adding a checked [trade request](../../Database-Interfaces/Trade/Trade-Requests/Requests-IMTRequest.md) in the requests queue.
    
    
    virtual void  IMTTradeSink::OnTradeRequestAdd(
       const IMTRequest*    request,      // A pointer to the request object
       const IMTConGroup*   group,        // A pointer to the group configuration object
       const IMTConSymbol*  symbol,       // A pointer to the symbol configuration object
       const IMTPosition*   position,     // A pointer to the position object
       const IMTOrder*      order         // A pointer to the order object
       )

### Parameters

**request**  
[in] A pointer to the object of atrade request.

**group**  
[in] A pointer to the object of theconfiguration of the groupof a client, for whom the request is being processed.

**symbol**  
[in] A pointer to the object of theconfiguration of a symbol, which request is being processed.

**position**  
[in] A pointer to the object of atrade position, which corresponds to the client and symbol, for which a request is being processed.

**order**  
[in] A pointer to the object of atrade order, which corresponds to the request being processed: a newly created or modified order.

### Note

This method notifies that the correctness of the appropriate trade request has been check and it has been added to the trade requests queue.
