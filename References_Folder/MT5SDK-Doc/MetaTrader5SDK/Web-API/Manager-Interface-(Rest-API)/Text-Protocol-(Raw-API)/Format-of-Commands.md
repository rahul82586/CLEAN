[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Text Protocol (Raw API)](../Text-Protocol-(Raw-API).md) / Format of Commands

[Previous](Format-of-Packages.md) | [Next](Authentication.md)

# Format of Commands

Commands sent between the server and the Web API client have a specific format.
    
    
    COMMAND|PARAM1=VALUE1|PARAM2=VALUE2|\r\n
    additional_body

A command can consist of three elements:

  * A text command of Web API — this element is required.
  * Command parameters and their values — each command can have multiple parameters separated by symbol "|". The end of a command is the newline character "\r\n". 
  * An additional body — this part is used only in commands sent from a server to a client. Usually, requested information in the JSON format is passed in it.



> Commands and parameters are always sent in the Unicode format (UTF-16, little endian). An additional body can be of any format, but currently the server sends an additional body in Unicode, which contains description in the JSON format.
