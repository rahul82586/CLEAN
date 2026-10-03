[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDatasetField](../IMTDatasetField.md) / WhereAddUIntArray

[Previous](WhereAddUInt.md) | [Next](WhereAddDouble.md)

# IMTDatasetField::WhereAddUIntArray

Add an array of selection conditions for fields of the [uint type (#enfieldtype)](Enumerations.md#enfieldtype).
    
    
    MTAPIRES  IMTDatasetField::WhereAddUIntArray(
       const UINT64*  values,          // Array of values
       const UINT     values_total     // Number of values
       )

### Parameters

**values**  
An array of uint field values. For example, for theIMTDatasetField::FIELD_CLIENT_TYPEfield you can specify the value of "IMTDatasetField::CLIENT_TYPE_INDIVIDUAL,IMTDatasetField::CLIENT_TYPE_CORPORATE" to select data on private and corporate clients.

**values_total**  
Number of values in the 'values' array.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
