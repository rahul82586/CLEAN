[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDatasetField](../IMTDatasetField.md) / Type

[Previous](Id.md) | [Next](Offset.md)

# IMTDatasetField::Type

Get the field type.
    
    
    UINT  IMTDatasetField::Type()  const

### Return Value

A value from [IMTDatasetField::EnFieldType (#enfieldtype)](Enumerations.md#enfieldtype).

### Note

Depending on the field type, the corresponding method should be used to set selection condition, [IMTDatasetField::Where*](WhereAddInt.md) or [IMTDatasetField::Between*](BetweenInt.md).
