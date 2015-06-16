################################ DESCRIPTION ##################################
# Description:  List ALL Services deployed in OSB Domain with Regular Expression
#               Match.
#
# Author: Jesus A. Ruiz - linuxwayven@gmail.com
# Place: Caracas - Venezuela - Oracle de Venezuela
# Date: 16/06/15
#
# History
# 16/06/15      The Begin                                               V1.0
#
#  Quota: The Key to grown: Hard work.
#
###############################################################################

# Import Section
import socket
import os
import time
import re #Regular Expression Package

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

from java.io import FileInputStream

PROP_FILE_NAME = "weblogic.properties"

def loadProperties ():
        # Read Properties File
        propInputStream = FileInputStream(PROP_FILE_NAME)
        configProps = Properties()
        configProps.load(propInputStream)
        print 'Properties File Loaded'
        return configProps;

# Load Configuration Properties
configuration = loadProperties();


# Set some constants
SCRIPT_NAME = 'get_osb_services_list_filtered_re.py'
DESCRIPTION = 'List ALL Services deployed in OSB Domain with Regular Expression Match.'
AUTHOR = 'Jesus A. Ruiz - linuxwayven@gmail.com'

WL_USERNAME = configuration.get("admin.username")
WL_PASSWORD = configuration.get("admin.password")

DOMAIN_PORT = configuration.get("domain.port")

RUN_USERNAME = os.getlogin()
LOCALHOST = socket.gethostname()
DOMAIN_NAME = os.getenv('WL_DOMAIN')
DOMAIN_DIR = os.getenv('WL_DOMAIN_DIR')
MWHOME = os.getenv('MW_HOME')

URL_CONNECT = configuration.get("domain.protocol") + '://' + LOCALHOST + ':' + DOMAIN_PORT
print "URL CONNECT" + URL_CONNECT

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

### Get the Configuration Manager
cfgManager = getConfigManager()
try:
   cfgManager.getChanges()
   print '===> Currently there is a Session'
   if cfgManager.isEditor() == true:
       ### You are making changes!!!
       print '===> Looks like you started that session'
       print '===> You can check the console for any pending changes'
       print '===> Try rerunning this script after you release or commit the pending changes'
   exit()

except NotEditorException, e:
   if cfgManager.getCurrentEditor() is None:
   ### No session
       print 'No active session  .. OK'
       pass
   else:
       ### Someone else is making changes
       userWithSession = cfgManager.getCurrentEditor().replace(' ', '')
       print '===> Currently there is a Session'
       print '===> User \"' +userWithSession+'\" is making the changes'
       print '===> Wait until \"' +userWithSession+'\" complete the current session'
       exit()
   pass
except Exception:
   ### Other Errors
   print '===> Error, see log for more info'
   exit()


print
print
# Main
domainRuntime()

servers = domainRuntimeService.getServerRuntimes();
print('################################################################')
print('# Java heap information per server')
print('################################################################')
print('%20s %10s %8s %8s %4s' % ('Server','Current','Free','Max','Free'))
for server in servers:
   free    = int(server.getJVMRuntime().getHeapFreeCurrent())/(1024*1024)
   freePct = int(server.getJVMRuntime().getHeapFreePercent())
   current = int(server.getJVMRuntime().getHeapSizeCurrent())/(1024*1024)
   max     = int(server.getJVMRuntime().getHeapSizeMax())/(1024*1024)
   print('%20s %7d MB %5d MB %5d MB %3d%%' % (server.getName(),current,free,max,freePct))

print
print
print 'Look for ALSB Object ..'
alsbCore = findService(ALSBConfigurationMBean.NAME, ALSBConfigurationMBean.TYPE)
print '.. OK'
print 'Find info about OSB Service Deployed ..'

allRefs = alsbCore.getRefs(Ref.DOMAIN)

STRING_MATCH = "BOLP"

for ref in allRefs:
        # Get Types
        typeID = ref.getTypeId()
        serviceFullName = ref.getFullName()
        if typeID == "ProxyService" :
                result = re.search(STRING_MATCH, ref.getFullName())
                if result != None:
                        print 'Proxy : ' + serviceFullName
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
