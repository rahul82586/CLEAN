[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Assets](../../Assets.md) / [IMTExposure](../IMTExposure.md) / PriceRate

[Previous](VolumeCoverage.md) | [Next](VolumeNet.md)

# IMTExposure::PriceRate

The rate of conversion of the net total to the selected currency.

C++
    
    
    double  IMTExposure::PriceRate()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTExposure.PriceRate()

### Return Value

The rate of conversion of the net total to the selected currency. The currency of the net total is specified by the [IMTManagerAPI::ExposureCurrency](../../../../Manager-API/Manager-Interface/Exposure/Currency.md) method.
