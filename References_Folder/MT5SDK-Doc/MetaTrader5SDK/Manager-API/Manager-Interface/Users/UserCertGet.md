[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Users](../Users.md) / UserCertGet

[Previous](UserCertUpdate.md) | [Next](UserCertDelete.md)

# IMTManagerAPI::UserCertGet

Get the certificate of a client by the login.

C++
    
    
    MTAPIRES  IMTManagerAPI::UserCertGet(
       const UINT64      login,            // Client login
       IMTCertificate*   certificate       // The object of the certificate
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.UserCertGet(
       ulong             login,            // Client login
       CIMTCertificate   obj               // The object of the certificate
       )

Python
    
    
    ManagerAPI.UserCertGet(
       login,            # Client login
       certificate       # The object of the certificate
       )

### Parameters

**login**  
[in] The login of a client.

**certificate**  
[out] The object of the certificate. The certificate object must be first created using theIMTManagerAPI::UserCertCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the data of a client with the specified login to the certificate object.
