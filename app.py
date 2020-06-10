import re
import requests
import docker


from pprint import pprint

log_format = '(?P<container>[\w\.\-]+)\s+\| (?P<host>[\w\.\-]+) (?P<remote_addr>[\d.]+) \- (?P<remote_user>[\w\.\-]+) ' \
             '\[(?P<local_time>.+)\] "(?P<method>[A-Z]+) (?P<request>[\w\.\-\/]+).+" ' \
             '(?P<status>\d{3}) (?P<bytes_sent>\d+) "(?P<http_referer>.+)" "(?P<http_user_agent>.+)"'

url = 'http://ip-api.com/{type}?fields={fields}'
fields = 'status,message,country,regionName,city,lat,lon,offset,isp,org,proxy,hosting,query'

def get_ip_data(ip, url, batch=True, fields=None):
    if not ip:
        return

    if batch:
        r = requests.post(
            url.format(type='batch', fields=fields),
            json = ip)

    else:
        r = requests.get(
            url.format(type='json/' + ip, fields=fields)
        )

    if r and r.status_code == requests.codes.ok:
        return r.json()



if __name__ == "__main__":

    pprint(get_ip_data(["208.80.152.201", "8.8.8.8", "24.48.0.1"], url, fields = fields))
    # pprint(get_ip_data("208.80.152.201", url, fields = fields, batch = False))

    # client = docker.from_env()
    # container = client.containers.get('local-nginx-proxy')

    # for line in container.logs(stream=True, follow=True):
    #     line = line.decode('utf-8')
    #     line = re.sub(r'\x1b\[[0-9;]*m', '', line)

    #     try:
    #         matches = re.match(log_format, line).groupdict()

    #     except Exception as e:
    #         pass
