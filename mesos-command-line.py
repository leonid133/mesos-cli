import argparse
from cli import MesosHttpClient
import ConfigParser

def list(args):
    print('List active frameworks id:')

    host = ConfigSectionMap("Mesos")['host']
    port = ConfigSectionMap("Mesos")['port']
    server_address = ':'.join([host.rstrip('/'), port])
    #print server_address
    client = MesosHttpClient(server=server_address)
    request = client.list_active_frameworks()

    if request:
        for framework in request:
            print framework['id']
    else:
        print "Not active frameworks"

def kill(args):
    print('Kill framework by id, {0}!'.format(args.id))
    host = ConfigSectionMap("Mesos")['host']
    port = ConfigSectionMap("Mesos")['port']
    server_address = ':'.join([host.rstrip('/'), port])
    client = MesosHttpClient(server=server_address)
    client.kill_framework_by_id(args.id)

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

list_parser = subparsers.add_parser('list')
list_parser.set_defaults(func=list)

kill_parser = subparsers.add_parser('kill')
kill_parser.add_argument('id')
kill_parser.set_defaults(func=kill)

def ConfigSectionMap(section):
    config = ConfigParser.ConfigParser()
    config.readfp(open('mesos_config.cfg'))
    dict1 = {}
    options = config.options(section)
    for option in options:
        try:
            dict1[option] = config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1

if __name__ == '__main__':
    args = parser.parse_args()
    args.func(args)

