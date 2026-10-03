[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDatasetColumn](../IMTDatasetColumn.md) / Digits

[Previous](WidthMax.md) | [Next](DigitsColumn.md)

# IMTDatasetColumn::Digits

Get the number of decimal places by default for values in a column.
    
    
    UINT  IMTDatasetColumn::Digits()  const

### Return Value

The number of decimal places by default for values in a column.

### Note

Used for formatting the figures with a floating point ([IMTDatasetColumn::TYPE_DOUBLE,TYPE_MONEY,TYPE_PRICE* (#entype)](Enumerations.md#entype)).

# IMTDatasetColumn::Digits

Set the number of decimal places by default for values in a column.
    
    
    MTAPIRES  IMTDatasetColumn::Digits(
       const UINT  digits      // Number of decimal places
       )

### Parameters

**digits**  
[in] The number of decimal places by default for values in a column.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

Used for formatting the figures with a floating point ([IMTDatasetColumn::TYPE_DOUBLE, TYPE_MONEY, TYPE_PRICE* (#entype)](Enumerations.md#entype)).
