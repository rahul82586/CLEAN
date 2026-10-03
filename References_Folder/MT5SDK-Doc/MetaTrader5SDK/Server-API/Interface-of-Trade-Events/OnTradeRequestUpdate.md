[🏠 Document Start](../../README.md) / [Server API](../README.md) / [Interface of Trade Events](../Interface-of-Trade-Events.md) / OnTradeRequestUpdate

[Previous](OnTradeRequestAdd.md) | [Next](OnTradeRequestDelete.md)

# IMTTradeSink::OnTradeRequestUpdate

A handler of the event that the state of a [trade request](../../Database-Interfaces/Trade/Trade-Requests/Requests-IMTRequest.md) has changed.
    
    
    virtual void  IMTTradeSink::OnTradeRequestUpdate(
       const IMTRequest*  request      // A pointer to the request object
       )

### Parameters

**request**  
[in] A pointer to the object of atrade request.

### Note

This method notifies that the state of a trade request has changed during its processing.
