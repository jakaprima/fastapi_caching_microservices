# FastAPI Caching Microservice
## Setup Instructions
1. Clone repository
``` sh
git clone https://github.com/jakaprima/fastapi_caching_microservices.git
cd fastapi-cache-microservice
```

2. Install dependencies
Create and activate a virtual environment:

``` bash
python -m venv venv
source venv/bin/activate
```

Install the required packages:
``` bash
pip install -r requirements.txt
cp .env.example .env
```

3. Initialize the database
Before running the service, initialize the SQLite or Postgresql database with settings .env:

``` bash
DATABASE_URL=postgresql://postgres:postgres@localhost/alpino
```

4. Run the FastAPI Application
Start the FastAPI server using Uvicorn:

```bash
uvicorn app.main:app --reload
The service will be available at http://127.0.0.1:8000.
```

5. Run with Docker
To run the application in a Docker container:
Build the Docker image:

``` bash
docker build -t fastapi-cache-service .
Run the Docker container:
```bash
docker run -d -p 8000:8000 fastapi-cache-service
```

6. Testing
To run the unit tests, install pytest:
```bash
pip install pytest
```

Then, run the tests:

``` bash
pytest
```