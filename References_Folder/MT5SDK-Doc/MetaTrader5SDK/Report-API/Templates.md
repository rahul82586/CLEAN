[🏠 Document Start](../README.md) / [Report API](README.md) / Templates

[Previous](Dashboards.md) | [Next](Charts.md)

# Templates

Templates can be used in MetaTrader 5 Report API to form [HTML reports](HTML-Reports.md) and [dashboards](Dashboard-Interfaces/IMTReportDashboardHtml.md). Templates are described according to the HTML markup rules.

There is no need to use the templates, as HTML can be directly generated from the code using the [IMTReportAPI::HTMLWrite](Main-Interface-of-Reports/HTML-Reports/HTML/HtmlWrite.md), [IMTReportAPI::HTMLWriteSafe](Main-Interface-of-Reports/HTML-Reports/HTML/HtmlWriteSafe.md), [IMTReportDashboardHtml::Write](Dashboard-Interfaces/IMTReportDashboardHtml/Write.md) and [IMTReportDashboardHtml::WriteSafe](Dashboard-Interfaces/IMTReportDashboardHtml/WriteSafe.md) functions. But it is not recommended to use such method, as the report formatting and its logics will be mixed in the source code. Further work with such a code will be considerably complicated.

The template allows to describe the look of the report separately from the logics. Further it will allow to easily change the template formatting and the source code will be clear and comprehensible.

## Macros

Special macroses cn be used with the templates. The macroses are replaced with the report data when the report is generated.

The macros is a construction having the <mt5:random_name> look. There are two types of macros:

  * Simple ones have the <mt5:.../> look. Simple macros do not contain embedded constructions.
  * Complex ones have the <mt5:...>...</mt5:...> look. Such macros can contain embedded constructions consisting of HTML contents or another macros.



MetaTrader 5 Report API provides two methods of the macroses processing:

  * [IMTReportAPI::HtmlTplNext](Main-Interface-of-Reports/HTML-Reports/HTML/HtmlTplNext.md) — this method orders to get the next macros in a template.
  * [IMTReportAPI::HtmlTplProcess](Main-Interface-of-Reports/HTML-Reports/HTML/HtmlTplProcess.md) — this method orders to process constructions embedded in a complex macros. Using complex macroses is similar to the using of the while cycle. As long as the IMTReportAPI::HtmlProcess method is called for a complex macros, its contents will be processed. When the final </mt5:...> macros is reached, transition to the macros beginning will be performed where the decision concerning its contents processing can be made again. And the counter passed by Report API to the [IMTReportAPI::HtmlTplNext](Main-Interface-of-Reports/HTML-Reports/HTML/HtmlTplNext.md) method will increase by one.



A similar pair of methods is available for dashboards: [IMTReportDashboardHtml::TplNext ](Dashboard-Interfaces/IMTReportDashboardHtml/TplNext.md) and [IMTReportDashboardHtml::TplProcess](Dashboard-Interfaces/IMTReportDashboardHtml/TplProcess.md).

Using the methods of working with macroses allows to easily process and display the data arrays received from a trade server. [Example of using the macroses (#macro-process)](HTML-Reports.md#macro-process) is described in the section devoted to HTML reports.
