[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequestSink](../Requests-IMTRequestSink.md) / Requests OnRequestDelete

[Previous](Requests-OnRequestUpdate.md) | [Next](Requests-OnRequestSync.md)

# IMTRequestSink::OnRequestDelete

A handler of the event of a trade request deletion.

C++
    
    
    virtual void  IMTRequestSink::OnRequestDelete(
       const IMTRequest*  request      // A pointer to the request object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTRequestSink.OnRequestDelete(
       CIMTRequest        request      // A pointer to the request object
       )

### Parameters

**request**  
[in] A pointer to the object of the deleted request.

### Note

This method is called by the API to notify that a trade request has been deleted.
