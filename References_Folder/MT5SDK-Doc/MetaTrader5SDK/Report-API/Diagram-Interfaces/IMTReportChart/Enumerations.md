[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Diagram Interfaces](../../Diagram-Interfaces.md) / [IMTReportChart](../IMTReportChart.md) / Enumerations

[Previous](../IMTReportChart.md) | [Next](Release.md)

<a id="imtreportchart"></a>
# IMTReportChart (#imtreportchart)

The [IMTReportChart](../IMTReportChart.md) interface contains the following enumerations:

  * [IMTReportChart::EnChartType (#encharttype)](Enumerations.md#encharttype)
  * [IMTReportChart::EnChartFlags (#enchartflags)](Enumerations.md#enchartflags)



<a id="encharttype"></a>
## IMTReportChart::EnChartType (#encharttype)

Types of charts are listed in IMTReportChart::EnChartType:

ID | Value | Description  
TYPE_GRAPH | 0 | Standard chart.  
TYPE_GRAPH_ACCUMULATION | 1 | Standard accumulated indications chart.  
TYPE_GRAPH_NORMALIZED | 2 | Standard normalized chart.  
TYPE_GRAPH_STACKED | 3 | Standard chart with stacking.  
TYPE_BAR | 100 | Bar graph.  
TYPE_BAR_ACCUMULATION | 101 | Accumulated indications bar graph.  
TYPE_BAR_NORMALIZED | 102 | Bar normalized graph.  
TYPE_BAR_STACKED | 103 | Bar grap with stacking.  
TYPE_PIE | 200 | Pie chart.  
  
This enumeration is used in the [IMTReportChart::Type](Type.md) method.

<a id="enchartflags"></a>
## IMTReportChart::EnChartFlags (#enchartflags)

Types of charts are listed in IMTReportChart::EnChartFlags:

ID | Value | Description  
FLAG_ACCUMULATED_VALUES | 1 | Show accumlated values.  
FLAG_SHOW_TABLE | 2 | Show the table with values.  
  
This enumeration is used in the [IMTReportChart::Flags](Flags.md) method.
