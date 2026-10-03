[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequest](../Requests-IMTRequest.md) / Requests PriceDeviationBottom

[Previous](Requests-PriceDeviationTop.md) | [Next](Requests-SpreadDiff.md)

# IMTRequest::PriceDeviationBottom

Get the allowed [price deviation (#max-deviation)](https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_execution#max-deviation) in the decrease direction.

C++
    
    
    double  IMTRequest::PriceDeviationBottom()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTRequest.PriceDeviationBottom()

### Return Value

Allowed price deviation in the  direction. Calculated as PriceOrder - PriceDeviation.
