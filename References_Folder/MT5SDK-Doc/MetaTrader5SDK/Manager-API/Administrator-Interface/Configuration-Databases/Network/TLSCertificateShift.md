[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Network](../Network.md) / TLSCertificateShift

[Previous](TLSCertificateDelete.md) | [Next](TLSCertificateTotal.md)

# IMTAdminAPI::TLSCertificateShift

Change the position of an SSL certificate in the list.

C++
    
    
    MTAPIRES  IMTAdminAPI::TLSCertificateShift(
       const UINT  pos,       // Certificate position
       const int   shift      // Shift
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI::TLSCertificateShift(
       uint        pos,       // Certificate position
       int         shift      // Shift
       )

### Parameters

**pos**  
[in] Certificate position starting with 0.

**shift**  
[in] Shift of the certificate relative to the current position. A negative value means shift towards the top of the list, a positive value shifts towards the end.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The certificate position can only be changed from the applications running on the main server. For all other plugins, the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) will be returned.
