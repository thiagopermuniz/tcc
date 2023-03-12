docker run -d \
  --name mysql-container \
  -e MYSQL_ALLOW_EMPTY_PASSWORD=yes \
  -e MYSQL_DATABASE=base-tcc \
  -e MYSQL_USER=usuario \
  -v mysql-data:/var/lib/mysql \
  -p 3306:3306 \
  --cpus=1 \
  --memory=2g \
  mysql:latest