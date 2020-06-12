import logging
import requests
from threading import Timer

from pprint import pprint


class AddressLocator(object):
    def __init__(self, url, waiting_interval = 60, fields=None):
        self.url = url
        self.waiting_interval = waiting_interval    # unit is seconds
        self.fields = fields
        self.ip_addresses = []
        self.timer = None
        self.timer_started = False

        # The IP locator API we are using has limitations on the number of requests
        # that can be performed in a given timeframe, stored in headers:
        # - X-Rl is how many requests left in a minute since the first request in that minute
        # - X-Ttl is how many seconds left before the minute-period gets restarted
        self.request_ttl = None
        self.request_rl = None

    def _locate_ips(self, batch=True):
        r = None

        try:
            if not self.ip_addresses:
                raise Exception('No IP address(es) provided.')

            if self.request_rl != None and self.request_rl < 1:
                self.request_rl = None  # Reset to let the timer start again
                raise Exception('No requests quota left for the time being. Time to wait is {} seconds.'
                                .format(self.request_ttl))

            if batch:
                r = requests.post(self.url.format(type='batch', fields=self.fields),
                    json=self.ip_addresses)

                # Raise an exception in case of a non-2xx status code
                r.raise_for_status()
            else:
                r = requests.get(self.url.format(type='json/' + self.ip_addresses,
                    fields=self.fields))

                # Raise an exception in case of a non-2xx status code
                r.raise_for_status()

        except Exception as e:
            logging.warning(e)

        else:
            # Clear last batch to let following batch fill-up
            self.ip_addresses.clear()
            self.request_ttl = int(r.headers['X-Ttl'])
            self.request_rl = int(r.headers['X-Rl'])

        finally:
            self.timer = None
            self.timer_started = False

        if r != None and r.status_code == requests.codes.ok:
            pprint(r.json())

    def accumulate(self, ip):
        """
        The locator API we are using has a limit on the number of requests that can
        be performed per second. We'll play it safe and accumulate IPs one by one
        during the period of one second then perform a batch request.
        """
        self.ip_addresses.append(ip)

        print(len(self.ip_addresses))

        if not self.timer_started:
            logging.debug('Timer started for {} seconds'.format(self.waiting_interval))

            self.timer = Timer(self.waiting_interval, self._locate_ips)
            self.timer.start()

            self.timer_started = True

