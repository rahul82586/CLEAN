[🏠 Document Start](../README.md) / [Clients and Trading Accounts](README.md) / Clients

[Previous](README.md) | [Next](Online-Accounts.md)

<a id="clients"></a>
# Clients (#clients)

The Client is a separate entity in the trading platform. This is the aggregate information on a trader, including personal data, documents and trading accounts. The client record stores the history of all changes: every version made by any manager is available in the Versions section.

All accounts registered in the platform are automatically connected to an existing or a new client. Thus, the client entity conveniently stores all accounts of a trader, even those opened in different groups or having different types. The new arrangement of data, registers all client performed actions before opening a real account, and allows evaluation of the client's real LTV (Life-Time Value).

All clients are displayed in a separate section:

![Client management section](images/clients.png)

The context menu contains commands for managing the Clients section:

  * Displayed data is managed by the Columns command
  * The [list of clients (#filter)](README.md#filter) can be managed using the Filters submenu
  * [Information to clients](Push-Notifications-SMS-and-Mail.md) can be sent using the "![Email...](images/mail_create_icon_1.png) Email..." command
  * Details on clients' operations can be retrieved from [the trade server journal](../Managing-Trade-Server-Settings/Trade-Server-Journal.md) using the "![Journal...](images/journal_icon_1.png) Journal..." command



If Autoscroll is enabled, the list of clients is scrolled to the last one whenever a new trading account is added to the list. The auto scroll can only be applied to a list sorted by the identifier (ID).

> The manager account needs to have appropriate permissions for accessing the Clients section. Such permissions are provided by the platform administrator.

<a id="create"></a>
## Creating clients automatically and manually (#create)

All accounts registered in the platform via client terminals are automatically linked to clients. If there is no client record for the newly created account, such a record is created automatically. All information from the account is copied to the client record. Minimum details are required for demo accounts: name, surname, company, email and phone number. More data can be requested during the registration of preliminary accounts via client terminals. Depending on platform settings, the following data may be requested:

  * Detailed personal data
  * ID and proof-of-address documents
  * Nationality and tax ID number
  * Social status, employment and education
  * Income and its sources
  * Trading experience in various financial markets



If you enable the extended account registration form, all the above data will be automatically added to client records. Thus, you will not need to additionally request this information and add it manually to the database.

![Information specified during account registration is automatically added to a client record](images/clients_info_copy.png)

To create a client manually, click "![New client](images/new_account_icon_1.png) New Client" in the context menu of the client list or press "Ctrl+Shift+N".

![Creating a client](images/clients_create.png)

Then specify required information in sections Personal data, Address and Regulation. Once you save the client record, document and trading account management sections will appear.

> When a [trading account is created](Creation-of-Accounts.md) via the Manager terminal, an appropriate client record is not created automatically. To create it manually based on account data, open the account dialog and click "New Client" in the lower left corner. To create an account linked to a client record, use the "Trading accounts" section in the appropriate client record.

<a id="binding"></a>
### Binding accounts to clients and copying data (#binding)

The trading platform automatically binds each trading account opened via the client terminal to a client record. Search is based on the comparison of trading account data with data in client records:

  * First, a client with the matching First Name, Last Name and E-Mail is searched (all the three should match, case insensitive).
  * If no such client is found, the system searches for a client with the matching First Name, Last Name and phone number (all the three fields should match, case insensitive).



If no suitable record is found, a new client is created and a trading account is bound to it. 

After that the account data are copied to the client record in accordance with priority. Demo accounts and client records created based on demo accounts have the lowest priority. The highest priority is given to data from real accounts and manually created clients.

  * Demo account — when binding such an account to an existing client record, which was created earlier on the basis of another demo account, only missing data is copied.
  * Preliminary account — when binding such an account to an existing client record, which was created earlier on the basis of a demo account, all data are copied (existing data are overwritten). If the client was created on the basis of a preliminary account, only missing data is copied. If the client was created on the basis of a real account or was added manually, data is not copied.
  * Real account — when binding such an account to an existing client record, which was created earlier on the basis of a preliminary or demo account, all data are copied (existing data are overwritten). If the client was created on the basis of a real account or was added manually, data is not copied.



If the account is linked to a newly created record, all account data are copied.

Data are also copied to clients after each time [the account is changed](README.md). In this case, the information is only copied to the empty fields of the client. For example, when the manager adds an address to account data. If the address is not filled for the client to whom the account is bound, the data will be copied.

<a id="access"></a>
## Differentiation of access to clients for managers (#access)

A client record is available to the manager if one of the following conditions is met:

  * The client is created by this manager
  * The client is explicitly assigned to the manager
  * The preferred trading group, set for the client is available to the manager (the manager has permissions for the group)
  * Any of the trading accounts bound to the client is available to the manager (the manager has permissions for the group in which the account is located)



<a id="general"></a>
## General client information (#general)

This section displays general information about the client, as well as the responsible employee by whom the client is managed.

![General client information](images/clients_general.png)

The following information is available:

  * Type — individual or corporate client. An additional tab "Company" is available for corporate clients, in which company details are specified.
  * Status sets the client status:
    * Not registered — an anonymous client, which was created based on a demo account without any data.
    * Registered — the client has created a demo account with filled contact details.
    * Not interested — the client has created a demo account with filled contact data but is not interested in opening a real account.
    * Not completed — the client has provided data for opening a real account.
    * Completed — the client has provided data for opening a real account and has submitted all the required documents.
    * Information — to open a real account, the client needs to provide additional information.
    * Rejected — the client is denied registration.
    * Approved — a real account has been opened for the client.
    * Funded — the client has deposited money to a real account.
    * Active — the client has trading activity.
    * Inactive — the client does not have trading activity.
    * Suspended — work with the client has been suspended.
    * Closed — the client has left at the client's own decision.
    * Terminated — work with the client was terminated at the initiative of the company.
  * KYC status — the result of a client check via the KYC service.
  * Assigned manager — the name of the responsible employee. To find all the clients managed by a certain employee, enable the "Assigned manager" column in the client list then sort the list by this column. The list of managers available for selection is formed in accordance with the settings of the manager who is viewing the client. If the current manager account is linked to a certain company on the trading server, the available list will only include managers from the same company. A manager without any company specified can access all managers on the server. If the required managers are not available to you in the list, please contact your trading platform administrator.
  * Preferred trading group — the field is used to distribute clients between manager accounts. If this field is empty, the client record will be available to managers regardless of their account group permissions. If the field is filled, the client will only be available to the managers having the specified group permissions.
  * Approved by — different employees can be responsible for creation and final approval of clients. For example, a manager can register a client, fill in necessary data and set the "Registered" status. Then a compliance specialist may verify the data, change the status to "Approved", set the approval date and specify his account in the "Approved by" field. 
  * Approval data — data and document verification and approval date. The date is set by the data approving specialist.
  * Close date — the date when the provision of services to the client was terminated.
  * Last contact date — by filling out this field, managers can easily identify which clients should be reminded of the latest promotions and whom to avoid bothering with too frequent emails/calls. Simply enable the display of this column in the list and then sort clients by this field.
  * Lead Source, Lead Campaign — the lead source website or the name of the marketing campaign (lead campaign) the client responded to.  
These fields are used for marketing campaigns and allow you to track where a client came from. To receive the data, add the following tags to the client or mobile platform download link:



https://download.mql5.com/cdn/web/metaquotes.ltd/mt5/mt5setup.exe?utm_source=YourWebsite&utm_campaign=YourCampaign  
https://download.mql5.com/cdn/mobile/mt5/ios?server=ABC-Demo,ABC-Real&utm_source=YourWebsite&utm_campaign=YourCampaign  
https://download.mql5.com/cdn/mobile/mt5/android?server=ABC-Demo,ABC-Real&utm_source=YourWebsite&utm_campaign=YourCampaign  
---  
  
Here YourCampaign is the company name, and YourWebsite is the address of the website hosting the link. In the 'server' parameter of the mobile platform links, enter the list of your servers to be shown to traders when they open an account.  
When opening a demo account and connecting to any trading account via the terminal downloaded using such a link, utm_source and utm_campaign values are written to a client record at the server side. If the fields are already filled, the tag values are not overwritten when re-connecting to the account (even if the terminal used for connection was downloaded by a link containing other labels).

  * Introducer — the login (trading account) of the user, who introduced the client.
  * Visitor ID — a unique identifier assigned to a user when he/she installs your terminal or visits your site, if a Finteza tracker is installed in it. With this tracker, you can trace trader behavior, from the first website visit to a real account deposit. For further details please visit the "[Analytics (#visitor)](../Analytics/README.md#visitor)" section.



> Lead Source and Lead Campaign data from terminal download links can be written to created accounts only if the broker has a [Finteza license](https://support.metaquotes.net/en/docs/mt5/platform/administration/integration/integration_finteza).

If you wish to work with client data using third-party software, you can save the relevant data to a file. Click "Export" and select the data which should be exported to a file: documents, history, etc. After that click "Save":

![Selecting client data to export to file](images/clients_export.png)

<a id="personal"></a>
## Client's Personal Data (#personal)

Personal details are written in this section: name, date of birth and contact details.

![Client's Personal Data](images/clients_personal.png)

The following information is available:

  * Title — choose Mr. or Mrs.
  * First name — the client's first name.
  * Second name — the client's second name. 
  * Middle name — the client's middle name.
  * Gender — the client's gender.
  * Birthdate — date of birth.
  * Language — the language spoken by the client. If the client record is created during the registration of a preliminary account through the client terminal, the language us set automatically based on the value specified in the registration form.
  * Preferred method — means the preferred communication method: email, phone calls, SMS, messengers.
  * Email — client's email address.
  * Mobile — client's mobile phone number.
  * Messengers — the list of the client's instant messenger accounts. You may use any form, but it is recommended to use the unified method: [messenger name]:[account].
  * Social Networks — the list of the client's accounts in social networks. You may use any form, but it is recommended to use the unified method: [network name]:[account].
  * External ID — client ID in an external trading system. This field can be used for integration and creating reports using API.



<a id="fix"></a>
### Automatic correction of personal data (#fix)

The manager terminal includes a function for automatic correction of personal data in the database of clients:

  * Names are converted to the proper case: First Name Last Name.
  * Country names are converted to standard ones.
  * Phone numbers are formatted to a unified style: +countrycode number. If the phone number does not initially include a country code, it will be added according to the country specified in the account/client data.



To apply the function, select clients and click "Fix Personal Data" in the context menu: 

![Automatic correction of personal data](images/clients_personal_fix.png)

<a id="kyc"></a>
## KYC Check (#kyc)

The trading platform integration with KYC (Know Your Customer) services enables the validation of client personal data and documents with one click or even in a fully automated mode.

> To enable this feature, configure KYC providers on the server. If the feature is not available, please contact your platform administrator.

The trader [requests a live account](Preliminary-Accounts.md) via the desktop or mobile terminal by filling out a form and uploading documents:

![Account opening form in the client terminal](images/kyc_open_account_form.png)

A preliminary account with a zero balance is created for the client. This account along with the relevant data and documents is linked to the client record. The manager clicks the "KYC Check" button in the client personal data section and the platform automatically sends a request to the KYC system.

> The platform can be configured to enable automated sending of client data to a KYC provider after the client opens a [preliminary account](Preliminary-Accounts.md) via the client terminal. This allows the full automation of the onboarding process.

![Launching KYC check from the client personal data section](images/kyc_check_start.png)

The KYC system checks data and documents and returns the result, which the manager can view in the platform as a report:

![Client data check report](images/kyc_report.png)

Based on the check result, the 'confirmed' or 'rejected' status is automatically assigned to the client and to the documents uploaded to the relevant client record. Furthermore, data from the KYC system can supplement client records on the platform side. These include the details which the system can read from the provided documents: name, date of birth, document type, number and expiration date, among other data. Updated data is indicated in a separate report block.

![The document status is updated automatically according to the check result](images/kyc_documents_status.png)

Once the check is complete, the manager can confirm registration and move the preliminary account to a real group. After that, the client can make a deposit and start trading.

<a id="address"></a>
## Client's address (#address)

Fill in here the client's address of residence and information about the appropriate ID document.

![Client's address](images/clients_address.png)

The following information is available:

  * Document type — the name of the document: passport, driving license, etc.
  * Document number — the number of the above document.
  * Issue date — the date when the document was issued.
  * Expiration date — document expiration date.
  * Comment — an arbitrary comment in addition to the document details.
  * Country — country of residence.
  * State — state (region) of residence.
  * City — city of residence.
  * ZIP code — zip or postal code
  * Address — full address including street name, house or apartment number, etc.



<a id="company"></a>
## Corporate clients (#company)

This section is only available for corporate clients. Company registration data are specified here.

![Information about a corporate client](images/clients_company.png)

The following information is available:

  * Country of registration — the country the company is registered in.
  * Company name — the name of the company. 
  * Registration number — the number assigned to the company by the registration authority.
  * Registration date — date of registration of the company.
  * Registration authority — the name of the body that registered the company.
  * VAT registration number — used for legal entities registered in the European Union.
  * LEI number for EMIR reports — EMIR (European Market Infrastructure Regulation) is a body of European legislation for the regulation of over-the-counter derivatives. EMIR requires from brokers to provide a report on transactions performed by legal entities. The transaction body in such a report must be identified by LEI (Legal Entity Identifier). It consists of a 20-character alphanumeric code.
  * License number — license number of the company.
  * License authority — the name of the authority which issued the license.
  * Legal address — full legal address of the company.
  * Website — company website address.



<a id="regulation"></a>
## Regulation (#regulation)

This section contains additional client data that may be required under the KYC (Know Your Customer) regulation.

![Additional client information for regulators](images/clients_regulationn.png)

The following information is available:

  * Nationality — the client's nationality.
  * Tax ID — identification number in the tax service, such as TIN.
  * Employment status — employed, unemployed, self-employed, etc.
  * Employment industry — agriculture, architecture and construction, health care, etc.
  * Education level — secondary, higher, no, degrees, etc.
  * Source of wealth — the source of funds which the client deposited to the account balance: employment, business, savings, income from investments, etc.
  * Net worth — the real value of the client's assets (money and property) less liabilities. 
  * Annual income — the amount of annual income received by the client.
  * Annual deposit — the amount which the client plans to deposit to the account during the year.
  * Trading experience — real trading experience relating to different instruments: Forex, stocks, futures, CFD.



<a id="documents"></a>
## Documents (#documents)

This section allows management of client's documents. Here you can add, edit or delete documents. Documents provided by the client during preliminary account opening are automatically added to this section.

The flexible system of permissions enables multi-level processing of documents. For example, a customer department employee creates a new record and adds documents to it. Further, a compliance specialist may download and check documents, and then set the appropriate status, such as 'approved' (for example, when the client confirms the authenticity of documents by visiting the office), 'rejected' (for example, if the document expired), etc. All document status changes are displayed in the version history.

![Client's documents](images/clients_documents.png)

The list shows general information about documents: document ID, type, etc. To view more information about the document, double-click on its line in the list. To view the document, click![Download the document](images/clients_documents_download.png).

<a id="adding-and-editing-documents"></a>
### Adding and editing documents (#adding-and-editing-documents)

To add a document, click "New" at the bottom of the section, to edit a document double click on it in the list. General information is shown in the Documents tab:

  * Created by — the name of the manager who has created the document and the date of creation.
  * Last changed by — the name of the manager who has made the most recent changes to the document and the date of changes.
  * Approved by — the name of the manager who has approved the document and the date of approval.
  * Status — the current document status: new, approved, rejected, in archive, deleted. When the status is changed to "Approved", the name of the manager who approved the document and the date of approval are written to the "Approved by" field.
  * Document type — ID, proof of address, legal address, company registration, etc.
  * Document subtype — a more specific document type: passport, driver's license, utility bill, bank statement, etc.
  * Issue date — the date when the document was issued.
  * Expiration date — document expiration date.
  * Name — the name of the document file. Documents provided by the client during preliminary account registration via terminals are automatically named according to the following rule: [Second Name] [First Name].[Document Type].[Extension]. The document type for proof of identity documents is 'Person', for proof of address it is 'Address'.
  * Comment — an arbitrary comment. For example, here you can specify the reason for rejecting the document.



You can view the document in the Files tab and replace it if necessary. The tab shows the date of document addition, the name of the document author, the file name and size. To view the document file, click![Download the document](images/clients_documents_download_1.png). If you have appropriate permissions, you can upload new document files by clicking "Attach documents".

![Viewing and editing a document](images/clients_documents_view.png)

<a id="document-versions"></a>
### Document versions (#document-versions)

Any changes made to client documents are displayed on the Versions tab:

![Document versions](images/clients_documents_versions.png)

Information on each change contains the number, date and the manager login. To view more information about changes, click on the line. The details show each changed parameter: its name, previous value and new value.

The list of changes can be filtered by the employee who made the changes. Use the Manager field to filter the list.

<a id="document-comments"></a>
### Document comments (#document-comments)

You can add here comments on client documents. If a document is not in order, you can add instructions to managers to contact the client.

All messages from this section are also displayed in the general list of client comments.

![Comments on client documents](images/clients_documents_comments.png)

<a id="comments"></a>
## Comments (#comments)

This section stores the client history and working correspondence with other managers. For example, sales managers can keep a call history, and the supervisory department can leave instructions to managers to contact a client if documents are not in order.

Several types of comments are supported for convenience and efficiency: general comments, log records, calls and automatic records. Choose the appropriate type for your messages, and you will be able to easily identify them in general correspondence.

![Working correspondence in the client record](images/clients_comments.png)

All comments on client documents are also displayed in this section.

<a id="versions"></a>
## History (#versions)

For efficient employee performance monitoring and secure storage of information, all changes in client records are tracked and displayed in the History section. Version support allows you to see all changes made to the client record. You can revert changes if necessary, since all earlier specified data are stored in the platform.

![Version storage of client data](images/clients_versions.png)

Information on each change contains the number, date and the manager login. To view more information about changes, click on the line. The details show each changed parameter: its name, previous value and new value.

The list of changes can be filtered by the employee who made the changes. Use the Manager field to filter the list.

<a id="accounts"></a>
## Trading accounts (#accounts)

This section contains information about the client's trading accounts, including demo, preliminary and real ones.

All accounts in the trading platform are automatically connected to clients. If an existing client opens a demo or preliminary account via the terminal, this account will be immediately added to the appropriate client record. If this is a new client, a new client record will be created, to which the newly opened account will be connected.

Also, this section allows you to [open accounts](Creation-of-Accounts.md) for the client. To do this, click "New Account" in the context menu. The account created will be automatically connected to the client record. To edit an existing account, double-click on it in the list. After that, all account [parameters](Account-Overview.md) will be shown in the right window part.

Using this menu, you can bind or unbind any other accounts:

  * Click "Link \ By Login" in the context menu. After that a new row will be added at the end of the table. Specify here the number of the account to bind.
  * Select an account and click "Unlink" in the context menu. After confirmation, the selected account will no longer be bind to the client and will be removed from the list.



![Client's trading accounts](images/clients_accounts.png)

You may use the context menu to export accounts to a file or to change the list view: show/hide columns and grid or enable/disable auto-size of columns.
