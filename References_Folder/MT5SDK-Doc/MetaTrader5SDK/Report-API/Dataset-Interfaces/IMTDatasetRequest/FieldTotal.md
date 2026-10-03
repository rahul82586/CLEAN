[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDatasetRequest](../IMTDatasetRequest.md) / FieldTotal

[Previous](FieldShift.md) | [Next](FieldNext.md)

# IMTDatasetRequest::FieldTotal

Get the total number of fields in a request.
    
    
    UINT  IMTDatasetRequest::FieldTotal()

### Return Value

The number of rows in a table.

### Note

A database query is performed as a collection of fields and selection conditions. Use this method to get the total number of fields in a request (optionally with conditions).
