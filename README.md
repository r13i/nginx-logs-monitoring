# nginx-logs-monitoring
Service to read logs from a (dockerized) NGINX reverse proxy and store data into a time-series database for monitoring.

## Development Process

WIP.

### Getting a local NginX environment

Since this project aims at parsing and monitoring logs from a dockerized Nginx proxy instance, we
will create a local environment with a minimal docker container based on the _de facto_ standard
[nginx-proxy from JWilder](https://github.com/nginx-proxy/nginx-proxy).

To start this container, run:
```bash
docker run --rm \
    --name local-nginx-proxy \
    -p 80:80 \
    -v /var/run/docker.sock:/tmp/docker.sock:ro \
    jwilder/nginx-proxy

# You can add --detach to run the container in detached mode (to free up your terminal)
```


### Parsing Logs

What format we base on:
```
$host $remote_addr - $remote_user [$time_local] "$request" $status $body_bytes_sent "$http_referer" "$http_user_agent"
```

## References

- [xtimon/nginxparser](https://github.com/xtimon/nginxparser)
