[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDatasetField](../IMTDatasetField.md) / WhereAddString

[Previous](WhereAddDoubleArray.md) | [Next](WhereAddStringArray.md)

# IMTDatasetField::WhereAddString

Add a selection condition for fields of the [string type (#enfieldtype)](Enumerations.md#enfieldtype).
    
    
    MTAPIRES  IMTDatasetField::WhereAddString(
       LPCWSTR  value      // Value
       )

### Parameters

**value**  
Field value of string type. For example, for theIMTDatasetField::FIELD_USER_GROUPfield you can specify "demo\forex-usd" to select data on accounts from the corresponding group.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
