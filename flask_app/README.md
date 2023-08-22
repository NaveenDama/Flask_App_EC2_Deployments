# flask_app_EC2_deployment

To deploy the flask app using gunicorn + Nginx

First create or paste the file "flaskapp.service" (file avaialable in the project flak_app) [we can give any name to gunicorn service here we are using the flaskapp name in flaskapp.service]
inside "/etc/systemd/system/" path in EC2 or linux system.

After creating the file, execute
"sudo systemctl daemon-reload" -> To reload all the .service files in order to refresh the services in linux
then
"sudo service flaskapp restart" -> This command will create flaskapp.sock file in project directory ( here flaskapp is the gunicorn service name creaed in /etc/systemd/system folder.)

Now create the nginx config as present in "flask_app" file in "/etc/nginx/sites-enabled" folder
then execute
"sudo service nginx restart"

Then the requests are forwarded to "flaskapp.sock" file from nginx to flask app through gunicorn.

This will ensure that the flaskapp run in background as service.

**Note**: When we create the project under "/home/ubuntu" folder in EC2 the folder by default will not have execute permission,
            due to which nginx cannot bind with gunicorn and we will get "permission denied error" in nginx which can be check
            using "error.log" file of nginx present under "/var/log/nginx/" folder.

To overcome this "change the permissions of /home/ubuntu folder" using:
"sudo chmod 755 /home/ubuntu" in my case, which /home/<username> in your case.

After changing this restart nginx and gunicorn service using "sudo service <service-name> restart" command.

Now using the public ip address with "http://<public-ip>/path(in @app.route()) you can see the response from web app.





