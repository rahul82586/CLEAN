[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDatasetField](../IMTDatasetField.md) / WhereAddIntArray

[Previous](WhereAddInt.md) | [Next](WhereAddUInt.md)

# IMTDatasetField::WhereAddIntArray

Add an array of selection conditions for fields of the [int type (#enfieldtype)](Enumerations.md#enfieldtype).
    
    
    MTAPIRES  IMTDatasetField::WhereAddIntArray(
       const INT64*  values,          // Array of values
       const UINT    values_total     // Number of values
       )

### Parameters

**values**  
An array of int field values. For example, for theIMTDatasetField::FIELD_USER_LOGINfield you can specify "1000,1001,1003" to select data on account with corresponding login numbers.

**values_total**  
Number of values in the 'values' array.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
