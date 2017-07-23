# -*- coding: utf-8 -*-
import sys
import os
sys.path.append(os.path.abspath(os.path.join('..', 'python-wrapper-lib')))
from kafka_wrapper_module import KafkaWrapperModule
sys.path.append(os.path.abspath(os.path.join('..', 'python-wrapper-lib')))
from in_message import InMessage
from out_message import OutMessage

class HelpModuleHelper(KafkaWrapperModule):

    def __init__(self, ip, port, in_topic, out_topic, command_list):
        KafkaWrapperModule.__init__(self, ip, port, in_topic, out_topic, command_list)
        
    def handle_command(self, in_message):
        text = "А ничего и нету :("
        out_message = OutMessage(
            key=in_message.key,
            connector_id=in_message.connector_id,
            text=text)
        return out_message
