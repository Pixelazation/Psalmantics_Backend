# Psalmantics Backend

Backend API for Psalmantics that fetches Bible verses and supports TF-IDF based search.

---

## Prerequisites

- Python 3.12 (or compatible version)  
- Git  

---

## Setup Instructions

1. **Clone the repository**

    `git clone https://github.com/Pixelazation/Psalmantics_Backend`
    `cd Psalmantics_Backend`

2. **Create and activate a virtual environment**

    `python -m venv venv`

- On macOS/Linux:

    `source venv/bin/activate`

- On Windows Git Bash:

    `source venv/Scripts/activate`

You should see `(venv)` appear in your terminal

3. **Install dependencies**

    `pip install -r requirements.txt`

4. **Run the API server**

    `uvicorn main:app --reload`

5. **Open the API docs**

Open your browser and navigate to:

    http://127.0.0.1:8000/docs

to see the interactive Swagger UI documentation.

6. **Deactivate venv if done working for the day**

    `deactivate`

You should see `(venv)` disappear from your terminal

---

## Project Structure

    ├── app/
    │   ├── api_client.py    # Bible API fetch logic
    │   ├── tfidf.py         # TF-IDF and vector space model functions
    │   └── routes.py        # API route definitions
    ├── data/                # Cached verse data (optional)
    ├── main.py              # FastAPI app entry point
    ├── requirements.txt     # Python dependencies
    └── README.md            # This file

---

## Notes

- Remember to activate the virtual environment **every time** before running the API.  
- If you add any new Python packages, run `pip freeze > requirements.txt` to update dependencies.  
- Feel free to reach out if you encounter any issues during setup.

---
