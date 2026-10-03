[🏠 Document Start](../../../../README.md) / [MetaTrader 5 Trading Platform](../../../../MetaTrader-5-Trading-Platform.md) / [MetaTrader 5 Administrator](../../../MetaTrader-5-Administrator.md) / [User Interface](../../User-Interface.md) / [Toolbar](../Toolbar.md) / Standard

[Previous](../Toolbar.md) | [Next](Search.md)

# Standard

The standard part of the toolbar is a set of commands for managing servers and the terminal. The set of commands that is displayed at the toolbar is [adjustable](Setup.md).

| Command | Description  
![Connect](images/toolbar_connect_button.png) | Connect | [Connect to a server](../../Getting-Started/Connect-to-Server.md).  
![Disconnect](images/toolbar_disconnect_button.png) | Disconnect | Disconnect from the server.  
![Update](images/toolbar_refresh_button.png) | Update | Request configuration changes from the server. If another administrator edited the server configuration during your session, administration inconsistencies may occur. To avoid such situations, it is recommended to run this command from time to time. The command is executed automatically upon login.  
![Restart](images/toolbar_restart_button.png) | Restart Server | [Restart](../../../Platform-Setup/Network-cluster/Restarting-and-Stopping-Servers.md) the selected server.  
![Apply](images/toolbar_apply_button.png) | Apply | Apply the new settings after changes. For example, when editing parameters in the Time tab, you should click this button for the changes to take effect.  
![Add](images/toolbar_add_button.png) | Add | Add an instruction. Depending on the selected section in the server tree, the command executes different commands. For example, it adds a holiday in the Holidays section or a new financial symbol in the Symbols section. The command applies to all sections except Time, Orders, Deals, Positions, Ticks and Update.  
![Edit](images/toolbar_edit_button.png) | Edit | Edit an existing instruction. To edit the settings, select an element in the right part of the terminal window in the relevant section. The command applies to all sections except Ticks and Update.  
![Delete](images/toolbar_delete_button.png) | Delete | Delete an existing instruction. To delete an instruction, select an element in the right part of the terminal window in the relevant section. The command applies to all sections except Time, Ticks and Update.  
![Sort Alphabetically](images/toolbar_sort_button.png) | Sort Alphabetically | [Sort (#sort)](../../../Platform-Setup/Symbols.md#sort) configurations alphabetically. Please note that sorting is done on the server, not in the local terminal.  
![Move Up](images/toolbar_up_button.png) | Move Up | Move an instruction up relative to others. Use this command to manage the priority in lists of access settings and data feeds. For example, if a data feed is higher than others, then the server will receive all information from this data feed. The server will switch to others only if the first one fails. In the Symbols tab, this command can be used to change the default arrangement of symbols in the Market Watch window in client terminals. In addition, using this button, you can move the added servers and their components in the Network tab.  
![Move Down](images/toolbar_down_button.png) | Move Down | Move an instruction down relative to others. The command is similar to the previous one.  
![Enable](images/toolbar_enable_button.png) | Enable | Enable the selected configuration.  
![Disable](images/toolbar_disable_button.png) | Disable | Disable the selected configuration.  
![Export](images/toolbar_export_button.png) | Export | [Export](../../../Platform-Setup/General-Information/ImportExport-Settings.md) platform settings to a JSON file. To export settings of only the selected section, for example, managers, select this section in the tree and execute the command.  
![Import](images/toolbar_import_button.png) | Import | [Import](../../../Platform-Setup/General-Information/ImportExport-Settings.md) platform settings from a JSON file.  
![Toolbox](images/toolbar_toolbox_button.png) | Toolbox | Show/hide the [Instruments](../Toolbox.md) window.  
![Help](images/toolbar_help_button.png) | Help | Use the context help of the Administrator terminal. When you select this command, a question mark will appear at the end of the cursor. Click on any interface element to view the relevant reference help.
