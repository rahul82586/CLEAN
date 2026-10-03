[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [Dataset](../Dataset.md) / Clear

[Previous](Append.md) | [Next](Delete.md)

# IMTReportAPI::DatasetClear

Delete all data sets from a dashboard.
    
    
    MTAPIRES  IMTReportAPI::DatasetClear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

After this method call, all previously created data sets ([IMTDataset](../../Dataset-Interfaces/IMTDataset.md) objects) are deleted.
