!!! IMPORTANT NOTE: The web-application ONLY WORKS ON PYTHON 3.12 !!! Else, the app will not be able to detect the flask / other dependecies in the project; and subsequently the app will not run. If you encounter this issue; open Visual Studio Code, hover oveer the 'missing' / undetected dependency(s) and choose 'Quick Fix'. Then, pick the 'Choose different interpeter' quick fix, and change to Python 3.12 interpreter (IF available). Else, you may have to resort to downloading this older version of Python. 

Continued: There IS a venv for this project (you can see the file yourself in the repo); however some frameworks were not installed within the environment. This is the reason why, if you choose the virtual environment, certain modules are available, but others arent (e.g reportlab modules). Thank you for your consideration; and apologies for the inconvenience. 

Recipe Finder and Generator Web Application
- A Flask-based web app to help MMU students find budget-friendly, easy-to-cook recipes based on available ingredients.

To set the project up on your personal device: 
1. Clone the repository
2. Create virtual environment (this is done in the terminal. For clarity, I did this in VSCode, but I believe you can perform this on any other IDE): `python -m venv venv`
3. Activate venv:
   - For Windows: `venv\Scripts\activate`
   - For Mac/Linux: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt` (basically every framework used in the project, as per listed below)
5. To run the app: `python app.py`


- Flask
- SQLAlchemy
- SQLite
- Bootstrap
- Spoonacular API
- ReportLab

