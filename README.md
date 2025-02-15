docker pull minedojo/minedojo:latest


docker run --gpus all -it -d -p 8080:8080 minedojo/minedojo:latest tail -f /dev/null

docker exec -it <running_container_id> /bin/bash

(in the container)

git clone https://github.com/tsereda/minedojo-scripts.git
cd minedojo-scripts
chmod +x fix-minedojo.sh
sudo ./fix-minedojo.sh
python validate_script.py
