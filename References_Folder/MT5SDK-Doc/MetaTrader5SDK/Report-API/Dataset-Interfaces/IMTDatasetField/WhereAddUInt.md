[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDatasetField](../IMTDatasetField.md) / WhereAddUInt

[Previous](WhereAddIntArray.md) | [Next](WhereAddUIntArray.md)

# IMTDatasetField::WhereAddUInt

Add a selection condition for fields of the [string uint (#enfieldtype)](Enumerations.md#enfieldtype).
    
    
    MTAPIRES  IMTDatasetField::WhereAddUInt(
       const UINT64  value      // Value
       )

### Parameters

**value**  
Field value of uint type. For example, for theIMTDatasetField::FIELD_CLIENT_TYPEfield you can specify the value of "IMTDatasetField::CLIENT_TYPE_INDIVIDUAL" to select data on private clients.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
