[🏠 Document Start](../README.md) / [Report API](README.md) / Configuration of Reports

[Previous](Interaction-with-Servers.md) | [Next](Request-for-Reports.md)

# Report Configuration

In order for the server to start using the reports module, add its configuration via the Administrator terminal:

![Reports section](images/admin_report_list.png)

To add or change the configuration of the module, click ![Add](images/add_button.png) Add or ![Edit](images/edit_button.png) Edit on the toolbar or in the context menu.

![Editing the report settings](images/report_edit.png)

Fill in the following fields in this window:

  * Enable — enable/disable the report. The module starts operating immediately after the option is enabled and the configuration is saved. To get started, server restart is not required.
  * Name — name of the report configuration. The same name is indicated in the report list of the Manager terminal.
  * Type — all reports available on the server are displayed here. The list is compiled based on the DLL report files which are located under the /report directory of the main trading server.
  * Trade server — to the right of the Name field, select a trade server the report is configured for. The report will be generated using the data on the specified server; and it will be available only when a manager connects to the specified server.



  * Each configuration of the report is bound to a specific server and thus generates reports concerning this server only.


  * Reports are generated for a manager in accordance with his or her access permissions. Reports are generated only for available groups of accounts.

  
---  
  
## Parameters

At the bottom of the window, there is a control block for managing the external parameters of reports. These parameters are provided for when writing modules and allow you to manage them from outside.

The following commands are available for managing the parameters:

  * Add — add a new parameter. After clicking, a new line will appear in the window. In the Parameter field, specify the name of the parameter, and in Value, assign a value to this parameter. String type parameters are created by default. To select another type (integer or fractional) click the arrow on the "Add" button.
  * Edit — change the selected parameter. The same operation can be done by a double-click on the required field.
  * Delete — delete the selected parameter.


