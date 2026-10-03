[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDatasetField](../IMTDatasetField.md) / WhereAddStringArray

[Previous](WhereAddString.md) | [Next](BetweenInt.md)

# IMTDatasetField::WhereAddStringArray

Add an array of selection conditions for fields of the [string type (#enfieldtype)](Enumerations.md#enfieldtype).
    
    
    MTAPIRES  IMTDatasetField::WhereAddStringArray(
       LPCWSTR*     values,          // Array of values
       const UINT   values_total     // Number of values
       )

### Parameters

**values**  
An array of string field values. For example, for theIMTDatasetField::FIELD_USER_GROUPfield you can specify "demo\forex-usd,demo\forex-eur" to select data on accounts from the corresponding groups.

**values_total**  
Number of values in the 'values' array.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
