#!/bin/bash

get_MBs()
{
    awk '/\/dev\/null/ {if ($4=="-") speed=$2 $3; else speed=$3 $4;} END {gsub(/\(|\)/,"",speed); print speed}' 
}


# Let' use only some links, because the monthly traffic is limited.
for iteration in "1" "2" "3"
do
    {
        declare -A test_files_100mb=(
            ["CacheFly CDN"]="http://cachefly.cachefly.net/100mb.test"
            # ["DigitalOcean (FR)"]="http://speedtest-fra1.digitalocean.com/100mb.test"
            ["DigitalOcean (GB)"]="http://speedtest-lon1.digitalocean.com/100mb.test"
            # ["DigitalOcean (NL)"]="http://speedtest-ams2.digitalocean.com/100mb.test"
            # ["DigitalOcean (NL)"]="http://speedtest-ams3.digitalocean.com/100mb.test"
            ["LeaseWeb (NL)"]="http://mirror.nl.leaseweb.net/speedtest/100mb.bin"
            # ["Linode (DE)"]="http://speedtest.frankfurt.linode.com/100MB-frankfurt.bin"   
            ["Linode (GB)"]="http://speedtest.london.linode.com/100MB-london.bin"         
            # ["Linode (JP)"]="http://speedtest.tokyo.linode.com/100MB-tokyo.bin"           
            # ["Linode (SG)"]="http://speedtest.singapore.linode.com/100MB-singapore.bin"   
            # ["Linode (US)"]="http://speedtest.dallas.linode.com/100MB-dallas.bin"         
            ["Online.net (FR)"]="http://ping.online.net/100Mo.dat"
            # ["OVH (CA)"]="http://proof.ovh.ca/files/100Mio.dat"
            # ["OVH (DE)"]="http://proof.ovh.ca/files/100Mio.dat"
            ["OVH (FR)"]="http://ovh.net/files/100Mb.dat"
            # ["Softlayer (DE)"]="http://speedtest.fra02.softlayer.com/downloads/test100.zip"  
            ["Softlayer (FR)"]="http://speedtest.par01.softlayer.com/downloads/test100.zip"  
            # ["Softlayer (JP)"]="http://speedtest.tok02.softlayer.com/downloads/test100.zip"  
            # ["Softlayer (SG)"]="http://speedtest.sng01.softlayer.com/downloads/test100.zip"  
            # ["Softlayer (US)"]="http://speedtest.dal05.softlayer.com/downloads/test100.zip"  
            # ["Vultr (DE)"]="https://fra-de-ping.vultr.com/vultr.com.100MB.bin"
            # ["Vultr (FR)"]="http://par-fr-ping.vultr.com/vultr.com.100MB.bin"
            ["Vultr (GB)"]="http://lon-gb-ping.vultr.com/vultr.com.100MB.bin"
            # ["Vultr (NL)"]="https://ams-nl-ping.vultr.com/vultr.com.100MB.bin"
        )

        declare -A test_files_10gb=(
            # ["CDN77.com (FR)"]="http://fra.download.10gbps.io/10000mb.bin"
            ["CDN77.com (NL)"]="http://ams.download.10gbps.io/10000mb.bin"
            ["Online.net (FR)"]="http://ping.online.net/10000Mo.dat"
            ["OVH (FR)"]="http://ovh.net/files/10Gb.dat"
        )

        ipv4=$(wget -qO - --timeout=5 http://ipv4.icanhazip.com/)
        ipv6=$(wget -qO - --timeout=5 http://ipv6.icanhazip.com/)

        printf 'Download a 100Mb file:\n'
        printf "======================\n\n"

        if [ -n "$ipv4" ]
        then
            printf 'IPv4 speedtests\n\n'
            for server in "${!test_files_100mb[@]}";
            do
                echo "$server (IPv4): " $(wget -4 -O /dev/null ${test_files_100mb[$server]} 2>&1 | get_MBs);
            done | sort
        fi

        printf '\n'

        if [ -n "$ipv6" ]
        then
            printf 'IPv6 speedtests\n\n'
            for server in "${!test_files_100mb[@]}";
            do
                echo "$server (IPv6): " $(wget -6 -O /dev/null ${test_files_100mb[$server]} 2>&1 | get_MBs);
            done | sort 
        fi

        printf '\n'
        printf 'Download a 10Gb file:\n'
        printf "======================\n\n"

        if [ -n "$ipv4" ]
        then
            printf 'IPv4 speedtests\n\n'
            for server in "${!test_files_10gb[@]}";
            do
                echo "$server (IPv4): " $(wget -4 -O /dev/null ${test_files_10gb[$server]} 2>&1 | get_MBs);
            done | sort
        fi

        printf '\n'

        if [ -n "$ipv6" ]
        then
            printf 'IPv6 speedtests\n\n'
            for server in "${!test_files_10gb[@]}";
            do
                echo "$server (IPv6): " $(wget -6 -O /dev/null ${test_files_10gb[$server]} 2>&1 | get_MBs);
            done | sort 
        fi
    }  2>&1 | tee -a /tmp/downloads_${iteration}.log
    printf '\n'
done
