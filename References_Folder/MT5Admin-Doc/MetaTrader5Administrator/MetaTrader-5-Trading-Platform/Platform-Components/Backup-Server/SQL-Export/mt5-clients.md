[🏠 Document Start](../../../../README.md) / [MetaTrader 5 Trading Platform](../../../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../../../Platform-Components.md) / [Backup Server](../../Backup-Server.md) / [SQL Export](../SQL-Export.md) / mt5_clients

[Previous](mt5-managers.md) | [Next](mt5-documents.md)

# mt5_clients

Data about [clients](../../../Platform-Setup/Clients.md) is exported to this table. The table contains the following fields:

Name | Type | Description  
ClientID | Integer | Initial key. Unique entry ID.  
Timestamp | Integer | A unique values within the table. Used by MetaTrader 5 servers for internal purposes. If the Timestamp of a record has changed, it means that the record has changed.  
ClientType | Integer | Client type:

  * 0 — Not specified
  * 1 — Individual
  * 2 — Corporate
  * 3 — Fund

  
ClientStatus | Integer | Client status:

  * 0 — Not registered
  * 1 — Registered
  * 2 — not interested
  * 3 — Not completed
  * 4 — Completed
  * 5 — Information
  * 6 — Rejected
  * 7 — Approved
  * 8 — Financed
  * 9 — Active
  * 10 — Inactive
  * 11 — Suspended
  * 12 — Closed
  * 13 — Deleted

  
AssignedManager | Integer | The login of the assigned manager.  
DateCreated | Integer | Client creation date.  
DateModified | Integer | Client's last modification date.  
Comment | String | A comment to the client.  
ComplianceApprovedBy | Integer | The login of the manager by whom the client was approved.  
ComplianceClientCategory | String | Client compliance category. Currently not used.  
ComplianceDateApproval | DateTime | The date when the client was approved, in the format of YYYY-MM-DD HH:MM:SS  
ComplianceDateTermination | DateTime | The date when the provision of services to the client was discontinued, in the format of YYYY-MM-DD HH:MM:SS  
LeadCampaign | String | The website from which the client came (lead source).  
LeadSource | String | The name of the marketing campaign, as a result of which the client came (lead campaign).  
Introducer | String | The login of the user by whom the client was introduced.  
PersonTitle | String | Client's title.  
PersonName | String | First name and last name  
PersonMiddleName | String | Middle name.  
PersonBirthDate | DateTime | Date of birth, in the format of YYYY-MM-DD HH:MM:SS  
PersonCitizenship | String | Citizenship.  
PersonGender | Integer | Gender:

  * 0 — Not specified
  * 1 — male
  * 2 — Female

  
PersonTaxID | String | Client's Tax ID.  
PersonDocumentType | String | Document type of document: passport, driver's license, etc.  
PersonDocumentNumber | String | Document number.  
PersonDocumentDate | DateTime | Document issue date, in the format of YYYY-MM-DD HH:MM:SS  
PersonDocumentExtra | String | Additional document information.  
PersonEmployment | Integer | Employment status:

  * 0 — Unemployed
  * 1 — Employed
  * 2 — Entrepreneur or self-employed
  * 3 — Retired
  * 4 — Student
  * 5 — Other

  
PersonIndustry | Integer | Employment area:

  * 0 — Not specified
  * 1 — Agriculture, Food and Natural Resources
  * 2 — Architecture and Construction
  * 3 — Business Administration and Management
  * 4 — Art, Audio/Video Technology and Communication
  * 5 — Education and Training
  * 6 — State and Administrative Management
  * 7 — Health
  * 8 — Tourism and Hospitality
  * 9 — Information Technology
  * 10 — Legal and Public Safety, Correction and Protection Services
  * 11 — Manufacturing
  * 12 — Marketing and Sales
  * 13 — Science and Technology
  * 14 — Engineering and Mathematics
  * 15 — Transportation, Distribution and Logistics
  * 16 — other

  
PersonEducation | Integer | Education:

  * 0 — Not specified
  * 1 — Secondary
  * 2 — Bachelor's degree or equivalent
  * 3 — Master's degree or equivalent
  * 4 — PhD or equivalent
  * 5 — other

  
PersonWealthSource | Integer | Source of income:

  * 0 — Employment/business activity
  * 1 — Savings or investments
  * 2 — Gift or inheritance
  * 3 — other

  
PersonAnnualIncome | Float | Annual income.  
PersonNetWorth | Float | Net assets.  
PersonAnnualDeposit | Float | Annual deposit.  
CompanyName | String | Company name.  
CompanyRegNumber | String | Company registration number.  
CompanyRegDate | String | company registration date.  
CompanyRegAuthority | String | Company registration authority.  
CompanyVat | String | VAT number.  
CompanyLei | String | LEI number for EMIR reports.  
CompanyLicenseNumber | String | Company license number.  
CompanyLicenseAuthority | String | Licensing authority.  
CompanyCountry | String | Country of incorporation.  
CompanyAddress | String | Company's legal address.  
CompanyWebsite | String | Company's webiste.  
ContactPreferred | Integer | Preferred method of communication:

  * 0 — Not specified
  * 1 — Email
  * 2 — Telephone
  * 3 — SMS
  * 4 — Messenger

  
ContactLanguage | String | Client's language.  
ContactEmail | String | Client's email.  
ContactPhone | String | Phone number.  
ContactMessengers | String | Messengers.  
ContactSocialNetworks | String | Accounts in social networks.  
ContactLastDate | DateTime | Last contact date, in the format of YYYY-MM-DD HH:MM:SS  
AddressCountry | String | Client's country.  
AddressPostcode | String | Client's postal code.  
AddressStreet | String | Client's address.  
AddressState | String | State/region of residence.  
AddressCity | String | City.  
ExperienceFX | Integer | Forex trading experience, number of years.  
ExperienceCFD | Integer | CFD trading experience, number of years.  
ExperienceFutures | Integer | Futures trading experience, number of years.  
ExperienceStocks | Integer | Stock trading experience, number of years.  
ClientOrigin | Integer | How the client record was created:

  * 0 — manually
  * 1 — based on a demo account
  * 2 — based on a contest account
  * 3 — based on a preliminary account
  * 4 — based on a real account

  
ClientOriginLogin | Integer | The number of the account, based on which the client record was created.
