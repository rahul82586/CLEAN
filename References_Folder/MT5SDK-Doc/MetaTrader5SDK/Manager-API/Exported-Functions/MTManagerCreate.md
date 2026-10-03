[🏠 Document Start](../../README.md) / [Manager API](../README.md) / [Exported Functions](../Exported-Functions.md) / MTManagerCreate

[Previous](MTManagerVersion.md) | [Next](MTManagerCreateExt.md)

# MTManagerCreate

The MTManagerCreate exported function creates a new instance of the [IMTManagerAPI](../Manager-Interface.md) interface and returns a pointer to it.
    
    
    MTAPIRES  MTManagerCreate(
       UINT             api_version    // API version
       IMTManagerAPI**  manager        // A pointer to the pointer to the interface
       )

### Parameters

**api_version**  
[out] The current version of Manager API supported by the server is passed in this parameter.

**manager**  
[out] A pointer to the pointer of the createdIMTManagerAPIinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The Manager API application can use separate data directories for each manager and administrator interface (to store the local data cache). However, the application log is always written to only one data directory, which is specified during creation of the first interface (no matter whether it is a manager or an administrator interface).
