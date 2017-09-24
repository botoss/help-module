# -*- coding: utf-8 -*-
import sys
import os
sys.path.append(os.path.abspath(os.path.join('python-wrapper-lib')))
from kafka_wrapper_module import KafkaWrapperModule
from in_message import InMessage
from out_message import OutMessage

class HelpModuleHelper(KafkaWrapperModule):

    def __init__(self, ip, port, in_topic, out_topic, command_list):
        KafkaWrapperModule.__init__(self, ip, port, in_topic, out_topic, command_list)
        
    def handle_command(self, in_message):
        help_file_path = "/opt/help-module/help.txt"
        is_help_file_exists = self.process_help_file(help_file_path)
        text = "Hello from help-module (error :()"
        if is_help_file_exists:
            text = "To add your info edit the help file: " + help_file_path + "\n"
            text += self.read_help_file(help_file_path)
        out_message = OutMessage(
            key=in_message.key,
            connector_id=in_message.connector_id,
            text=text)
        return out_message

    def process_help_file(help_file_path):
        if os.path.exists(help_file_path) == False:
            try:
                makedirs(path.dirname(help_file_path))
                open(help_file_path, 'a').close()
            except Exception as e:
                print "Create help file error: " + help_file_path
                print e.message
                return False
        return True

    def read_help_file(help_file_path):
        text = "Error :("
        if os.path.exists(help_file_path):
            try:
                help_file = open(help_file_path, 'r')
                text = help_file.read()
            except Exception as e:
                print "Open help file error: " + help_file_path
                print e.message
        return text
