[🏠 Document Start](../../README.md) / [Server API](../README.md) / [Interface of Trade Events](../Interface-of-Trade-Events.md) / OnTradeRequestDelete

[Previous](OnTradeRequestUpdate.md) | [Next](OnTradeRequestProcess.md)

# IMTTradeSink::OnTradeRequestDelete

A handler of the event of a [trade request](../../Database-Interfaces/Trade/Trade-Requests/Requests-IMTRequest.md) deletion.
    
    
    virtual void  IMTTradeSink::OnTradeRequestDelete(
       const IMTRequest*  request      // A pointer to the request object
       )

### Parameters

**request**  
[in] A pointer to the object of a trade request.

### Note

This method notifies of the removal of a trade request. To get the reason for the removal, the [IMTRequest::ResultRetcode](../../Database-Interfaces/Trade/Trade-Requests/IMTRequest/Requests-ResultRetcode.md) property of a trade request should be analyzed.
