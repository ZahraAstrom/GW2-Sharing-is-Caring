# GW2-Sharing-is-Caring

## Setup

Install dependencies with

`poetry install`

Start the API with

`poetry run uvicorn GW2_Sharing_is_Caring.main:app --reload`

set DB_URI locally to

`postgresql+psycopg2://myuser:secret@127.0.0.1:5432/mydatabase`