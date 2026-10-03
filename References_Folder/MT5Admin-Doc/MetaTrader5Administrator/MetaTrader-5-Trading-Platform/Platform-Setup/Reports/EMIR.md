[🏠 Document Start](../../../README.md) / [MetaTrader 5 Trading Platform](../../../MetaTrader-5-Trading-Platform.md) / [Platform Setup](../../Platform-Setup.md) / [Reports](../Reports.md) / EMIR

[Previous](NFA.md) | [Next](Fund-Overview.md)

<a id="emir-report"></a>
# EMIR Report (#emir-report)

EMIR (European Market Infrastructure Regulation) is a regulation by European Parliament and Council of the European Union, which sets unified requirements for over-the-counter derivatives trading, aims at reducing related risks and trade reporting. EMIR came into force on August 16, 2012. For more details please visit the [ESMA website](https://www.esma.europa.eu/policy-rules/post-trading/trade-reporting).

One of the EMIR requirements concerns reporting derivative trades to licensed trade repositories. The standard "EMIR Reports" report is available in the platform package to assist brokers in meeting this requirement. It enables the automatic generation of reports in the appropriate format and sending them to the repository's FTP server.

Among all the repositories to which the reports can be sent, the largest and the most popular one is [CME Group](https://www.cmegroup.com/trading/global-repository-services/cme-european-trade-repository.html). MetaTrader 5 EMIR Reports are designed specifically for operations with this repository. The report specification is available at the [CME Group (#etr)](https://www.cmegroup.com/trading/global-repository-services/technical-documentation.html#etr) website.

<a id="a-book-and-b-book-trades-in-the-report"></a>
## A Book and B Book trades in the report (#a-book-and-b-book-trades-in-the-report)

The main difference in the trades presentation in the report concerns the number of rows corresponding to each of them. B Book deals which are processed directly in the MetaTrader 5 platform and not sent to external trading systems, are reflected in a single report table row. A Book deals are shown in two rows: one of them reflects the internal part of the deal between the trader and the broker (intermediary party) and the second row shows the external part between the broker and the external system (exchange). In other words, B Book trades have only the internal part, while an A Book trade consists of an internal and an external part.

![A Book and B Book Trades](images/emir-deals.png)

In addition, some of the report fields are filled in different ways, depending on the deal part:

Field | The B Book trade or the internal part of the A Book trade | External part of the A Book trade  
NonReportingPartyIDType | Value "LEI", if the broker's client who has performed the trade is [marked (#client-type)](../Clients.md#client-type) as "Corporate" or "Fund". Value "CLC" for all other client types. | Value "LEI".  
NonReportingPartyLEI | If "LEI" is specified in the NonReportingPartyIDType field, the value of "LEI number for EMIR reports" from the [client record (#company)](../Clients.md#company) will be used. If "CLC" is specified in "NonReportingPartyIDType", the value is determined as follows (in order of priority):

  * External client ID from [trading account settings (#trade-accounts)](../Accounts/Editing-Account.md#trade-accounts).
  * Internal client ID, which is equal to the [client record](../Clients.md) ID in MetaTrader 5.
  * Trading account ID, i.e. [account](../Accounts/Editing-Account.md) login/number.

| LEI of the liquidity provider in accordance with the [gateway settings (#gateway)](EMIR.md#gateway).  
NonReportingPartyCountry | The value is determined as follows:

  * For legal entities — from the "Registration country" field of the [client record (#company)](../Clients.md#company).
  * For individuals — from the "Country" field of the [client record (#address)](../Clients.md#address).

| The "EMIR Report Country" parameter value from the [gateway settings (#gateway)](EMIR.md#gateway).  
UTI | Consists of three parts: [E02][LEI][Transaction ID]:

  * E02 — the first part always consists of these three characters.
  * LEI — broker's LEI from the "Broker LEI" parameter in the [plugin settings (#install-plugin)](EMIR.md#install-plugin).
  * Transaction ID — [deal ticket (#view)](../Deals.md#view) in MetaTrader 5.

| Consists of three parts: [E02][LEI][Transaction ID]:

  * E02 — the first part always consists of these three characters.
  * LEI — liquidity provider's LEI from the [gateway settings (#gateway)](EMIR.md#gateway).
  * Transaction ID — [deal ID in the external system (#view)](../Deals.md#view).

  
ExecutionVenue | Value "XXXX". | The "EMIR Report MIC" parameter value from the [gateway settings (#gateway)](EMIR.md#gateway).  
  
The detailed description of the report contents is provided in the "[Reported data (#data)](EMIR.md#data)" section below.

<a id="install-plugin"></a>
## Plugin Installation and Features (#install-plugin)

The report is implemented as the EMIR.Reports64.dll file combining two report modules and the server plugin:

  * The plugin collects data required for report sending via FTP, and saves this data in the trade server directory.
  * [Reports (#install-report)](EMIR.md#install-report) enable the convenient view of information in the created files and the manual generation of relevant reports.



The EMIR.Reports64.dll file is included into the standard platform package and is located under the Reports directory of the MetaTrader 5 trading server.

The plugin generates the reports daily, based on previous-day data. Report creation time is set in the [plugin settings (#install-plugin)](EMIR.md#install-plugin). Along with generation, the plugin can automatically send reports to the regulator's SFTP server, and thus you do not have to submit them manually. Report sending time and address are also specified in the settings.

The generated files are saved in the directory of the server for which the plugin is installed: [trading server installation directory]\Reports\EMIR.Reports\CME\Outbox. Once a file is sent to the SFTP server, it is moved from the "Outbox" folder to "Sent", located under the same directory.

To install the report, navigate to the [Plugins](../Plugins.md) section in MetaTrader 5 Administrator. After the server with the installed plugin has been selected, click ![Add](images/add_button.png)Add.

![Configuring the Plugin](images/emir_plugin_config.png)

The following parameters are available here:

  * Report Time — report generation time in the format of HH:MM:SS. This is the MetaTrader 5 trading platform site.
  * Symbol — sort by symbols. A comma separated list of symbols. The mask "*" and the negation sign "!" can be used here. For example, the value "EURUSD,GBPUSD" means that the plugin will collect information related to deals for EURUSD and GBPUSD symbols. The value "*" is for all symbols. *,!CFD\* value is for all symbols except those in the CFD group.
  * Groups — sort by groups. A comma separated list of groups. The mask "*" and the negation sign "!" can be used here. For example, the value "demoforex,democfd" means that the plugin will collect the transaction details for users in demoforex and democfd groups. The value "*" is for all groups. The default value is "*,!demo*,!contest*" which means all groups except those whose names start with demo and contest.
  * Send Time — time when the report will be send to the regulator's FTP server, HH:MM:SS. This is the MetaTrader 5 trading platform site.
  * CME firm's SFTP account ID — broker's ID in the Secured FTP server of the repository, to which [reports will be uploaded (#send)](EMIR.md#send). If the reports are to be sent manually, this field can be left blank.
  * SFTP Host — address for connecting to Secured FTP server. If the reports are to be sent manually, this field can be left blank.
  * SFTP Port — port for connecting to Secured FTP server. If the reports are to be sent manually, this field can be left blank.
  * SFTP Login — login for connecting to Secured FTP server. If the reports are to be sent manually, this field can be left blank.
  * SFTP Password — password for connecting to Secured FTP server. If the reports are to be sent manually, this field can be left blank.
  * SFTP Private Key Path — path to the [private key (#send)](EMIR.md#send) for authorization on the Secured FTP server. If the reports are to be sent manually, this field can be left blank.
  * Broker LEI — broker's Legal Entity Identifier (LEI), consists of a 20-digit alphanumeric code. The value is used in various fields of the report.
  * 1.6 CorporateSector — the sector in which the company operates. For example, F — an investment company, C — a credit company, etc. The value is directly substituted in the appropriate report field. The default value is F.
  * 1.7 FinancialOrNonFinancialCounterParty — type of the reporting company. For example, F — financial counterparty, N — non-financial counterparty, etc. The value is directly substituted in the appropriate report field. The default value is F.
  * 1.9 ReportingEntityLEI — Legal Entity Identifier (LEI) of the reporting entity. The value is directly substituted in the appropriate report field.
  * 2.1 ContractType CD — symbol path mask, according to which it will be assigned to type "CD" (Financial contracts for difference). It is used to fill the "2.1 ContractType" field in the report. For example, if *\cfd\* is specified in the parameter, then the "CD" value will be set in the "2.1 ContractType" field for all symbols, having \cfd\ in their path. For example, you can use this mask if contracts for difference in your platform are created in the CFD\, CME\CFD\, Real\CFD\Main\ and similar sections.
  * 2.1 ContractType FU — the same for the "FU" type (Futures).
  * 2.1 ContractType FW — the same for the "FW" type (Forwards).
  * 2.1 ContractType OP — the same for the "OP" type (Option).
  * 2.1 ContractType SB — the same for the "SB" type (Spreadbet).
  * 2.1 ContractType SW — the same for the "SW" type (Swap).
  * 2.1 ContractType ST — the same for the "ST" type (Swaption).
  * 2.1 ContractType OT — the same for the "OT" (Other).
  * 2.2 AssetClass CO — symbol path mask, according to which it will be assigned to "CO" assets class (Commodity and emission allowances). It is used to fill the "2.2 AssetClass" field in the report. For example, if *\commodity\* is specified in the parameter, then the "CO" value will be set in the "2.2 AssetClass" field for all symbols, having \commodity\ in their path. For example, you can use this mask if contracts for difference in your platform are created in the Commodity\, CME\Commodity\, Real\Commodity\Main\ and similar sections.
  * 2.2 AssetClass CR — the same for the "CR" class (Credit).
  * 2.2 AssetClass CU — the same for the "CU" class (Currency).
  * 2.2 AssetClass EQ — the same for the "EQ" class (Equity).
  * 2.2 AssetClass IR — the same for the "IR" class (Interest Rate).
  * 2.38 Intragroup — determines whether both counterparts of the deal belong to the same company. One of the two values : Y — belong to one company, N — do not belong. The value is directly substituted in the appropriate report field. The default value is N.
  * Mail Login List — the list of [manager logins](../Managers.md), to which [report generation errors (#errors)](EMIR.md#errors) will be emailed.
  * Stop On Error — report generation mode in case [data is not enough (#errors)](EMIR.md#errors). If "Yes" (default), the report will not be generated if at least one of the fields has no data. If "No", the report will be generated even of there is missing data. The report fields having no data will be left empty. Additionally, the list of relevant errors will be added to the "Comment" field of each unfilled row.



  * Data from the plugin parameters is extracted at the report generation time and is not stored in deal details. If you change plugin parameters after the execution of the relevant deals but prior to report generation, then the new parameter values as of the report generation time will be used for the report.
  * For the detailed description of all report fields please visit the [ESMA](https://www.esma.europa.eu/policy-rules/post-trading/trade-reporting) site.

  
---  
  
<a id="errors"></a>
## Handling Report Generation Errors (#errors)

The report generation is based on data from different settings and databases of the platform, including trading accounts, client records and gateway settings. If any of the data is missing, the generation report will be interrupted by default, i.e. the report file will not be generated and will not be sent to the SFTP server. This prevents the sending of incorrect data to the trading repository.

There is the possibility to disable report generation interruption in case of missing data. To do this, set "No" in [Stop On Error (#stop-error)](EMIR.md#stop-error). In this case, the report generation will not be interrupted, but some of the report fields will be left blank. For example, if only client LEI is not available for a transaction, the transaction row in the report will have one field empty, while all other fields will be filled. In this case you can add the missing data manually and send the report to the repository.

<a id="errors"></a>
### Errors (#errors)

All missing data errors are recorded to the [trade server journal](../Network-cluster/Journal.md). To request relevant logs, use the "EMIR Reporter" and "EMIR CME Manual" keywords. Error reports are additionally [sent via the internal email system (#notifications)](EMIR.md#notifications).

Data on encountered issues is also reflected in the reports. A brief description of errors which occurred when filling the fields is displayed in the Comment fields of appropriate report rows.

For [EMIR CME Manual (#install-report)](EMIR.md#install-report) report, summary information is additionally shown in the last row. This includes the total number of rows in the report and the number of rows with missing data.

<a id="notifications"></a>
### Notifications (#notifications)

After each report generation attempt, the plugin sends a message with the attempt results to managers, via the internal email system. The list of logins to whom the emails will be sent is specified in the [Mail Login List (#mail)](EMIR.md#mail) parameter of the plugin.

The email subject is "EMIR report automated generation status". It contains the following details:

  * If the report has been generated without errors, the email will contain the following message: "successfully generated X rows for the report by specification "CME"", where X is the number of records in the created report, excluding the table header.
  * If the report has been created, but one or more fields could not be filled, the email will contain the following: "generated X rows for the report by specification "CME", Y rows have warnings (see trade server log by keyword EMIR for details)". X — the number of report records excluding the table header, Y — the number of records with warnings. The warnings are displayed in the "Comment" column of appropriate rows in the table.
  * If the report could not be created, the email will state: "failed to generate report (see trade server log by keyword EMIR for details)". In this case, you should request the [trade server journal](../Network-cluster/Journal.md) using the "EMIR" keyword.



After each attempt to [upload a report to the FTP server (#send)](EMIR.md#send), the plugin also sends notifications to managers from the "[Mail Login List (#mail)](EMIR.md#mail)" parameter. A separate email is generated for each sent file.

The email subject is "EMIR report uploading status". It contains the name of the file and its sending status:

  * When uploaded successfully, the message is "successfully uploaded".
  * If error occurs, one of the following statuses will be delivered depending on the error:


  * "internal error (see trade server log by keyword EMIR for details)" — the error could not be identified.
  * "failed to initialize SFTP connection (see trade server log by keyword EMIR for details)" — repository server connection error.
  * "failed to upload (see trade server log by keyword EMIR for details)" — file uploading error.



<a id="gateway"></a>
## Configure gateways for reporting A-book transactions (#gateway)

For operations sent to external trading systems through [gateways](../Gateways.md) (operations with an external counterparty), additional information is indicated in the EMIR report:

  * ReportingPartyLEI — LEI of the reporting company. It is always filled with the "ReportingEntityLEI" parameter value from the [plugin settings (#install-plugin)](EMIR.md#install-plugin).
  * BeneficiaryLEI — LEI of the company which acts as a beneficiary in the operation. It is always filled with the "ReportingEntityLEI" parameter value from the plugin settings.
  * NonReportingPartyLEI and NonReportingPartyCountry — LEI and country code of the counterparty.
  * ExecutionVenue — code of the execution venue (exchange) to which the gateway is connected.



Since the broker can work with different external systems, the values for these two parameters should be specified in the settings of the gateway via which the deals are forwarded.

Open the [gateway settings (#parameters)](../Gateways/Configuration-of.md#parameters) and add the following parameters:

  * EMIR Report LEI — LEI of the liquidity provider to which the gateway is connected. Used to fill the NonReportingPartyLEI report field.
  * EMIR Report Country — code of liquidity provider's registration country. It is used in accordance with the [ISO 3166](https://www.iso.org/iso-3166-country-codes.html) standard. Used to fill the NonReportingPartyCountry report field.
  * EMIR Report MIC — the code of the trading exchange to which the gateway is connected. It is indicated in accordance with the [ISO 10383 (#iso:std:iso:10383:ed-3:v1:en)](https://www.iso.org/obp/ui/fr/#iso:std:iso:10383:ed-3:v1:en) standard. Used to fill the ExecutionVenue report field. If the parameter is not specified, the "XXXX" value will be inserted into the report field.



![Gateway parameters setup](images/emir_gateway_parameters.png)

These parameters can be added to any gateway. They will only be used for the report and do not affect the gateway operation.

> Data from the gateway parameters is extracted at the report generation time and are not stored in deal details. If you change gateway parameters after the execution of the relevant deals but prior to report generation, then the new parameter values as of the report generation time will be used for the report.

<a id="install-report"></a>
## Report Installation (#install-report)

EMIR Report includes two report modules: EMIR CME Automated and EMIR CME Manual.

<a id="emir-cme-automated"></a>
### EMIR CME Automated (#emir-cme-automated)

This report allows viewing data from the file [generated by the plugin (#install-plugin)](EMIR.md#install-plugin). These include files from two directories

  * [trade server installation directory]\Reports\EMIR.Reports\CME\Outbox — the generated files which has not yet been sent
  * [trade server installation directory]\Reports\EMIR.Reports\CME\Sent — the files which were successfully sent to the repository



  * To start collecting information, the [plugin must be enabled (#install-plugin)](EMIR.md#install-plugin) in the appropriate trade server settings. If the plugin is not enabled, report data will not be updated and the report will provide data only for the plugin operation period.
  * When the EMIR CME Automated report is used in the Manager terminal, no requests are sent to the server database. The report only presents data from the files generated by the plugin.

  
---  
  
<a id="emir-cme-manual"></a>
### EMIR CME Manual (#emir-cme-manual)

This module enables manual report generation for any time frame. This feature can be useful if the automated report was not generated for any of the previous days, for some reason. Set the required time interval, request report generation from the Manager terminal, export the received data to file and upload it to the repository manually.

Unlike the Automated report, this mode does not access the generated files and does not depend on whether the [server plugin (#install-plugin)](EMIR.md#install-plugin) is installed or not. The data is requested directly from the server database.

<a id="installation"></a>
### Installation (#installation)

To install the reports, open the [Reports](../Reports.md) section of MetaTrader 5 Administrator. After selecting a server for report installation, ![Add](images/add_button_1.png)Add.

![Configuring the Report](images/emir_report_config.png)

Once the configuration is added, select the required report in the Type field. No additional parameters are used for EMIR CME Automatic.

The set of parameters for the EMIR CME Manual almost coincides with [plugin (#install-plugin)](EMIR.md#install-plugin) parameters. These values are used to fill the report.

  * Broker LEI — broker's Legal Entity Identifier (LEI), consists of a 20-digit alphanumeric code. The value is used in various fields of the report.
  * 1.6 CorporateSector — the sector in which the company operates. For example, F — an investment company, C — a credit company, etc. The value is directly substituted in the appropriate report field. The default value is F.
  * 1.7 FinancialOrNonFinancialCounterParty — type of the reporting company. For example, F — financial counterparty, N — non-financial counterparty, etc. The value is directly substituted in the appropriate report field. The default value is F.
  * 1.9 ReportingEntityLEI — Legal Entity Identifier (LEI) of the reporting entity. The value is directly substituted in the appropriate report field.
  * 2.1 ContractType CD — symbol path mask, according to which it will be assigned to type "CD" (Financial contracts for difference). It is used to fill the "2.1 ContractType" field in the report. For example, if *\cfd\* is specified in the parameter, then the "CD" value will be set in the "2.1 ContractType" field for all symbols, having \cfd\ in their path. For example, you can use this mask if contracts for difference in your platform are created in the CFD\, CME\CFD\, Real\CFD\Main\ and similar sections.
  * 2.1 ContractType FU — the same for the "FU" type (Futures).
  * 2.1 ContractType FW — the same for the "FW" type (Forwards).
  * 2.1 ContractType OP — the same for the "OP" type (Option).
  * 2.1 ContractType SB — the same for the "SB" type (Spreadbet).
  * 2.1 ContractType SW — the same for the "SW" type (Swap).
  * 2.1 ContractType ST — the same for the "ST" type (Swaption).
  * 2.1 ContractType OT — the same for the "OT" (Other).
  * 2.2 AssetClass CO — symbol path mask, according to which it will be assigned to "CO" assets class (Commodity and emission allowances). It is used to fill the "2.2 AssetClass" field in the report. For example, if *\commodity\* is specified in the parameter, then the "CO" value will be set in the "2.2 AssetClass" field for all symbols, having \commodity\ in their path. For example, you can use this mask if contracts for difference in your platform are created in the Commodity\, CME\Commodity\, Real\Commodity\Main\ and similar sections.
  * 2.2 AssetClass CR — the same for the "CR" class (Credit).
  * 2.2 AssetClass CU — the same for the "CU" class (Currency).
  * 2.2 AssetClass EQ — the same for the "EQ" class (Equity).
  * 2.2 AssetClass IR — the same for the "IR" class (Interest Rate).
  * 2.38 Intragroup — determines whether both counterparts of the deal belong to the same company. One of the two values : Y — belong to one company, N — do not belong. The value is directly substituted in the appropriate report field. The default value is N.



The Symbols and Groups parameters are not used here, since filtering by groups and symbols can be set when requesting a report from the Manager terminal.

<a id="viewing-the-reports"></a>
## Viewing the Reports (#viewing-the-reports)

To view the report request, use MetaTrader 5 Manager. Simply select the necessary report in the Server Reports section to retrieve data from the server.

For report operation details, please visit the appropriate section of MetaTrader 5 Manager documentation.

![Report viewing in MetaTrader 5 Manager](images/emir_manager_request.png)

> The [plugin (#install-plugin)](EMIR.md#install-plugin) access to server data is not restricted. To generate files, the plugin can use any available information on groups and symbols. In contrast, the EMIR CME Manual report has restricted access to data in accordance with the [manager account](../Managers.md) permissions and [settings of the group](../Groups/Group-Settings.md) to which this account belongs.

<a id="send"></a>
## Sending Reports to Repository (#send)

To send the reports to the repository, the corresponding files need to be uploaded to a special SFTP server. The EMIR Reports plugin is able to send reports to the server automatically. For this, you should specify report sending time and SFTP server connection details, in the [plugin settings (#install-plugin)](EMIR.md#install-plugin).

Contact an appropriate repository to get SFTP access (address, login and password). For example, server access specifications for the CME Group are available at <https://www.cmegroup.com/trading/global-repository-services/files/ftp-connectivity.pdf>.

The plugin create file reports to be sent, in the [trade server installation directory]\Reports\EMIR.Reports\CME\Outbox. If sending to repository is not activated in [plugin settings (#install-plugin)](EMIR.md#install-plugin) by the time of report generation (the "SFTP Host" field is empty), the files will be simply saved in this directory. Once you set the required settings, all the saved files will be uploaded to the repository at the next report sending time.

If sending to repository fails for any reason, its file is saved under [trade server installation directory]\Reports\EMIR.Reports\CME\Outbox. The next day the plugin will retry to send the file at the scheduled time.

<a id="data"></a>
## Report Data (#data)

Some fields in the report are always empty. Data for this fields may not be available in MetaTrader 5 or may be optional. Only the fields marked in the specification as "FX only" or "All" are implemented in the report. Fields "Commodities only", "Credit only" and "Rates only" are not available, because they are not applicable in MetaTrader 5.

For the detailed description of the reports please visit the [ESMA](https://www.esma.europa.eu/policy-rules/post-trading/trade-reporting) site. The general description is provided below for more convenience.

Field | Description | Value  
Comment | Description of errors that occurred during the formation of this row (or empty if there are no errors) | A list of errors or an empty value if there are no errors  
Action | The action type performed by the transaction | N — new operation  
Level | Indicates the object which the action refers to. | T — trade, P — position  
ReportingTimestamp | Report generation date and time | Report generation date and time  
ReportingPartyLEI  | LEI of the reporting company | The value of the "Broker LEI" parameter from the [plugin settings (#install-plugin)](EMIR.md#install-plugin). If the parameter is not filled, an error will be generated and the field will be left blank  
NonReportingPartyIDType | Code for the external counterparty ID type | For the rows describing the external transaction part the value "LEI" is always used. For the rows describing the transaction on the MetaTrader 5 side:

  * The value "LEI" if the broker client who performed the transaction is [marked (#client-type)](../Clients.md#client-type) as "Corporate" or "Fund"
  * Value "CLC" for all other client types

  
NonReportingPartyLEI | LEI of the second party of the transaction | For the rows describing the external deal part, liquidity provider's LEI in accordance with the [gateways settings (#gateway)](EMIR.md#gateway) is specified For the rows describing the transaction on the MetaTrader 5 side the value depends in the NonReportingPartyIDType field: If "LEI" is specified in the NonReportingPartyIDType field, the value of "LEI number for EMIR reports" from the [client record (#company)](../Clients.md#company) will be used. If "CLC" is specified in "NonReportingPartyIDType", the value is determined as follows (in order of priority):

  * External client ID from [trading account settings (#trade-accounts)](../Accounts/Editing-Account.md#trade-accounts).
  * Internal client ID, which is equal to the [client record](../Clients.md) ID in MetaTrader 5.
  * Trading account ID, i.e. [account](../Accounts/Editing-Account.md) login/number.

If LEI is specified in the NonReportingPartyIDType field, but the NonReportingPartyLEI field value cannot be determined, and error will be generated and the field will be left blank. If gateway configuration via which a transaction was executed is not found for an external deal (for example the configuration was deleted), an error will be generated and the field will be left blank.  
NonReportingPartyCountry | Country of the second party of the transaction | For the rows describing the external part of the transaction, the "EMIR Report Country" parameter value from the [gateway settings (#gateway)](EMIR.md#gateway) is specified. For the rows describing the transaction on the MetaTrader 5 side, the value is determined as follows:

  * For legal entities — from the "Registration country" field of the [client record (#company)](../Clients.md#company).
  * For individuals — from the "Country" field of the [client record (#address)](../Clients.md#address).

If the appropriate gateway or client record parameter is not filled, an error will be generated and the field will be left blank. If gateway configuration via which a transaction was executed is not found for an external deal (for example the configuration was deleted), an error will be generated and the field will be left blank.  
CorporateSector | The sector in which the company operates | The "1.6 CorporateSector" parameter value from the [plugin settings (#install-plugin)](EMIR.md#install-plugin). If the parameter is not filled, an error will be generated and the field will be left blank  
FinancialOrNonFinancialCounterParty | Type of reporting company | The "1.7 FinancialOrNonFinancialCounterParty" parameter value from [plugin settings (#install-plugin)](EMIR.md#install-plugin). If the parameter is not filled, an error will be generated and the field will be left blank  
ReportingBrokerLEI | Broker's LEI | Not filled  
ReportingAssetManagerLEI | Asset manager's LEI | Not filled  
ReprotingEntityLEI | LEI of the reporting broker, if the report is submitted via a third party | The "1.9 ReportingEntityLEI" parameter value from the [plugin settings (#install-plugin)](EMIR.md#install-plugin). If the parameter is not filled, an error will be generated and the field will be left blank  
ClearingMemberLEI | Clearing member's LEI | Not filled  
BeneficiaryIDType | Code for specifying the identifier of the beneficiary: LEI or CLC (client code) | "LEI" is always used  
BeneficiaryLEI | Transaction beneficiary's LEI | The value of the "Broker LEI" parameter from the [plugin settings (#install-plugin)](EMIR.md#install-plugin). If the parameter is not filled, an error will be generated and the field will be left blank  
TradingCapacity  | How the transaction was performed: personally (P) or via an agent (A) | The value "A" is always used  
CounteryPartySide | Indicates who the counterparty is: buyer (B) or seller (S) | The "B" value for buy deals and "S" for sell deals  
CommercialOrTreasuryLink | Determines whether the object is associated with the financial activity of the counterparty | Not filled  
ClearingThreshold | Determines whether the counterparty has exceeded the clearing threshold | Not filled  
MTM | The last price of the transaction asset at the trading session close time, multiplied by deal size | The last price as at the report generation time, which is equal to the "Report Time" from the [plugin settings (#install-plugin)](EMIR.md#install-plugin). If the last price is unavailable for any reason, the average price between ask and bid is used  
MTMCurrency | Currency in which the value of the "MTM" field is indicated | The quote currency of the transaction symbol  
ValuationDateTime | The date for which the value of the "MTM" field is indicated | Report generation date, which is equal to the "Report Time" from the [plugin settings (#install-plugin)](EMIR.md#install-plugin)  
ValuationMethod | "MTM" valuation method: Mark-to-market (M), Mark-to-model (O), CCP's valuation (C) | The value "M" is always used  
Collateralizaion | Determines whether a collateral agreement is concluded between the parties | Not filled  
CollateralPortfolio | Determines if the collateral is a portfolio | Not filled  
CollateralPortfolioCode | Portfolio code | Not filled  
ProductType | Financial product type | Filled in accordance with the deal [symbol type (#calculation)](../Symbols/Symbol-Settings/Trade.md#calculation):

  * Forex, Forex No Leverage — FXForward
  * Futures, Exchange Futures, Exchange FORTS Futures — FUT
  * CFD, CFD Index, CFD Leverage — CFD
  * Exchange Options, Exchange Margin Options — Option

  
ExchangeTraded | The exchange in which the product is traded | Not filled  
ContractType | Contract type | Filled in accordance with the plugin [2.1 ContractType* settings (#install-plugin)](EMIR.md#install-plugin). If no mask matches a symbol, or more than one mask match, an error will be generated and the field will be left blank  
AssetClass | Asset class | Filled in accordance with the plugin [2.2 AssetClass* settings (#install-plugin)](EMIR.md#install-plugin). If no mask matches a symbol, or more than one mask match, an error will be generated and the field will be left blank  
ProductClassificationType | Product classification type: CFI (C) or UPI (U) | The value "C" is always used  
ProductClassification | Product classification in accordance with the [ISO 10692](https://www.iso.org/standard/44799.html) standard (for CFI) | Filled using the "CFI" field from the relevant [financial instrument settings](../Symbols/Symbol-Settings/Common.md)  
ProductIdentificationType | Product identification type | Not filled  
ProductIdentification | Product ID | Not filled  
UnderlyingType | Underlying asset type | Not filled  
Underlying | Underlying asset identifier | Not filled  
NotionalCurrency1 | Base currency | Base currency of the transaction symbol  
NotionalCurrency2 | Quote currency | Quote currency of the transaction symbol  
SettlementCurrency | Settlement currency | Quote currency of the transaction symbol  
UTI | Unique Transaction Identifier | Consists of three parts: [E02][LEI][Transaction ID]:

  * E02 — the first part always consists of these three characters
  * LEI — for the deals forwarded to an external system it is the liquidity provider's LEI from the [gateway settings (#gateway)](EMIR.md#gateway). For B-book deals — broker's LEI from the "Broker LEI" parameter in [plugin settings (#install-plugin)](EMIR.md#install-plugin)
  * Deal ID — for A-book it is the [deal ID In the external system (#view)](../Deals.md#view), for B-book it is [deal ticket (#view)](../Deals.md#view) in MetaTrader 5

Deals related to one position have the same UTI. The above formula uses the ID of the deal which opened the position. Positions have the same UTI as the deals by which the positions were opened.  
ReportTrackingNumber | Report group identifier | Not filled  
ComplexTradeComponentID | Internal identifier for report grouping | Not filled  
ExecutionVenue | Execution venue code | For the rows describing the external part of the transaction, it is filled in accordance with the "EMIR Report MIC" parameter from [gateway settings (#gateway)](EMIR.md#gateway). If not specified, the "XXXX" value is used. For the rows describing the transaction on the MetaTrader 5 side "XXXX" is always used  
Compression | Determines whether the operation is the result of portfolio compression | The value "N" is always used (it is not)  
PriceOrRate | Derivative price minus fees and accumulate profit | Transaction price  
PriceNotation | Units in which the price is indicated | The value "U" (units) is always used  
PriceCurrency | Currency in which the price is indicated | Quote currency of the transaction  
NotionalAmount | Amount of product for which the price is specified | Volume of a deal  
PriceMultiplier | Contract size | Transaction contract size  
Quantity | The volume of operations in lots | The volume of operations in lots  
UprfontFee | Upfront payment amount | Not filled  
SettlementMethod | Settlement method: monetary (C), physical (P), optional (O), U (cash) | The value "U" is always used  
ExecutionDateTime | Contract execution date | Transaction date and time  
StartDate | Contract effective date | Transaction date and time  
MaturityDate | Contract maturity date | Not filled  
TerminationDate | Contract termination date | Not filled  
SettlementDate | Settlement date | Not filled  
MasterAgreementType | Link to the master agreement | Not filled  
MasterAgreementVersion | Year of the master agreement | Not filled  
ConfirmDateTime | Contract confirmation date | Transaction date and time  
ConfirmType | Contract confirmation type: non-electronic (Y), not-conformed (N), electronic (E) | The value "E" is always used  
ClearingObligation | Indicates the need of clearing for the operation | The value "N" is always used (no need)  
Cleared | Indicates if clearing was performed | The value "N" is always used (was not performed)  
ClearingDateTime | Clearing date | Not filled  
ClearingVenueLEI | Clearing organization LEI | Not filled  
Intragroup | Determines whether both counterparts of the deal belong to the same company | "2.38 Intragroup" parameter value from [plugin settings (#intragroup)](EMIR.md#intragroup)  
FinalSettleCcy | Final settlement currency | Quote currency of the transaction  
ExchangeRate | Price as on the date of the transaction | Transaction price  
ForwardExchangeRate | Forward price | Transaction price  
ExchangeRateBasis | Exchanged currencies | The symbol, for which the deal is executed  
OptionType | Type of option | Not filled  
OptionExerciseType | Option exercise type | Not filled  
OptionStrikePrice | The strike price of the option | Not filled  
StrikePriceNotation | Units in which the option strike price is indicated | Not filled  
UnderlyingMaturityDate | Option expiration date | Not filled
