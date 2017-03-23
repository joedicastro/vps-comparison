**WARNING: A work in progress!**

VPS Comparison
==============

A comparison between some VPS providers that have data centers located in **Europe**.

Initially I'm comparing only entry plans, below **5$** monthly.

VPS Providers
=============

Company
-------

|              | OVH                           | Linode                            | DigitalOcean                                 | Scaleway                              | Vultr                           | Amazon Lightsail                                 |
|--------------|-------------------------------|-----------------------------------|----------------------------------------------|---------------------------------------|---------------------------------|--------------------------------------------------|
| Foundation   | 1999                          | 2003                              | 2011                                         | 2013                                  | 2014                            | 2016                                             |
| Headquarters | Roubaix (FR)                  | Galloway, NJ (US)                 | New York (US)                                | Paris (FR)                            | Matawan, NJ (US)                | Seattle, WA (US)                                 |
| Market       | 3° largest                    |                                   | 2° largest                                   |                                       |                                 | 1° largest                                       |
| Website      | [OVH](https://www.ovh.com/us) | [Linode](https://www.linode.com/) | [DigitalOcean](https://www.digitalocean.com) | [Scaleway](https://www.scaleway.com/) | [Vultr](https://www.vultr.com/) | [Amazon Lightsail](https://amazonlightsail.com/) |

Notes:

-   The companies are sorted by the year of foundation.
-   Scaleway is a cloud division of Online.net (1999), itself subsidiary of the Iliad group (1990) owner also of the famous French ISP Free.
-   Vultr Holdings LLC is owned by Choopa LLC founded in 2010.
-   Amazon LightSail is a service of Amazon Web Services (2006) a subsidiary of Amazon.com (1994).
-   The Market numbers are extracted from the Wikipedia an other sources

Billing
-------

|                    | OVH | Linode | DigitalOcean | Scaleway | Vultr | Lightsail |
|--------------------|-----|--------|--------------|----------|-------|-----------|
| Credit Card        | Yes | Yes    | Yes          | Yes      | Yes   |           |
| PayPal             | Yes | Yes    | Yes          |          | Yes   |           |
| Bitcoin            | No  |        | No           |          | Yes   |           |
| Affiliate/Referral | No  |        | Yes          |          | Yes   |           |
| Coupon Codes       | No  | Yes    | Yes          |          | Yes   |           |

Note:

-   Linode needs a credit card associated to be able to pay with PayPal.

General Features
----------------

|                            | OVH                                                | Linode                                 | DigitalOcean                                                   | Scaleway                                                                                       | Vultr                                   | Lightsail                                                                               |
|----------------------------|----------------------------------------------------|----------------------------------------|----------------------------------------------------------------|------------------------------------------------------------------------------------------------|-----------------------------------------|-----------------------------------------------------------------------------------------|
| European data centers      | 3                                                  | 2                                      | 3                                                              | 2                                                                                              | 4                                       | 3                                                                                       |
| Documentation              | [Docs](https://www.ovh.co.uk/community/knowledge/) | [Docs](https://www.linode.com/docs/)   | [Docs](https://www.digitalocean.com/community)                 | [Docs](https://www.scaleway.com/docs/)                                                         | [Docs](https://www.vultr.com/docs/)     | [Docs](https://amazonlightsail.com/docs/)                                               |
| Doc. subjetive valuation   | 6/10                                               | 9/10                                   | 9/10                                                           |                                                                                                | 8/10                                    |                                                                                         |
| Uptime guaranteed (SLA)    | 99,95%                                             | 99,9%                                  | 99,99%                                                         | 99,9%                                                                                          | 100%                                    | 99,95%                                                                                  |
| Outage refund/credit (SLA) | Yes                                                | Yes                                    | Yes                                                            | No                                                                                             | Yes                                     | Yes                                                                                     |
| API                        | Yes                                                | Yes                                    | Yes                                                            | Yes                                                                                            | Yes                                     | Yes                                                                                     |
| API Docs                   | [API Docs](https://api.ovh.com/)                   | [API Docs](https://www.linode.com/api) | [API Docs](https://developers.digitalocean.com/documentation/) | [API Docs](https://developer.scaleway.com/)                                                    | [API Docs](https://www.vultr.com/api/)  | [API Docs](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/Welcome.html) |
| Services status page       | [Status](http://status.ovh.com/)                   | [Status](https://status.linode.com/)   | [Status](https://status.digitalocean.com/)                     | [Status](https://status.online.net/tasklist/?project=11&status=&perpage=50&order=id&sort=desc) | [Status](https://www.vultr.com/status/) | [AWS Status](https://status.aws.amazon.com/)                                            |
| Support Quality            |                                                    |                                        |                                                                |                                                                                                |                                         |                                                                                         |

Note:

-   Scaleway has four grades of SLA, the first basic is for free if you want something better, you have to pay a monthly fee.

### European data centers

-   **OVH**: Gravelines (FR), Roubaix (FR), Strasboug (DE). It has also a data center in Paris (FR), but is not available for these plans.
-   **Linode**: Frankfurt (DE), London (GB)
-   **DigitalOcean**: Amsterdam (NL), Frankfurt (DE), London (GB)
-   **Scaleway**: Amsterdam (NL), Paris (FR)
-   **Vultr**: Amsterdam (NL), Frankfurt (DE), London (GB), Paris (FR)
-   **Lightsail**: Dublin (IE), Frankfurt (DE), London (GB) and soon Paris (FR)

Control Panel
=============

Features
--------

|                                    | OVH               | Linode | DigitalOcean                                  | Scaleway | Vultr                                | Lightsail |
|------------------------------------|-------------------|--------|-----------------------------------------------|----------|--------------------------------------|-----------|
| Subjective control panel valuation | 5/10              |        | 8/10                                          |          | 9/10                                 |           |
| Graphs                             | Traffic, CPU, RAM |        | CPU, RAM, Disk I/O, Disk usage, Bandwith, Top |          | Monthly Bandwith, CPU, Disk, Network |           |
| Subjective graphs valuation        | 5/10              |        | 9/10                                          |          | 8/10                                 |           |
| Monthly usage per instance         | No                |        | No                                            |          | Bandwith, Credits                    |           |
| KVM Console                        | Yes               |        | Yes (VNC)                                     |          | Yes                                  |           |
| Power management                   | Yes               |        | Yes                                           |          | Yes                                  |           |
| Reset root password                | Yes               |        | Yes                                           |          | No                                   |           |
| Reinstall instance                 | Yes               |        | Yes                                           |          | Yes                                  |           |
| Median reinstall time              | ~12,5 min         |        | ~35 s                                         |          | ~2,1 min                             |           |
| Upgrade instance                   | Yes               |        | Yes                                           |          | Yes                                  |           |
| Change Linux Kernel                | No                |        | CentOS                                        |          | No                                   | No        |
| Recovery mode                      | No                |        | Yes                                           |          | Boot with custom ISO                 |           |
| Tag instances                      | No                |        | Yes                                           |          | Yes                                  |           |
| Android App                        | No                | Yes    | No                                            | No       | Yes                                  | No        |
| iOS App                            |                   |        |                                               |          |                                      |           |

Notes:

-   To reset the root password from the control panel is not a good security measure IMHO, it's useful, but you already have the KVM console for that.
-   In Vultr you can copy/see the masked default root password, but not reset it. This is necessary because the password is never sent by email.
-   You can resintall the instances using the same SO/App or choosing another one.
-   In Vultr can use a custom ISO or choose one from the library like SystemRescueCD or Trinity Rescue Kit to boot your instance and perform recovery tasks.

Instance creation
-----------------

### Operating Systems

|          | OVH                                | Linode | DigitalOcean                   | Scaleway | Vultr                          | Lightsail |
|----------|------------------------------------|--------|--------------------------------|----------|--------------------------------|-----------|
| Linux    | Arch Linux, CentOS, Debian, Ubuntu |        | CentOS, Debian, Fedora, Ubuntu |          | CentOS, Debian, Fedora, Ubuntu |           |
| BSD      | No                                 |        | FreeBSD                        |          | FreeBSD, OpenBSD               |           |
| Windows  | No                                 |        | No                             |          | Windows 2012 R2 (16$)          |           |
| Other SO | No                                 |        | CoreOS                         |          | CoreOS                         |           |

Note:

-   OVH also offers Linux desktop distributions like Kubuntu and OVH Release 3.

### One-click Apps

|                | OVH                      | Linode | DigitalOcean          | Scaleway | Vultr                | Lightsail |
|----------------|--------------------------|--------|-----------------------|----------|----------------------|-----------|
| Docker         | Yes                      |        | Yes                   |          | Yes                  |           |
| Stacks         | LAMP                     |        | LAMP, LEMP, ELK, MEAN |          | LAMP, LEMP           |           |
| Drupal         | Yes                      |        | Yes                   |          | Yes                  |           |
| WordPress      | Yes                      |        | Yes                   |          | Yes                  |           |
| Joomla         | Yes                      |        | No                    |          | Yes                  |           |
| Django         | No                       |        | Yes                   |          | No                   |           |
| RoR            | No                       |        | Yes                   |          | No                   |           |
| GitLab         | No                       |        | Yes                   |          | Yes                  |           |
| E-Commerce     | PrestaShop               |        | Magento               |          | Magento, PrestaShop  |           |
| Personal cloud | No                       |        | NextCloud, ownCloud   |          | NextCloud, ownCloud  |           |
| Panels         | Plesk, cPanel, CozyCloud |        | No                    |          | cPanel (15$), Webmin |           |

Notes:

-   Some providers offer more one-click Apps that I do not include here to save space.
-   Some of this apps in some providers require a bigger and more expensive plan that the entry ones below 5$ that I analyze here.
-   OVH uses Ubuntu, Debian or CentOS as SO for its apps.
-   Digital Ocean uses Ubuntu as SO for all of its apps.
-   Vultr uses CentOS as SO for all of its apps.
-   OVH Also offers Dokku on Ubuntu.
-   Do you really need a Panel (like cPanel)? They usually are a considerable security risk with several vulnerabilities.

### Other features

|                            | OVH                                   | Linode | DigitalOcean | Scaleway | Vultr | Lightsail |
|----------------------------|---------------------------------------|--------|--------------|----------|-------|-----------|
| ISO images library         | No                                    |        | No           |          | Yes   |           |
| Custom ISO image           | No                                    |        | No           |          | Yes   |           |
| Install scripts            | No                                    |        | Cloud-init   |          | iPXE  |           |
| Preloaded SSH keys         | Yes                                   |        | Yes          |          | Yes   |           |
| Distro install in instance | Partial, requires manual intervention |        | Yes          |          | Yes   |           |

Notes:

-   The Vultr's ISO image library include several ISOs like Alpine, Arch, Finnix, FreePBX, pfSense, Rancher Os, SystemRescueCD, and Trinity Rescue Kit.
-   The Vultr's "Custom ISO image" feature allows you to install virtually any SO supported by KVM and the server architecture.
-   To test the "Distro install in instance" I use a installation script to install Arch Linux from an official Debian instance. The purpose is to test if you are restricted in any way to use a different SO than the ones officially supported.

Security
--------

|                             | OVH | Linode | DigitalOcean | Scaleway | Vultr | Lightsail |
|-----------------------------|-----|--------|--------------|----------|-------|-----------|
| 2FA                         | Yes |        | Yes          |          | Yes   |           |
| Restrict access IPs         | Yes |        | No           |          | No    |           |
| Account Login Logs          | No  |        | Yes          |          | No    |           |
| SSL Quality                 |     |        |              |          |       |           |
| Send root password by email | Yes |        | No           |          | No    |           |
| Account password recovery   |     |        |              | Link     |       |           |

Notes:

-   Send plain text passwords by email is a very bad practice in terms of security.
-   OVH sends you the root password optionally if you use SSH keys, always in plain text if not.
-   DigitalOcean sends you the passwrods only if you don't use SSH keys, in plain text.
-   Vultr never sends you the root password, only the needed ones for one-click apps.

Plans (&lt;= $5)
================

Features
--------

|                      | OVH            | Linode | DigitalOcean                           | Scaleway | Vultr                                  | Vultr                                  | Lightsail |
|----------------------|----------------|--------|----------------------------------------|----------|----------------------------------------|----------------------------------------|-----------|
| Name                 | VPS SSD 1      |        | 5bucks                                 |          | 20GB SSD                               | 25GB SSD                               |           |
| Monthly Price        | 3,62€          |        | 5$                                     |          | 2,5$                                   | 5$                                     |           |
| CPU / Threads        | 1/1            |        | 1/1                                    |          | 1/1                                    | 1/1                                    |           |
| RAM                  | 2 GB           |        | 512 MB                                 |          | 512 MB                                 | 1 GB                                   |           |
| SSD Storage          | 10 GB          |        | 20 GB                                  |          | 20 GB                                  | 25 GB                                  |           |
| Traffic              | ∞              |        | 1 TB                                   |          | 500 GB                                 | 1 TB                                   |           |
| Bandwidth (In / Out) | 100/100 Mbps   |        | 1/10 Gbps                              |          | 1 / 10 Gbps                            | 1/10 Gbps                              |           |
| Virtualization       | KVM            |        | KVM                                    |          | KVM                                    | KVM                                    |           |
| Anti-DDoS Protection | Yes            |        | No                                     |          | 10$                                    | 10$                                    |           |
| Backups              | No             |        | 1$                                     |          | 0,5 $                                  | 1$                                     |           |
| Snapshots            | 2,99$          |        | 0,05$ per GB                           |          | Free (Beta)                            | Free (Beta)                            |           |
| IPv6                 | Yes            |        | Optional                               |          | Optional                               | Optional                               |           |
| Additional public IP | 2$ (up to 16)  |        | Floating IPs (0,006$ hour if inactive) |          | 2$ (up to 2) / 3$ floating IPs         | 2$ (up to 2) / 3$ floating IPs         |           |
| Private Network      | No             |        | Optional                               |          | Optional                               | Optional                               |           |
| Group firewall       | No             |        | No                                     |          | Yes                                    | Yes                                    |           |
| Block Storage        | From 5€ - 50GB |        | From 10$ - 100GB                       |          | From 1$ - 10GB                         | From 1$ - 10GB                         |           |
| Monitoring           | Yes (SLA)      |        | Beta (metrics, perfornance, SLA)       |          | No                                     | No                                     |           |
| Load Balancer        | 13$            |        | 20$                                    |          | High availability (floating IPs & BGP) | High availability (floating IPs & BGP) |           |
| DNS                  | Yes            |        | Yes                                    |          | Yes                                    | Yes                                    |           |
| Reverse DNS          | Yes            |        | Yes                                    |          | Yes                                    | Yes                                    |           |

Note:

-   The prices for DigitalOcean and Vultr not include taxes (VAT) for European countries.
-   I have serious doubts about the OVH's unlimited traffic, seems more marketing than real to me (joe di castro).

System Performance
------------------

|                     | OVH             | Linode | DigitalOcean | Scaleway | Vultr       | Vultr       | Lightsail |
|---------------------|-----------------|--------|--------------|----------|-------------|-------------|-----------|
| Name                | VPS SSD 1       |        | 5bucks       |          | 20GB SSD    | 25GB SSD    |           |
| Location            | Gravelines (FR) |        | London (GB)  |          | London (GB) | London (GB) |           |
| Instance            | Debian 8        |        | Debian 8     |          | Debian 8    | Debian 8    |           |
| UnixBench           | 1749,1          |        | 1450,6       |          | 1613        | 1731,2      |           |
| Sysbench            | 27,727 s        |        | 36,886 s     |          | 66,436 s    | 29,775 s    |           |
| Video Transcode     | 7 FPS           |        | 4 FPS        |          | 2 FPS       | 5 / 6 FPS   |           |
| Write IO            | 4 MB/s          |        | 42,91 MB/s   |          | 83,62 MB/s  | 175,93 MB/s |           |
| Read IO             | 4 MB/s          |        | 306,71 MB/s  |          | 162,55 MB/s | 252,32 MB/s |           |
| Write IOPS          | 1000            |        | 10728        |          | 20904       | 43982       |           |
| Read IOPS           | 1000            |        | 76768        |          | 40538       | 63079       |           |
| Download 100MB file | 12 MB/s         |        | 103 MB/s     |          | 177 MB/s    | 375 MB/s    |           |
| Download 10GB file  | 12 MB/s         |        | 83,6 MB/s    |          | 108 MB/s    | 203 MB/s    |           |

Notes:

-   Clearly the OVH's disk performance is limited by software, there is no other way to get so round results. Seems that older instances or other plans are not affected by this problem.
-   The small bandwidth available in this OVH plan clearly affects the network performance.

    **Warning**: Performance tests can be affected by locations, data centers and VPS host neighbors.

    **Warning**: These numbers are provisional ones, I'm automating this process, so I going to repeat all of this tests for the already tested and extend them to the other VPS providers. I also have the intention of provide in this repository both the means to reproduce these tests and the tests results itself. Lastly I also have the intention to add another tests.

Web Performance
---------------

|                     | OVH             | Linode | DigitalOcean | Scaleway | Vultr       | Vultr       | Lightsail |
|---------------------|-----------------|--------|--------------|----------|-------------|-------------|-----------|
| Name                | VPS SSD 1       |        | 5bucks       |          | 20GB SSD    | 25GB SSD    |           |
| Location            | Gravelines (FR) |        | London (GB)  |          | London (GB) | London (GB) |           |
| Instance            | Debian 8        |        | Debian 8     |          | Debian 8    | Debian 8    |           |
| Ping                | ~48,5 ms        |        | ~47,5 ms     |          | ~39,3 ms    | ~39,3 ms    |           |
| Apache benchmark A  | Fail            |        | Fail         |          |             | 14,68 RPS   |           |
| Apache benchmark B  | 24,61 RPS       |        | Fail         |          |             | 14,21 RPS   |           |
| Apache benchmark C  | 21,53 RPS       |        | 31,65 RPS    |          |             | 12,19 RPS   |           |
| Wordpress page load | 0,93 s          |        | 0,86 s       |          |             | 0,98 s      |           |

Note:

-   The ping is made from A Coruña (ES) over a 50/50Mbps Fiber connection.

    **Warning**: These numbers are provisional ones, I'm automating this process, so I going to repeat all of this tests for the already tested and extend them to the other VPS providers. I also have the intention of provide in this repository both the means to reproduce these tests and the tests results itself. Lastly I also have the intention to add another tests.

Default Security
----------------

|                             | OVH       | Linode | DigitalOcean | Scaleway | Vultr    | Vultr    | Lightsail |
|-----------------------------|-----------|--------|--------------|----------|----------|----------|-----------|
| Name                        | VPS SSD 1 |        | 5bucks       |          | 20GB SSD | 25GB SSD |           |
| Lynis Debian 8              | 58 / 217  |        | 59 / 217     |          | 61 / 220 | 61 / 220 |           |
| Lynis CentOS 7              | 66 / 217  |        | 67 / 217     |          | 66 / 211 | 66 / 211 |           |
| Lynis Wordpress             | 61 / 231  |        | 64 / 234     |          |          | 67 / 218 |           |
| gcc & build tools installed | Yes       |        | No           |          | No       | No       |           |

Notes:

-   The DigitalOcean Wordpress app comes with ufw and fail2ban pre-installed. Also comes prepared to use Let's Encrypt SSL certificates. These are good security measures for less security versed people.
-   It's a good security practice to not have installed builder tools and compilers in your server.

    **Warning**: Security in a VPS is your responsibility, nobody else. But taking a look to the default security applied in the default instances of a provider could give you a reference of the care that they take in this matter. And maybe it could give you also a good reference of how they care about their own systems security.

    **Warning**: Lynis index should be take with caution, it's not an absolute value, only a reference. It not covers yet all the security measures of a machine and could be not well balanced to do a effective comparison.

    **Warning**: These numbers are provisional ones, I'm automating this process, so I going to repeat all of this tests for the already tested and extend them to the other VPS providers. I also have the intention of provide in this repository both the means to reproduce these tests and the tests results itself. Lastly I also have the intention to add another tests.
