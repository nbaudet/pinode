"""Some functions to facilitate the use of management commands"""
import os
from uuid import getnode


class CommandUtils():
    """Some functions to facilitate the use of management commands"""
    def __init__(self, command):
        self.command = command

    def get_ip(self):
        """Return the first IP that 'hostname -I' command returns"""
        return os.popen('hostname -I').read().split(' ')[0]

    def get_mac(self):
        """Return the MAC address"""
        mac = getnode()
        return ':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))

    def write(self, val):
        """Write in the command output"""
        if val:
            self.command.stdout.write(val)
        else:
            self.command.stdout.write('no value given')

    def success(self, val):
        """Write successful in the command output"""
        if val:
            self.command.stdout.write(self.command.style.SUCCESS(val))
        else:
            self.command.stdout.write('no value given')

    def write_array(self, array):
        """Write an array in command output, each string item per line"""
        if array:
            for val in array:
                self.command.stdout.write(val)
        else:
            self.command.stdout.write('no value given')
