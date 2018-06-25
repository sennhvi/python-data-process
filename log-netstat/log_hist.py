#!/usr/bin/env python3
# encoding: utf-8

from urllib.request import urlopen
from urllib.request import HTTPError
from bs4 import BeautifulSoup
from sudo_exec import sudo_exec
import re, datetime


url_head = "http://www.ip138.com/ips138.asp?action=2&ip="
### get raw data from cli
tmp_list = str(sudo_exec('sudo netstat -antlup', 'wangsh92'))[2:-1].split('\\n')[2:]


def get_formatted_ip_list(raw_list):
    ip_list = []

    ### get header and content of netstat, like Proto, Recv-Q,etc.
    ### log_header = raw_list[0].strip('\\r').split()
    ### ip_list.append(log_header)

    ### format and filter meaningful ip address
    for raw_line in raw_list[1:-1]:
        process_line = raw_line.strip('\\r').split()
        try:
            if (re.match(r"\d+\.\d+\.\d+\.\d+\:\d+",process_line[4]) != None and
                    re.match(r"127\.0\.0\.1\:\d+", process_line[4]) == None and
                    re.match(r"0\.0\.0\.0", process_line[4]) == None and
                    process_line[6] != '-'):
                ip_list.append(process_line)
        except Exception as err:
            print(Exception, "in get_formatted_ip_list: " + err)
    return ip_list


def save_ip_list_to_file():
    ### initialize log filename
    log_date = datetime.date.today()

    log_hour = datetime.datetime.now().hour
    log_min = datetime.datetime.now().minute
    log_sec = datetime.datetime.now().second

    log_file = "/home/wangsenhui/log/" + '-'.join(("NETSTAT", "LOG", str(log_date),
            str(log_hour), str(log_min), str(log_sec))) + ".txt"

    ### write data into file
    try:
        with open(str(log_file), 'wt') as output_file:
            output_file.write(str(tmp_list[0].strip('\\r')) + "\n")
            for each_line in get_formatted_ip_list(tmp_list):
                output_file.write(str(each_line) + "\n")
    except Exception as err:
        print(Exception, "in save_ip_list_to_file: ", err)


def format_output_ip_address(input_list):
    print("Active Internet Connections[TCP]:")
    print("RQ::SQ::   LP::      State::Program::District")
    for ip_line in input_list:
        try:
            ### Print ip country in console
            print(" %s:: %s::%s::%s::%s::%s"
                    %(str(ip_line[1]), str(ip_line[2]), str(ip_line[3]).split(":", 2)[1],
                        str(ip_line[5]), str(ip_line[6]).split("/", 2)[1],
                        get_country(ip_line[4].split(":", 2)[0])))
        except Exception as err:
            print(Exception, "in format_output_ip_address: ", err)


def get_country(ip_address):
    url = url_head + ip_address
    try:
        html = urlopen(url).read().decode('gb2312')
    except HTTPError:
        return None

    try:
        bsObj = BeautifulSoup(html, "html.parser")
        try:
            response = bsObj.findAll(
                    text = re.compile("："))[0].split("：")[2]
        except IndexError:
            response = bsObj.findAll(
                    text = re.compile("数据"))[0:2]
    except AttributeError:
        return None
    return str(response)

if __name__ == '__main__':
    if_print = input("Do you want to save ip log?\n y/n: ").upper()
    if (if_print == 'Y'):
        save_ip_list_to_file()
    elif (if_print == 'N'):
        pass
    else:
        print("log will not be saved")
    ip_list = get_formatted_ip_list(tmp_list)
    format_output_ip_address(ip_list)

