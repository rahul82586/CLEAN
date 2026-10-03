[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDatasetSummary](../IMTDatasetSummary.md) / ValuePricesBid

[Previous](ValuePrice.md) | [Next](ValuePricesAsk.md)

# IMTDatasetSummary::ValuePricesBid

Get a previously set Bid price value in a summary cell.
    
    
    double  IMTDatasetSummary::ValuePricesBid()  const

### Return Value

A previously set Bid price value in a summary cell.

### Note

A received summary must be of [IMTDatasetSummary::TYPE_PRICES (#entype)](Enumerations.md#entype) type. Otherwise, the method returns 0.
