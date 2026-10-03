[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Clients](../Clients.md) / Data Structure

[Previous](../Clients.md) | [Next](Add.md)

<a id="data-structure"></a>
# Data Structure (#data-structure)

Client information is passed in the JSON format in response to [/api/client/add](Add.md), [/api/client/update](Update.md) and [/api/client/get](Get.md) requests.

<a id="client-parameters"></a>
## Client Parameters (#client-parameters)

Parameter | Type | Description  
RecordID | Integer | Client ID.  
ClientType | Integer | Client type. Passed as the [EnClientType (#enclienttype)](../../../Database-Interfaces/Clients/IMTClient/Enumerations.md#enclienttype) enumeration value.  
ClientStatus | Integer | Client status. Passed as the [EnClientStatus (#enclientstatus)](../../../Database-Interfaces/Clients/IMTClient/Enumerations.md#enclientstatus) enumeration value.  
ClientExternalID | String | Client ID in the external trading system.  
AssignedManager | Integer | The manager responsible for the client.  
DateCreated | Integer | Client creation date.  
DateModified | Integer | Last client modification date.  
Comment | String | A comment to a client.  
ComplianceApprovedBy | Integer | The manager who checked the client data and approved registration.  
ComplianceClientCategory | String | Client compliance category — client classification based on the regulator rules.  
ComplianceDateApproval | Integer | Client approval date.  
ComplianceDateTermination | Integer | The date of service termination for the client.  
LeadCampaign | String | Lead campaign — the name of an advertising campaign the client was attracted by.  
LeadSource | String | Lead source — a website the client has come from.  
Introducer | String | The login (trading account) of the user who attracted this client.  
PersonTitle | String | Client's title, such as Mr. or Mrs.  
PersonName | String | Client's name.  
PersonMiddleName | String | Client's middle name.  
PersonLastName | String | Client's last name.  
PersonBirthDate | Integer | Client's date of birth. Specified in the [FILETIME](https://docs.microsoft.com/en-us/windows/win32/api/minwinbase/ns-minwinbase-filetime) format.  
PersonCitizenship | String | Client's citizenship.  
PersonGender | Integer | Client's gender. Passed as a value of the [EnGender (#engender)](../../../Database-Interfaces/Clients/IMTClient/Enumerations.md#engender) enumeration.  
PersonTaxID | String | Client's tax ID, for example TIN.  
PersonDocumentType | String | Client's identification document type: passport, driver's license, etc.  
PersonDocumentNumber | String | The number of the identification document (of passport, driver's license, etc.).  
PersonDocumentDate | Integer | The issue date of the identification document (of passport, driver's license, etc.).  
PersonDocumentExpiration | Integer | The expiration date of the identification document (of passport, driver's license, etc.).  
PersonDocumentExtra | String | Additional information (comment) to the identification document.  
PersonEmployment | Integer | Client's employment status. Passed as a value from the [EnEmployment (#enemployment)](../../../Database-Interfaces/Clients/IMTClient/Enumerations.md#enemployment) enumeration.  
PersonIndustry | Integer | Client's employment industry. Passed as a value from the [EnEmploymentIndustry (#enemploymentindustry)](../../../Database-Interfaces/Clients/IMTClient/Enumerations.md#enemploymentindustry) enumeration.  
PersonEducation | Integer | Client's education level. Passed as a value from the [EnEducationLevel (#eneducationlevel)](../../../Database-Interfaces/Clients/IMTClient/Enumerations.md#eneducationlevel) enumeration.  
PersonWealthSource | Integer | Client's income source. Passed as a value from from the [EnWealthSource (#enwealthsource)](../../../Database-Interfaces/Clients/IMTClient/Enumerations.md#enwealthsource) enumeration.  
PersonAnnualIncome | Float | Client's annual income amount.  
PersonNetWorth | Float | The amount of the client's net assets.  
PersonAnnualDeposit | Float | The amount of the client's annual deposit.  
CompanyName | String | Company name (for corporate clients).  
CompanyRegNumber | String | Company registration number (for corporate clients).  
CompanyRegDate | Integer | Company registration date (for corporate clients).  
CompanyRegAuthority | String | The name of the registration authority with which the company is registered (for corporate body).  
CompanyVat | String | VAT number (for corporate clients).  
CompanyLei | String | LEI number for EMIR reports (for corporate clients).  
CompanyLicenseNumber | String | License number (for corporate clients).  
CompanyLicenseAuthority | String | The name of the licensing authority (for corporate clients).  
CompanyCountry | String | Company registration country (for corporate clients).  
CompanyAddress | String | Legal address of the company (for corporate clients).  
CompanyWebsite | String | Website address (for corporate clients).  
ContactPreferred | Integer | Client's preferred contact method. Passed as a value of the [EnPreferredCommunication (#enpreferredcommunication)](../../../Database-Interfaces/Clients/IMTClient/Enumerations.md#enpreferredcommunication) enumeration.  
ContactLanguage | String | The language spoken by the client.  
ContactEmail | String | Client's email address.  
ContactPhone | String | Client's phone number.  
ContactMessengers | String | List of the client's accounts in instant messengers.  
ContactSocialNetworks | String | List of the client's accounts in social networks.  
ContactLastDate | Integer | Date of the last client contact.  
AddressCountry | String | Client's country of residence.  
AddressPostcode | String | Client's zip code.  
AddressStreet | String | Client's address.  
AddressState | String | Client's region of residence.  
AddressCity | String | Client's city of residence.  
ExperienceFX | Integer | Information about the client's Forex trading experience. Passed as a value of the [EnTradingExperience (#entradingexperience)](../../../Database-Interfaces/Clients/IMTClient/Enumerations.md#entradingexperience) enumeration.  
ExperienceCFD | Integer | Information about the client's CFD trading experience. Passed as a value of the [EnTradingExperience (#entradingexperience)](../../../Database-Interfaces/Clients/IMTClient/Enumerations.md#entradingexperience) enumeration.  
ExperienceFutures | Integer | Information about the client's Futures trading experience. Passed as a value of the [EnTradingExperience (#entradingexperience)](../../../Database-Interfaces/Clients/IMTClient/Enumerations.md#entradingexperience) enumeration.  
ExperienceStocks | Integer | Information about the client's Stock trading experience. Passed as a value of the [EnTradingExperience (#entradingexperience)](../../../Database-Interfaces/Clients/IMTClient/Enumerations.md#entradingexperience) enumeration.  
TradingGroup | String | Preferred trading group for the client.  
ClientOrigin | Integer | Client record creation method. Passed as a value of the [EnClientOrigin (#enclientorigin)](../../../Database-Interfaces/Clients/IMTClient/Enumerations.md#enclientorigin) enumeration.  
ClientOriginLogin | Integer | The trading account number, based on which the client was created.  
KYCApplicantSumSub | String | Client's ID in the [SumSub KYC-system](https://support.metaquotes.net/en/docs/mt5/platform/administration/integration/integration_kyc).  
  
Document Parameters

Parameter | Type | Description  
RecordID | Integer | Document ID.  
RelatedClient | Integer | ID of the client with whom the document is associated.  
RelatedUser | Integer | Login of the client with whom the document is associated. Currently not used.  
RelatedTransfer | Integer | The number of the operation with which the document is associated. Currently not used.  
ApprovedDate | Integer | Document approval date.  
ApprovedBy | Integer | The manager who approved/checked the document.  
DateIssue | Integer | Document issue date.  
DateExpiration | Integer | Document expiry date.  
DocumentType | Integer | Document type. Passed as a value from the [EnDocumentTypes (#endocumenttypes)](../../../Database-Interfaces/Clients/IMTDocument/Enumerations.md#endocumenttypes) enumeration.  
DocumentSubtype | Integer | Document subtype. Passed as a value from the [EnDocumentSubtype (#endocumentsubtype)](../../../Database-Interfaces/Clients/IMTDocument/Enumerations.md#endocumentsubtype) enumeration.  
DocumentName | String | Document name.  
DocumentComment | String | Comment to a document.  
DocumentStatus | Integer | Document status. Passed as a value from the [EnDocumentStatus (#endocumentstatus)](../../../Database-Interfaces/Clients/IMTDocument/Enumerations.md#endocumentstatus) enumeration.  
DocumentFiles | Array | Array of [document files (#file)](Data-Structure.md#file).  
  
Document files

Parameter | Type | Description  
CreatedBy | Integer | The login of the manager who added the file.  
CreatedDate | Integer | File adding date.  
ID | Integer | File identifier.  
Size | Integer | File size in bytes  
Hash | Integer | File hash.  
Flags | Integer | File flags. Passed as a value of [EnFileFlags (#enfileflags)](../../../Database-Interfaces/Clients/IMTAttachment/Enumerations.md#enfileflags).  
Name | String | File name.  
  
Comment parameters

Method | Type | Purpose  
RecordID | Integer | Comment ID.  
RelatedClient | Integer | The ID of the client with which the comment is associated.  
RelatedDocument | Integer | The ID of the document with which the comment is associated.  
Flags | Integer | Comment flags. Passed as a value of [EnCommentFlags (#encommentflags)](../../../Database-Interfaces/Clients/IMTComment/Enumerations.md#encommentflags).  
Extra | String | Additional information about the comment.  
Text | String | Comment text.  
CommentType | Integer | Comment type. Passed as a value of [EnCommentType (#encommenttype)](../../../Database-Interfaces/Clients/IMTComment/Enumerations.md#encommenttype).  
CommentResult | Integer | Call result from a comment. Passed as a value of [EnCommentResult (#encommentresult)](../../../Database-Interfaces/Clients/IMTComment/Enumerations.md#encommentresult).  
AttachmentFiles | Array | Array of [files (#file)](Data-Structure.md#file) attached to a comment.  
  
Attachment Parameters

Parameter | Type | Description  
RecordID | Integer | Attachment ID. Corresponds to the ["ID" parameter of the file (#file)](Data-Structure.md#file).  
RelatedClient | Integer | The client ID with which the attachment is associated.  
FileType | Integer | File type. Passed as a value of [EnFileType (#enfiletype)](../../../Database-Interfaces/Clients/IMTAttachment/Enumerations.md#enfiletype).  
FileName | String | File Name  
FileContent | String | Base64 encoded binary file contents.  
FileHash | String | File hash.  
FileFlags | Integer | File flags. Passed as a value of [EnFileFlags (#enfileflags)](../../../Database-Interfaces/Clients/IMTAttachment/Enumerations.md#enfileflags).
