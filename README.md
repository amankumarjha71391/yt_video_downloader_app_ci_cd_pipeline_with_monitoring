# Project Name

FastAPI project which allows users to download YouTube videos.
python_project/
│
├── backend/
│   ├── main.py
│   ├── downloads/
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── venv/
│
├── requirements.txt
└── README.md

## Technologies Used

- **Backend**: Python, FastAPI, yt-dlp
- **Frontend**: HTML, CSS, JavaScript

## Setup Instructions

### Prerequisites
- Python 3.x
- FastAPI
- yt-dlp
- Uvicorn
- Node.js (for frontend if applicable)
- Any other dependencies specified in `requirements.txt`

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/your-repo.git
    ```

2. Navigate to the project folder:
    ```bash
    cd python_project
    ```

3. Set up a virtual environment (for backend):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

4. Install the required dependencies for the backend:
    ```bash
    pip install -r requirements.txt
    ```

5. For the frontend (if applicable):
    - Navigate to the `frontend` folder.
    - Install the required dependencies:
    ```bash
    npm install
    ```

### Running the Backend

To start the FastAPI backend:
```bash
uvicorn backend.main:app --reload

