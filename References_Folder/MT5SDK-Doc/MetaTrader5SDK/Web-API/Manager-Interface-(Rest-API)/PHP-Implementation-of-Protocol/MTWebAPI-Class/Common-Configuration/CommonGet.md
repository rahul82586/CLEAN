[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [PHP Implementation of Protocol](../../../PHP-Implementation-of-Protocol.md) / [MTWebAPI Class](../../MTWebAPI-Class.md) / [Common Configuration](../Common-Configuration.md) / CommonGet

[Previous](../Common-Configuration.md) | [Next](../Timing.md)

# MTWebAPI::CommonGet

Get the common configuration of the trading platform.
    
    
    MTAPIRES  MTWebAPI::CommonGet(
       MTConCommon  &$common      // Common configuration
       )

### Parameters

**& $common**  
[out] The MTConCommon structure that describes the common configuration of the trading platform. The structure parameters are described in section"Data Structure".

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
