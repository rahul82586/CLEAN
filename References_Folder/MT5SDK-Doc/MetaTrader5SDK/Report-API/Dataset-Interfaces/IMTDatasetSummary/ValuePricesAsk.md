[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDatasetSummary](../IMTDatasetSummary.md) / ValuePricesAsk

[Previous](ValuePricesBid.md) | [Next](ValuePrices.md)

# IMTDatasetSummary::ValuePricesAsk

Get a previously set Ask price value in a summary cell.
    
    
    double  IMTDatasetSummary::ValuePricesAsk()  const

### Return Value

A previously set Ask price value in a summary cell.

### Note

A received summary must be of [IMTDatasetSummary::TYPE_PRICES (#entype)](Enumerations.md#entype) type. Otherwise, the method returns 0.
