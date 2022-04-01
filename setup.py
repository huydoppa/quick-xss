import os


os.system("wget -iL https://github.com/tomnomnom/waybackurls/releases/download/v0.0.2/waybackurls-linux-amd64-0.0.2.tgz ; tar zxvf waybackurls-linux-amd64-0.0.2.tgz ; mv waybackurls /usr/bin/waybackurl ; rm -rf waybackurls-linux-amd64-0.0.2.tgz")
os.system("wget -iL https://github.com/tomnomnom/qsreplace/releases/download/v0.0.1/qsreplace-linux-amd64-0.0.1.tgz; tar zxvf qsreplace-linux-amd64-0.0.1.tgz; mv qsreplace /usr/bin/qsreplace; rm -rf qsreplace-linux-amd64-0.0.1.tgz")
os.system("cp freq /usr/bin/freq")
