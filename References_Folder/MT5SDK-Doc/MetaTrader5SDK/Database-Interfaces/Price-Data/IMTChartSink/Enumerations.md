[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Price Data](../../Price-Data.md) / [IMTChartSink](../IMTChartSink.md) / Enumerations

[Previous](../IMTChartSink.md) | [Next](OnChartSplit.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

The [IMTChartSink](../IMTChartSink.md) class contains the following enumerations:

  * [IMTChartSink::EnSplitRounding (#ensplitrounding)](Enumerations.md#ensplitrounding)



<a id="ensplitrounding"></a>
## IMTChartSink::EnSplitRounding (#ensplitrounding)

IMTChartSink::EnSplitRounding lists types of rounding used when splitting price data.

ID | Value | Description  
SPLIT_ROUNDING_STANDARD | 0 | Standard rounding.  
SPLIT_ROUNDING_DOWN | 1 | Rounding down.  
SPLIT_ROUNDING_UP | 2 | Rounding up.  
SPLIT_ROUNDING_FIRST |  | Enumeration start. Corresponds to SPLIT_ROUNDING_STANDARD.  
SPLIT_ROUNDING_LAST |  | Enumeration end. Corresponds to SPLIT_ROUNDING_UP.  
  
The enumeration is used in the following methods:

  * [OnChartSplit](OnChartSplit.md)
  * [HookChartSplit](HookChartSplit.md)


