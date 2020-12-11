# Image Scrapper

### Installation Instructions

Install these packages for setting up your environment if you don't have them installed.

- Python3.
- PostgreSQL.
- Node.js

### Setup Instructions

- Create a virtualenv, navigate to the `img_scrapper_backend` directory and run `pip install -r requirements.txt` command to install the packages.
- Create a .env file in the topmost `img_scrapper_backend` directory, copy the content of the `.env.example` file and paste in your .env file. Replace the values with your database values.
- Run database migrations with the `python manage.py migrate` command.
- Run `python3 scrapper_api/scrapper.py` command to scrap the data from the FormPlus features page and save them in your database.
- Navigate to the `SnapShot` directory, run `npm install` to install the dependencies.
- Run `npm start` to run the app. Open [http://localhost:3000](http://localhost:3000) to view the images in the browser.
