from jnpr.junos import Device
from xml.etree import ElementTree as etree
from pprint import pprint
from jnpr.junos.utils.sw import SW
import logging
logging.basicConfig( level=logging.DEBUG)
 
dev = Device(host='xyz', user='xyz', password='xyz', gather_facts=False, port=22, huge_tree=True)
dev.open()
 
def myprogress(dev, report):
        print("host: {}, report: {}".format( dev.hostname, report))
pkg = "jinstall-host-ex-4300mp-x86-64-secure-signed.tgz"
sw = SW(dev)
ok, msg = sw.install(package=pkg,
                     validate=False,
                     remote_path='/var/tmp',
                     progress=myprogress,
                     no_copy=True,
                     force_host=False,
                     reboot=False,
                     issu=False,
                     nssu = False,
                     cleanfs=False,
                     vmhost=True,
                     force_copy=False,
                     timeout=8000)
if ok:
   #sw.reboot()
   print("Pass")
