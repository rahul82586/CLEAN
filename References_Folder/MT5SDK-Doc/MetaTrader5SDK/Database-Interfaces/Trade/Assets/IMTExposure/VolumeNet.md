[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Assets](../../Assets.md) / [IMTExposure](../IMTExposure.md) / VolumeNet

[Previous](PriceRate.md) | [Next](../IMTExposureArray.md)

# IMTExposure::VolumeNet

The difference (net total) between the volume of [client](VolumeClients.md) positions and [hedged](VolumeCoverage.md) positions in the exposure currency [IMTManagerAPI::ExposureCurrency](../../../../Manager-API/Manager-Interface/Exposure/Currency.md).

C++
    
    
    double  IMTExposure::VolumeNet()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTExposure.VolumeNet()

### Return Value

The net total between the volume of client positions and hedged positions in the exposure currency [IMTManagerAPI::ExposureCurrency](../../../../Manager-API/Manager-Interface/Exposure/Currency.md).
