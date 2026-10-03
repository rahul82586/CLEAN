[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClient](../IMTClient.md) / Enumerations

[Previous](../IMTClient.md) | [Next](Release.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

The [IMTClient](../IMTClient.md) interface contains the following enumerations:

  * [IMTClient::EnGender (#engender)](Enumerations.md#engender)
  * [IMTClient::EnClientType (#enclienttype)](Enumerations.md#enclienttype)
  * [IMTClient::EnClientStatus (#enclientstatus)](Enumerations.md#enclientstatus)
  * [IMTClient::EnEmployment (#enemployment)](Enumerations.md#enemployment)
  * [IMTClient::EnEmploymentIndustry (#enemploymentindustry)](Enumerations.md#enemploymentindustry)
  * [IMTClient::EnEducationLevel (#eneducationlevel)](Enumerations.md#eneducationlevel)
  * [IMTClient::EnWealthSource (#enwealthsource)](Enumerations.md#enwealthsource)
  * [IMTClient::EnPreferredCommunication (#enpreferredcommunication)](Enumerations.md#enpreferredcommunication)
  * [IMTClient::EnTradingExperience (#entradingexperience)](Enumerations.md#entradingexperience)
  * [IMTClient::EnClientOrigin (#enclientorigin)](Enumerations.md#enclientorigin)
  * [IMTClient::EnKYCStatus (#enkycstatus)](Enumerations.md#enkycstatus)



<a id="engender"></a>
## IMTClient::EnGender (#engender)

The "Gender" property values are enumerated in IMTClient::EnGender:

Identifier | Value | Description  
GENDER_UNSPECIFIED | 0 | Not specified.  
GENDER_MALE | 1 | Male.  
GENDER_FEMALE | 2 | Female.  
GENDER_FIRST |  | Beginning of enumeration. Corresponds to GENDER_UNSPECIFIED.  
GENDER_LAST |  | End of enumerationing. Corresponds to GENDER_FEMALE.  
  
The enumeration is used in method [IMTClient::PersonGender](PersonGender.md).

<a id="enclienttype"></a>
## IMTClient::EnClientType (#enclienttype)

IMTClient::EnClientType contains an enumeration of client types:

Identifier | Value | Description  
CLIENT_TYPE_UNDEFINED | 0 | Not set.  
CLIENT_TYPE_INDIVIDUAL | 1 | Private.  
CLIENT_TYPE_CORPORATE | 2 | Corporate.  
CLIENT_TYPE_FUND | 3 | Fund.  
CLIENT_TYPE_FIRST |  | Beginning of enumeration. Corresponds to CLIENT_TYPE_UNDEFINED.  
CLIENT_TYPE_LAST |  | End of enumerationing. Corresponds to CLIENT_TYPE_FUND.  
  
The enumeration is used in method [IMTClient::ClientType](ClientType.md).

<a id="enclientstatus"></a>
## IMTClient::EnClientStatus (#enclientstatus)

Client statuses are enumerated in IMTClient::EnClientStatus:

Identifier | Value | Description  
CLIENT_STATUS_UNREGISTERED | 0 | Not registered. An anonymous client, which was created based on a demo account without any data.  
CLIENT_STATUS_REGISTERED | 100 | Registered. The client has created a demo account with filled contact details.  
CLIENT_STATUS_NOTINTERESTED | 200 | Not interested. The client has created a demo account with filled contact data but is not interested in opening a real account.  
CLIENT_STATUS_APPLICATION_INCOMPLETED | 300 | Not completed. The client has provided data for opening a real account.  
CLIENT_STATUS_APPLICATION_COMPLETED | 400 | Completed. The client has provided data for opening a real account and has submitted all the required documents.  
CLIENT_STATUS_APPLICATION_INFORMATION | 500 | Information is needed. To open a real account, the client needs to provide additional information.  
CLIENT_STATUS_APPLICATION_REJECTED | 600 | Rejected. The client is denied registration.  
CLIENT_STATUS_APPROVED | 700 | Approved. A real account has been opened for the client.  
CLIENT_STATUS_FUNDED | 800 | Funded. The client has deposited money to a real account.  
CLIENT_STATUS_ACTIVE | 900 | Active. The client has trading activity.  
CLIENT_STATUS_INACTIVE | 1000 | Inactive. The client does not have trading activity.  
CLIENT_STATUS_SUSPENDED | 1100 | Suspended. Work with the client has been suspended.  
CLIENT_STATUS_CLOSED | 1200 | Closed. The client has left at the client's own decision.  
CLIENT_STATUS_TERMINATED | 1300 | Terminated. Work with the client was terminated at the initiative of the company.  
CLIENT_STATUS_FIRST |  | Beginning of enumeration. Corresponds to CLIENT_STATUS_UNREGISTERED.  
CLIENT_STATUS_LAST |  | End of enumerationing. Corresponds to CLIENT_STATUS_TERMINATED.  
  
The enumeration is used in the [IMTClient::ClientStatus](ClientStatus.md) method.

<a id="enemployment"></a>
## IMTClient::EnEmployment (#enemployment)

IMTClient::EnEmployment contains client types by employment:

Identifier | Value | Description  
EMPLOY_UNEMPLOYED | 0 | Unemployed.  
EMPLOY_EMPLOYED | 1 | Employed.  
EMPLOY_SELF_EMPLOYED | 2 | Entrepreneur or self-employed.  
EMPLOY_RETIRED | 3 | Retired.  
EMPLOY_STUDENT | 4 | Student.  
EMPLOY_OTHER | 5 | Other.  
EMPLOY_FIRST |  | Beginning of enumeration. Corresponds to EMPLOY_UNEMPLOYED.  
EMPLOY_LAST |  | End of enumerationing. Corresponds to EMPLOY_OTHER.  
  
The enumeration is used in the [IMTClient::PersonEmployment](PersonEmployment.md) method.

<a id="enemploymentindustry"></a>
## IMTClient::EnEmploymentIndustry (#enemploymentindustry)

IMTClient::EnEmploymentIndustry contains the enumeration of client employment industries:

Identifier | Value | Description  
INDUSTRY_NONE | 0 | None.  
INDUSTRY_AGRICULTURE | 1 | Agriculture, food and natural resources.  
INDUSTRY_CONSTRUCTION | 2 | Architecture and construction.  
INDUSTRY_MANAGEMENT | 3 | Administration and business management.  
INDUSTRY_COMMUNICATION | 4 | Art, audio/video technology and communication.  
INDUSTRY_EDUCATION | 5 | Education and training.  
INDUSTRY_GOVERNMENT | 6 | State and administrative management.  
INDUSTRY_HEALTHCARE | 7 | Health care.  
INDUSTRY_TOURISM | 8 | Tourism and hospitality.  
INDUSTRY_IT | 9 | Information technology.  
INDUSTRY_SECURITY | 10 | Legal and public safety, correction and protection services.  
INDUSTRY_MANUFACTURING | 11 | Production.  
INDUSTRY_MARKETING | 12 | Marketing and sales.  
INDUSTRY_SCIENCE | 13 | Science and technology.  
INDUSTRY_ENGINEERING | 14 | Engineering and mathematics.  
INDUSTRY_TRANSPORT | 15 | Transportation, distribution and logistics.  
INDUSTRY_OTHER | 16 | Other.  
INDUSTRY_FIRST |  | Beginning of enumeration. Corresponds to INDUSTRY_NONE.  
INDUSTRY_LAST |  | End of enumerationing. Corresponds to INDUSTRY_OTHER.  
  
The enumeration is used in the [IMTClient::PersonIndustry](PersonIndustry.md) method.

<a id="eneducationlevel"></a>
## IMTClient::EnEducationLevel (#eneducationlevel)

IMTClient::EnEducationLevel contains the enumeration of client education levels:

Identifier | Value | Description  
EDUCATION_LEVEL_NONE | 0 | None.  
EDUCATION_LEVEL_HIGH_SCHOOL | 1 | Secondary.  
EDUCATION_LEVEL_BACHELOR | 2 | Bachelor's degree or equivalent.  
EDUCATION_LEVEL_MASTER | 3 | Master's degree or equivalent.  
EDUCATION_LEVEL_PHD | 4 | PhD or equivalent.  
EDUCATION_LEVEL_OTHER | 5 | Other.  
EDUCATION_LEVEL_FIRST |  | Beginning of enumeration. Corresponds to EDUCATION_LEVEL_NONE.  
EDUCATION_LEVEL_LAST |  | End of enumerationing. Corresponds to EDUCATION_LEVEL_OTHER.  
  
The enumeration is used in method [IMTClient::PersonEducation](PersonEducation.md).

<a id="enwealthsource"></a>
## IMTClient::EnWealthSource (#enwealthsource)

IMTClient::EnWealthSource contains the enumeration of client's income sources:

Identifier | Value | Description  
WEALTH_SOURCE_EMPLOYMENT | 0 | Employment/business  
WEALTH_SOURCE_SAVINGS | 1 | Savings or investments.  
WEALTH_SOURCE_INHERITANCE | 2 | Gift or inheritance.  
WEALTH_SOURCE_OTHER | 3 | Other.  
WEALTH_SOURCE_FIRST |  | Beginning of enumeration. Corresponds to WEALTH_SOURCE_EMPLOYMENT.  
WEALTH_SOURCE_LAST |  | End of enumerationing. Corresponds to WEALTH_SOURCE_OTHER.  
  
The enumeration is used in method [IMTClient::PersonWealthSource](PersonWealthSource.md).

<a id="enpreferredcommunication"></a>
## IMTClient::EnPreferredCommunication (#enpreferredcommunication)

IMTClient::EnPreferredCommunication contains the enumeration of preferred client contact methods:

Identifier | Value | Description  
PREFERRED_COMMUNICATION_UNDEFINED | 0 | Not specified.  
PREFERRED_COMMUNICATION_EMAIL | 1 | Email.  
PREFERRED_COMMUNICATION_PHONE | 2 | Phone.  
PREFERRED_COMMUNICATION_PHONE_SMS | 3 | SMS.  
PREFERRED_COMMUNICATION_MESSENGER | 4 | Instant messenger.  
PREFERRED_COMMUNICATION_FIRST |  | Beginning of enumeration. Corresponds to PREFERRED_COMMUNICATION_UNDEFINED.  
PREFERRED_COMMUNICATION_LAST |  | End of enumerationing. Corresponds to PREFERRED_COMMUNICATION_MESSENGER.  
  
The enumeration is used in method [IMTClient::ContactPreferred](ContactPreferred.md).

<a id="entradingexperience"></a>
## IMTClient::EnTradingExperience (#entradingexperience)

IMTClient::EnTradingExperience contains values describing clients' financial market trading experience:

Identifier | Value | Description  
EXPERIENCE_LESS_1_YEAR | 0 | < 1 year.  
EXPERIENCE_1_3_YEAR | 1 | 1 — 3 years.  
EXPERIENCE_ABOVE_3_YEAR | 2 | > 3 year.  
EXPERIENCE_FIRST |  | Beginning of enumeration. Corresponds to EXPERIENCE_LESS_1_YEAR.  
EXPERIENCE_LAST |  | End of enumerationing. Corresponds to EXPERIENCE_ABOVE_3_YEAR.  
  
The enumeration is used in the following methods:

  * [IMTClient::ExperienceCFD](ExperienceCFD.md)
  * [IMTClient::ExperienceFutures](ExperienceFutures.md)
  * [IMTClient::ExperienceFX](ExperienceFX.md)
  * [IMTClient::ExperienceStocks](ExperienceStocks.md)



<a id="enclientorigin"></a>
## IMTClient::EnClientOrigin (#enclientorigin)

Methods for creating clients in the system are enumerated in IMTClient::EnClientOrigin:

Identifier | Value | Description  
CLIENT_ORIGIN_MANUAL | 0 | Created manually.  
CLIENT_ORIGIN_DEMO | 1 | Created automatically based on a demo account.  
CLIENT_ORIGIN_CONTEST | 2 | Created automatically based on a contest account.  
CLIENT_ORIGIN_PRELIMINARY | 3 | Created automatically based on a preliminary account.  
CLIENT_ORIGIN_REAL |  | Created automatically based on a real account.  
CLIENT_ORIGIN_FIRST |  | Beginning of enumeration. Corresponds to CLIENT_ORIGIN_MANUAL.  
CLIENT_ORIGIN_LAST |  | End of enumerationing. Corresponds to CLIENT_ORIGIN_REAL.  
  
The enumeration is used in the [IMTClient::ClientOrigin](ClientOrigin.md) method.

<a id="enkycstatus"></a>
## IMTClient::EnKYCStatus (#enkycstatus)

IMTClient::EnKYCStatus contains KYC verification statuses:

ID | Value | Description  
KYC_STATUS_UNDEFINED | 0 | The status is not determined; the KYC verification has not yet been performed.  
KYC_STATUS_APPROVED | 1 | The client has been approved by the KYC system.  
KYC_STATUS_DECLINED | 2 | The client has been rejected by the KYC system.  
KYC_STATUS_FIRST |  | Beginning of enumeration. Corresponds to KYC_STATUS_UNDEFINED.  
KYC_STATUS_LAST |  | End of enumeration. Corresponds to KYC_STATUS_DECLINED.  
  
The enumeration is used in the [IMTClient::KYCStatus](KYCStatus.md) method.
