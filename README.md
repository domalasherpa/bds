# Bird Detection App

This is a Bird Detection application that allows users to upload bird images and automatically get identification using an object detection model (YOLOv1). The app is built as a final project for the partial fulfillment of a Bachelor's in Computer Science and Information Technology.

The system uses YOLOv1 for real-time object detection and inference. The frontend is developed with Nuxt.js, and the backend API for model inference is powered by FastAPI.

## Tech Stack

- **Frontend:** Nuxt.js (Vue.js framework)
- **Backend:** FastAPI
- **Model:** YOLOv1 for object detection
- **Database:** SQLite and drizzle-orm
- **Authentication:** nuxt-auth-utils for authentication and password hashing

## Prerequisites

Before starting the setup, ensure you have the following installed:

- **Python 3.x** (preferably 3.8 or higher)
- **pnpm** (for nuxt package installation)
- **pip** (for Python package installation)
- **git** (for cloning the repository)

---

## Setup Instructions

Follow the steps below to set up the project on your local machine.

### 1. Clone the Repository

Start by cloning the repository to your local machine:

```bash
git clone https://github.com/yourusername/bird-detection-app.git
cd bird-detection-app
```
### 2. Install Required packages

```bash
cd frontend
pnpm install
```


```bash
cd ../backend
pip install -r requirements.txt
```

### 3. Run the FastApi service
Make sure you have your model file inside backend folder.Then, Run the fast api service

```bash
uvicorn main:app --reload
```
### 4. Run the frontend
Open new terminal. Make sure you are inside frontend folder
```bash
pnpm dev
```


There you go!!!. you can access the system from browser at "http://localhost:3000" or as per your setup. Rest the api handles all.. ENJOY!!!!

