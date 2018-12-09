# FileSublime

### Product Vision Statement
For HPE support users who need to download specific HPE system files, FileSublime is a file browser that provides access to raw support files, previously only indirectly available through other support tools. Our product is a simple and direct way to retrieve raw data.

FileSublime is used to filter through specific Json files which contain certain identifying information, such as system and date.

### Technologies Used
- *[Bootstrap] Version: 4.1.3*
- *[JQuery] Version: 3.3.1*
- *[DataTables] Version: 1.10.18*
- *[Django] Version: 2.1.1*
- *[PostgreSQL] Version: 10*

### Getting Started

FileSublime’s front end interface is built using Bootstrap, JQuery and DataTables. These are included in this repository. FileSublime’s back end is built upon Django and PostgreSQL. These you will need to download and setup yourself on your machine. See the [Getting Started page](https://github.com/sushant10/CS320_gameofthreads/wiki/Getting-Started) on how to set up FileSublime.

### File structure
```
├── src
    ├── app
    |   ├── FileBrowser
    |   |   ├── Filebrowser
    |   |   |   ├── settings.py 
    |   |   |   ├── urls.py 
    |   |   ├── browser
    |   |   |   ├── management/commands
    |   |   |   ├── migrations
    |   |   |   ├── static
    |   |   |   ├── templates/browser
    |   |   |   ├── models.py
    |   |   |   ├── views.py
    |   |   |   ├── tests.py
    |   |   ├── manage.py
```
| Folder/File | Contains |
| ------ | ------ |
| `settings.py` |  *Django settings* |
| `urls.py` | *URL scheme and configuration*  |
| `management/commands` | *Custom scripts for addings users to database or importing a data dump* |
| `migrations` | *PostgreSQL database creation script*  |
| `static` | *CSS, images and Javascript files*  |
| `templates/browser` | *Django templates for all pages* |
| `models.py` | *Database models for FileSublime* |
| `view.py` | *Django Views that return web responses* |
| `tests.py` | *Whitebox and Blackbox tests for FileSublime* |
| `manage.py` | *Helps run all commands like runserver* |

### Commands:
**_Prerequisite_** <br>
*Must be in the below directory:*

```sh
$ cd src/app/FileBrowser
```
**Import Files**

```sh
$ python3 manage.py importJson [app] [TargetFolder]
```

**Add User**
```sh
$ python3 manage.py add_User [tenant name] [password] admin  
```



[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. )

[Bootstrap]: <https://getbootstrap.com/docs/4.1/getting-started/introduction/>
[jQuery]: <http://jquery.com>
[DataTables]: <https://datatables.net/>
[Django]: <https://www.djangoproject.com/>
[PostgreSQL]: <https://www.postgresql.org/>

  
