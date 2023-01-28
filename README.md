## About The Project

An upcoming REST API that gives details like State, Country, IRS SOI Code, Longitude/Latitude & more from a given ZIP code. Built using Python, Flask & PostgreSQL.

## Development
Here's how to set this project up for development purposes.

### Prerequisites
You will need Python and PostgreSQL installed:

* Python
  ```sh
  sudo apt install python3.10

* PostgreSQL
  ```sh
  sudo apt install postgresql postgresql-contrib 

Ensure that the PostgreSQL service is started:
* Start PostgreSQL Service
  ```sh
  sudo service postgresql restart

### Setup
Use `python3 -V` and `psql -V` to verify that both Python and PostgreSQL are setup properly. 

1. Clone this repository:
   ```sh
   git clone https://github.com/Afrokk/soy.rest
   ```
  The repository already comes with a virtual environment `vEnv` which you can use. 

2. Activate the virtual environment using: 
    ```sh
    source <yourRootPath>/soy.rest/vEnv/bin/activate
    ```
    In my case, this was:
    ```sh
    source /home/afrokk/Projects/soy.rest/vEnv/bin/activate
    ```

    This will activate the virtual environment. 

3. Install the required dependencies:

    Once you are in the virtual environment, run
    ```sh
    pip3 install -r requirements.txt
    ```
    This will install all the required dependencies.
  
4. Create a blank PostgreSQL database by running the following commands:
    ```sh
    sudo -iu postgres psql
    ```

    Create a database:
    ```sql
    CREATE DATABASE state_data;
    ```

    Create a user for your database:
    ```sql
    CREATE USER <yourUsername> WITH PASSWORD 'yourPassword';
    ```

    Grant the user permissions to the database:
    ```sql
    GRANT ALL PRIVILEGES ON DATABASE state_data TO <yourUsername>;
    ```

    Verify everything was created successfully:
    ```sh
    \l
    ```
    The `\l` command should display a list of databases on your system, and should include the database called `state_data` we created above.

    Exit from psql:
    ```sh
    \q
    ```

5. Import the dataset into your database:
    ```sh
    psql -U afrokk state_data < dataset.pgsql
    ```
    After this, your database is all setup!

6. Start the application:

    Setup environment variables:
    ```sh
    export DB_USERNAME=<yourUsername>
    export DB_PASSWORD='<yourPassword>'
    ```
    The `username` and `password` should be the same as ones you setup in step 4. After this, run

    ```sh
    flask --app api run
    ```
    If the above command gives a `flask: command not found` error, run this instead:
    ```sh
    python3 -m flask --app api run
    ```
    This will start the application with everything setup as needed.

Note: If you are encountering issues with `app.py` warning about libraries not found, you need to select the Python interpreter for the `vEnv` virtual environment. You can do so by pressing `Ctrl+Shift+P` and selecting `Python: Select Interpreter` in VSCode. Then, select `Enter interpreter path` and give it the path to `python3.10` file located in `vEnv/bin/`. Read more about this [here](https://code.visualstudio.com/docs/python/environments#_using-the-create-environment-command).

## To-Do
Some of the things I'd like to do with this project, as I work on it:

- [x] Gather necessary data and clean it up.
- [x] Setup database.
- [x] Code the API. (IN PROGESS)
- [x] Add JSON functionality and setup routes. COMPLETED.

## Contact
If you have any feedback or need help, please reach out to me:

Afrasiyab (Afrokk) Khan - [@afrokk_](https://www.instagram.com/afrokk_/) - [afrokk.design](https://afrokk.design/) - [afrokk.dev](https://afrokk.dev/) - [LinkedIn](https://www.linkedin.com/in/afrasiyab-k/) - afrasiyabkhan379@gmail.com
