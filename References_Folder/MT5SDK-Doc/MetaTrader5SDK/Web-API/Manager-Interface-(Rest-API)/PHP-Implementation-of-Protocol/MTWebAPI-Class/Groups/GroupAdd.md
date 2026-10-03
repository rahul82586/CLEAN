[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [PHP Implementation of Protocol](../../../PHP-Implementation-of-Protocol.md) / [MTWebAPI Class](../../MTWebAPI-Class.md) / [Groups](../Groups.md) / GroupAdd

[Previous](GroupCreate.md) | [Next](GroupDelete.md)

# MTWebAPI::GroupAdd

Add or change a group configuration on the server.
    
    
    MTAPIRES  MTWebAPI::GroupAdd(
       MTConGroup  $group,      // Description of the group to create
       MTConGroup  &$new_group  // Description of the created group
       )

### Parameters

**$group**  
[in] The MTConGroup object that describes the configuration of the group that you need to create. The object must first be created using theMTWebAPI::GroupCreatemethod.

**& $new_group**  
[Out] The MTConGroup object that describes the configuration of the group, which was created on the server. Description of the structure parameters is provided in the"Data Structure"section.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

  * To create a group, all parameters of the MTConGroup object must be filled.


  * When creating an object using the [MTWebAPI::GroupCreate](GroupCreate.md) method, all the structure fields are filled with zeros or default values. When updating a group, you should either set all its parameters manually or get its configuration using the [MTWebAPI::GroupNext](GroupNext.md) or [MTWebAPI::GroupGet](GroupGet.md) method and edit it appropriately.


  * This method works only when connected to the main trade server. Otherwise, error [MT_RET_ERR_NOTMAIN](../../../../../Return-Codes/API.md) is returned.
  * When calling the method, a check is made whether the group already exists. The key field for comparison is the name of the group (including the path). If such a group already exists, its settings are updated.
  * Before adding, the correctness of the record is checked. If the record is incorrect, the error code [MT_RET_ERR_PARAMS](../../../../../Return-Codes/Common-errors.md) is returned.
  * [The manager account](../../../Text-Protocol-(Raw-API)/Authentication.md#client-start) must have rights to connect as an administrator and edit group configurations. Otherwise, error code [MT_RET_ERR_PERMISSIONS](../../../../../Return-Codes/Common-errors.md) is returned.
  * To enable a newly added group, [restart the main trade server](../Service-Commands/ServerRestart.md).


