[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDatasetField](../IMTDatasetField.md) / WhereAddInt

[Previous](Flags.md) | [Next](WhereAddIntArray.md)

# IMTDatasetField::WhereAddInt

Add a selection condition for fields of the [int type (#enfieldtype)](Enumerations.md#enfieldtype).
    
    
    MTAPIRES  IMTDatasetField::WhereAddInt(
       const INT64  value      // Value
       )

### Parameters

**value**  
Field value of int type. For example, for theIMTDatasetField::FIELD_USER_LOGINfield you can specify the value of "1000" to select data on the account with the appropriate login.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
