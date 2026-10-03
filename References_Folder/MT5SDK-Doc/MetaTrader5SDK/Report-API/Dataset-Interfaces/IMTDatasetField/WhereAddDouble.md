[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDatasetField](../IMTDatasetField.md) / WhereAddDouble

[Previous](WhereAddUIntArray.md) | [Next](WhereAddDoubleArray.md)

# IMTDatasetField::WhereAddDouble

Add a selection condition for fields of the [double type (#enfieldtype)](Enumerations.md#enfieldtype).
    
    
    MTAPIRES  IMTDatasetField::WhereAddDouble(
       const double  value      // Value
       )

### Parameters

**value**  
Field value of double type. For example, for theIMTDatasetField::FIELD_DEAL_PRICE_SLfield you can specify "1.31689" to select data on deals having the appropriate Stop Loss level.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
