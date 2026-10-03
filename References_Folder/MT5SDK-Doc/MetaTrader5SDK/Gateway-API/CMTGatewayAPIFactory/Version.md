[🏠 Document Start](../../README.md) / [Gateway API](../README.md) / [CMTGatewayAPIFactory](../CMTGatewayAPIFactory.md) / Version

[Previous](LicenseCheck.md) | [Next](../Main-Interface.md)

# CMTGatewayAPIFactory::Version

Get the version of the loaded Gateway API library.

C++
    
    
    MTAPIRES  CMTGatewayAPIFactory::Version(
       UINT&     version   // Gateway API version
       )

.NET
    
    
    MTRetCode SMTGatewayAPIFactory.GetVersion(
       out uint  version   // Gateway API version
       )

### Parameters

**version**  
[in] The version of the loaded Gateway API library.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
