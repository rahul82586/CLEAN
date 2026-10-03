[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequest](../Requests-IMTRequest.md) / Requests PriceDeviation

[Previous](Requests-PriceTP.md) | [Next](Requests-PriceDeviationTop.md)

# IMTRequest::PriceDeviation

Get the maximum allowed [deviation (#max-deviation)](https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_execution#max-deviation) of the execution price from the price requested in an order.

C++
    
    
    UINT64  IMTRequest::PriceDeviation()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTRequest.PriceDeviation()

### Return Value

The maximum allowed deviation of the execution price from the price requested in an order. When the deviation is exceeded, a new price (requote) is sent.

# IMTRequest::PriceDeviation

Set the maximum allowed [deviation (#max-deviation)](https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_execution#max-deviation) of the execution price from the price specified in an order.

C++
    
    
    MTAPIRES  IMTRequest::PriceDeviation(
       const UINT64  deviation      // Deviation
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTRequest.PriceDeviation(
       ulong         deviation      // Deviation
       )

### Parameters

**deviation**  
[in] The maximum allowed deviation of the execution price from the price requested in an order.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

When the deviation is exceeded, a new price (requote) is sent.
