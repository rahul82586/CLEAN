[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [News](../News.md) / Data Structure

[Previous](../News.md) | [Next](Send.md)

# Data Structure

News messages are passed in the JSON format in response to the [/api/news/get](Get-Without-Body.md) and [/api/news/get_body](Get-With-Body.md) requests.

Field | Type | Description  
ID | Integer | News ID.  
Size | Integer | The size of the news body in bytes.  
Time | Integer | The time of news sending in seconds that have elapsed since 01.01.1970.  
Language | Integer | News language in the LANGID format used in [MS Windows](https://msdn.microsoft.com/en-us/library/windows/desktop/dd318693) systems (value from Prim.lang.identifier).  
Category | String | News category.  
Subject | String | News subject.  
Body | String | News body in the Base64 format.
