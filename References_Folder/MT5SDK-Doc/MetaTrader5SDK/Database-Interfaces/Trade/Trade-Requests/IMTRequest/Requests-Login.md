[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequest](../Requests-IMTRequest.md) / Requests Login

[Previous](Requests-ID.md) | [Next](Requests-ExternalAccount.md)

# IMTRequest::Login

Get the login of the client who has sent the request.

C++
    
    
    UINT64  IMTRequest::Login()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTRequest.Login()

### Return Value

The login of the client who has sent the request.

# IMTRequest::Login

Set the login of the client who is sending the request.

C++
    
    
    MTAPIRES  IMTRequest::Login(
       const UINT64  login      // Login
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTRequest.Login(
       ulong         login      // Login
       )

### Parameters

**login**  
[in] Client login in a request.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
