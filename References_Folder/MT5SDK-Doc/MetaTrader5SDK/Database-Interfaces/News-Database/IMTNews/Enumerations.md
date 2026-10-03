[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [News Database](../../News-Database.md) / [IMTNews](../IMTNews.md) / Enumerations

[Previous](../IMTNews.md) | [Next](Release.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

The [IMTNews](../IMTNews.md) class contains the following enumerations:

<a id="ennewsflags"></a>
## IMTNews::EnNewsFlags (#ennewsflags)

Available news flags are enumerated in IMTNews::EnNewsFlags:

ID | Value | Description  
NEWS_FLAGS_NONE | 0x0000 | No flags.  
NEWS_FLAGS_PRIORITY | 0x0001 | Flag of a high-priority news item.  
NEWS_FLAGS_READ | 0x0002 | Flag of whether a news item is read or unread.  
NEWS_FLAGS_NOBODY | 0x0004 | Flag of a news item that does not have the body (only the header).  
NEWS_FLAGS_CALENDAR | 0x0008 | Flag of economic calendar news.  
NEWS_FLAGS_FIRST |  | Beginning of enumeration. It corresponds to NEWS_FLAGS_NONE.  
NEWS_FLAGS_ALL |  | End of enumeration. It corresponds to NEWS_FLAGS_CALENDAR.  
  
This enumeration is used in the [IMTNews::Flags](Flags.md) method.
