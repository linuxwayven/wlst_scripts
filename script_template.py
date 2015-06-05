################################ DESCRIPTION ##################################
# Description: <Put Script Description here>.
#  
# Author: <Put Author Name here>. - <Put Author Email here>. 
# Place: <Put City here> - <Put Country here> - <Put Company here>
# Date: <Put Date here>
# 
# History
# <Put Date here>	The Begin						V1.0
#
#  Quota: The Key to grown: Hard work.
#  
###############################################################################

# Import Section
import socket
import os
import time

from com.bea.wli.sb.management.configuration import ALSBConfigurationMBean
from com.bea.wli.config import Ref
from java.lang import String
from com.bea.wli.config import Ref
from com.bea.wli.sb.util import Refs
from com.bea.wli.sb.management.configuration import CommonServiceConfigurationMBean
from com.bea.wli.sb.management.configuration import SessionManagementMBean
from com.bea.wli.sb.management.configuration import ProxyServiceConfigurationMBean
from com.bea.wli.monitoring import StatisticType
from com.bea.wli.monitoring import ServiceDomainMBean
from com.bea.wli.monitoring import ServiceResourceStatistic
from com.bea.wli.monitoring import StatisticValue
from com.bea.wli.monitoring import ResourceType

from weblogic.management.mbeanservers.edit import NotEditorException

# Set some constants
SCRIPT_NAME = '<Put Script Name here>'
DESCRIPTION = '<Put Script Description here>.'
AUTHOR = '<Put Author Name here>. - <Put Author Email here>.'

WL_USERNAME = '****'
WL_PASSWORD = '****'

RUN_USERNAME = os.getlogin()
LOCALHOST = socket.gethostname()
DOMAIN_NAME = os.getenv('WL_DOMAIN')
DOMAIN_PORT = '22011'
DOMAIN_DIR = os.getenv('WL_DOMAIN_DIR')
MWHOME = os.getenv('MW_HOME')
URL_CONNECT ='t3://' + LOCALHOST + ':' + DOMAIN_PORT

ACTUAL_TIME = time.strftime("%H:%M:%S")
ACTUAL_DATE = time.strftime("%d/%m/%Y")
 
# Information Screen
print '#########################################################################'
print '#'
print '#  DATE:           ' + ACTUAL_DATE
print '#  TIME:           ' + ACTUAL_TIME
print '#  MW HOME:        ' + MWHOME
print '#  SCRIPT NAME:    ' + SCRIPT_NAME
print '#  DESCRIPTION:    ' + DESCRIPTION
print '#  URL CONNECTION: ' + URL_CONNECT
print '#'  
print '#  AUTHOR:         ' + AUTHOR
print '#'
print '#########################################################################'
print
print

# Connect with WL Server..
print 'Try connection ..'
print
connect(WL_USERNAME, WL_PASSWORD, URL_CONNECT)

print
print
# Main
print 'Hello World of Webglogic Scripting!!'





print
print
print
# Disconnect from Server..
print 'Disconnecting from Server ..'
disconnect()
# The End
print
print 'Exiting from the script now ..'
exit()
