[🏠 Document Start](../../README.md) / [Report API](../README.md) / [Dataset Interfaces](../Dataset-Interfaces.md) / IMTDatasetRequest

[Previous](IMTDatasetField/BetweenDouble.md) | [Next](IMTDatasetRequest/Release.md)

# IMTDatasetRequest

The IMTDatasetRequest interface is a description of a [database request (#request)](../Dataset-Interfaces.md#request). It consists of a set of [IMTDatasetField](IMTDatasetField.md) objects. The interface contains the following methods:

Method | Purpose  
---|---  
[Release](IMTDatasetRequest/Release.md) | Delete the current object.  
[Assign](IMTDatasetRequest/Assign.md) | Assign a passed object to the current one.  
[Clear](IMTDatasetRequest/Clear.md) | Clear an object.  
[FieldCreate](IMTDatasetRequest/FieldCreate.md) | Create a field object.  
[FieldCreateReference](IMTDatasetRequest/FieldCreateReference.md) | Create a reference to the object of the field at the specified position.  
[FieldAdd](IMTDatasetRequest/FieldAdd.md) | Add a field object to the request.  
[FieldUpdate](IMTDatasetRequest/FieldUpdate.md) | Change a field object in the request.  
[FieldDelete](IMTDatasetRequest/FieldDelete.md) | Delete a field object from the request.  
[FieldClear](IMTDatasetRequest/FieldClear.md) | Clear the request description.  
[FieldShift](IMTDatasetRequest/FieldShift.md) | Change the position of the field description in the request.  
[FieldTotal](IMTDatasetRequest/FieldTotal.md) | Get the total number of fields in a request.  
[FieldNext](IMTDatasetRequest/FieldNext.md) | Get a field description in a request based on its index.
