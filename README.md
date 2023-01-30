# pihole-adlists
Create a unified and unique list for ad lists


## Usage

- Install required packages by running the following command:

```
pip install -r requirements.txt
```

- Update the list urls.list with your own lists and run:

```
python convert.py
```

## Alternative: Docker

```
docker build -t adlists-convert . -f Dockerfile
docker run --rm  -v $(pwd)/:/app --name adlists-convert adlists-convert
```

---


## Information

The script will generate an output file named adlists.list that combines all lists from urls.list. This file can be imported into Pi-hole using the raw link from Github.

To import the list into Pi-hole, use the following link:

Adlist - https://github.com/MiddleCloud/pihole-adlists/raw/main/adlists.list

----

## Source lists


### The script uses the following Pi-hole lists as source:


* http://sysctl.org/cameleon/hosts
* https://s3.amazonaws.com/lists.disconnect.me/simple_tracking.txt
* https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/fakenews-gambling/hosts
* https://encrypt-the-planet.com/downloads/hosts
* https://dbl.oisd.nl
* https://raw.githubusercontent.com/FadeMind/hosts.extras/master/add.Spam/hosts
* https://adaway.org/hosts.txt
* https://v.firebog.net/hosts/AdguardDNS.txt
* https://raw.githubusercontent.com/anudeepND/blacklist/master/adservers.txt
* https://v.firebog.net/hosts/Easylist.txt
* https://pgl.yoyo.org/adservers/serverlist.php?hostformat=hosts&showintro=0&mimetype=plaintext
* https://raw.githubusercontent.com/FadeMind/hosts.extras/master/UncheckyAds/hosts
* https://raw.githubusercontent.com/bigdargon/hostsVN/master/hosts
* https://v.firebog.net/hosts/Easyprivacy.txt
* https://v.firebog.net/hosts/Prigent-Ads.txt
* https://gitlab.com/quidsup/notrack-blocklists/raw/master/notrack-blocklist.txt
* https://raw.githubusercontent.com/FadeMind/hosts.extras/master/add.2o7Net/hosts
* https://raw.githubusercontent.com/crazy-max/WindowsSpyBlocker/master/data/hosts/spy.txt
* https://hostfiles.frogeye.fr/firstparty-trackers-hosts.txt
* https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Alternate%20versions%20Anti-Malware%20List/AntiMalwareHosts.txt
* https://osint.digitalside.it/Threat-Intel/lists/latestdomains.txt
* https://s3.amazonaws.com/lists.disconnect.me/simple_malvertising.txt
* https://v.firebog.net/hosts/Prigent-Malware.txt
* https://mirror.cedia.org.ec/malwaredomains/immortal_domains.txt
* https://www.malwaredomainlist.com/hostslist/hosts.txt
* https://bitbucket.org/ethanr/dns-blacklists/raw/8575c9f96e5b4a1308f2f12394abd86d0927a4a0/bad_lists/Mandiant_APT1_Report_Appendix_D.txt
* https://phishing.army/download/phishing_army_blocklist_extended.txt
* https://gitlab.com/quidsup/notrack-blocklists/raw/master/notrack-malware.txt
* https://v.firebog.net/hosts/Shalla-mal.txt
* https://raw.githubusercontent.com/FadeMind/hosts.extras/master/add.Risk/hosts
* https://urlhaus.abuse.ch/downloads/hostfile/
* https://zerodot1.gitlab.io/CoinBlockerLists/hosts_browser
* https://s3.amazonaws.com/lists.disconnect.me/simple_ad.txt
* https://raw.githubusercontent.com/hoshsadiq/adblock-nocoin-list/master/hosts.txt
* https://raw.githubusercontent.com/notracking/hosts-blocklists/master/hostnames.txt
* https://gitlab.com/ZeroDot1/CoinBlockerLists/-/raw/master/hosts
* https://raw.githubusercontent.com/jfoboss/dnscrypt-domain-blacklists/master/blacklist.txt
* https://block.energized.pro/basic/formats/domains.txt
* https://block.energized.pro/extensions/xtreme/formats/domains.txt
* https://block.energized.pro/extensions/ips/formats/list.txt
* https://raw.githubusercontent.com/PolishFiltersTeam/KADhosts/master/KADhosts_without_controversies.txt
* https://v.firebog.net/hosts/static/w3kbl.txt
* https://raw.githubusercontent.com/matomo-org/referrer-spam-blacklist/master/spammers.txt
* https://someonewhocares.org/hosts/zero/hosts
* https://raw.githubusercontent.com/vokins/yhosts/master/hosts
* https://winhelp2002.mvps.org/hosts.txt
* https://v.firebog.net/hosts/neohostsbasic.txt
* https://raw.githubusercontent.com/RooneyMcNibNug/pihole-stuff/master/SNAFU.txt
* https://paulgb.github.io/BarbBlock/blacklists/hosts-file.txt
* https://hostsfile.mine.nu/hosts0.txt
* https://v.firebog.net/hosts/BillStearns.txt
* https://hostsfile.org/Downloads/hosts.txt
* https://www.joewein.net/dl/bl/dom-bl-base.txt
* https://v.firebog.net/hosts/Kowabit.txt
* https://adblock.mahakala.is
* https://v.firebog.net/hosts/Admiral.txt
* https://raw.githubusercontent.com/jdlingyu/ad-wars/master/hosts
* https://github.com/Kees1958/W3C_annual_most_used_survey_blocklist/blob/master/TOP_EU_US_Ads_Trackers_HOST
* https://hostfiles.frogeye.fr/multiparty-trackers-hosts.txt
* https://www.github.developerdan.com/hosts/lists/ads-and-tracking-extended.txt
* https://raw.githubusercontent.com/Perflyst/PiHoleBlocklist/master/android-tracking.txt
* https://raw.githubusercontent.com/Perflyst/PiHoleBlocklist/master/SmartTV.txt
* https://raw.githubusercontent.com/Perflyst/PiHoleBlocklist/master/AmazonFireTV.txt
* https://v.firebog.net/hosts/Airelle-trc.txt
* https://v.firebog.net/hosts/Prigent-Crypto.txt
* https://raw.githubusercontent.com/Spam404/lists/master/main-blacklist.txt
* https://raw.githubusercontent.com/HorusTeknoloji/TR-PhishingList/master/url-lists.txt
* https://v.firebog.net/hosts/Airelle-hrsk.txt
* https://raw.githubusercontent.com/PolishFiltersTeam/KADhosts/master/KADhosts.txt
* https://raw.githubusercontent.com/VeleSila/yhosts/master/hosts
* https://raw.githubusercontent.com/chadmayfield/my-pihole-blocklists/master/lists/pi_blocklist_porn_all.list
* https://raw.githubusercontent.com/chadmayfield/my-pihole-blocklists/master/lists/pi_blocklist_porn_top1m.list
* https://raw.githubusercontent.com/anudeepND/blacklist/master/facebook.txt
* https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/fakenews-gambling-porn-social/hosts
* https://raw.githubusercontent.com/AdguardTeam/cname-trackers/master/combined_disguised_trackers_justdomains.txt
* https://raw.githubusercontent.com/MetaMask/eth-phishing-detect/master/src/hosts.txt
* https://raw.githubusercontent.com/Sinfonietta/hostfiles/master/gambling-hosts

