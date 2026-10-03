[🏠 Document Start](../../README.md) / [Gateway API](../README.md) / [Event Interface](../Event-Interface.md) / OnDealerAnswer

[Previous](OnGatewayAccountAnswer.md) | [Next](OnDealerLock.md)

# IMTGatewaySink::OnDealerAnswer

A handler of the event notifying on a request confirmation result.

C++
    
    
    virtual void  IMTGatewaySink::OnDealerAnswer(
       const MTAPIRES    retcode,      // Result
       const IMTConfirm* confirm       // Request confirmation object
       )

.NET
    
    
    virtual void  CIMTGatewaySink.OnDealerAnswer(
       MTRetCode         retcode,      // Result
       CIMTConfirm       confirm       // Request confirmation object
       )

### Parameters

**retcode**  
[in] Request confirmationresult code.MT_RET_OKis returned, in case a request is confirmed successfully.

**confirm**  
[in]Request confirmation object.

# IMTGatewaySink::OnDealerAnswer

A handler of the event notifying on a request execution result.

C++
    
    
    virtual void  IMTGatewaySink::OnDealerAnswer(
       const UINT64        login,        // Server ID
       const MTAPIRES      retcode,      // Result
       const IMTExecution* execution     // Trade execution object
       )

.NET
    
    
    virtual void  CIMTGatewaySink.OnDealerAnswer(
       ulong               login,        // Server ID
       MTRetCode           retcode,      // Result
       CIMTExecution       execution     // Trade execution object
       )

### Parameters

**login**  
[in] Identifier of a server that has executed the request.

**retcode**  
[in] Request executionresult code.MT_RET_OKis returned, in case a request is executed successfully.

**execution**  
[in]Trade execution object.

### Note

This event informs about the result of applying a trade execution object [IMTExecution](../../Database-Interfaces/Trade/Trade-Requests/Requests-IMTExecution.md) sent via [IMTGatewayAPI:DealerExecuteAsync](../Main-Interface/Processing-Trade-Requests/DealerExecuteAsync.md) to a trade server data base.
