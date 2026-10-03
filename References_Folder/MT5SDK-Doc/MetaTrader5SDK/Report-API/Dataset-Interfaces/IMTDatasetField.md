[🏠 Document Start](../../README.md) / [Report API](../README.md) / [Dataset Interfaces](../Dataset-Interfaces.md) / IMTDatasetField

[Previous](IMTDataset/SummaryTotal.md) | [Next](IMTDatasetField/Enumerations.md)

# IMTDatasetField

The IMTDatasetField interface is used for descriptions of the fields of accounts, deals and clients used in relevant data [request](../Dataset-Interfaces.md) from the trading platform database. The interface contains the following methods:

Method | Purpose  
---|---  
[Release](IMTDatasetField/Release.md) | Delete the current object.  
[Assign](IMTDatasetField/Assign.md) | Assign a passed object to the current one.  
[Clear](IMTDatasetField/Clear.md) | Clear an object.  
[Id](IMTDatasetField/Id.md) | Get and set the field ID.  
[Type](IMTDatasetField/Type.md) | Get the field type.  
[Offset](IMTDatasetField/Offset.md) | Get and set the offset inside one entry defining the data beginning.  
[Size](IMTDatasetField/Size.md) | Get and set the size of the field data in bytes.  
[Flags](IMTDatasetField/Flags.md) | Get and set the field flags.  
[WhereAddInt](IMTDatasetField/WhereAddInt.md) | Add a selection condition for fields of the int type.  
[WhereAddIntArray](IMTDatasetField/WhereAddIntArray.md) | Add an array of selection conditions for fields of the int type.  
[WhereAddUInt](IMTDatasetField/WhereAddUInt.md) | Add a selection condition for fields of the uint type.  
[WhereAddUIntArray](IMTDatasetField/WhereAddUIntArray.md) | Add an array of selection conditions for fields of the uint type.  
[WhereAddDouble](IMTDatasetField/WhereAddDouble.md) | Add a selection condition for fields of the double type.  
[WhereAddDoubleArray](IMTDatasetField/WhereAddDoubleArray.md) | Add an array of selection conditions for fields of the double type.  
[WhereAddString](IMTDatasetField/WhereAddString.md) | Add a selection condition for fields of the string type.  
[WhereAddStringArray](IMTDatasetField/WhereAddStringArray.md) | Add an array of selection conditions for fields of the string type.  
[BetweenInt](IMTDatasetField/BetweenInt.md) | Add a selection condition as a range of values for fields of the int type.  
[BetweenUInt](IMTDatasetField/BetweenUInt.md) | Add a selection condition as a range of values for fields of the uint type.  
[BetweenDouble](IMTDatasetField/BetweenDouble.md) | Add a selection condition as a range of values for fields of the double type.  
  
The IMTDataset interface contains the following enumerations:

Enumeration | Description  
---|---  
[EnFieldType (#enfieldtype)](IMTDatasetField/Enumerations.md#enfieldtype) | Types of fields.  
[EnFieldId (#enfieldid)](IMTDatasetField/Enumerations.md#enfieldid) | Field IDs.  
[EnFieldFlags (#enfieldflags)](IMTDatasetField/Enumerations.md#enfieldflags) | Field flags.  
[EnGender (#engender)](IMTDatasetField/Enumerations.md#engender) | Values of the "Gender" property.  
[EnClientType (#enclienttype)](IMTDatasetField/Enumerations.md#enclienttype) | Client types.  
[EnClientStatus (#enclientstatus)](IMTDatasetField/Enumerations.md#enclientstatus) | Client statuses.  
[EnEmployment (#enemployment)](IMTDatasetField/Enumerations.md#enemployment) | Client types by employment.  
[EnEmploymentIndustry (#enemploymentindustry)](IMTDatasetField/Enumerations.md#enemploymentindustry) | Client employment areas.  
[EnEducationLevel (#eneducationlevel)](IMTDatasetField/Enumerations.md#eneducationlevel) | Client education levels.  
[EnWealthSource (#enwealthsource)](IMTDatasetField/Enumerations.md#enwealthsource) | Clients' income sources.  
[EnPreferredCommunication (#enpreferredcommunication)](IMTDatasetField/Enumerations.md#enpreferredcommunication) | Preferred contact methods.  
[EnTradingExperience (#entradingexperience)](IMTDatasetField/Enumerations.md#entradingexperience) | Clients' trading experience.
