import os
import configparser
import psutil
import time
import json
from datetime import datetime


def createfileini(path):
    """ create *.ini file """
    config = configparser.ConfigParser()
    config.add_section('common')
    config.set('common', 'format', 'json')
    config.set('common', 'interval', '1')
    # config.set('common', 'count', '30')
    config.set('common', 'addr', 'Ethernet')
    config.set('common', 'stdout', 'True')
    with open(path, 'w') as configfile:
        config.write(configfile)
        print("File created")


def main():
    try:  # used try so that if user pressed other than the given key error will not be shown
        ccount = 0
        while True:  # making a loop
            m = Monitoring()
            time.sleep(int(readparam(ini_file, 'common', 'interval')))
            ccount += 1
            m.savetofile(ccount)
        #    break
    except KeyboardInterrupt:
        pass
        #            break  # if user pressed a key other than the given key the loop will break
    print('Loop ended.')


def readparam(path, section, key):
    """ read *.ini param """
    cfg = configparser.ConfigParser()
    cfg.read(path)
    return cfg.get(section, key)


class Monitoring(object):

    def __init__(self):
        """Constructor"""
        # , cpu, memory, vmemory, iostat, network
        self.cpu = 0

    def getcputime(self):
        return psutil.cpu_percent()

    def getmemory(self):
        return psutil.swap_memory()[0]

    def getvmemory(self):
        return psutil.virtual_memory()[0]

    def getio(self):
        sdiskio = psutil.disk_io_counters()
        value_dic = {
            'iostats': {
                'io.disks_read': sdiskio.read_bytes / (1024 * 1024),
                'io.disks_write': sdiskio.write_bytes / (1024 * 1024),
                'io.disks_read_count': sdiskio.read_count / (1024 * 1024),
                'io.disks_write_count': sdiskio.write_count / (1024 * 1024),
                'io.disks_read_time': sdiskio.read_time / 1000,
                'io.disks_write_time': sdiskio.write_time / 1000,
                'io.disks_busy_time': sdiskio.write_time / 1000,
            }
        }
        return value_dic['iostats']['io.disks_write_time']

    def getnet(self):
        network = psutil.net_io_counters(pernic=True)
        ifaces = psutil.net_if_addrs()
        networks = list()
        for k, v in ifaces.items():
            ip = v[0].address
            data = network[k]
            ifnet = dict()
            ifnet['ip'] = ip
            ifnet['iface'] = k
            ifnet['sent'] = '%.2fMB' % (data.bytes_sent / 1024 / 1024)
            ifnet['recv'] = '%.2fMB' % (data.bytes_recv / 1024 / 1024)
            networks.append(ifnet)
        return networks

    def getdatatxt(self, par):
        return 'SNAPSHOT{}:\t"{:%Y-%m-%d %H:%M:%S}":\tCPU:{:<5s}:\tMemory:{:<15s}:' \
               '\tVMemory:{:<15s}:\tIO:{:<10s}:NETStat{:<10s}\n'.format(par, datetime.now(),
                                                                        str(self.getcpuTime()),
                                                                        str(self.getmemory()),
                                                                        str(self.getvmemory()),
                                                                        str(self.getio()),
                                                                        str(self.getnet()))

    def getdatajson(self, par):
        outdata = {'SNAPSHOT': par, 'date': '{:%Y-%m-%d %H:%M:%S}'.format(datetime.now()),
                   'io_time': str(self.getio()),
                   'cpu': self.getcputime(), 'memory_utilization': str(self.getmemory()),
                   'virt_memory': str(self.getvmemory()), 'network': str(self.getnet())}
        # .strftime("%Y-%m-%d %H:%M:%S")

        return outdata

    def printall(self, data_str):
        """Print all info to stdout"""
        print(data_str)

    def savetofile(self, par):
        """save all info to file"""
        if readparam(ini_file, 'common', 'format') == 'json':
            with open('monit.' + readparam(ini_file, 'common', 'format'), 'a') as MyFile:
                json.dump(self.getdatajson(par), MyFile, indent=4)
        else:
            with open('monit.' + readparam(ini_file, 'common', 'format'), 'a') as MyFile:
                MyFile.write(self.getdatatxt(par))
                if readparam(ini_file, 'common', 'stdout') == 'True':
                    print(self.getdatatxt(par))
                else:
                    print('quiet mode: {} '.format(readparam(ini_file, 'common', 'stdout')))


if __name__ == "__main__":
    ini_file = "settings.ini"
    output_file = "monit.log"
    if not os.path.exists(ini_file):
        createfileini(ini_file)
    else:
        print("File exist")
    global ccount
    main()
