[🏠 Document Start](../README.md) / [Report API](README.md) / Dashboards

[Previous](HTML-Reports.md) | [Next](Templates.md)

<a id="dashboards"></a>
# Dashboards (#dashboards)

Dashboards form a separate type of reports that allow combining different data and their presentation on one sheet.

A dashboard consists of widgets representing data either in the form of HTML content, or in the form of a diagram and/or table. Each of these cases uses its own source data.

  * [IMTDataset](Dataset-Interfaces/IMTDataset.md) — set of tabular data for widgets displaying diagrams and tables. Working with these data is completely equivalent to [tabular reports](Tabular-Reports.md).
  * [IMTReportDashboardHtml](Dashboard-Interfaces/IMTReportDashboardHtml.md) \- data set for widgets displaying HTML content. Working with these data is completely equivalent to [HTML reports](HTML-Reports.md).



A data set is bound to the widget using the [IMTReportDashboardWidget::Html](Dashboard-Interfaces/IMTReportDashboardWidget/Html.md) or [IMTReportDashboardWidget::Data](Dashboard-Interfaces/IMTReportDashboardWidget/Data.md) method depending on its type. The same data set can be used in different widgets, for example for displaying the same data in different ways or displaying different parts of the data set in separate tables.

<a id="example-of-creating-a-dashboard-with-charts-and-tables"></a>
## Example of creating a dashboard with charts and tables (#example-of-creating-a-dashboard-with-charts-and-tables)

