[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [Dataset](../Dataset.md) / Next

[Previous](Total.md) | [Next](RequestCreate.md)

# IMTReportAPI::DatasetNext

Get the data set description based in the index.
    
    
    IMTDataset*  IMTReportAPI::DatasetNext(
       const UINT       pos          // data set position
       )

### Parameters

**pos**  
[in] Data set position starting with 0.

### Return Value

Pointer to the [IMTDataset](../../Dataset-Interfaces/IMTDataset.md) tabular data set object.

### Note

The previous name of the method was DashboardDataNext.
