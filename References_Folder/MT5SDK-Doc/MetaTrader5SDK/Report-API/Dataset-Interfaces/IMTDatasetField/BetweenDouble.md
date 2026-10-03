[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDatasetField](../IMTDatasetField.md) / BetweenDouble

[Previous](BetweenUInt.md) | [Next](../IMTDatasetRequest.md)

# IMTDatasetField::BetweenDouble

Add a selection condition as a range of values for fields of the [double type (#enfieldtype)](Enumerations.md#enfieldtype).
    
    
    MTAPIRES  IMTDatasetField::BetweenDouble(
       const double  from,     // Range beginning
       const double  to        // Range end
       )

### Parameters

**from**  
The value of the double field used as the range beginning.

**to**  
The value of the double field used as the range end.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

For example, for the [IMTDatasetField::FIELD_USER_BALANCE (#enfieldid)](Enumerations.md#enfieldid) field you can specify the range "100.00-5000.00" to select data on accounts with the appropriate balances.
