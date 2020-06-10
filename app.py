import re
import requests
import docker


from pprint import pprint

log_format = '(?P<container>[\w\.\-]+)\s+\| (?P<host>[\w\.\-]+) (?P<remote_addr>[\d.]+) \- (?P<remote_user>[\w\.\-]+) ' \
             '\[(?P<local_time>.+)\] "(?P<method>[A-Z]+) (?P<request>[\w\.\-\/]+).+" ' \
             '(?P<status>\d{3}) (?P<bytes_sent>\d+) "(?P<http_referer>.+)" "(?P<http_user_agent>.+)"'

if __name__ == "__main__":


    # client = docker.from_env()
    # container = client.containers.get('local-nginx-proxy')

    # for line in container.logs(stream=True, follow=True):
    #     line = line.decode('utf-8')
    #     line = re.sub(r'\x1b\[[0-9;]*m', '', line)

    #     try:
    #         matches = re.match(log_format, line).groupdict()

    #     except Exception as e:
    #         pass
