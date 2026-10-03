[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Data Feeds](../../Data-Feeds.md) / [IMTConFeederModule](../IMTConFeederModule.md) / ParameterNext

[Previous](ParameterTotal.md) | [Next](ParameterGet.md)

# IMTConFeederModule::ParameterNext

Get parameters of a data feed module by the index.

C++
    
    
    MTAPIRES  IMTConFeederModule::ParameterNext(
       const UINT    pos,       // Position of the data feed
       IMTConParam*  param      // An object of a data feed module parameter
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFeederModule.ParameterNext(
       uint          pos,       // Position of the data feed
       CIMTConParam  param      // An object of a data feed module parameter
       )

Python (Manager API)
    
    
    MTConFeederModule.ParameterNext(
       pos           # Position of the data feed
       )

### Parameters

**pos**  
[in] Position of a data feed, starting with 0.

**param**  
[out] An object of a data feed module parameter. The 'param' object must first be created using theIMTAdminAPI::FeederParamCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the parameters of a data feed module with a specified index to the param object.
