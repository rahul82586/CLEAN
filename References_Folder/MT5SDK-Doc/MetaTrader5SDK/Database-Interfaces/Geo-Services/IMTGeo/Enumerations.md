[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Geo Services](../../Geo-Services.md) / [IMTGeo](../IMTGeo.md) / Enumerations

[Previous](../IMTGeo.md) | [Next](Release.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

The [IMTGeo](../IMTGeo.md) class contains the following enumerations:

  * [IMTGeo::EnGeoRequestFlags (#engeorequestflags)](Enumerations.md#engeorequestflags)
  * [IMTGeo::EnFlags (#engeorecorddetails)](Enumerations.md#engeorecorddetails)



<a id="engeorequestflags"></a>
## IMTGeo::EnGeoRequestFlags (#engeorequestflags)

IMTGeo::EnGeoRequestFlags lists types of data requested about the IP address.

ID | Value | Description  
GEO_REQUEST_FLAGS_CONTINENT | 0x00000001 | Continent.  
GEO_REQUEST_FLAGS_COUNTRY | 0x00000002 | Country.  
GEO_REQUEST_FLAGS_CITY | 0x00000004 | City.  
GEO_REQUEST_FLAGS_REGION | 0x00000008 | Region/State.  
GEO_REQUEST_FLAGS_PROVINCE | 0x00000010 | Province.  
GEO_REQUEST_FLAGS_ASN | 0x00000020 | [Autonomous system](https://ru.wikipedia.org/wiki/%D0%90%D0%B2%D1%82%D0%BE%D0%BD%D0%BE%D0%BC%D0%BD%D0%B0%D1%8F_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0_(%D0%98%D0%BD%D1%82%D0%B5%D1%80%D0%BD%D0%B5%D1%82)) number (ASN).  
GEO_REQUEST_FLAGS_ASNNAME | 0x00000040 | Name of the autonomous system.  
GEO_REQUEST_FLAGS_ISP | 0x00000080 | Internet service provider name.  
GEO_REQUEST_FLAGS_ORGANIZATION | 0x00000100 | The organization that owns an address.  
GEO_REQUEST_FLAGS_COORDINATES | 0x00000200 | Geographical coordinates.  
GEO_REQUEST_FLAGS_DETAILS | 0x00000400 | Additional details.  
GEO_REQUEST_FLAGS_NONE | 0x00000000 | No flags.  
GEO_REQUEST_FLAGS_ADDRESS |  | All geographic data of the address: GEO_REQUEST_FLAGS_COUNTRY|GEO_REQUEST_FLAGS_CITY|GEO_REQUEST_FLAGS_REGION|GEO_REQUEST_FLAGS_PROVINCE.  
GEO_REQUEST_FLAGS_ALL |  | All flags are set.  
  
The enumeration is used in the following methods:

  * [IMTServerAPI::GeoResolve*](../../../Server-API/Main-API-Interface/Geo-Services/GeoResolveAny.md)
  * IMTAdminAPI::GeoResolve*
  * IMTManagerAPI::GeoResolve*
  * IMTReportAPI::GeoResolve*



<a id="engeorecorddetails"></a>
## IMTGeo::EnGeoRecordDetails (#engeorecorddetails)

IMTGeo::EnGeoRecordDetails lists flags for transmitting additional information about an IP address.

ID | Value | Description  
GEO_DETAILS_PROXY_TOR | 0x00000001 | The address belongs to the [TOR](https://ru.wikipedia.org/wiki/Tor) network.  
GEO_DETAILS_PROXY_HTTP | 0x00000002 | The address is a proxy server.  
GEO_DETAILS_PROXY_VPN | 0x00000004 | The address is a VPN server.  
GEO_DETAILS_DATACENTER | 0x00000008 | The address belongs to a data center.  
GEO_DETAILS_ATTACK_MAIL | 0x00000010 | The address belongs to a spammer or was involved in an attack on mail systems.  
GEO_DETAILS_ATTACK_SSH | 0x00000020 | The address was involved in an attack on SSH servers or password brute-forcing.  
GEO_DETAILS_ATTACK_WEB | 0x00000040 | The address was involved in attacks on websites.  
GEO_DETAILS_ATTACK_APP | 0x00000080 | The address was involved in an attack on applications.  
GEO_DETAILS_BOT_BOTNET | 0x00000100 | The address belongs to a botnet.  
GEO_DETAILS_BOT_SEARCH_ENGINE | 0x00000200 | Search engine, social network or messenger bot.  
GEO_DETAILS_BLACKLIST | 0x00000400 | Blacklisted address  
GEO_DETAILS_WEBDRIVER | 0x00000800 | Browser connection in the headless mode, connection via [Selenium](https://www.selenium.dev/)/[Webdriver](https://www.selenium.dev/documentation/webdriver/).  
GEO_DETAILS_BOT_ANY | 0x00001000 | The address is a bot.  
GEO_DETAILS_BOT_FAKE | 0x00002000 | The address is a fake crawler.  
GEO_DETAILS_NONE | 0x00000000 | No flags.  
GEO_DETAILS_ALL |  | All flags are set.  
  
The enumeration is used in the [IMTGeo::Details](Details.md) method.
