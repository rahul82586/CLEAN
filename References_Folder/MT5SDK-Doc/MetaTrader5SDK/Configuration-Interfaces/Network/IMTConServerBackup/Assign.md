[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerBackup](../IMTConServerBackup.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTConServerBackup::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTConServerBackup::Assign(
       const IMTConServerBackup*  param  // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerBackup.Assign(
       CIMTConServerBackup        param  // Source object
       )

### Parameters

**param**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
