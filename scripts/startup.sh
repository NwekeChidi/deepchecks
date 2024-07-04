# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate

# build docker image
docker compose up -d deepchecks_db
docker compose build
docker compose up