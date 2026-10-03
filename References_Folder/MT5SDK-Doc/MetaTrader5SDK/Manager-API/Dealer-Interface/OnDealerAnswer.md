[🏠 Document Start](../../README.md) / [Manager API](../README.md) / [Dealer Interface](../Dealer-Interface.md) / OnDealerAnswer

[Previous](OnDealerResult.md) | [Next](../Interface-of-Events.md)

# IMTDealerSink::OnDealerAnswer

Asynchronous answer to a dealer's trade request in the form of the object of request.

C++
    
    
    virtual void  IMTDealerSink::OnDealerAnswer(
       const IMTRequest*  request      // An object of a trade request
       )

.NET
    
    
    virtual void  CIMTDealerSink.OnDealerAnswer(
       CIMTRequest        request      // An object of a trade request
       )

### Parameters

**request**  
[in]An object of the trade request.

### Note

This method is an asynchronous response of the server to a dealer's trade request performed using the [IMTManagerAPI::DealerSend](../Manager-Interface/Trade-Activity/Dealing/DealerSend.md) method.
