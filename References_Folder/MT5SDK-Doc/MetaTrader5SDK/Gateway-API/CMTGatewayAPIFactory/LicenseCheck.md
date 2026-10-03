[🏠 Document Start](../../README.md) / [Gateway API](../README.md) / [CMTGatewayAPIFactory](../CMTGatewayAPIFactory.md) / LicenseCheck

[Previous](Create.md) | [Next](Version.md)

# CMTGatewayAPIFactory::LicenseCheck

Gateway/data feed module usage license verification.

C++
    
    
    static MTAPIRES  CMTGatewayAPIFactory::LicenseCheck(
       IMTGatewayAPI*  gateway,      // Pointer to the IMTGatewayAPI interface
       LPCWSTR         name          // The name of the module
       )

.NET
    
    
    static MTRetCode  SMTGatewayAPIFactory.LicenseCheck(
       CIMTGatewayAPI  gateway,      // Pointer to the IMTGatewayAPI interface
       string          name          // The name of the module
       )

### Parameters

**gateway**  
[in] Pointer to theIMTGatewayAPIinterface for gateway/data feed module license verification.

**name**  
[in] The name of the gateway/data feed that is to be verified for license. Module's unique name must be preliminarily determined in the program code.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This factory method is provided to ease the license verification process. Comprehensive description of the verification algorithm can be found at the [IMTGatewayAPI::LicenseCheck](../Main-Interface/Common-Functions/LicenseCheck.md) function section.
