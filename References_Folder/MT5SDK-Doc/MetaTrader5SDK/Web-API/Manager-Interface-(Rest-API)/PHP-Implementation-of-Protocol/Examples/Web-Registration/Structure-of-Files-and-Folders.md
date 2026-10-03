[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [PHP Implementation of Protocol](../../../PHP-Implementation-of-Protocol.md) / [Examples](../../Examples.md) / [Web Registration](../Web-Registration.md) / Structure of Files and Folders

[Previous](../Web-Registration.md) | [Next](Setup.md)

# Structure of Files and Folders

The Web Registration project is located in the /Examples/PHP/web_registration/ subdirectory of the [Web API installation](../../../../../Getting-Started/Setup.md) directory. The project consists of the following files and folders:

Folder/File | Description | Folders/Files  
errors | A folder with files describing possible registration errors. | 

  * already.html — a user with the same key has already been registered.
  * blocked.html — the IP address is blocked.
  * database.html — database error.
  * email.html — error sending mail.
  * empty_key.html — invalid activation key.
  * internal.html — internal error.
  * invalid_data.html — incorrect information specified during registration.
  * invalid.key.html — invalid activation link.
  * invalid_sql.html — invalid sql request.

  
lib | Used libraries. | The PEAR folder contains a library required for working with the mail server at a low level.  
templates | Mail templates. | This folder contains the template of the email sent to the user for completing registration.  
complete.phtml | A page that provides information about a newly opened account.  
image.php | Showing the verification code ("CAPTCHA").  
index.php | The main file of the project. Various parameters are set in this file.  
mysql.php | A file for working with the MySQL database.  
register.phtml | A file of the registration form.  
sql-dump.sql | A file for creating a table to store activation keys.  
tools.php | A file with additional functions.  
web_pageform.php | A file for showing the registration form.  
wr_styles.css | A table of page styles.
