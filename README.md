# CS320 File Browser

### Product Vision Statement:
For HP support users who need to download specific HP system files, our file browser will provide a simple, reliable, and secure way to access and filter important files. Our file browser will take the burden off of HP employees to deliver system files to customers.  

**Bootstrap Version**: 4.1.3  
**JQuery Version**: 3.3.1

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
    ├── templates
    |   ├── ...
    
    
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

  
Database Credentials:  
      Database Name: file_browser_db  
      User Name: db_admin  
      Password: cs320
