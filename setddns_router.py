from six.moves import urllib
import os, stat

url = 'https://raw.githubusercontent.com/namukcom/SynologyCloudflareDDNS/master/cloudflare.php'
target_file = '/usr/syno/bin/ddns/cloudflare.php'

data = ""
with open("/etc.defaults/ddns_provider.conf", "r") as configFile:
        data = configFile.read().rstrip()

if "[Cloudflare]" not in data:
        print("no data")
        data += "[Cloudflare]\n"
        data += "        modulepath=/usr/syno/bin/ddns/cloudflare.php\n"
        data += "        queryurl=https://www.cloudflare.com/"
        with oprn("/etc.defaults/ddns_provider.conf", "w") as configFile:
                configFile.write(data)
                print("write complete")
else:
        print("exist data")

urllib.request.urlretrieve(url, target_file)
os.chmod(target_file, stat.S_IRUSR |  stat.S_IWUSR |  stat.S_IXUSR |  stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH)
