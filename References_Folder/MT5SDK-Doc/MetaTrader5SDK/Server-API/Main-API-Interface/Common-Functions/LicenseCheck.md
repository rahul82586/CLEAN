[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Common Functions](../Common-Functions.md) / LicenseCheck

[Previous](About.md) | [Next](../Configuration-Databases.md)

# IMTServerAPI::LicenseCheck

Check the plugin license.
    
    
    MTAPIRES  IMTServerAPI::LicenseCheck(
       LPCWSTR  license_name      // Name of the license module
       )

### Parameters

**license_name**  
[in] The name of the license module.

### Return Value

An indication of permission to use the plugin in the platform license is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The process of licensing plugins is connected with the MetaTrader 5 platform license, which is issued by MetaQuotes Software Corp. The name of the license module (plugin) is added to the trading platform license upon a request sent by the client company to the technical support team or during the purchase of the plugin from the Market on the technical support website.
