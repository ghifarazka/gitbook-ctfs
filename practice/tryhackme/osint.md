# OSINT

### Google Dorking

_Summary: How crawlers work & how to google dork_&#x20;

Room: [https://tryhackme.com/r/room/googledorking](https://tryhackme.com/r/room/googledorking)

* crawler indexes websites, note the keywords, search for insite urls, then crawl that url recursively
* crawlers first check for `robots.txt`
* you might want to hide all `.ini` file with `/*.ini$`
* in UNIX system, hide all `.conf` files
* `sitemap.xml` provides the websute structure, helps with SEO
* [https://pagespeed.web.dev/](https://pagespeed.web.dev/) -> google site analyzer, check speed performance

### Web OSINT

_Summary: there are so many ways we can do to uncover the owner of a website & unveil connections between websites_

Room: [https://tryhackme.com/r/room/webosint](https://tryhackme.com/r/room/webosint)&#x20;

* [https://www.namecheap.com/](https://www.namecheap.com/) -> check who owns the domain
* [Wayback machine](https://wayback-api.archive.org/) -> check archived snapshot of website
* [ViewDNS.info](https://viewdns.info/) -> anything about domain (history, etc)
* Does a site feel like a legit source of info?
  * Language - What grade level is the writing? Does it seem to be written by a native English speaker?
  * UX - Is it user friendly? Is the design modern?
  * What pages does the site have?
* [https://ahrefs.com/blog/seo-best-practices/](https://ahrefs.com/blog/seo-best-practices/) -> SEO best practices
* Search terms in the website's source code:
  * `<!--` is HTML comments
  * `@` for [Pivoting from an Email address](https://nixintel.info/osint/12-osint-resources-for-e-mail-addresses/)
  * `ca-pub` is [Google Publisher ID](https://support.google.com/adsense/answer/105516?hl=en)
  * `ua-` is [Google AdSense ID](https://www.bellingcat.com/resources/how-tos/2015/07/23/unveiling-hidden-connections-with-google-analytics-ids/)
  * `.jpg` and other img exts. to reveal more directory structure
* tools to check google codes: [https://www.nerdydata.com/](https://www.nerdydata.com/) and [https://spyonweb.com/](https://spyonweb.com/)
* common link between heat.net & purchase.org: in 2011-2012, their IP shares the same hosting (liquid web, l.l.c); around the same time as when the link is placed (according to wayback machine)
* heat.net is likely a PBN (private blog network) to purchase.org; its sole purpose is to make purchase.org rank higher in search engine results
* this is why heat.net doesn't seem "natural" to the eyes

### Geolocating Images

_Summary: how to know location from image_

Room: [https://tryhackme.com/r/room/geolocatingimages](https://tryhackme.com/r/room/geolocatingimages)

#### Reverse Image Search

* Best reverse image search: Yandex > Bing > Google
  * Yandex uses AI, it tries to get what's really in the picture
  * Google finds exact match
  * TinEye looks for exact duplicate
* increase the image resolution, 200x200 and below is no hope
* try mirrorring, cropping, rotating the photo
* [blurring out](https://x.com/AricToler/status/1206679612543111169) the photo subject can let the search engine focus on finding the background

#### Geolocating

* rough estimate
  * get text, landmarks, road layouts
  * what is likely to be on the country/region
    * climate
    * popular brand of cars
    * driving side
    * etc
  * IP/ASN number
  * metadata/EXIF, social media geotagging
* pinpointing
  * building floor: [eye level and perspective](https://www.bellingcat.com/resources/2024/07/16/dubai-uae-cartel-organised-crime-geolocation-open-source-guide-technique-tools/)
