#!/usr/local/bin/python3.8

import re

# (?P<remote_user>.*)
log_format = '(?P<host>[\w\.\-]+) (?P<remote_addr>[\d.]+) \- (?P<remote_user>[\w\.\-]+) ' \
             '\[(?P<local_time>.+)\] "(?P<method>[A-Z]+) (?P<request>[\w\.\-\/]+).+" ' \
             '(?P<status>\d{3}) (?P<bytes_sent>\d+) "(?P<http_referer>.+)" "(?P<http_user_agent>.+)"'

if __name__ == "__main__":

    line = 'some.host.name 172.17.0.1 - - [09/Jun/2020:20:40:08 +0000] "GET /server-status?auto HTTP/1.1" 503 197 "-" "munin/2.0.37-1ubuntu0.1 (libwww-perl/6.31)"'

    m = re.match(log_format, line)
    parsed = m.groupdict()

    print(parsed)
