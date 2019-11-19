#!/usr/bin/env python3

from datetime import datetime

package_name = "main"


def log_generator(node_name, msg, log_type=None):
    if log_type == "pub":
        log_msg = pub_log_generator(node_name, msg)
    elif log_type == "sub":
        log_msg = sub_log_generator(node_name, msg)
    else:
        log_msg = general_log_generator(node_name, msg)
    return log_msg


def general_log_generator(node_name, str_msg):
    log_text = '[{}/{}][{}] {}'.format(package_name, node_name, time_generator(), str_msg)
    print(log_text)
    return log_text


def pub_log_generator(node_name, topic_name):
    str_msg = 'Publish to <{}> topic'.format(topic_name)
    log_text = '[{}/{}][{}][{}] {}'.format(package_name, node_name, "PUB", time_generator(), str_msg)
    print(log_text)
    return log_text


def sub_log_generator(node_name, topic_name):
    str_msg = 'Subscribe from <{}> topic'.format(topic_name)
    log_text = '[{}/{}][{}][{}] {}'.format(package_name, node_name, "SUB", time_generator(), str_msg)
    print(log_text)
    return log_text


def time_generator():
    return str(datetime.now()).replace(' ', '_')