Generate a simple tabular report that will display clients names and their leverage sizes using the previously [created report example](Creating-a-Simple-Report.md). Generation process can be divided into the following steps:

  * [Report description (#description)](Tabular-Reports.md#description)
  * [Table record description (#table-record)](Tabular-Reports.md#table-record)
  * [Report generation and output (#implementation)](Tabular-Reports.md#implementation)



<a id="description"></a>
### Report description (#description)

Before the start of a request implementation and data output, we should return to the report type and its parameters described in the [MTReportInfo (#mtreportinfo)](Creating-a-Simple-Report.md#mtreportinfo) structure.
    
    
    //+------------------------------------------------------------------+
    //| Module description structure                                     |
    //+------------------------------------------------------------------+
    const MTReportInfo CMyTableReport::s_info=
      {
       100,
       MTReportAPIVersion,
       MTReportInfo::IE_VERSION_ANY,
       L"My Table Report",
       L"Copyright 2001-2011, MetaQuotes Software Corp.",
       L"MetaTrader 5 Report API plug-in",
       0,
       MTReportInfo::TYPE_DASHBOARD,
         L"Example",
         {              // parameters
          { MTReportParam::TYPE_GROUPS, MTAPI_PARAM_GROUPS, L"*" },
         },1            // number of parameters
      };
    //+------------------------------------------------------------------+

The key parameters here are:

  * MTReportInfo::TYPE_DASHBOARD — [dashboard type report (#entypes)](../Structures/MTReportInfo.md#entypes).
  * { MTReportParam::TYPE_GROUPS, MTAPI_PARAM_GROUPS, L"*" } — [external parameters](../Structures/MTReportParam.md) of a report generation (type, name and value by default) that are set during a report request in MetaTrader 5 Manager. A list of the groups, from which the clients will be requested, may be set for that report. All groups is a default value (the symbol "*" is indicated);
  * 1 — number of parameters.



> The [MTAPI_PARAM_GROUPS (#parameters)](../Structures/MTReportParam.md#parameters) macro is used as the parameter name. This macro inserts a name of a field where the groups in the Manager terminal are selected.

<a id="table-record"></a>
### Table record description (#table-record)

Also, the structure of a report record that will be created should be described before the generation process starts. Name the structure TableRecord and add its description into the MyTableReport.h file to the [CMyTableReport (#implementation)](Creating-a-Simple-Report.md#implementation) class private part:
    
    
    class CDashboard : public IMTReportContext
      {
    private:
       static const MTReportInfo s_info;            // Report data
       //--- table record
       #pragma pack(push,1)
       struct TableRecord
         {
          wchar_t        name[32];
          UINT           leverage;
         };
       #pragma pack(pop)     
    //--- ...
      };
    //+------------------------------------------------------------------+

<a id="implementation"></a>
### Report generation and output process (#implementation)

Report generation and output are performed in the [CMyTableReport::Generate (#generate)](Creating-a-Simple-Report.md#generate) method.
    
    
    //+------------------------------------------------------------------+
    //| Report generation method                                         |
    //+------------------------------------------------------------------+
    MTAPIRES CDashboard::Generate(const UINT type,IMTReportAPI *api)
      {
       IMTDatasetColumn *column=NULL;
       IMTDataset       *data=NULL;
       IMTUser          *user=NULL;
       UINT64           *logins=NULL;
       UINT              logins_total=0;
       MTAPIRES          res;
    //--- check the pointer
       if(!api) 
         return(MT_RET_ERR_PARAMS);
    //--- create a data set
       if((data=api->DatasetAppend())==NULL)
         {
          return(MT_RET_ERR_MEM);
         }
    //--- create a column
       if((column=data->ColumnCreate())==NULL)
         {
          return(MT_RET_ERR_MEM);
         }
    //--- prepare the first column
       column->Clear();
       column->Name(L"Name");
       column->ColumnID(1);
       column->Offset(offsetof(TableRecord,name));
       column->Type(IMTDatasetColumn::TYPE_STRING);
       column->Size(MtFieldSize(TableRecord,name));
       if((res=data->ColumnAdd(column))!=MT_RET_OK)
         {
          column->Release();
          return(res);
         }
    //--- prepare the second column
       column->Clear();
       column->Name(L"Leverage");
       column->ColumnID(2);
       column->Offset(offsetof(TableRecord,leverage));
       column->Type(IMTDatasetColumn::TYPE_UINT32);
    //---
       if((res=data->ColumnAdd(column))!=MT_RET_OK)
         {
          column->Release();
          return(res);
         }
    //---
       column->Release();     
    //--- get the list of users
       if((res=api->ParamLogins(logins,logins_total))!=MT_RET_OK)
          return(res);
    //--- check whether the data have been received?
       if(logins && logins_total)
         {
          //--- create an object of a client record
          if((user=api->UserCreate())==NULL)
            {
             api->Free(logins);
             return(MT_RET_ERR_MEM);
            }
          //--- table generation
          for(UINT i=0;i<logins_total;i++)
            {
             //---
             if(api->UserGet(logins[i],user)!=MT_RET_OK) continue;
             //---
             TableRecord record={0};
             //---
             CMTStr::Copy(record.name,user->Name());
             record.leverage=user->Leverage();
             //---
             if((res=data->RowWrite(&record,sizeof(record)))!=MT_RET_OK)
               {
                api->Free(logins);
                user->Release();
                return(res);
               }
            }
          //--- release of the logins list
          api->Free(logins);
          //---
          user->Release();     
         }

Now, let's thoroughly examine this example by dividing it into blocks:

  * [Variables (#variables)](Tabular-Reports.md#variables)
  * [Checks (#checks)](Tabular-Reports.md#checks)
  * [A column object creation (#column-create)](Tabular-Reports.md#column-create)
  * [Preparing the first column (#first-column)](Tabular-Reports.md#first-column)
  * [Preparing the second column (#second-column)](Tabular-Reports.md#second-column)
  * [Get the list of users (#list)](Tabular-Reports.md#list)
  * [Report generation (#generation)](Tabular-Reports.md#generation)



Variables

Essential variables are declared at first:
    
    
    IMTDatasetColumn *column=NULL;
       IMTDataset       *data=NULL;
       IMTUser          *user=NULL;
       UINT64           *logins=NULL;
       UINT              logins_total=0;
       MTAPIRES          res;

It is recommended to null all variables during the declaration.

Checks
    
    
    //--- check of pointer
       if(!api) 
         return(MT_RET_ERR_PARAMS);

In this block, the pointer to [IMTReportAPI](Main-Interface-of-Reports.md) is checked for validity.

Creating a column object and a data set
    
    
    //--- create a data set
       if((data=api->DatasetAppend())==NULL)
         {
          return(MT_RET_ERR_MEM);
         }
    //--- create a column
       if((column=data->ColumnCreate())==NULL)
         {
          return(MT_RET_ERR_MEM);
         }

The [IMTReportAPI::DatasetAppend](Main-Interface-of-Reports/Dataset/Append.md) and [IMTDataset::ColumnCreate](Dataset-Interfaces/IMTDataset.md) methods are used for creating data set and column objects.

Preparing the first column

The first column will contain user names. The column preparation practically means specifying a cell with its header.
    
    
    //--- prepare the first column
       column->Clear();
       column->Name(L"Name");
       column->ColumnID(1);
       column->Offset(offsetof(TableRecord,name));
       column->Type(IMTDatasetColumn::TYPE_STRING);
       column->Size(MtFieldSize(TableRecord,name));
       if((res=data->ColumnAdd(column))!=MT_RET_OK)
         {
          column->Release();
          return(res);
         }

Procedure:

  * The column is cleared using the [IMTDatasetColumn::Clear](Dataset-Interfaces/IMTDatasetColumn/Clear.md) method;
  * The "Name" is assigned to the column using the [IMTDatasetColumn::Name](Dataset-Interfaces/IMTDatasetColumn/Name.md) method;
  * ID "1" is assigned to the column using the [IMTDatasetColumn::ColumnID](Dataset-Interfaces/IMTDatasetColumn/ColumnID.md) method;
  * A shift in bytes is assigned to the column using the [IMTDatasetColumn::Offset](Dataset-Interfaces/IMTDatasetColumn/Offset.md) method. "Offsetof" macros is used in the example to avoid calculation of a shift for each column (calculated as previous columns size). The stddef.h file should be included into the project to use the macros. The name of a field from the previously described table record structure ([TableRecord (#table-record)](Tabular-Reports.md#table-record)) is transferred to the macros.
  * "String" type is assigned to the column using the [IMTDatasetColumn::Type](Dataset-Interfaces/IMTDatasetColumn/Type.md) method;
  * A size in bytes is assigned to the column using the [IMTDatasetColumn::Size](Dataset-Interfaces/IMTDatasetColumn/Size.md) method. The MtFieldSize macros is used to simplify the defining of a column size. The name of a field from the previously described table record structure (TableRecord) is also transferred to the macro. This macro is not standard. Its realization should be added to the stdafx.h file.
  * The generated column is then added to the IMTReportAPI object copy with the help of the [IMTDataset::ColumnAdd](Dataset-Interfaces/IMTDataset/ColumnAdd.md) method.
  * In case of an adding error, the column object should be necessarily freed by using the Release method ([IMTDatasetColumn::Release](Dataset-Interfaces/IMTDatasetColumn/Release.md)).



MtFieldSize macro realization:
    
    
    //+------------------------------------------------------------------+
    //| Macros for a size calculation                                    |
    //+------------------------------------------------------------------+
    #define MtFieldSize(type,member) (sizeof(((type*)(0))->member))
    //+------------------------------------------------------------------+

Preparing the second column

The column for a leverage size recording should be prepared similar to the previous column:
    
    
    //--- prepare the second column
       column->Clear();
       column->Name(L"Leverage");
       column->ColumnID(2);
       column->Offset(offsetof(TableRecord,leverage));
       column->Type(IMTDatasetColumn::TYPE_UINT32);
    //---
       if((res=data->ColumnAdd(column))!=MT_RET_OK)
         {
          column->Release();
          return(res);
         }
    //---
       column->Release();

In all cases except strings, data size is specified by its type ([IMTDatasetColumn::EnType (#entype)](Dataset-Interfaces/IMTDatasetColumn/Enumerations.md#entype)). Therefore, the [IMTDatasetColumn::Size](Dataset-Interfaces/IMTDatasetColumn/Size.md) method is not called during the second column preparation.

The column object should be freed by calling the Release method ([IMTDatasetColumn::Release](Dataset-Interfaces/IMTDatasetColumn/Release.md)) after the second column preparation is finished.

Get the list of users
    
    
    //--- get the list of users
       if((res=api->ParamLogins(logins,logins_total))!=MT_RET_OK)
          return(res);

The [IMTReportAPI::ParamLogins](Main-Interface-of-Reports/Report-Parameters/ParamLogins.md) method is used to get the list of users. To make the method work, the [report description (#description)](Tabular-Reports.md#description) contains the [MTReportParam::TYPE_GROUPS](../Structures/MTReportParam.md) parameter that has been turned on.

Data generation

After a user list is received, the name and the leverage should be requested for each of them in the loop.
    
    
    //--- check whether the data have been received
       if(logins && logins_total)
         {
          //--- create an object of a client record
          if((user=api->UserCreate())==NULL)
            {
             api->Free(logins);
             return(MT_RET_ERR_MEM);
            }
          //--- table generation
          for(UINT i=0;i<logins_total;i++)
            {
             //---
             if(api->UserGet(logins[i],user)!=MT_RET_OK) continue;
             //---
             TableRecord record={0};
             //---
             CMTStr::Copy(record.name,user->Name());
             record.leverage=user->Leverage();
             //---
             if((res=api->TableRowWrite(&record,sizeof(record)))!=MT_RET_OK)
               {
                api->Free(logins);
                user->Release();
                return(res);
               }
            }
          //--- release of the logins list
          api->Free(logins);
          //---
          user->Release();     
         }

Procedure:

  * Whether the list of logins is received is checked in the 'if' statement.
  * A client record object is then created by using the [IMTReportAPI::UserCreate](Main-Interface-of-Reports/Users/UserCreate.md) method. In case of a creation error, received list of logins is freed by using the [IMTReportAPI::Free](Main-Interface-of-Reports/Common-Functions/Free.md) method.
  * Client records (IMTUser) for each of the received logins are requested in the 'for' loop using the [IMTReportAPI::UserGet](Main-Interface-of-Reports/Users/UserGet.md) method.
  * The 'record' table record structure ([TableRecord (#table-record)](Tabular-Reports.md#table-record)) is set to zero.
  * A name from a client record is copied to an appropriate record structure field using the auxiliary CMTStr::Copy method.
  * A leverage value is copied from a client record to an appropriate record structure field.
  * Received row is assigned to the api report object using the [IMTReportAPI::TableRowWrite](Main-Interface-of-Reports/Tabular-Reports/Rows/TableRowWrite.md) method. In case of a record error, received list of logins is freed by using the [IMTReportAPI::Free](Main-Interface-of-Reports/Common-Functions/Free.md) method.
  * After the report generation is complete, the previously received array of logins is freed using the [IMTReportAPI::Free](Main-Interface-of-Reports/Common-Functions/Free.md) method.
  * The client record object is freed by the Release method ([IMTUser::Release](../Database-Interfaces/Users/IMTUser/Release.md)).



Configuring a widget

//--- create a widget   
if((widget=api->DashboardWidgetAppend())==NULL)   
{   
return(MT_RET_ERR_MEM);   
} //--- create a widget widget->Title(L"Leverage"); widget->Type(IMTReportDashboardWidget::WIDGET_TYPE_CHART_AREA); //--- bind data to a widget widget->Data(data);   
//--- successful   
return(MT_RET_OK);   
}   
//+------------------------------------------------------------------+  
---  
  
Procedure:

  * The [IMTReportAPI::DashboardWidgetAppend](Main-Interface-of-Reports/Dashboards/DashboardWidgetAppend.md) method is used to create a widget object.
  * Widget title and type are specified.
  * The previously created data set is bound to the widget by the [IMTReportDashboardWidget::Data](Dashboard-Interfaces/IMTReportDashboardWidget/Data.md) method.
  * [MT_RET_OK](../Return-Codes/Successful-completion.md) operation successful accomplishment code is returned at the end of the report generation.


