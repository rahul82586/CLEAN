[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequest](../Requests-IMTRequest.md) / Requests PriceDeviationTop

[Previous](Requests-PriceDeviation.md) | [Next](Requests-PriceDeviationBottom.md)

# IMTRequest::PriceDeviationTop

Get the allowed [price deviation (#max-deviation)](https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_execution#max-deviation) in the increase direction.

C++
    
    
    double  IMTRequest::PriceDeviationTop()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTRequest.PriceDeviationTop()

### Return Value

Allowed price deviation in the  direction. Calculated as PriceOrder + PriceDeviation.
