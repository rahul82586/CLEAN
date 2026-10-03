[🏠 Document Start](../README.md) / [Dealing and Risk Management](README.md) / Exposure

[Previous](Summary-Positions-and-Coverage.md) | [Next](../Managing-Trade-Server-Settings/README.md)

<a id="exposure"></a>
# Exposure (#exposure)

The Exposure tab contains the assets of clients and the covered assets of a company grouped by currencies. The information about the covered assets is displayed from a special coverage account.

> Coverage accounts are those created in groups whose names start with "coverage". For example, coverage\forex. This tab displays summary exposure for all coverage accounts of a trade server. A more detailed description about coverage is provided in the ["Summary positions" (#coverage)](Summary-Positions-and-Coverage.md#coverage).

![Exposure](images/toolbox_exposure.png)

The following information is available about assets:

  * Asset — name of an asset.
  * Clients — volume of clients' positions by a selected asset (in units).
  * Coverage — volume of the positions on the coverage account by a selected asset (in units).
  * Net Total — difference between the clients' positions and the covered positions.
  * Rate — rate of converting the net total to a selected currency.
  * Net Total (Currency) — net total displayed in a selected currency. One can select a currency using the corresponding command of the context menu.
  * Positive (Currency) — positive net total displayed in a selected currency.
  * Graph — graphical ratio of clients' and covered assets as well as their net total are displayed here.



The lower part contains the Total line, which displays the summary rates by all assets. Client and covered assets are displayed on the right side as a diagram. Click on it to switch between short/long position data. The diagram can also be changed via the context menu.

<a id="context"></a>
## Context menu (#context)

The following commands can be run from the context menu of this tab:

  * Currency — open the submenu of selecting a currency the net total and the positive net total will be displayed in. Any currency used as the deposit currency of a group of accounts at the server is available for selection.
  * Graph — open the submenu for managing the diagram by assets:


  * Long Positions — display the diagram by buy positions.
  * Short Positions — display the diagram by sell positions.
  * Clients — display the diagram by the clients' assets.
  * Coverage — display the diagram by the covered assets.
  * Net Total — display the diagram of the difference between clients' and covered positions.
  * Hide — hide the diagram.
  * ![Copy](images/copy_icon.png) Copy — copy a selected line to the clipboard.
  * Report — generate a report on assets in the XML or HTML format.
  * ![Save](images/save_icon.png) Save — save the information about assets as an HTML file.
  * Reset Sort Order — restore the default sorting order.
  * Auto Arrange — if enabled, the size of columns is selected automatically.
  * Grid — show/hide the grid to separate the table fields.


