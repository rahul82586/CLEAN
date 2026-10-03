[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Exposure](../Exposure.md) / Currency

[Previous](Unsubscribe.md) | [Next](Total.md)

# IMTManagerAPI::ExposureCurrency

Get a currency of the net total of assets.

C++
    
    
    LPCWSTR  IMTManagerAPI::ExposureCurrency()

.NET
    
    
    string   CIMTManagerAPI.ExposureCurrency()

Python
    
    
    ManagerAPI.ExposureCurrency()

### Return Value

The currency of the net total of assets.

# IMTManagerAPI::ExposureCurrency

Set a currency of the net total of assets.

C++
    
    
    MTAPIRES  IMTManagerAPI::ExposureCurrency(
       LPCWSTR  currency      // Currency
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.ExposureCurrency(
       string   currency      // Currency
       )

Python
    
    
    ManagerAPI.ExposureCurrency(
       str      currency      # Currency
       )

### Parameters

**currency**  
[in] The currency of the net total of assets.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
