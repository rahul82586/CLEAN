[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Custom Functions](../Custom-Functions.md) / CustomCommand

[Previous](../Custom-Functions.md) | [Next](CustomCreateStream.md)

# IMTAdminAPI::CustomCommand

Sends a custom command to the server.

C++
    
    
    virtual MTAPIRES  IMTAdminAPI::CustomCommand(
       LPCVOID        indata,         // Input data
       const UINT     indata_len,     // Size of input data
       LPVOID&        outdata,        // Output data
       UINT&          outdata_len     // Size of output data
       )

.NET
    
    
    byte[]  CIMTAdminAPI.CustomCommand(
       byte[]         indata,         // Input data
       out MTRetCode  res             // Response code
       )

### Parameters

**indata**  
[in] Data returned to the server.

**indata_len**  
[in] Size of data to pass in bytes.

**outdata**  
[out] A reference to the data returned in response to the command.

**outdata_len**  
[out] A reference to the size of data returned in response to the command.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

An appropriate plugin must be installed in the server for processing custom commands ([IMTCustomSink::HookManagerCommand](../../../Server-API/Interface-of-Custom-Events/HookManagerCommand.md)).

# IMTAdminAPI::CustomCommand

Sends a custom command to the server.

C++
    
    
    virtual MTAPIRES  IMTAdminAPI::CustomCommand(
       IMTByteStream*  indata,      // Input data
       IMTByteStream*  outdata,     // Output data
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.CustomCommand(
       CIMTByteStream  indata,      // Input data
       CIMTByteStream  outdata,     // Output data
       )

### Parameters

**indata**  
[in] A pointer to theobject of a byte streampassed to the server.

**outdata**  
[out] A pointer to theobject of a byte streamreturned in response to the command.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

An appropriate plugin must be installed in the server for processing custom commands. ([IMTCustomSink::HookManagerCommand](../../../Server-API/Interface-of-Custom-Events/HookManagerCommand.md)).
