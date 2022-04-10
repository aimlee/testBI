
<!-- ABOUT THE PROJECT -->
## About The Project

Данная статья предназначена для практического ознакомления со стеком технологий используемых для разработки на Python в управлении инфраструктуры компании.


<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python](https://www.python.org/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [SQLite](https://www.sqlite.org/)

<p align="right">(<a href="#top">back to top</a>)</p>





### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/aimlee/testBI.git
   ```
2. Install Virtual Environment
   ```sh
   virutual venv
   ```
3. Install libraries
    ```sh
    pip install fastapi sqlite requests "uvicorn[standard]"
    ```


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Application is in following structures:

*First applcation: app1
*Second application: app2
*The application to store the application: dbapp
*The application that store and check status in every some seconds: main


Because it is written in Fast API and to demonstrate that every application is different, I strongly recomment you to run API server in different ports:
for example:
uvicorn app1:app --host 0.0.0.0 --port 8080    
uvicorn app2:app --host 0.0.0.0 --port 8081    
uvicorn dbapp:app --host 0.0.0.0 --port 8000

After running all applications:
1) It is better to start with creating a DB for the app, using get http://0.0.0.0:8000/create
2) Let us store application 1 and application 2 in our DB using following request http://0.0.0.0:8000/addapp1db and http://0.0.0.0:8000/addapp2db
3) Using virtual env run the main app, which includes some algrotihm that calls the function from dbapp that checks the status of each Application source in every several seconds

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Ali Kurban- [@kurlyli](https://instagram.com/kurlyli) - kurban.lee@gmail.com

Project Link: [https://github.com/aimlee/testBI](https://github.com/aimlee/testBI)

<p align="right">(<a href="#top">back to top</a>)</p>



