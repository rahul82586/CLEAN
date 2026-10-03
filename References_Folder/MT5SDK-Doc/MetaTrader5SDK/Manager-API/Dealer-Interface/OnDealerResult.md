[🏠 Document Start](../../README.md) / [Manager API](../README.md) / [Dealer Interface](../Dealer-Interface.md) / OnDealerResult

[Previous](../Dealer-Interface.md) | [Next](OnDealerAnswer.md)

# IMTDealerSink::OnDealerResult

Asynchronous answer to a dealer's trade request in the form of the object of confirmation.

C++
    
    
    virtual void  IMTDealerSink::OnDealerResult(
       const IMTConfirm*  result      // Request confirmation result
       )

.NET
    
    
    virtual void  CIMTDealerSink.OnDealerResult(
       CIMTConfirm        result      // Request confirmation result
       )

### Parameters

**result**  
[in] The result ofconfirmation of the trade request.

### Note

The method is obsolete, it is recommended to use [IMTDealerSink::OnDealerAnswer](OnDealerAnswer.md) instead.
