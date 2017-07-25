#!/usrbin/env python3.5
import json
import fileinput
import sys
import os
import shutil


attributes = [
  ("hostname",                     lambda x: x['hostname']),
  ("hardware/model",               lambda x: x['hardware']['model']),
  ("location/longitude",           lambda x: x['location']['longitude']),
  ("location/latitude",            lambda x: x['location']['latitude']),
  ("location/altitude",            lambda x: x['location']['altitude']),
  ("location/zip",                 lambda x: x['location']['zip']),
  ("network/addresses/small",      lambda x: sorted(x['network']['addresses'], key = len)[0]),
  ("network/addresses/medium",     lambda x: sorted(x['network']['addresses'], key = len)[1]),
  ("network/addresses/long",       lambda x: sorted(x['network']['addresses'], key = len)[2]),
  ("flags/online",                 lambda x: 'true' if x['flags']['online'] else 'false'),
  ("flags/gateway",                lambda x: 'true' if x['flags']['gateway'] else 'false'),
  ("statistics/uptime",            lambda x: x['statistics']['uptime']),
  ("statistics/gateway",           lambda x: x['statistics']['gateway']),
  ("statistics/memory_usage",      lambda x: x['statistics']['memory_usage']),
  ("statistics/rootfs_usage",      lambda x: x['statistics']['rootfs_usage']),
  ("statistics/clients",           lambda x: x['statistics']['clients']),
  ("statistics/loadavg",           lambda x: x['statistics']['loadavg']),
  ("lastseen",                     lambda x: x['lastseen']),
  ("firstseen",                    lambda x: x['firstseen']),
  ("software/autoupdater/branch",  lambda x: x['software']['autoupdater']['branch']),
  ("software/autoupdater/enabled", lambda x: 'true' if x['software']['autoupdater']['enabled'] else 'false'),
  ("software/batman-adv/version",  lambda x: x['software']['batman-adv']['version']),
  ("software/firmware/base",       lambda x: x['software']['firmware']['base']),
  ("software/firmware/release",    lambda x: x['software']['firmware']['release']),
]

def write(filename, string):
  os.makedirs(os.path.dirname(filename), exist_ok=True)
  f = open(filename, 'w+', encoding="utf-8")
  f.write(string)
  f.close()

if __name__ == '__main__':
  shutil.rmtree('v0', ignore_errors=True)

  s = ''
  for line in fileinput.input(openhook=fileinput.hook_encoded("utf-8")):
    s += line
  jdata = json.loads(s)

  for node in jdata['nodes']:
    nodeinfo = node['nodeinfo']
    prefix = 'v0/' + nodeinfo['node_id'] + '/'
    for attr, func in attributes:
      try:
        write(prefix + attr, str(func(nodeinfo)))
      except KeyError:     # if an JSON attribute is'nt there, e.g. with missing coordinates
        pass
      except IndexError:   # if e.g. there are less than 3 IPv6 addresses
        pass
