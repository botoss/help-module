#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import getopt
import os
sys.path.append(os.path.abspath(os.path.join('.')))
from help_module_handler import HelpModuleHelper

def print_help():
    print 'help_module.py --ip=127.0.0.1 --port=9092 --in_topic=test-in --out_topic=test-out --command_list=help,помощь'

def main(argv):
    ip = '127.0.0.1'
    port = 9092
    in_topic = 'test-in'
    out_topic = 'test-out'
    command_list = []

    try:
        opts, args = getopt.getopt(argv, "h", ["ip=", "port=", "in_topic=", "out_topic=", "command_list="])
        
        for opt, arg in opts:
            if opt == '-h':
                print_help()
                sys.exit()
            elif opt in ("--ip"):
                ip = arg
            elif opt in ("--port"):
                port = arg
            elif opt in ("--in_topic"):
                in_topic = arg
            elif opt in ("--out_topic"):
                out_topic = arg
            elif opt in ("--command_list"):
                command_list = arg.split(',')
    except getopt.GetoptError:
        print_help()
        sys.exit(2)

    print('===============================================================================')
    print('Input args')
    print('ip', ip)
    print('port', port)
    print('in_topic', in_topic)
    print('out_topic', out_topic)
    print('command_list', command_list)
    print('===============================================================================')

    helpModuleHelper = HelpModuleHelper(
        ip=ip,
        port=port,
        in_topic=in_topic,
        out_topic=out_topic,
        command_list=command_list
    )

    helpModuleHelper.start()

if __name__ == "__main__":
    main(sys.argv[1:])
