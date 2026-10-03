[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDatasetField](../IMTDatasetField.md) / BetweenInt

[Previous](WhereAddStringArray.md) | [Next](BetweenUInt.md)

# IMTDatasetField::BetweenInt

Add a selection condition as a range of values for fields of the [int type (#enfieldtype)](Enumerations.md#enfieldtype).
    
    
    MTAPIRES  IMTDatasetField::BetweenInt(
       const INT64  from,     // Range beginning
       const INT64  to        // Range end
       )

### Parameters

**from**  
The value of the int field used as the range beginning.

**to**  
The value of the int field used as the range beginning.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

For example, for the [IMTDatasetField::FIELD_USER_LOGIN (#enfieldid)](Enumerations.md#enfieldid) field you can specify the range "1000-1100" to select data on accounts with the appropriate numbers.
