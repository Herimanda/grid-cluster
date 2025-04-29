#!/bin/bash
# Wait for MySQL to be ready
echo "Waiting for MySQL to be ready..."
while ! docker-compose exec mysql mysqladmin ping -h localhost -u root -prootpass --silent; do
  sleep 1
done

echo "MySQL is ready. Setting up permissions..."
# Execute SQL commands to grant permissions
docker-compose exec mysql mysql -u root -prootpass -e "
CREATE USER IF NOT EXISTS 'root'@'%' IDENTIFIED BY 'rootpass';
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;
"

echo "MySQL permissions setup complete!"