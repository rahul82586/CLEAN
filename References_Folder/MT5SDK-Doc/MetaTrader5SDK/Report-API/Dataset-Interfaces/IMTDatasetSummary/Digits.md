[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDatasetSummary](../IMTDatasetSummary.md) / Digits

[Previous](Type.md) | [Next](ValueInt.md)

# IMTDatasetSummary::Digits

Get the number of decimal places for formatting the values shown in a cell.
    
    
    UINT  IMTDatasetSummary::Digits()  const

### Return Value

The number of decimal places for formatting the values shown in a cell.

### Note

Used for formatting the figures with a floating point ([IMTDatasetSummary::TYPE_DOUBLE, TYPE_MONEY, TYPE_PRICE* (#entype)](Enumerations.md#entype)).

# IMTDatasetSummary::Digits

Set the number of decimal places for formatting the values shown in a cell.
    
    
    MTAPIRES  IMTDatasetSummary::Digits(
       const UINT  digits      // Decimal places
       )

### Parameters

**digits**  
[in] The number of decimal places for formatting the values shown in a cell.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

Used for formatting the figures with a floating point ([IMTDatasetSummary::TYPE_DOUBLE, TYPE_MONEY, TYPE_PRICE* (#entype)](Enumerations.md#entype)).
