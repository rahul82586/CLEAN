[🏠 Document Start](../../README.md) / [Gateway API](../README.md) / [Event Interface](../Event-Interface.md) / OnDealerLock

[Previous](OnDealerAnswer.md) | [Next](HookServerConnect.md)

# IMTGatewaySink::OnDealerLock

A handler of the event of capturing (blocking) of a successive trade request from a requests queue.

C++
    
    
    virtual void  IMTGatewaySink::OnDealerLock(
       const MTAPIRES     retcode,       // Result
       const IMTRequest*  request,       // An object of a trade request
       const IMTUser*     user,          // An object of a client record
       const IMTAccount*  account,       // An object of a trading account
       const IMTOrder*    order,         // An order object
       const IMTPosition* position       // Position object
       )

.NET
    
    
    virtual void  CIMTGatewaySink.OnDealerLock(
       MTRetCoed          retcode,       // Result
       CIMTRequest        request,       // An object of a trade request
       CIMTUser           user,          // An object of a client record
       CIMTAccount        account,       // An object of a trading account
       CIMTOrder          order,         // An order object
       CIMTPosition       position       // Position object
       )

### Parameters

**retcode**  
[in] Trading request captureresult code.MT_RET_OKis returned, in case of a successful capture. Code MT_RET_OK_NONE means that the request is no longer available on the trade server. For example, it could have been captured by another dealer or application.

**request**  
[in] Capturedtrade request object.

**user**  
[in]Client record objectwho formed a request.

**account**  
[in]Trading account objectof the client who formed a request.

**order**  
[in]Object of the orderthat corresponds to a request.

**position**  
[in] Clientposition objectby the request instrument before its execution.

### Note

The method is used only for gateways.
