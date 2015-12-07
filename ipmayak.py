#!/usr/bin/env python

import csv
import datetime
import sys
import urllib

fieldnames = ['timestamp', 'ip']
filename = sys.argv[1]
lookup_url = 'http://icanhazip.com/'

def create_csv(filename):
  """
  Creates a CSV file at the desired location with a custom file name

  :type filename: str
  :param filename: File name to create
  """

  with open(filename, 'wb') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

def fetch_current_ip_address(url):
  """
  Fetches the external IP address from URL
  Note that the website has to return a very basic IP address
  Tested with "http://icanhazip.com/"

  TODO: Replace with `ipgetter <https://github.com/phoemur/ipgetter/>`_
        for a more robust solution

  :type url: str
  :param url: URL to fetch IP address from

  :rtype: str
  :return: Trimmer IP address
  """

  return urllib.urlopen(url).read().strip()

def read_latest_ip_address(filename):
  """
  Gets the latest IP address from the CSV file
  Creates the file if it does not exist
  Reads the IP as the second item from the last comma-delimited row

  :type filename: str
  :param filename: File name to read

  :rtype: str
  :return: Trimmed IP address
  """

  try:
    with open(filename, 'rb') as csvfile:
      content = csvfile.readlines()

      return content[-1].split(',')[1].strip()

  except (IndexError, IOError):
    create_csv(filename)

def set_current_ip_address(filename, ip_address):
  """
  Writes a timestamped IP address to the CSV file

  :type filename: str
  :param filename: File name to read

  :type ip_address: str
  :param ip_address: Trimmer IP address
  """

  with open(filename, 'a+') as csvfile:
    iso_time = datetime.datetime.now().isoformat()

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writerow({'timestamp': iso_time, 'ip': ip_address})

current_ip_address = fetch_current_ip_address(lookup_url)
latest_ip_address = read_latest_ip_address(filename)

if (current_ip_address != latest_ip_address):
  set_current_ip_address(filename, current_ip_address)
