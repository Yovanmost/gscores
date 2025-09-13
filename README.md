# Gscores Django Project

## Prerequisites

- Python 3.8+ installed
- pip installed
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
   - Open your browser and go to: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Notes

- Static files are in `scores/static/scores/`
- Templates are in `scores/templates/scores/`
- Main app code is in `scores/`

