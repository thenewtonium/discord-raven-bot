## About
This is a PHP page that verifies Discord users as being (former) University of Cambridge students or staff, using SRCF's built-in Raven protection of directories.

In the current setup it also verifies alumni. To restrict to *current* students and staff only, replace the `.htaccess` file in the root directory (i.e. the one with `index.php`) with `current_only.htaccess`.

Currently, this project only consists of the 'verifier' script, and not the 'front end' to direct those who join a server to the correct address.
If you would like to extend this to a full bot, the format of URLs to use is `[URL of index.php]?u=[id of user to verify]&g=[id of server in which to verify the user]`.

## Setup
To setup this verifier, you need to add the relevant data - such as your bot token, and the id of the 'verified' role in each server you want to use this verifier for – to `scripts/config.json`.

After that you can just put the entire folder in an internet-facing directory on SRCF. The `.htaccess` files will ensure that none of the contents of `script` are publicly accessible, and that anyone visiting this folder's `index.php` page will have to
