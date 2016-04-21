# -*- coding: utf-8 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from re import compile, escape

from ..scraper import _BasicScraper
from ..helpers import indirectStarter
from ..util import tagre
from .common import (_ComicControlScraper, _WordPressScraper, WP_LATEST_SEARCH,
                     xpath_class)


class Namesake(_ComicControlScraper):
    url = 'http://namesakecomic.com/'


class NamirDeiter(_BasicScraper):
    url = 'http://www.namirdeiter.com/'
    rurl = escape(url)
    stripUrl = url + 'comics/index.php?date=%s'
    firstStripUrl = stripUrl % '19991128'
    imageSearch = compile(tagre("img", "src", r"'?(%scomics/\d+\.jpg)'?" % rurl, quote=""))
    prevSearch = compile(tagre("a", "href", r'(%scomics/index\.php\?date=\d+)' % rurl, quote="'") + "Previous")
    help = 'Index format: yyyymmdd'


class NatalieDee(_BasicScraper):
    url = 'http://www.nataliedee.com/'
    rurl = escape(url)
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % '022806'
    imageSearch = compile(tagre("img", "src", r'(%s\d+/[^"]+)' % rurl,
                                before="overflow"))
    prevSearch = compile(tagre("a", "href", r'([^"]+)') + "&lt;&lt; Yesterday")
    help = 'Index format: mmddyy'

    def namer(self, image_url, page_url):
        unused, date, filename = image_url.rsplit('/', 2)
        return '%s-%s' % (date, filename)


class Nedroid(_WordPressScraper):
    url = 'http://nedroid.com/'
    prevSearch = '//a[@rel="prev"]'


class NeoEarth(_BasicScraper):
    url = 'http://www.neo-earth.com/NE/'
    stripUrl = url + 'index.php?date=%s'
    firstStripUrl = stripUrl % '2007-03-23'
    imageSearch = compile(r'<img src="(strips/.+?)"')
    prevSearch = compile(r'<a href="(.+?)">Previous</a>')
    help = 'Index format: yyyy-mm-dd'


class NerfNow(_WordPressScraper):
    url = 'https://www.nerfnow.com/'
    prevSearch = '//li[@id="nav_previous"]/a'


class NewWorld(_BasicScraper):
    url = 'http://www.tfsnewworld.com/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2007/08/30/63'
    imageSearch = compile(r'<img src="(http://www.tfsnewworld.com/comics/.+?)"')
    prevSearch = compile(r'<div class="nav-previous"><a href="([^"]+)" rel="prev">')
    help = 'Index format: yyyy/mm/dd/stripn'


class NichtLustig(_BasicScraper):
    url = 'http://www.nichtlustig.de/main.html'
    stripUrl = 'http://static.nichtlustig.de/toondb/%s.html'
    lang = 'de'
    imageSearch = compile('background-image:url\((http://static\.nichtlustig\.de/comics/full/\d+\.jpg)')
    prevSearch = compile(tagre("a", "href", r'(http://static\.nichtlustig\.de/toondb/\d+\.html)'))
    latestSearch = compile(tagre("a", "href", r'([^"]*toondb/\d+\.html)'))
    help = 'Index format: yymmdd'
    starter = indirectStarter


class Nicky510(_WordPressScraper):
    url = 'http://www.nickyitis.com/'
    prevSearch = '//a[%s]' % xpath_class('navi-prev')


class Nimona(_BasicScraper):
    url = 'http://gingerhaze.com/nimona/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % "comic/page-1"
    imageSearch = compile(tagre("img", "src", r'(http://gingerhaze\.com/sites/default/files/nimona-pages/.+?)'))
    prevSearch = compile(r'<a href="(/nimona/comic/[^"]+)"><img src="http://gingerhaze\.com/sites/default/files/comicdrop/comicdrop_prev_label_file\.png"')
    help = 'Index format: stripname'
    endOfLife = True


class NobodyScores(_BasicScraper):
    url = 'http://nobodyscores.loosenutstudio.com/'
    rurl = escape(url)
    stripUrl = url + 'index.php?id=%s'
    firstStripUrl = stripUrl % '4'
    imageSearch = compile(tagre("img", "src", r'(%scomix/[^"]+)' % rurl))
    multipleImagesPerStrip = True
    prevSearch = compile(r'<a href="(%sindex.php.+?)">the one before </a>' % rurl)
    help = 'Index format: nnn'


class NoMoreSavePoints(_WordPressScraper):
    url = 'http://www.flowerlarkstudios.com/comic/no-more-save-points/mushroom-hopping/'
    firstStripUrl = url
    latestSearch = WP_LATEST_SEARCH
    starter = indirectStarter


class NoNeedForBushido(_BasicScraper):
    url = 'http://nn4b.com/'
    rurl = escape(url)
    stripUrl = url + '?webcomic1=%s'
    imageSearch = compile(
      tagre("a", "rel", "next") +
      tagre("img", "src", r'(%swp-content/uploads/\d+/\d+/[^"]+)' % rurl,
            after="attachment-full"))
    prevSearch = compile(tagre("a", "href", r'(%s\?webcomic1=[^"]+)' % rurl,
                               after="previous-webcomic"))
    latestSearch = compile(tagre("a", "href", r'(%s\?webcomic1=[^"]+)' % rurl,
                                 after="last-webcomic"))
    help = 'Index format: nnn'
    starter = indirectStarter


class NotInventedHere(_BasicScraper):
    url = 'http://notinventedhe.re/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % 'on/2009-9-21'
    imageSearch = compile(tagre("img", "src", r'(http://thiswas.notinventedhe.re/on/\d+-\d+-\d+)'))
    prevSearch = compile(tagre("a", "href", r'(/on/\d+-\d+-\d+)') +
                         '\s*Previous')
    help = 'Index format: yyyy-mm-dd'


class Nukees(_BasicScraper):
    url = 'http://www.nukees.com/'
    stripUrl = url + 'd/%s'
    firstStripUrl = stripUrl % '19970121'
    imageSearch = compile(r'"comic".+?"(/comics/.+?)"')
    prevSearch = compile(r'"(/d/.+?)".+?previous')
    help = 'Index format: yyyymmdd.html'
