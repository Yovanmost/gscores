# Gscores Django Project

## Prerequisites

- Python 3.8+ installed
- pip installed
- postgres 17 installed and setup
- Node.js v22.19.0 (with package: http-server@14.1.1)
- (Optional) Virtualenv for isolated environment

## Setup Instructions

1. **Clone the repository**
   ```sh
   git clone https://github.com/Yovanmost/gscores.git
   cd gscores
   ```

2. **Create and activate a virtual environment (recommended)**
   ```sh
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```


4. **Set up environment variables**
   - Create a `.env` file in the project root  (follow `.env.example`).

5. **Create and Apply migrations**
   ```sh
   python manage.py makemigrations

   python manage.py migrate
   ```

6. **Seed the database**
   ```sh
   python manage.py seed_students dataset/diem_thi_thpt_2024.csv
   ```

7. **Run the development server**
   ```sh
   python manage.py runserver
   ```

8. **Access the app**
   - For Django backend: Open your browser and go to [http://127.0.0.1:8000/api](http://127.0.0.1:8000/api).
   - For static frontend: 
      1. Access the `gscores/templates/js/config.js` and replace the `API_BASE_URL` with `http://127.0.0.1:8000/api`

      2. Open `index.html` by serving it with a static server (e.g., [http-server](https://www.npmjs.com/package/http-server)):
     ```sh
     npx http-server templates
     ```
      3. There will be an url for FE like: [http://127.0.0.1:8080/](http://127.0.0.1:8080/) (or the port shown in your terminal).

      4. Put your FE url in `FRONTEND_URL` in the `.env` so that the API can be called the without CORS problem.

      5. Access the FE with the given url.

      

## Notes

- FE files are in `gscores/templates`
- Main app code is in `scores/`

