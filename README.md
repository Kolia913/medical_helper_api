# medical_helper_api
## Start api(Windows):
1. Add project to empty directory and open it in CMD
2. run command "python -m venv .venv". Directory should be like:
"""/project
      /.venv
      /medical_helper"""
3. Run your .venv in shell: cd .venv\Scripts -> run activate file from shell
4. Install Django3, Pillow, DjangoRestFramewrok to your .venv (" (.venv) C://project: pip install django " - example)
5. Go to directory with manage.py file
6. Run "python manage.py runserver"

### Endpoints:
      |'admin/'| - admin routes (login: admin, password: 111111)
      |'api-auth/'| - api
      |'api-auth/login'| - login to API (same as admin data)
  ### Prefix:
    |'api/v1/'| - api prefix
  ### Diseases:
    |'disease/'| - list of diseases
    |'disease/<slug:slug>/'| - disease details :param: slug
    |'pill/'| - list of pills
    |'pill/<slug:slug>/'| - pill details :param: slug
    
