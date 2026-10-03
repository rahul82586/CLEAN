[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Diagram Interfaces](../../Diagram-Interfaces.md) / [IMTReportSeries](../IMTReportSeries.md) / Enumerations

[Previous](../IMTReportSeries.md) | [Next](Release.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

The [IMTReportSeries](../IMTReportSeries.md)interface contains the following enumerations:

  * [IMTReportSeries::EnSeriesType (#enseriestype)](Enumerations.md#enseriestype)
  * [IMTReportSeries::EnSeriesFlags (#enseriesflags)](Enumerations.md#enseriesflags)



<a id="enseriestype"></a>
## IMTReportSeries::EnSeriesType (#enseriestype)

Types of series (values arrays) for creating charts are listed in IMTReportSeries::EnSeriesType:

ID | Value | Description  
TYPE_TITLE | 0 | Header values series. The values of that series are used as text labels attached to chart axes.  
TYPE_LINE | 100 | Series of the values that will be displayed as a line. Applicable for the charts of the [IMTReportChart::TYPE_GRAPH* (#encharttype)](../IMTReportChart/Enumerations.md#encharttype) type.  
TYPE_HISTOGRAM | 101 | Series of the values that will be displayed as vertical bars (bar graph). Applicable for the charts of the [IMTReportCHart::TYPE_GRAPH* (#encharttype)](../IMTReportChart/Enumerations.md#encharttype) type.  
TYPE_BAR | 102 | Series of the values that will be displayed as horizontal bars (bar graph). Applicable for the charts of the [IMTReportChart::TYPE_BAR* (#encharttype)](../IMTReportChart/Enumerations.md#encharttype) type.  
TYPE_AREA | 103 | Series of the values that will be displayed as a colored polygon (area graph). Applicable for the charts of the [IMTReportChart::TYPE_GRAPH* (#encharttype)](../IMTReportChart/Enumerations.md#encharttype) type.  
TYPE_PIECE | 104 | The series consisting of one value that will be displayed as a circle sector. Applicable for the charts of the [IMTReportChart::TYPE_PIE* (#encharttype)](../IMTReportChart/Enumerations.md#encharttype) type.  
  
This enumeration is used in the [IMTReportSeries::Type](Type.md) method.

<a id="enseriesflags"></a>
## IMTReportSeries::EnSeriesFlags (#enseriesflags)

Types of series flags are listed in IMTReportSeries::EnSeriesFlags:

ID | Value | Description  
FLAG_SHOW_VALUES | 1 | Show a series value on a chart.  
  
This enumeration is used in the [IMTReportSeries::Flags](Flags.md) method.
