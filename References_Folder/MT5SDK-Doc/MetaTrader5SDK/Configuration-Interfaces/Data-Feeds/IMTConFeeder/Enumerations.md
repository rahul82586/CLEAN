[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Data Feeds](../../Data-Feeds.md) / [IMTConFeeder](../IMTConFeeder.md) / Enumerations

[Previous](../IMTConFeeder.md) | [Next](Release.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

The [IMTConFeeder](../IMTConFeeder.md) class contains two enumerations.

<a id="enfeederflags"></a>
## IMTConFeeder::EnFeederFlags (#enfeederflags)

Flags of predefined data feed settings are listed in IMTConFeeder::EnFeederFlags.

ID | Value | Description  
FEED_FLAG_QUOTES | 0x0000001 | The data feed sends quotes.  
FEED_FLAG_NEWS | 0x0000002 | The data feed sends news.  
FEED_FLAG_REMOTE | 0x0000008 | The data feed is running on a remote computer.  
FEED_FLAG_TRIAL | 0x0000010 | The data feed is running in demo mode. The mode is checked based on the license at the time the module is loaded.  
FEED_FLAG_INTERNAL | 0x0000020 | The data feed is integrated into the platform. This is [MetaTrader 5 Feeder](https://support.metaquotes.net/ru/docs/mt5/platform/components/datafeeds/metatrader5feeder).  
FEED_FLAG_IMPORT_SYMBOLS | 0x0000040 | The data feed is allowed to import symbol settings.  
FEED_FLAG_NONE | 0 | Beginning of enumeration. It corresponds to the absence of flags  
FEED_FLAG_ALL |  | End of enumeration. It correspond to the presence of all flags.  
  
This enumeration is used in the following methods:

  * [IMTConFeeder::Flags](Flags.md)
  * [IMTConFeederModule::Modes](../IMTConFeederModule/Modes.md)



<a id="enfeedersmode"></a>
## IMTConFeeder::EnFeedersMode (#enfeedersmode)

Modes of data feed operation are listed in IMTConFeeder::EnFeedersMode.

ID | Value | Description  
FEEDER_DISBALED | 0 | The data feed is disabled.  
FEEDER_ENABLED | 1 | The data feed is enabled.  
FEEDER_FIRST |  | Beginning of enumeration. It corresponds to FEEDER_DISBALED.  
FEEDER_LAST |  | End of enumeration. It corresponds to FEEDER_ENABLED.  
  
This enumeration is used in the [IMTConFeeder::Mode](Mode.md) method.
