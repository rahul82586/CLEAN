[🏠 Document Start](../../README.md) / [Server API](../README.md) / [Interface of Custom Events](../Interface-of-Custom-Events.md) / HookManagerCommand

[Previous](../Interface-of-Custom-Events.md) | [Next](HookWebAPICommand.md)

# IMTCustomSink::HookManagerCommand

A hook of an event of execution of a [manager's](../../Manager-API/Manager-Interface/Custom-Functions.md) or [administrator's custom command](../../Manager-API/Administrator-Interface/Custom-Functions.md).
    
    
    MTAPIRES  IMTCustomSink::HookManagerCommand(
       LPCWSTR               ip,              // Manager's IP address
       const IMTConManager*  manager,         // An object of the manager configuration
       LPCVOID               indata,          // Input data
       const UINT            indata_len,      // Size of input data
       LPVOID&               outdata,         // Output data
       UINT&                 outdata_len      // Size of output data
       )

### Parameters

**ip**  
[in] The IP address of the manager who has sent the custom command.

**manager**  
[in] An object of configuration of the manager who has sent the custom command.

**indata**  
[in] Data transmitted to the server.

**indata_len**  
[in] Size of transmitted data in bytes.

**outdata**  
[out] A pointer to the data returned in response to the command. For the data returned you need to preliminary allocate the memory using theIMTServerAPI::Allocatemethod.

**outdata_len**  
[out] A pointer to the size of data returned in response to the command.

### Return Value

If the hook does not handle the event, it returns [MT_RET_OK_NONE](../../Return-Codes/Successful-completion.md). If the event is handled, the return code is forwarded to the Manager API together with the outdata buffer.

### Note

The hook is called consistently in accordance with the order of plugins in the list until the first plugin that has returned a response code other than [MT_RET_OK_NONE](../../Return-Codes/Successful-completion.md).

# IMTCustomSink::HookManagerCommand

A hook of an event of execution of a [manager's](../../Manager-API/Manager-Interface/Custom-Functions.md) or [administrator's custom command](../../Manager-API/Administrator-Interface/Custom-Functions.md).
    
    
    MTAPIRES  IMTCustomSink::HookManagerCommand(
       const UINT64          session,         // Session identifier
       LPCWSTR               ip,              // Manager's IP address
       const IMTConManager*  manager,         // An object of the manager configuration
       IMTByteStream*        indata,          // Input data
       IMTByteStream*        outdata,         // Output data
       )

### Parameters

**session**  
[in] Identifier of the session of the manager connection.

**ip**  
[in] The IP address of the manager who has sent the custom command.

**manager**  
[in] An object of configuration of the manager who has sent the custom command.

**indata**  
[in]The object of the data streamsent to the server.

**outdata**  
[out] A pointer to theobject of the data streamreturned in response to the command.

### Return Value

If the hook does not handle the event, it returns [MT_RET_OK_NONE](../../Return-Codes/Successful-completion.md). If the event is handled, the return code is forwarded to the Manager API together with the outdata buffer.

### Note

The hook is called consistently in accordance with the order of plugins in the list until the first plugin that has returned a response code other than [MT_RET_OK_NONE](../../Return-Codes/Successful-completion.md).
