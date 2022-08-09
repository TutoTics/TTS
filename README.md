# TutoTics
It's academic project created to help teachers and students in the organization of their schedule in tutorials
    
    
## Initial setup    
 You must create a file in the root of the project with the name .env with the following data:    
    
    #Django
    DEBUG=False      
    SECRET_KEY=8^dv4m()q9_u+rc6f4k#&6qzdivz*94cd^-lr)ktdz7agosgob      
    TZ=America/Bogota      
    DJANGO_SETTINGS_MODULE=tuto.settings    
          
    #Postgres      
    POSTGRES_DB=tuto_db      
    POSTGRES_USER=tuto_user      
    POSTGRES_PASSWORD=tuto2021**.      
    POSTGRES_HOST=postgres      
    POSTGRES_PORT=5432      
          
    
 Then you must run the following command to build all the project containers:    
    
 $ make build    
Finally you should generate the initial Django migrations, for them execute the following command    
    
 $ make migrate    
## Run project    
 To run the project you must execute the following command    
    
 $ make up    
> If you have problems connecting Django with Postgres, you should run the command: make restart CONTAINER=django    
 ## Other commands    
    
 1. **Create a new app:** make startapp NAME=example    
 2. **Generate migrations:** make migrate    
 3. **Create a superuser:** make superuser  
  


## Sort packages in the requirements.txt file

First you need to add the package to the requirements.txt file, then you run the **make build** command.
Finally, so that the packages are ordered and with their version established in the requirements.txt file, you must execute the following command.

    $ make get-requirements

