# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate

# build docker image
docker compose build
docker compose up