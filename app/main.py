
from fastapi import FastAPI
from models import Jobs
from logs.logging import logger

app = FastAPI()


@app.get("/")
def root():
    response = {"Status Code": 200}
    return response

@app.post("/jobs")
def jobs(job: Jobs):
    job_title = job.title + "hello bhi elel"
    logger.info(f"Job Title: {job_title}")  
    logger.error(f"Error: {job_title}")  
    return job_title


if __name__=='__main__':
    import uvicorn
    uvicorn.run(app="app:app", host="0.0.0.0", port=8090, reload=True)