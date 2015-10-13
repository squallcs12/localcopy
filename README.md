# localcopy

Clone 3rd party source (javascript, css, etc) to local for developement.

**This service run a django server on port 80, which may need sudo permission on linux and os x**

# Requirement
Python 3

# Install

Clone this project and install requirements
```
pip install -r requirements.txt
```

# Start (python3)

```
python manage.py runserver 80
```
need root permission to open port 80 and auto clone

# Clone 3rd-party source

```
python manage.py copy {url}
```

# Enable serve static file from local

```
python manage.py enable
```
need root permission to edit hosts file

# Disable service

```
python manage.py disable
```
need root permission to edit hosts file

**This service auto clone any files from same domain that has been cloned before**

# NO HTTPS support

You may want to change your 3rd-party url to `//:` instead of `https://`
