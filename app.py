import logging
import re
import requests
import docker

from addressLocator import AddressLocator
from utils import mock_generator


log_format = '(?P<container>[\w\.\-]+)\s+\| (?P<host>[\w\.\-]+) (?P<remote_addr>[\d.]+) \- (?P<remote_user>[\w\.\-]+) ' \
             '\[(?P<local_time>.+)\] "(?P<method>[A-Z]+) (?P<request>[\w\.\-\/]+).+" ' \
             '(?P<status>\d{3}) (?P<bytes_sent>\d+) "(?P<http_referer>.+)" "(?P<http_user_agent>.+)"'

url = 'http://ip-api.com/{type}?fields={fields}'
fields = 'status,message,country,regionName,city,lat,lon,offset,isp,org,proxy,hosting,query'



if __name__ == "__main__":

    logging.basicConfig(
        level = logging.INFO,
        format = "[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")

    locator = AddressLocator(url, 60, fields)

    # client = docker.from_env()
    # container = client.containers.get('local-nginx-proxy')

    # for line in container.logs(stream=True, follow=True):
    #     line = line.decode('utf-8')
    #     line = re.sub(r'\x1b\[[0-9;]*m', '', line)

    #     try:
    #         matches = re.match(log_format, line).groupdict()
    #         locator.accumulate(matches['remote_addr'])

    #     except KeyboardInterrupt as e:
    #         locator.timer.cancel()
    #         exit(0)
    #     except Exception as e:
    #         logging.warning('Following exception occurred: {}'.format(e))
    #         logging.warning('Did not manage to match this: \'{}\''.format(line))


    while True:
        try:
            locator.accumulate(mock_generator())

        except KeyboardInterrupt:
            locator.timer.cancel()
            exit(0)
