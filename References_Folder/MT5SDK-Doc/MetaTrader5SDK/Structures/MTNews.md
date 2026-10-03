[🏠 Document Start](../README.md) / [Structures](README.md) / MTNews

[Previous](MTGatewayInfo.md) | [Next](MTEconomicEvent.md)

<a id="mtnews"></a>
# MTNews (#mtnews)

The news structure is described in MTNews. The structure is defined with the one-byte alignment.
    
    
    #pragma pack(push,1)
    struct MTNews
      {
       //--- Constants
       enum constants
         {
          MAX_NEWS_BODY_LEN=1024*1024                           // max. body length
         };
       //--- News flags
       enum EnNewsFlags
         {
          FLAG_PRIORITY    =1,                                  // Priority flag
          FLAG_CALENDAR    =2                                   // Calendar news flag
          FLAG_MIME        =4,                                  // MIME content flag
          FLAG_CALENDAR    =8                                   // Flag to allow full news
         };
       UINT              language;                              // Language
       wchar_t           subject[256];                          // News subject
       wchar_t           category[256];                         // News category
       UINT              flags;                                 // News flags
       wchar_t          *body;                                  // Body
       UINT              body_len;                              // Body length
       UINT              languages_list[32];                    // The list of languages
       INT64             datetime;                              // Publication time
       UINT              reserved[64];                          // A reserved field
      };
    #pragma pack(pop)

This structure is used in the [IMTGatewayAPI::SendNews](../Gateway-API/Main-Interface/Quote-and-News-Feeds/SendNews.md) method.

<a id="enumerations"></a>
## Enumerations (#enumerations)

The following enumerations are described in the structure:

  * constants
  * EnNewsFlags



<a id="constants"></a>
### constants (#constants)

Used constants are described in this enumeration.

ID | Value | Description  
MAX_NEWS_BODY_LEN | 1024*1024 | The maximum allowable news size.  
  
<a id="ennewsflags"></a>
### EnNewsFlags (#ennewsflags)

News flags are listed in EnNewsFlags.

ID | Value | Description  
FLAG_PRIORITY | 1 | If the flag is set, the newsletter appears as important.  
FLAG_CALENDAR | 2 | If this flag is enabled, the news should be formed as an element of the economic calendar. At the moment, the flag is obsolete and supported only for backward compatibility. For the the economic calendar, one should use structure [MTEconomicEvent](MTEconomicEvent.md) and method [IMTGatewayAPI::SendEconomicEvents](../Gateway-API/Main-Interface/Quote-and-News-Feeds/SendEconomicEvents.md).  
FLAG_MIME | 4  | This flag determines how the news is interpreted. If there is no flag, the news is considered to have the UTF-16 encoding. If the flag is not set, the news is believed to be in UTF-16. If the flag is enabled, the news is believed to be in UTF-8. Regardless of the news encoding, the news length (body_len) must be specified in the number of wchart_t characters.  
FLAG_ALLOW_DEMO | 8 | Enabling this flag allow receiving the news entirely (including the body) for the groups that are allowed to receive news headers only ([EnNewsMode::NEWS_MODE_HEADERS (#ennewsmode)](../Configuration-Interfaces/Groups/IMTConGroup/Enumerations.md#ennewsmode)).  
  
<a id="parameters"></a>
## Parameters (#parameters)

MTNews structure contains the following parameters:

Field | Type | Description  
language | UINT | News language. Specified in the standard used in [MS Windows](https://msdn.microsoft.com/en-us/library/windows/desktop/dd318693) (a value from Prim.lang.identifier). The language code can also be retrieved using the WinAPI function:   
LCID LocaleNameToLCID(LPCWSTR lpName,DWORD dwFlags); The language ID is stored in the last two bytes of a received LCID.  
subject | wchar_t | The news subject in the UTF-16 encoding. An example of copying a news subject:   
CMTStr::Copy(news.subject,L"Asia stocks, euro hit as ECB takes hard line on Greek debt");  
category | wchar_t | The category in UTF-16, to which the news belongs. The tree structure of the news categories is created automatically on the client terminal side. A separator character '\' is used for dividing categories into subcategories. An example of news category:   
CMTStr::Copy(news.category,L"Markets\\\ Asian Markets News");  
flags | UINT | News flags. Specified using the EnNewsFlags enumeration.  
body | wchar_t | News body. The memory for a news body is reserved and prepared by a programmer. HTML is supported in newsletter. To send an HTML newsletter, start its body with the <html> tag and end with the </html> tag.  
body_len | UINT | News size. Limited by a value of MAX_NEWS_BODY_LEN.For example, if FLAG_MIME is ysed and the MIME size of the news is 800*1024 bytes, then in body_len one should specify (800*1024)/sizeof(wchar_t) = 400*1024 symbols.  
languages_list | UINT | An array containing the list of languages. The language is used to filter news when receiving them in terminals (in the settings of the terminal one can select news in what languages should be received) and when sending them to different client [groups](../Configuration-Interfaces/Groups/IMTConGroup/NewsLangAdd.md). The language is specified in the LANGID format used in [MS Windows](https://msdn.microsoft.com/en-us/library/windows/desktop/dd318693) systems (a value from Prim.lang.identifier).  
datetime | INT64 | The date/time of the news release in the number of seconds since January 01, 1970. This date is displayed in the "Time" filed of a newsletter in client terminals. The date/time value should be specified in the time zone of the trade server. Time zone parameters are passed to a data feed in a command line when the application is run. Command line parameter: /timezone:<time zone in minutes>, /timecorrect (if the parameter is set, daylight saving time correction should be taken into account).  
reserved | UINT | A reserved field for future use.
