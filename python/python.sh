docker run --name python_container \
    --cpus=2 \
    --memory=2g \
    -v /mongodb:/app/mongodb \
    -v /mysql:/app/mysql \
    python:latest 