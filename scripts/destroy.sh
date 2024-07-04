# deactivate virtual environment
deactivate

# stop and remove containers
docker stop deepchecks_logger deepchecks_db
docker rm deepchecks_logger deepchecks_db