[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequestSink](../Requests-IMTRequestSink.md) / Requests OnRequestUpdate

[Previous](Requests-OnRequestAdd.md) | [Next](Requests-OnRequestDelete.md)

# IMTRequestSink::OnRequestUpdate

A handler of the event of trade request change.

C++
    
    
    virtual void  IMTRequestSink::OnRequestUpdate(
       const IMTRequest*  request      // A pointer to the request object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTRequestSink.OnRequestUpdate(
       CIMTRequest        request      // An object of a trade request
       )

### Parameters

**request**  
[in] A pointer to the object of the changed request.

### Note

This method is called by the API to notify that a trade request has been modified.
