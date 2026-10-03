[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [HTML Reports](../HTML-Reports.md) / Charts

[Previous](HTML/HtmlTplProcess.md) | [Next](Charts/ChartCreate.md)

# Charts Functions

The following functions for managing the charts are available:

Function | Purpose  
---|---  
[ChartCreate](Charts/ChartCreate.md) | Create a chart object.  
[ChartCreateSeries](Charts/ChartCreateSeries.md) | Create a data series object for a chart.  
[ChartWriteHtml](Charts/ChartWriteHtml.md) | Output of a chart to an HTML report.  
  
  * The functions described in this section work only in case of an HTML report generation ([EnTypes::TYPE_HTML (#entypes)](../../../Structures/MTReportInfo.md#entypes)).
  * The Internet Explorer browser installed together with a manager terminal is used to show HTML reports including SVG charts. Note that SVG charts are supported beginnig from the Internet Explorer 9.   
On default, Internet Explorer that is used in the manager terminal works in the 7 version compatibility mode. For the SVG chart to be displayed correctly, force it to use the Internet Explorer 9 compatibility mode. To do it, in the [heading of the HTML page (#html)](../../Charts.md#html) (within the pair of tags <head></head>), include the following line:  
<meta http-equiv=\"X-UA-Compatible\" content=\"IE=9\" />

  
---
