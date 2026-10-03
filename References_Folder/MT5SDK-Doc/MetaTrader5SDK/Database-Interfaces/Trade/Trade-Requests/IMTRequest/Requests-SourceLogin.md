[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequest](../Requests-IMTRequest.md) / Requests SourceLogin

[Previous](Requests-IP.md) | [Next](Requests-Position.md)

# IMTRequest::SourceLogin

Get the login of the dealer, on whose behalf the request is performed.

C++
    
    
    UINT64  IMTRequest::SourceLogin()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTRequest.SourceLogin()

### Return Value

The login of the dealer, on whose behalf the request is performed.

# IMTRequest::SourceLogin

Set the login of the dealer, on whose behalf the request is performed.

C++
    
    
    MTAPIRES  IMTRequest::SourceLogin(
       const UINT64  login      // Dealer's login
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTRequest.SourceLogin(
       ulong         login      // Dealer's login
       )

### Parameters

**login**  
[in] The login of the dealer, on whose behalf the request is performed.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
