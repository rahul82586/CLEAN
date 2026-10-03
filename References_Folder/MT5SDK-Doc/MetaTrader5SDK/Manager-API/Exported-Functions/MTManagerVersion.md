[🏠 Document Start](../../README.md) / [Manager API](../README.md) / [Exported Functions](../Exported-Functions.md) / MTManagerVersion

[Previous](../Exported-Functions.md) | [Next](MTManagerCreate.md)

# MTManagerVersion

The exported function MTManagerVersion returns the version of the Manager API library.
    
    
    MTAPIRES  MTManagerVersion(
       UINT&  version      // Reference to the version of the Manager API
       )

### Parameters

**version**  
[in] A reference to the version of the Manager API library.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
