[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDatasetField](../IMTDatasetField.md) / BetweenUInt

[Previous](BetweenInt.md) | [Next](BetweenDouble.md)

# IMTDatasetField::BetweenUInt

Add a selection condition as a range of values for fields of the [uint type (#enfieldtype)](Enumerations.md#enfieldtype).
    
    
    MTAPIRES  IMTDatasetField::BetweenUInt(
       const UINT64  from,     // Range beginning
       const UINT64  to        // Range end
       )

### Parameters

**from**  
The value of the uint field used as the range beginning.

**to**  
The value of the uint field used as the range end.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

For example, for the [IMTDatasetField::FIELD_USER_LEVERAGE (#enfieldid)](Enumerations.md#enfieldid) field you can specify the range "10-50" to select data on accounts with the appropriate leverages.
