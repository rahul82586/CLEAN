[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [HTML Reports](../HTML-Reports.md) / HTML

[Previous](../HTML-Reports.md) | [Next](HTML/HtmlWrite.md)

# HTML Functions

The following functions for managing HTML code are available:

Function | Purpose  
---|---  
[HtmlWrite](HTML/HtmlWrite.md) | Output a formatted string into an HTML page.  
[HtmlWriteString](HTML/HtmlWriteString.md) | Output an unformatted string into an HTML page (faster output).  
[HtmlWriteSafe](HTML/HtmlWriteSafe.md) | Output a string into HTML with HTML service symbols screening.  
[HtmlTplLoad](HTML/HtmlTplLoad.md) | Load a template from the submitted line.  
[HtmlTplLoadFile](HTML/HtmlTplLoadFile.md) | Load a template from a file.  
[HtmlTplLoadResource](HTML/HtmlTplLoadResource.md) | Load a template from a resource.  
[HtmlTplNext](HTML/HtmlTplNext.md) | Get the next macros (predetermined tag) from a template for processing.  
[HtmlTplProcess](HTML/HtmlTplProcess.md) | Set the feature of the processing of all tags inside the current macros (predetermined tag).  
  
> The functions described in this section work only in case of an HTML report generation ([EnTypes::TYPE_HTML (#entypes)](../../../Structures/MTReportInfo.md#entypes)).
