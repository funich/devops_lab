#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psutil
try:
    import configparser
except:
    from six.moves import configparser

import sys
# import time
from getopt import getopt, GetoptError

config = configparser.ConfigParser()
config.sections()
config.read('monitoring.ini')
print(config.sections())


class Monit(object):
    """docstring"""
    def __init__(self):
        """Constructor"""
# , cpu, memory, vmemory, iostat, network
        self.cpu = 0
        self.memory = 0
        self.vmemory = 0

    def get_cpu(self):
        """
        get cpu use
        """
        return psutil.cpu_percent(interval=1, percpu=True)
# for x in range(1):

    def get_loadavg(self):
        """
        get loadavg
        """
        return psutil.getloadavg()

    def get_memory(self):
        """
        get mem
        """
        return psutil.swap_memory()

    def get_vmemory(self):
        """
        get virtual mem
        """
        return psutil.virtual_memory()

    def get_iostats(self):
        """
        get virtual mem
        """
        return psutil.disk_io_counters(perdisk=True)

    def get_if_stats(self):
        """
        get ifstats
        """
        return psutil.net_if_stats()


def usage():
    print("Usage: monitoring.py [-a] [-f] [-h]")
    print("\t-a\tall")
    print("\t-f\tfile")
    print("\t-h\tDisplay this help and exit")
    sys.exit(0)


def main(argv):
    print('ARGV      :', sys.argv[1:])
    try:
        opts, args = getopt(argv, "afh")
        if not opts:
            get_data = Monit()
            print(get_data.get_cpu())
            print(get_data.get_loadavg())
            print(get_data.get_memory())
            print(get_data.get_vmemory())
            print(get_data.get_iostats())
            print(get_data.get_if_stats())
        for opt, arg in opts:
            if (opt == "-h") or (opt == "--help"):
                usage()
            elif opt in "-a":
                S_ACTIVE = True
            elif opt in "-f":
                ALL_VMS = True
    except GetoptError:
        usage()


if __name__ == "__main__":
    main(sys.argv[1:])
