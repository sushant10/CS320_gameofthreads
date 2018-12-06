# CS320 File Browser

### Product Vision Statement:
For HPE support users who need to download specific HPE system files, FileSublime is a file browser that provides access to raw support files, previously only indirectly available through other support tools. Our product is a simple and direct way to retrieve raw data.

**Bootstrap Version**: 4.1.3  
**JQuery Version**: 3.3.1
**DataTables version**: 1.10.18
**Django version**: 2.1.1
**PostgreSQL version**: 10


File structure to follow (Subject to change)

```
├── docs
    ├── ...
├── src
    ├── app
    |   ├── ...
    ├── logs
    |   ├── ...
    ├── static
    |   ├── css
    |   |   ├── ... 
    |   ├── fonts
    |   |   ├── ...
    |   ├── images
    |   |   ├── ...
    |   ├── js
    |   |   ├── ...
    |   ├── templates
    |   |   ├── ...
    
    
```
**docs**: will contain design & other docs  
**app**: will contain Django python server files  
**logs**: will contain Server logs  
**static**: all static files  
**css**: will contain css files including Bootstrap css  
**fonts**: will contain any external downloaded fonts  
**images**: will contain any images  
**js**: will contain bootstrap, JQuery and other files   
**templates**: will contain all the django template files for each page  

  Setup Instructions:
  https://docs.google.com/document/d/1NCx2q0U3q0VcgsMp5Eqq_OFFOb0YKr6My26RTzn6EI4/edit?usp=sharing

**Commands** (These should be run from the directory with manage.py):
**Import Files**: python3 manage.py importJson (app) (TargetFolder)
**Add User**: python3 manage.py add_User (tenant name) (password) (role=admin)
