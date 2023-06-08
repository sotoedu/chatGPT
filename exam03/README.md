# OpenAI API Quickstart - Python example app

This is an example pet name generator app used in the OpenAI API. It uses the [Flask](https://flask.palletsprojects.com/en/2.0.x/) web framework. Check out the tutorial or follow the instructions below to get set up.

## Setup

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/).

2. Navigate into the project directory:

   ```bash
   $ mkdir workspace
   $ cd workspace
   $ mkdir openai-web
   $ cd openai-web
   ```
   
3. Create a new virtual environment:

   ```bash
   $ python -m venv venv
   $ source venv/bin/activate
   ```

4. Clone this repository.
   ```bash
   $ git clone https://github.com/sotoedu/chatGPT.git
   $ cd chatGPT
   ```

5. Install the requirements:

   ```bash
   $ pip install -r requirements.txt
   ```

6. Make a copy of the example environment variables file:

   ```bash
   $ cp .env.example .env
   ```

7. Add your [API key](https://beta.openai.com/account/api-keys) to the newly created `.env` file.

   ```bash
   $ touch .env
   
   FLASK_APP=app
   FLASK_ENV=development

   # Once you add your API key below, make sure to not share it with anyone! The API key should remain private.
   OPENAI_API_KEY=
   ```

8. Run the app:

   ```bash
   $ flask run
   ```

You should now be able to access the app at [http://localhost:5000](http://localhost:5000)
