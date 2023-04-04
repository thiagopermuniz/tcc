docker run -d \
  --name mongodb-container \
  -p 27017:27017 \
  --cpus=1 \
  --memory=2g \
  mongo:6.0.5