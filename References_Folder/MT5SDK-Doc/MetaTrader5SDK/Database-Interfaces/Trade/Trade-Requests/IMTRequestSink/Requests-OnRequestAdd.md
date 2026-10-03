[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequestSink](../Requests-IMTRequestSink.md) / Requests OnRequestAdd

[Previous](../Requests-IMTRequestSink.md) | [Next](Requests-OnRequestUpdate.md)

# IMTRequestSink::OnRequestAdd

A handler of the event of adding a trade request.

C++
    
    
    virtual void  IMTRequestSink::OnRequestAdd(
       const IMTRequest*  request      // A pointer to the request object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTRequestSink.OnRequestAdd(
       CIMTRequest        request      // An object of a trade request
       )

### Parameters

**request**  
[in] A pointer to the object of the added request.

### Note

This method is called by the API to notify that a new trade request has been added.
