[🏠 Document Start](../README.md) / [Report API](README.md) / Dataset Interfaces

[Previous](Diagram-Interfaces/IMTReportChart/SeriesNext.md) | [Next](Dataset-Interfaces/IMTDataset.md)

<a id="dataset-interfaces"></a>
# Dataset interfaces (#dataset-interfaces)

The interfaces described in this section are used for preparing source data for creating [dashboards](Dashboards.md) and [tabular reports](Tabular-Reports.md). Data in a set is stored as a table with a set of columns and rows and a special summary row.

The following interfaces are provided for managing data sets:

  * [IMTDataset](Dataset-Interfaces/IMTDataset.md) — description of a data set which consists of rows and columns.
  * [IMTDatasetColumn](Dataset-Interfaces/IMTDatasetColumn.md) — description of a column in a data set.
  * [IMTDatasetSummary](Dataset-Interfaces/IMTDatasetSummary.md) — description of a summary row in a data set.



<a id="request"></a>
## Highly efficient requests for information from databases (#request)

The Report API enables highly efficient queries to the trading platform databases, with the flexible description of selection conditions (similar to SQL queries). Two interfaces are provided for operations with data requests: [IMTDatasetField](Dataset-Interfaces/IMTDatasetField.md) for describing conditions, [IMTDatasetRequest](Dataset-Interfaces/IMTDatasetRequest.md) for describing a request as a set of conditions.

To request data perform the following steps:

1\. Use the [IMTReprotAPI::DatasetRequestCreate](Main-Interface-of-Reports/Dataset/RequestCreate.md) method to create a data request object ([IMTDatasetRequest](Dataset-Interfaces/IMTDatasetRequest.md)).

2\. Use [IMTReportAPI::DatasetAppend](Main-Interface-of-Reports/Dataset/Append.md) to create an object of a data set to which the query results will be added ([IMTDataset](Dataset-Interfaces/IMTDataset.md))

3\. Use [IMTDatasetRequest::FieldCreate](Dataset-Interfaces/IMTDatasetRequest/FieldCreate.md) to create the object of a field data for which will be requested ([IMTDatasetField](Dataset-Interfaces.md)).

4\. Describe the request condition using [IMTDatasetField](Dataset-Interfaces.md) methods and add it to the request object using the [IMTDatasetRequest::FieldAdd](Dataset-Interfaces/IMTDatasetRequest/FieldAdd.md) method.

5\. If you need to specify multiple conditions, repeat steps 3 and 4.

6\. Depending on the database from which you want to request data, call [IMTReportAPI::UserSelect](Main-Interface-of-Reports/Users/UserSelect.md), [IMTReportAPI::ClientSelect](Main-Interface-of-Reports/Users/ClientSelect.md) or [IMTReportAPI::DealSelect](Main-Interface-of-Reports/Trade-Databases/Deals/DealSelect.md), while passing to it the prepared request object ([IMTDatasetRequest](Dataset-Interfaces/IMTDatasetRequest.md)).

7\. The request result will be added to the previously created data set object ([IMTDataset](Dataset-Interfaces/IMTDataset.md)). Note that only fields marked as selected ([IMTDatasetField::FLAG_SELECT (#enfieldflags)](Dataset-Interfaces/IMTDatasetField/Enumerations.md#enfieldflags)) are added to the resulting data set.

Data request examples are provided in the source code of the Capital report, which is available in "[Report API installation directory]\Report\Examples\Capital.Standard.Reports".
