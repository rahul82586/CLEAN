[🏠 Document Start](../README.md) / [Return Codes](README.md) / Report Generation

[Previous](Trade-management.md) | [Next](Price-Data.md)

# Report Generation

This group of codes is returned by the server during generation of reports:

Constant | Value | Description  
MT_RET_REPORT_SNAPSHOT | 5001 | Database snapshot error.  
MT_RET_REPORT_NOTSUPPORTED | 5002 | The method is not supported for this report.  
MT_RET_REPORT_NODATA | 5003 | No information for the report.  
MT_RET_REPORT_TEMPLATE_BAD | 5004 | Wrong template.  
MT_RET_REPORT_TEMPLATE_END | 5005 | The end of the template.  
MT_RET_REPORT_INVALID_ROW | 5006 | Invalid row size.  
MT_RET_REPORT_LIMIT_REPEAT | 5007 | Reached the limit of the number of duplicate tags.  
MT_RET_REPORT_LIMIT_REPORT | 5008 | Reached the limit of the report size.
