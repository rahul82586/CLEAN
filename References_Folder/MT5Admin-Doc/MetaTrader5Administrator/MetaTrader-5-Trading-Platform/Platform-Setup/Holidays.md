[🏠 Document Start](../../README.md) / [MetaTrader 5 Trading Platform](../../MetaTrader-5-Trading-Platform.md) / [Platform Setup](../Platform-Setup.md) / Holidays

[Previous](Time.md) | [Next](Leverages.md)

<a id="holidays"></a>
# Holidays (#holidays)

In this section you can add holidays to the working time schedule both for symbol groups and separate symbols. During holidays clients can connect, watch charts and trading history, but cannot conduct trade operations.

  * [Data feeds](Data-Feeds.md) that receive quotes only are automatically disabled on holidays. As soon as a holiday is over, the data feeds are automatically enabled. Data feeds that receive news keep working.


  * Holiday settings do not affect [swap calculation](Symbols/Symbol-Settings/Swaps.md).

  
---  
  
Holidays are represented like this:

![Holidays](images/holidays.png)

In order to add or edit a holiday, press "![Add](images/add_button_10.png) Add" or "![Edit](images/edit_button_11.png) Edit", respectively. These buttons are located in the [Edit](../MetaTrader-5-Administrator/User-Interface/Main-Menu/Edit.md) menu, on the [Standard](../MetaTrader-5-Administrator/User-Interface/Toolbar/Standard.md) toolbar and in the [context menu (#context)](Holidays.md#context). The window of holiday settings will be opened as soon as you press them.

> Additional general information about working with configuration records is given in the ["Working with Instructions"](General-Information/Working-with-Instructions.md) section.

<a id="common"></a>
## Common (#common)

![Common](images/holidays_common.png)

The following parameters are set up here:

  * Enable â enable/disable a holiday;
  * Every year â enable holiday repeating every year. For such holidays "****" is shown instead of the year;
  * Date â date of the holiday. A date is selected via a calendar that is opened upon pressing ![Calendar](images/calendar_button_2.png). The date can also be entered manually;
  * Work time â server work time on the holiday. If there is no working time on this day, leave zero values in these fields;
  * Description â text description of the holiday.



> The delivery of quotes and trading continue until the last minute of the working time range inclusive. For example, if the specified range is from 00:00 to 18:00, then the actual working time is 00:00:00  18:00:59.

<a id="symbols"></a>
## Symbol (#symbols)

![Symbols](images/holidays_symbols.png)

here you should specify symbols or groups of symbols, for which this holiday will be effective:

  * Add â add symbols. As soon as you press this button, a new field will appear in this window. Click on this field and select a symbol or group from the appeared list of symbols available on the server. To specify all symbols, select the "Symbols" point. Read more details in ["Specifying Symbols"](General-Information/Specifying-Symbols-and-Groups.md);
  * Delete â delete a selected symbol or group of symbols;
  * Edit â edit a selected symbol or group of symbols.



To complete creation or editing of a holiday press "OK". If you press "Cancel", the window will be closed, while changes will not be saved.

In order to delete a holiday, select it and press "![Delete](images/delete_button_11.png) Delete" in the [Edit (#delete)](../MetaTrader-5-Administrator/User-Interface/Main-Menu/Edit.md#delete) menu, on the [Standard](../MetaTrader-5-Administrator/User-Interface/Toolbar/Standard.md) toolbar or in the context menu.

<a id="holidays-check"></a>
## Holidays Check (#holidays-check)

Holiday rules are checked from top downward. If any rule allows trading for a symbol in the specified interval, all further rules will be ignored for this symbol-interval binding. Thus:

  * It is not possible to override an allowing rule by subsequent prohibiting rules.
  * It is possible to override a prohibiting rule by subsequent allow rules.



![Example of Holidays setup](images/holidays_example.png)

Let's consider example:

  * The first rule prohibits trading for all symbols on January 1, 2014
  * The second rule allows trading for Forex group symbols from 10:00 to 12:00 on that day
  * The third rule allows trading for the same symbols from 13:00 to 22:00
  * The fourth rule prohibits trading for all symbols on January 1, 2014.



As a result, on January 1, 2014, trading will be allowed for Forex group symbols from 10:00 to 12:00 and from 13:00 to 22:00. The fourth rule is ignored for the earlier allowed intervals as the check for these intervals stopped after the rules allowing trading for them.

Thus, in order to set several trading intervals inside one time interval, you should first set a prohibitive rule followed by permissive ones.

<a id="context"></a>
## Context Menu (#context)

The context menu of Holidays contains the following commands:

  * ![Add](images/add_button_11.png) Add â add a new holiday;
  * ![Edit](images/edit_button_12.png) Edit â edit a selected holiday;
  * ![Delete](images/delete_button_12.png) Delete â delete a selected holiday;
  * ![Move Up](images/move_up_button_4.png) Move Up â move the selected holiday up relative to others;
  * ![Move Down](images/move_down_button_4.png) Move Down â move the selected holiday down relative to others;
  * ![Sort Alphabetically](images/sort_symbols_icon_3.png) Sort Alphabetically â sort configurations alphabetically. Please note that sorting is done on the server, not in the local terminal.
  * ![Export](images/export_button_6.png) Export to File â [export](General-Information/ImportExport-Settings.md) holidays settings to a file.
  * ![Import](images/import_button_5.png) Import from File â [import (#import)](General-Information/ImportExport-Settings.md#import) holidays settings to a file.
  * ![Journal](images/journal_icon_5.png) Journal â request [logs](Network-cluster/Journal.md) according to the selected configuration. This will open the trade server logs section, with the name of the selected configuration automatically specified in the query field. You will only need to press the request button.
  * ![Find](images/find_button_7.png) Find â open the [search](../MetaTrader-5-Administrator/User-Interface/Search.md) window;
  * Auto Arrange â if this option is enabled the size of columns is selected automatically;
  * Grid â this option shows/hides field separators in the table.


