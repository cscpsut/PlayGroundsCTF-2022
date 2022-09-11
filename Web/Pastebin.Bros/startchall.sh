docker rm /hastebin
docker run --name hastebin -d -p 7777:7777 -e STORAGE_TYPE=file -v /data:/app/data rlister/hastebin
