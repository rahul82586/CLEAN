[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Assets](../../Assets.md) / [IMTExposure](../IMTExposure.md) / Digits

[Previous](Symbol.md) | [Next](VolumeClients.md)

# IMTExposure::Digits

Gets the number of decimal places in the [rate of conversion](PriceRate.md) of the [net total](VolumeNet.md) to the exposure currency[IMTManagerAPi::ExposureCurrency](../../../../Manager-API/Manager-Interface/Exposure/Currency.md).

C++
    
    
    UINT  IMTExposure::Digits()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTExposure.Digits()

### Return Value

The number of decimal places in the conversion rate.
