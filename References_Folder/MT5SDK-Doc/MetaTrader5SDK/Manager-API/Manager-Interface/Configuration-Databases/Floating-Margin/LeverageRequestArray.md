[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Floating Margin](../Floating-Margin.md) / LeverageRequestArray

[Previous](LeverageRequest.md) | [Next](../Spreads.md)

# IMTManagerAPI::LeverageRequestArray

Request an array of floating margin configurations from the server by groups.

C++
    
    
    MTAPIRES  IMTManagerAPI::LeverageRequestArray(
       LPCWSTR              groups_mask, // Group mask
       IMTConLeverageArray  leverages    // Configuration object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.LeverageRequestArray(
       string               groups_mask, // Group mask
       CIMTConLeverageArray leverages    // Object configuration
       )

Python
    
    
    ManagerAPI.LeverageRequestArray(
       groups_mask          # Group mask
       )

### Parameters

**groups_mask**  
[in] Groups to which floating margin configurations are being applied. You can specify one group, several groups separated by commas, or a group mask. A mask is indicated using "*" (any value) and "!" (exception). For example: "demo*,!demoforex" includes all groups with the names beginning with 'demo', except for the 'demoforex' group. The value of 'nullptr' means "all groups".

**leverages**  
[out] Object of the configurations arrayIMTConLeverageArray. The 'config' object must be created in advance using theIMTManagerAPI::LeverageCreateArraymethod.

### Return Value

An indication of a successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, the code of the encountered error is returned.

### Note

The method cannot be called from event handlers (any IMT*Sink class methods).
