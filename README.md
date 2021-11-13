# Bell_tech_interview_rest_service
  
## Reasons behing the architecture & API choices:
For this interview project, I decided to go with Python, a coding language of choice as it is one of my favourite. I find Python to be very straight forward and easy to use. As for the framework to implement the API, I used the Flask web framework. Not really a reason why I chose Flask over Django, just thought it would be easier for rapid development. I used the flask_restful library to implement my REST API to query data from the csv.   

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

## Other comments and messages:  
For the pagination, I wanted to use Flask built in pagination along with SQLAlchemy. But, since I couldn't make a database and the pagination library only supports for database querying, I wasn't able to use it. Therefore, I came up with my own solution by separating the pages by myself. I added some comments on the code, hope it helps!
