[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConBackupFolder](../IMTConBackupFolder.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTConBackupFolder::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTConBackupFolder::Assign(
       const IMTConBackupFolder*  param  // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConBackupFolder.Assign(
       CIMTConBackupFolder        param  // Source object
       )

### Parameters

**param**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
