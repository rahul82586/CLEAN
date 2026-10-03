[🏠 Document Start](../README.md) / [Report API](README.md) / Charts

[Previous](Templates.md) | [Next](Memory-Management.md)

<a id="charts"></a>
# Charts (#charts)

The MetaTrader 5 Report API allows to add SVG charts into [HTML reports](HTML-Reports.md) and [dashboards](Dashboard-Interfaces/IMTReportDashboardHtml.md). A chart consists of two basic elements:

  * Headers series — a data series that is displayed in the form of labels to the one of the chart's axes;
  * Values series — data series that are displayed directly on the chart.



> The Internet Explorer browser installed together with a manager terminal is used to show HTML reports including SVG charts. Note that SVG charts are supported beginnig from the Internet Explorer 9.

An example of working with an SVG chart. The following actions must be performed to add the charts into the report:

  * Add a new CMyChartTable report class equivalent to the way it is done for a [HTML report (#class-add)](HTML-Reports.md#class-add).
  * Realize the class equivalent to the way it is done for a [HTML report (#class-implement)](HTML-Reports.md#class-implement).
  * [Set report parameters (#description)](Charts.md#description) transferred in the MTReportInfo structure.
  * Fill the entry points equivalent to the way it is done for a [HTML report (#exported-functions)](HTML-Reports.md#exported-functions).
  * [Add the charts realization (#implementation)](Charts.md#implementation) into the report code.



This section covers only working with charts.

<a id="description"></a>
## Report parameters (#description)

Before we start adding the charts [report parameters (#description)](HTML-Reports.md#description) transferred by the [MTReportInfo](../Structures/MTReportInfo.md) structure must be properly filled. Report parameters are filled in the MyChartReport.cpp file:
    
    
    //+------------------------------------------------------------------+
    //| Module description structure                                     |
    //+------------------------------------------------------------------+
    const MTReportInfo CMyChartReport::s_info=
      {
       100,
       MTReportAPIVersion,
       MTReportInfo::IE_VERSION_9,
       L"My Chart Report",
       L"Copyright 2001-2011, MetaQuotes Software Corp.",
       L"MetaTrader 5 Report API plug-in",
       0,
       MTReportInfo::TYPE_HTML,
         { 0 },
         {              // Parameters
          { MTReportParam::TYPE_GROUPS, MTAPI_PARAM_GROUPS, L"*" },
         },1            // Number of parameters
      };
    //+------------------------------------------------------------------+

The MTReportInfo::IE_VERSION_9 parameter must be indicated in the structure description. Therefore, Internet Explorer browser version installed together with a manager terminal will be checked when requesting a report. In case the Internet Explorer version is lower that 9, it will be suggested to a manager to update it to the last version.

<a id="implementation"></a>
## Adding of charts (#implementation)

Report generation is performed in the CMyChartReport::Generate method at the MyChartReport.cpp file.
    
    
    //+------------------------------------------------------------------+
    //| Report generation method                                         |
    //+------------------------------------------------------------------+
    MTAPIRES CMyChartReport::Generate(const UINT type,IMTReportAPI *api)
      {
       IMTReportChart  *chart=NULL;
       IMTReportSeries *series_title=NULL,*series_values=NULL;
    //--- Checking for a pointer
       if(!api)
          return(MT_RET_ERR_PARAMS);
    //--- Checking the type of a requested report
       if(type!=MTReportInfo::TYPE_HTML)
          return(MT_RET_ERR_PARAMS);
    //--- Creating a chart object
       if((chart=api->ChartCreate())==NULL)
          return(MT_RET_ERR_MEM);
    //--- Chart setting
       chart->Title(L"My Chart");
       chart->Type(IMTReportChart::TYPE_GRAPH);
    //--- Creating a headers series
       if((series_title=api->ChartCreateSeries())==NULL)
         {
          chart->Release();
          return(MT_RET_ERR_MEM);
         }
    //--- Add a series to a chart
    //--- (after the series is successfully added it belongs to the chart and the latter is responsible for the series deletion)
       if(chart->SeriesAdd(series_title)!=MT_RET_OK)
         {
          series_title->Release();
          chart->Release();
          return(MT_RET_ERR_MEM);
         }
    //--- Set the headers series
       series_title->Type(IMTReportSeries::TYPE_TITLE);
    //--- Creating a values series
       if((series_values=api->ChartCreateSeries())==NULL)
         {
          series_title->Release();
          chart->Release();
          return(MT_RET_ERR_MEM);
         }
    //--- Add a series to a chart
    //--- (after the series is successfully added it belongs to the chart and the latter is responsible for the series deletion)
       if(chart->SeriesAdd(series_values)!=MT_RET_OK)
         {
          series_values->Release();
          chart->Release();
          return(MT_RET_ERR_MEM);
         }
    //--- The value series setting
       series_values->Type(IMTReportSeries::TYPE_AREA);
       series_values->Tooltip(L"%VARIABLE% * %VARIABLE% = %VALUE%");
    //--- Forming the data
       for(UINT i=1;i<=10;i++)
         {
          series_title->ValueAddDouble(i);
          series_values->ValueAddDouble(i*i);
         }
    //--- Writing to HTML
       api->HtmlWrite(L"%s",L"<html><head>\r\n");
    //--- It is important to specify the mode of working in the Internet Explorer in the HTML header
       api->HtmlWrite(L"%s",L"<meta http-equiv=\"X-UA-Compatible\" content=\"IE=9\" />\r\n");
    //--- The record is continued
       api->HtmlWrite(L"%s",L"</head><body style=\"height:400px;\">\r\n");
    //--- The chart display
       api->ChartWriteHtml(chart);
    //--- Display end
       api->HtmlWrite(L"%s",L"</body></html>\r\n");
    //--- Deleting the chart object
    //--- (its deletion will lead to the deletion of the both data series)
       chart->Release();
    //--- Successful
       return(MT_RET_OK);
      }
    //+------------------------------------------------------------------+

Let's thoroughly examine the previously mentioned code by dividing it into blocks:

  * [Variables (#variables)](Charts.md#variables)
  * [Checks (#checks)](Charts.md#checks)
  * [Creating a chart object and setting (#chart-object)](Charts.md#chart-object)
  * [Creating a headers series (#title-series)](Charts.md#title-series)
  * [Creating a values series (#value-series)](Charts.md#value-series)
  * [Forming the data (#data)](Charts.md#data)
  * [Output in HTML (#html)](Charts.md#html)



<a id="variables"></a>
### Variables (#variables)

Essential variables are declared at first:
    
    
    IMTReportChart  *chart=NULL;                              // the chart object
       IMTReportSeries *series_title=NULL,*series_values=NULL;   // the chart series object

It is recommended to null all variables during the declaration.

<a id="checks"></a>
### Checks (#checks)
    
    
    //--- Checking for a pointer
       if(!api)
          return(MT_RET_ERR_PARAMS);
    //--- Checking the type of a requested report
       if(type!=MTReportInfo::TYPE_HTML)
          return(MT_RET_ERR_PARAMS);

Checking the pointer validity at the [IMTReportAPI](Main-Interface-of-Reports.md) and also verification of the requested report type (transferred by the type parameter into the CMyChartReport::Generate function) are performed in this block.

<a id="chart-object"></a>
### Creating a chart object and setting (#chart-object)
    
    
    //--- Creating a chart object
       if((chart=api->ChartCreate())==NULL)
          return(MT_RET_ERR_MEM);
    //--- Chart setting
       chart->Title(L"My Chart");
       chart->Type(IMTReportChart::TYPE_GRAPH);

The chart object is created using the [IMTReportAPI::ChartCreate](Main-Interface-of-Reports/HTML-Reports/Charts/ChartCreate.md) method. Minimum chart settings include the indication of its name and type using the [IMTReportChart::Title](Diagram-Interfaces/IMTReportChart/Title.md) and [IMTReportChart::Type](Diagram-Interfaces/IMTReportChart/Type.md) methods respectively. In our case the chart is [linear (#encharttype)](Diagram-Interfaces/IMTReportChart/Enumerations.md#encharttype).

<a id="title-series"></a>
### Creating a headers series (#title-series)

The headers series is displayed as a labels to the chart's axis.
    
    
    //--- Creating a headers series
       if((series_title=api->ChartCreateSeries())==NULL)
         {
          chart->Release();
          return(MT_RET_ERR_MEM);
         }
    //--- Add a series to a chart
       if(chart->SeriesAdd(series_title)!=MT_RET_OK)
         {
          series_title->Release();
          chart->Release();
          return(MT_RET_ERR_MEM);
         }
    //--- Set the headers series
       series_title->Type(IMTReportSeries::TYPE_TITLE);

Clarifications to the code:

  * The [IMTReportAPI::ChartCreateSeries](Main-Interface-of-Reports/HTML-Reports/Charts/ChartCreateSeries.md) method is used for a series object creation. In case of a creation error, previously created "chart" object must be freed by using the [IMTReportChart::Release](Diagram-Interfaces/IMTReportChart/Release.md) method.
  * The [IMTReportChart::SeriesAdd](Diagram-Interfaces/IMTReportChart/SeriesAdd.md) method is used to add the series object to the chart object. After that the series object managing is fully passed to the chart object.
  * In case of an adding error, previously created chart and series object must be freed using the [IMTReportChart::Release](Diagram-Interfaces/IMTReportChart/Release.md) and [IMTReportSeries::Release](Diagram-Interfaces/IMTReportSeries/Release.md) methods respectively.
  * To turn the added series into the headers series the [TYPE_TITLE (#enseriestype)](Diagram-Interfaces/IMTReportSeries/Enumerations.md#enseriestype) type is assigned to it using the [IMTReportSeries::Type](Diagram-Interfaces/IMTReportSeries/Type.md) method.



<a id="value-series"></a>
### Creating a values series (#value-series)

The values series is directly displayed on the chart in the selected display mode.
    
    
    //--- Creating a values series
       if((series_values=api->ChartCreateSeries())==NULL)
         {
          series_title->Release();
          chart->Release();
          return(MT_RET_ERR_MEM);
         }
    //--- Add a series to a chart
       if(chart->SeriesAdd(series_values)!=MT_RET_OK)
         {
          series_values->Release();
          chart->Release();
          return(MT_RET_ERR_MEM);
         }
    //--- The value series setting
       series_values->Type(IMTReportSeries::TYPE_AREA);
       series_values->Tooltip(L"%VARIABLE% * %VARIABLE% = %VALUE%");

Clarifications to the code:

  * The [IMTReportAPI::ChartCreateSeries](Main-Interface-of-Reports/HTML-Reports/Charts/ChartCreateSeries.md) method is used for a series object creation. In case of a generation error, previously created chart and series object must be freed using the [IMTReportChart::Release](Diagram-Interfaces/IMTReportChart/Release.md) and [IMTReportSeries::Release](Diagram-Interfaces/IMTReportSeries/Release.md) methods respectively.
  * The [IMTReportChart::SeriesAdd](Diagram-Interfaces/IMTReportChart/SeriesAdd.md) method is used to add the series object to the chart object. After that the series object managing is fully passed to the chart object.
  * In case of an adding error, previously created chart and series object must be freed using the [IMTReportChart::Release](Diagram-Interfaces/IMTReportChart/Release.md) and [IMTReportSeries::Release](Diagram-Interfaces/IMTReportSeries/Release.md) methods respectively.
  * To set the kind of the series type on the chart, the [TYPE_AREA (#enseriestype)](Diagram-Interfaces/IMTReportSeries/Enumerations.md#enseriestype) type is assigned to it using the [IMTReportSeries::Type](Diagram-Interfaces/IMTReportSeries/Type.md) method.
  * The tooltips are set additionally to the series values with the help of the [IMTReportSeries::Tooltip](Diagram-Interfaces/IMTReportSeries/Tooltip.md) method. The tooltips appear when putting the mouse cursor over the series points. The tooltips may contain special macroses. Complete list of macroses is included into the [IMTReportSeries::Tooltip](Diagram-Interfaces/IMTReportSeries/Tooltip.md) method description.



<a id="data"></a>
### Forming the data (#data)

Fill the chart by the sequence of the numbers raised to their own power.
    
    
    //--- Forming the data
       for(UINT i=1;i<=10;i++)
         {
          series_title->ValueAddDouble(i);
          series_values->ValueAddDouble(i*i);
         }

The values from 1 to 10 are assigned to the header series in the for cycle, the same values raised to their own power are assigned to the values series. The [IMTReportSeries::ValueAddDouble](Diagram-Interfaces/IMTReportSeries/ValueAddDouble.md) method is used for assigning the values.

<a id="html"></a>
### Output in HTML (#html)

This report presents the example of the HTML output without using the [templates](Templates.md). It is not recommended to use that method to create custom reports.
    
    
    //--- Writing to HTML
       api->HtmlWrite(L"%s",L"<html><head>\r\n");
    //--- It is important to specify the mode of working in the Internet Explorer in the HTML header
       api->HtmlWrite(L"%s",L"<meta http-equiv=\"X-UA-Compatible\" content=\"IE=9\" />\r\n");
    //--- The record is continued
       api->HtmlWrite(L"%s",L"</head><body style=\"height:400px;\">\r\n");
    //--- The chart display
       api->ChartWriteHtml(chart);
    //--- Display end
       api->HtmlWrite(L"%s",L"</body></html>\r\n");
    //--- deleting the chart object (its deletion will lead to the deletion of the both data series)
       chart->Release();
    //--- Successful
       return(MT_RET_OK);
      }
    //+------------------------------------------------------------------+

Explanation to the code:

  * Standard HTML file body is created using the HtmlWrite method.
  * One of the key moments is an output of the <meta http-equiv=\"X-UA-Compatible\" content=\"IE=9\" /> row. This row is a command for the Internet Explorer browser to work in the version 9 mode without using compatibility mode. This row is necessary for correct display of a HTML page with charts.
  * The chart occupies the whole space of the parent container in HTML. Therefore, to specify the size of the chart you need to specify the size of the container it is inserted in. In our case the container is <body></body>.
  * The [IMTReportAPI::ChartWriteHtml](Main-Interface-of-Reports/HTML-Reports/Charts/ChartWriteHtml.md) method is used to display the chart on a page.
  * After the page is displayed the chart object is freed and the [MT_RET_OK](../Return-Codes/Successful-completion.md) code is returned.


