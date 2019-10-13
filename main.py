#!/usr/bin/python3

import datetime
import json
import os
import xml.etree.ElementTree as ET


def parse_time():
    '''
    Func to easily parse time
    '''
    dt_now = datetime.datetime.now()

    parser = {
        'year': str(dt_now.year),
        'month': str(dt_now.month),
        'day': str(dt_now.day),
        'year': str(dt_now.year),
        'minute': str(dt_now.minute),
        'second': str(dt_now.second)
    }

    return parser

def make_main_file(backgrounds_dir, conf_file):
    '''
    Create main configuration file if missing
    '''
    dt_now = parse_time()

    background = ET.Element('background')
    starttime = ET.SubElement(background, 'starttime')
    ET.SubElement(starttime, 'year').text = dt_now['year']
    ET.SubElement(starttime, 'month').text = dt_now['month']
    ET.SubElement(starttime, 'day').text = dt_now['day']
    ET.SubElement(starttime, 'year').text = dt_now['year']
    ET.SubElement(starttime, 'minute').text = dt_now['minute']
    ET.SubElement(starttime, 'second').text = dt_now['second']

    # create dir
    if not os.path.exists(backgrounds_dir):
        os.mkdir(backgrounds_dir)

    tree = ET.ElementTree(background)

    tree.write(conf_file)


def diff_tree(backgrounds_dir, tree):

    conf_file_root = tree.getroot()

    img_exts = {
        '.jpeg', '.jpg', '.png'
    }

    backgrounds = [
        el for el in os.listdir(backgrounds_dir)
        if el[el.rfind('.'):] in img_exts
    ]

    to_add = []

    # for bg in backgrounds:


def write_conf(backgrounds, tree):

    conf_file_root = background



def main():

    with open('settings.json') as f:
        settings = json.load(f)

    home = os.environ['HOME']

    backgrounds_dir = os.path.join(home, settings['backgrounds_dir'])
    conf_file = os.path.join(backgrounds_dir, settings['conf_file'])

    if not os.path.exists(os.path.join(backgrounds_dir, conf_file)):
        make_main_file(backgrounds_dir, conf_file)
    else:
        tree = ET.ElementTree(file=conf_file)
        diff_tree(backgrounds_dir, tree)



if __name__ == '__main__':
    main()
