[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Mail Servers](../Mail-Servers.md) / EmailShift

[Previous](EmailDeleteBatch.md) | [Next](EmailTotal.md)

# IMTAdminAPI::EmailShift

Change the position of a mail server configuration in the list.

C++
    
    
    MTAPIRES  IMTAdminAPI::EmailShift(
       const UINT  pos,       // Configuration position
       const int   shift      // Shift
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.EmailShift(
       uint        pos,       // Configuration position
       int         shift      // Shift
       )

Python
    
    
    AdminAPI.EmailShift(
       pos,        # Configuration position
       shift       # Shift
       )

### Parameters

**pos**  
[in] Position of the configuration, starting with 0.

**shift**  
[in] The shift of the configuration relative to its current position. A negative value means shift towards the top of the list, a positive value shifts towards the end.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The position of a configuration can only be changed from the applications running on the main server. For all other plugins the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) will be returned.
