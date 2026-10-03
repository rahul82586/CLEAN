[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDatasetSummary](../IMTDatasetSummary.md) / ValuePrices

[Previous](ValuePricesAsk.md) | [Next](ValueVolume.md)

# IMTDatasetSummary::ValuePrices

Set Bid and Ask prices values in a summary cell.
    
    
    MTAPIRES  IMTDatasetSummary::ValuePrices(
       const double  value_bid,     // Bid price
       const double  value_ask      // Ask price
       )

### Parameters

**value_bid**  
[in] Bid price.

**value_ask**  
[in] Ask price.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

After the method is called summary cell type changes for [IMTDatasetSummary::TYPE_PRICES (#entype)](Enumerations.md#entype).
