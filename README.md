# rest_service

Developed a REST service simulation to retrieve the top 10 TV shows by provider from a server (csv file) using pagination technology. 

## Steps to run the API from Windows:
1- Open command prompt at the location of the python script and the csv file.  

2- Make sure to install the python requirements before testing the API. Run the command "pip install -r Requirements.txt".  

3- Then, run "python main.py". This should start the API.  

4- When the API has successfully been started, open Postman. You can use whatever app you want.  

5- In Postman, create a new workspace. Then, you should be able to start testing. Make sure to select the GET request on the dropdown.  

6- To grab the top 10 shows from the "server" from a certain provider (for example: ATN), type "http://127.0.0.1:5000/shows/ATN" and press send.  

7- You shall then see the top 10 shows from the server, ordered in alphabetical order by title.  

8- If you want to see the top 10 shows by page, try and type "http://127.0.0.1:5000/shows/ATN/1". This should show you the first page of the top 10 shows.  

9- One page would contain maximum 4 shows listed. If you wish to see other top shows, navigate to page 2 by changing 1 to 2 at the end of the url.

10- You can test with other provider as well.  

11- I also created a test.py script so that you can run it and test it. Make sure to run it after the API has been started. Make sure to install requests by doing "pip install requests".

