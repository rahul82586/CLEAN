[🏠 Document Start](../README.md) / [Structures](README.md) / MTEconomicEvent

[Previous](MTNews.md) | [Next](MTReportInfo.md)

<a id="mteconomicevent"></a>
# MTEconomicEvent (#mteconomicevent)

The structure of the event (news) of an economic calendar is described in MTEconomicEvent. The structure is defined with the one-byte alignment.
    
    
    #pragma pack(push,1)
    struct MTEconomicEvent
      {
       //--- Flags
       enum EnEconomicEventPriority
         {
          PRIORITY_LOW =0,                                       // Low priority of an event
          PRIORITY_NORMAL =1,                                    // Normal priority of an event
          PRIORITY_HIGH =2                                       // High priority of an event
         };
       INT64             eventtime;                              // Date and time of an event
       wchar_t           name[128];                              // Event name
       wchar_t           currency[32];                           // Event currency
       UINT              priority;                               // Event priority
       wchar_t           period[128];                            // Event frequency
       wchar_t           val_previous[32];                       // Previous value
       wchar_t           val_forecast[32];                       // Predicted value
       wchar_t           val_actual[32];                         // Current value
       UINT              reserved[64];                           // Reserved field
      };
    #pragma pack(pop)

This structure is used in the [IMTGatewayAPI::SendEconomicEvents](../Gateway-API/Main-Interface/Quote-and-News-Feeds/SendEconomicEvents.md) method.

<a id="enumerations"></a>
## Enumerations (#enumerations)

The structure contains one enumeration:

<a id="eneconomiceventpriority"></a>
### EnEconomicEventPriority (#eneconomiceventpriority)

Flags of events of the economic calendar are listed in EnEconomicEventPriority:

ID | Value | Description  
PRIORITY_LOW | 0 | Low priority of an event. The event priority is shown with icons in terminals.  
PRIORITY_NORMAL | 1 | Normal priority of an event.  
PRIORITY_HIGH | 2 | High priority of an event.  
  
<a id="parameters"></a>
## Parameters (#parameters)

The MTEconomicEvent structure contains the following parameters:

Field | Type | Description  
eventtime | INT64 | Date and time of an event in seconds that have elapsed since 01.01.1970.  
name | wchar_t | Event name.  
currency | wchar_t | The currency of the country/region of the economic event;  
priority | UINT | Event priority. Transfered using the MTEconomicEvent::EnEconomicEventPriority enumeration.  
period | wchar_t | Period, for which the economic indicator is released, or its release date.  
val_previous | wchar_t | Previous value of the indicator. To specify an empty value an empty string is specified.  
val_forecast | wchar_t | Predicted value of the indicator. To specify an empty value an empty string is specified.  
val_actual | wchar_t | Current value of the indicator. To specify an empty value an empty string is specified.  
reserved | UINT | A reserved field for future use.
