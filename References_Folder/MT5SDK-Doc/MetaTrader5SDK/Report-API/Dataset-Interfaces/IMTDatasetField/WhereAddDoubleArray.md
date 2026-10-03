[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDatasetField](../IMTDatasetField.md) / WhereAddDoubleArray

[Previous](WhereAddDouble.md) | [Next](WhereAddString.md)

# IMTDatasetField::WhereAddDoubleArray

Add an array of selection conditions for fields of the [double type (#enfieldtype)](Enumerations.md#enfieldtype).
    
    
    MTAPIRES  IMTDatasetField::WhereAddDoubleArray(
       const double*  values,          // Array of values
       const UINT     values_total     // Number of values
       )

### Parameters

**values**  
An array of field values of the double type. For example, for theIMTDatasetField::FIELD_DEAL_PRICE_SLfield you can specify "1.31689, 1.31690" to select data on deals having the appropriate Stop Loss levels.

**values_total**  
Number of values in the 'values' array.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
