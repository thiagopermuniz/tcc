docker run --name mysql-container \
  -e MYSQL_ALLOW_EMPTY_PASSWORD=yes \
  -e MYSQL_USER=usuario \
  -e MYSQL_DATABASE=mysqldb \
  --cpus=1 \
  --memory=2g \
  -p 3306:3306 \
  -v /home/thiago/projects/tcc/mysql/init.sql:/docker-entrypoint-initdb.d/init.sql \
  mysql:5.7 