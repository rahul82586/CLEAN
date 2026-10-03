[🏠 Document Start](../../README.md) / [Server API](../README.md) / [Interface of Trade Events](../Interface-of-Trade-Events.md) / OnTradeRequestRefuse

[Previous](OnTradeRequestProcessCloseBy.md) | [Next](OnTradeExecution.md)

# IMTTradeSink::OnTradeRequestRefuse

A handler of the event of refusal to execute a [trade request](../../Database-Interfaces/Trade/Trade-Requests/Requests-IMTRequest.md) before it is added to the queue. 
    
    
    virtual void  IMTTradeSink::OnTradeRequestRefuse(
       const IMTRequest*    request       // A pointer to the request object
       )

### Parameters

**request**  
[in] A pointer to the object of the rejectedtrade request.

### Note

Execution can be refused for some reasons, for example due to incorrect parameters or insufficient funds. The exact reason is added to the trade request field [IMTRequest::ResultRetcode](../../Database-Interfaces/Trade/Trade-Requests/IMTRequest/Requests-ResultRetcode.md).
