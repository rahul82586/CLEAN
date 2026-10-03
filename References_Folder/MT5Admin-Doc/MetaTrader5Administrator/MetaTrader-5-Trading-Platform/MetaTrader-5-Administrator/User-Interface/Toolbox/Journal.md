[🏠 Document Start](../../../../README.md) / [MetaTrader 5 Trading Platform](../../../../MetaTrader-5-Trading-Platform.md) / [MetaTrader 5 Administrator](../../../MetaTrader-5-Administrator.md) / [User Interface](../../User-Interface.md) / [Toolbox](../Toolbox.md) / Journal

[Previous](Search.md) | [Next](../../Terminal-Settings.md)

<a id="journal"></a>
# Journal (#journal)

The "Journal" tab contains information about the registered actions of the administrator terminal for the current session of connection to the server. The information about the terminal start and events that occur during its working is registered in the journal. Only the last messages are displayed in the window. In order to view the folder that contains all the log files it is necessary to execute the "![Open](images/open_data_folder_button.png) Open" command in the context menu.

![Journal](images/toolbox_journal.png)

The journal entries are marked with the corresponding icons depending on their types:

  * ![Information](images/journal_info_icon.png) — information message;
  * ![Warning](images/journal_warning_icon.png) — warning;
  * ![Error](images/journal_error_icon.png) — error message.



> Different types of errors returned by the server are described in the [separate section](../../../Platform-Components/Trade-Server/Return-Errors.md).

<a id="context"></a>
## Context Menu (#context)

Context menu of the "Journal" tab contains the following commands:

  * ![Open](images/open_data_folder_button_1.png) Open — open the folder that contains the text files of the journal entries;
  * ![Copy](images/copy_button.png) Copy — copy a selected entry of the journal to clipboard. You can copy the selected record using the "Ctrl+C" key combination;
  * Auto Arrange — if this option is enabled, the size of columns is selected automatically;
  * Grid — this option shows/hides grid to separate the fields of the journal entries table.


