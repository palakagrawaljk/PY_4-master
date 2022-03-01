"""Generation of Test Report of representations in different forms"""
import json
import unittest
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
from PY_4 import representation as RepresentationClass

class Test(unittest.TestCase):
  """generate test report of different representational formats"""

  representation = RepresentationClass.Representation({'report-id': '0moexa', 'website': 'https://pythonscraping.com/', 'total-links': 55, 'external-references': [['http://matthewritter.net', '1.27s'], ['http://webdata-scraping.com', '1.44s'], ['http://www.ryanemitchell.com/RMitchellResume.pdf', '0.59s'], ['https://en.wikipedia.org/wiki/Nguyen_v._Barnes_%26_Noble,_Inc.', '1.43s'], ['http://en.wikipedia.org/wiki/Python_%28programming_language%29', '6.13s'], ['http://gizmodo.com/5993535/holy-crap-is-this-mark-zuckerbergs-childhood-angelfire-website', '23.59s'], ['http://shop.oreilly.com/product/0636920078067.do', '2.6s'], ['https://covers.oreillystatic.com/images/0636920078067/lrg.jpg', '0.14s'], ['http://google.com', '0.32s'], ['https://en.wikipedia.org/wiki/Ticketmaster_Corp._v._Tickets.com,_Inc.', '2.34s'], ['http://shop.oreilly.com/product/0636920034391.do', '1.56s'], ['https://en.wikipedia.org/wiki/Specht_v._Netscape_Communications_Corp.', '1.72s']], 'internal-references': [['https://pythonscraping.com/', '0.92s'], ['https://pythonscraping.com/blog', '0.9s'], ['https://pythonscraping.com/node/5', '0.92s'], ['https://pythonscraping.com/sites/default/files/lrg_0.jpg', '0.86s'], ['http://pythonscraping.com/img/lrg%20(1).jpg', '0.59s'], ['https://pythonscraping.com/node/15', '0.9s'], ['https://pythonscraping.com/blog/tos-and-robots', '1.11s'], ['https://pythonscraping.com/blog/selenium-headers', '1.12s'], ['https://pythonscraping.com/blog/second-edition-changes', '1.17s'], ['https://pythonscraping.com/blog/javascript', '1.14s'], ['https://pythonscraping.com/blog/second-edition', '1.28s'], ['https://pythonscraping.com/blog/xpath-and-scrapy', '1.13s'], ['http://pythonscraping.com/img/profile_web.png', '0.58s'], ['https://pythonscraping.com/filter/tips', '0.89s'], ['http://pythonscraping.com/pages/javascript/ajaxDemo.html', '0.57s'], ['https://pythonscraping.com/comment/reply/16/7', '1.07s'], ['https://pythonscraping.com/comment/9', '4.29s'], ['https://pythonscraping.com/comment/7', '1.3s'], ['https://pythonscraping.com/comment/reply/16/9', '1.12s'], ['http://pythonscraping.com', '0.6s'], ['http://pythonscraping.com/pages/aPage.html', '0.58s'], ['http://pythonscraping.com/sites/default/files/lrg_0.jpg', '0.58s'], ['http://pythonscraping.com/blog', '0.63s'], ['http://pythonscraping.com/node/15', '0.61s'], ['http://pythonscraping.com/node/5', '0.62s'], ['http://pythonscraping.com/', '0.6s'], ['http://pythonscraping.com/blog/javascript', '0.81s'], ['http://pythonscraping.com/blog/second-edition', '0.84s'], ['http://pythonscraping.com/blog/xpath-and-scrapy', '0.89s'], ['http://pythonscraping.com/blog/selenium-headers', '2.43s'], ['http://pythonscraping.com/blog/tos-and-robots', '1.52s'], ['http://pythonscraping.com/blog/second-edition-changes', '0.9s'], ['http://pythonscraping.com/comment/reply/16/9', '0.85s'], ['http://pythonscraping.com/comment/reply/16/7', '1.05s'], ['http://pythonscraping.com/comment/9', '0.87s'], ['http://pythonscraping.com/filter/tips', '0.61s'], ['http://pythonscraping.com/comment/7', '2.33s']], 'broken-links': [['http://pythonscraping.com/wikiSpider.zip', '404: Not Found'], ['http://www.procato.com', '500: Internal Server Error'], ['https://www.packtpub.com/web-development/instant-web-scraping-java-instant', '403: Forbidden'], ['http://www.procato.com/my+headers/', '500: Internal Server Error'], ['http://www.procato.com/my+headers/as', '500: Internal Server Error'], ['https://github.com/REMitchell/python-scraping/blob/master/chapter13/4-dragAndDrop.py', '404: Not Found']]})
  
  """test report of yaml format"""
  def test_yaml_report(self):
        mock_input_val = '''report-id: 0moexa
website: https://pythonscraping.com/
total-links: 55

external-references: 
   # [ links-to-external-websites, response-time-in-seconds ] 
   - [ http://matthewritter.net, 1.27s ]
   - [ http://webdata-scraping.com, 1.44s ]
   - [ http://www.ryanemitchell.com/RMitchellResume.pdf, 0.59s ]
   - [ https://en.wikipedia.org/wiki/Nguyen_v._Barnes_%26_Noble,_Inc., 1.43s ]
   - [ http://en.wikipedia.org/wiki/Python_%28programming_language%29, 6.13s ]
   - [ http://gizmodo.com/5993535/holy-crap-is-this-mark-zuckerbergs-childhood-angelfire-website, 23.59s ]
   - [ http://shop.oreilly.com/product/0636920078067.do, 2.6s ]
   - [ https://covers.oreillystatic.com/images/0636920078067/lrg.jpg, 0.14s ]
   - [ http://google.com, 0.32s ]
   - [ https://en.wikipedia.org/wiki/Ticketmaster_Corp._v._Tickets.com,_Inc., 2.34s ]
   - [ http://shop.oreilly.com/product/0636920034391.do, 1.56s ]
   - [ https://en.wikipedia.org/wiki/Specht_v._Netscape_Communications_Corp., 1.72s ]

internal-references: 
   # [ links-to-internal-webpages-and-resources, response-time-in-seconds ]
   - [ https://pythonscraping.com/, 0.92s ]
   - [ https://pythonscraping.com/blog, 0.9s ]
   - [ https://pythonscraping.com/node/5, 0.92s ]
   - [ https://pythonscraping.com/sites/default/files/lrg_0.jpg, 0.86s ]
   - [ http://pythonscraping.com/img/lrg%20(1).jpg, 0.59s ]
   - [ https://pythonscraping.com/node/15, 0.9s ]
   - [ https://pythonscraping.com/blog/tos-and-robots, 1.11s ]
   - [ https://pythonscraping.com/blog/selenium-headers, 1.12s ]
   - [ https://pythonscraping.com/blog/second-edition-changes, 1.17s ]
   - [ https://pythonscraping.com/blog/javascript, 1.14s ]
   - [ https://pythonscraping.com/blog/second-edition, 1.28s ]
   - [ https://pythonscraping.com/blog/xpath-and-scrapy, 1.13s ]
   - [ http://pythonscraping.com/img/profile_web.png, 0.58s ]
   - [ https://pythonscraping.com/filter/tips, 0.89s ]
   - [ http://pythonscraping.com/pages/javascript/ajaxDemo.html, 0.57s ]
   - [ https://pythonscraping.com/comment/reply/16/7, 1.07s ]
   - [ https://pythonscraping.com/comment/9, 4.29s ]
   - [ https://pythonscraping.com/comment/7, 1.3s ]
   - [ https://pythonscraping.com/comment/reply/16/9, 1.12s ]
   - [ http://pythonscraping.com, 0.6s ]
   - [ http://pythonscraping.com/pages/aPage.html, 0.58s ]
   - [ http://pythonscraping.com/sites/default/files/lrg_0.jpg, 0.58s ]
   - [ http://pythonscraping.com/blog, 0.63s ]
   - [ http://pythonscraping.com/node/15, 0.61s ]
   - [ http://pythonscraping.com/node/5, 0.62s ]
   - [ http://pythonscraping.com/, 0.6s ]
   - [ http://pythonscraping.com/blog/javascript, 0.81s ]
   - [ http://pythonscraping.com/blog/second-edition, 0.84s ]
   - [ http://pythonscraping.com/blog/xpath-and-scrapy, 0.89s ]
   - [ http://pythonscraping.com/blog/selenium-headers, 2.43s ]
   - [ http://pythonscraping.com/blog/tos-and-robots, 1.52s ]
   - [ http://pythonscraping.com/blog/second-edition-changes, 0.9s ]
   - [ http://pythonscraping.com/comment/reply/16/9, 0.85s ]
   - [ http://pythonscraping.com/comment/reply/16/7, 1.05s ]
   - [ http://pythonscraping.com/comment/9, 0.87s ]
   - [ http://pythonscraping.com/filter/tips, 0.61s ]
   - [ http://pythonscraping.com/comment/7, 2.33s ]

broken-links: 
   # [ links-that-could-not-be-resolved, http-error-status-code ]
   - [ http://pythonscraping.com/wikiSpider.zip, 404: Not Found ]
   - [ http://www.procato.com, 500: Internal Server Error ]
   - [ https://www.packtpub.com/web-development/instant-web-scraping-java-instant, 403: Forbidden ]
   - [ http://www.procato.com/my+headers/, 500: Internal Server Error ]
   - [ http://www.procato.com/my+headers/as, 500: Internal Server Error ]
   - [ https://github.com/REMitchell/python-scraping/blob/master/chapter13/4-dragAndDrop.py, 404: Not Found ]
'''
        # representation = RepresentationClass.Representation({'report-id': '0moexa', 'website': 'https://pythonscraping.com/', 'total-links': 55, 'external-references': [['http://matthewritter.net', '1.27s'], ['http://webdata-scraping.com', '1.44s'], ['http://www.ryanemitchell.com/RMitchellResume.pdf', '0.59s'], ['https://en.wikipedia.org/wiki/Nguyen_v._Barnes_%26_Noble,_Inc.', '1.43s'], ['http://en.wikipedia.org/wiki/Python_%28programming_language%29', '6.13s'], ['http://gizmodo.com/5993535/holy-crap-is-this-mark-zuckerbergs-childhood-angelfire-website', '23.59s'], ['http://shop.oreilly.com/product/0636920078067.do', '2.6s'], ['https://covers.oreillystatic.com/images/0636920078067/lrg.jpg', '0.14s'], ['http://google.com', '0.32s'], ['https://en.wikipedia.org/wiki/Ticketmaster_Corp._v._Tickets.com,_Inc.', '2.34s'], ['http://shop.oreilly.com/product/0636920034391.do', '1.56s'], ['https://en.wikipedia.org/wiki/Specht_v._Netscape_Communications_Corp.', '1.72s']], 'internal-references': [['https://pythonscraping.com/', '0.92s'], ['https://pythonscraping.com/blog', '0.9s'], ['https://pythonscraping.com/node/5', '0.92s'], ['https://pythonscraping.com/sites/default/files/lrg_0.jpg', '0.86s'], ['http://pythonscraping.com/img/lrg%20(1).jpg', '0.59s'], ['https://pythonscraping.com/node/15', '0.9s'], ['https://pythonscraping.com/blog/tos-and-robots', '1.11s'], ['https://pythonscraping.com/blog/selenium-headers', '1.12s'], ['https://pythonscraping.com/blog/second-edition-changes', '1.17s'], ['https://pythonscraping.com/blog/javascript', '1.14s'], ['https://pythonscraping.com/blog/second-edition', '1.28s'], ['https://pythonscraping.com/blog/xpath-and-scrapy', '1.13s'], ['http://pythonscraping.com/img/profile_web.png', '0.58s'], ['https://pythonscraping.com/filter/tips', '0.89s'], ['http://pythonscraping.com/pages/javascript/ajaxDemo.html', '0.57s'], ['https://pythonscraping.com/comment/reply/16/7', '1.07s'], ['https://pythonscraping.com/comment/9', '4.29s'], ['https://pythonscraping.com/comment/7', '1.3s'], ['https://pythonscraping.com/comment/reply/16/9', '1.12s'], ['http://pythonscraping.com', '0.6s'], ['http://pythonscraping.com/pages/aPage.html', '0.58s'], ['http://pythonscraping.com/sites/default/files/lrg_0.jpg', '0.58s'], ['http://pythonscraping.com/blog', '0.63s'], ['http://pythonscraping.com/node/15', '0.61s'], ['http://pythonscraping.com/node/5', '0.62s'], ['http://pythonscraping.com/', '0.6s'], ['http://pythonscraping.com/blog/javascript', '0.81s'], ['http://pythonscraping.com/blog/second-edition', '0.84s'], ['http://pythonscraping.com/blog/xpath-and-scrapy', '0.89s'], ['http://pythonscraping.com/blog/selenium-headers', '2.43s'], ['http://pythonscraping.com/blog/tos-and-robots', '1.52s'], ['http://pythonscraping.com/blog/second-edition-changes', '0.9s'], ['http://pythonscraping.com/comment/reply/16/9', '0.85s'], ['http://pythonscraping.com/comment/reply/16/7', '1.05s'], ['http://pythonscraping.com/comment/9', '0.87s'], ['http://pythonscraping.com/filter/tips', '0.61s'], ['http://pythonscraping.com/comment/7', '2.33s']], 'broken-links': [['http://pythonscraping.com/wikiSpider.zip', '404: Not Found'], ['http://www.procato.com', '500: Internal Server Error'], ['https://www.packtpub.com/web-development/instant-web-scraping-java-instant', '403: Forbidden'], ['http://www.procato.com/my+headers/', '500: Internal Server Error'], ['http://www.procato.com/my+headers/as', '500: Internal Server Error'], ['https://github.com/REMitchell/python-scraping/blob/master/chapter13/4-dragAndDrop.py', '404: Not Found']]})
        # self.representation.yaml_report()
        self.assertEqual(mock_input_val, self.representation.yaml_report())
 
  """test report of json format"""
  def test_json_report(self):
    mock_input_val = '''{
  "report-id": "0moexa",
  "website": "https://pythonscraping.com/",
  "total-links": 55,
  "external-references": [
    [
      "http://matthewritter.net",
      "1.27s"
    ],
    [
      "http://webdata-scraping.com",
      "1.44s"
    ],
    [
      "http://www.ryanemitchell.com/RMitchellResume.pdf",
      "0.59s"
    ],
    [
      "https://en.wikipedia.org/wiki/Nguyen_v._Barnes_%26_Noble,_Inc.",
      "1.43s"
    ],
    [
      "http://en.wikipedia.org/wiki/Python_%28programming_language%29",
      "6.13s"
    ],
    [
      "http://gizmodo.com/5993535/holy-crap-is-this-mark-zuckerbergs-childhood-angelfire-website",
      "23.59s"
    ],
    [
      "http://shop.oreilly.com/product/0636920078067.do",
      "2.6s"
    ],
    [
      "https://covers.oreillystatic.com/images/0636920078067/lrg.jpg",
      "0.14s"
    ],
    [
      "http://google.com",
      "0.32s"
    ],
    [
      "https://en.wikipedia.org/wiki/Ticketmaster_Corp._v._Tickets.com,_Inc.",
      "2.34s"
    ],
    [
      "http://shop.oreilly.com/product/0636920034391.do",
      "1.56s"
    ],
    [
      "https://en.wikipedia.org/wiki/Specht_v._Netscape_Communications_Corp.",
      "1.72s"
    ]
  ],
  "internal-references": [
    [
      "https://pythonscraping.com/",
      "0.92s"
    ],
    [
      "https://pythonscraping.com/blog",
      "0.9s"
    ],
    [
      "https://pythonscraping.com/node/5",
      "0.92s"
    ],
    [
      "https://pythonscraping.com/sites/default/files/lrg_0.jpg",
      "0.86s"
    ],
    [
      "http://pythonscraping.com/img/lrg%20(1).jpg",
      "0.59s"
    ],
    [
      "https://pythonscraping.com/node/15",
      "0.9s"
    ],
    [
      "https://pythonscraping.com/blog/tos-and-robots",
      "1.11s"
    ],
    [
      "https://pythonscraping.com/blog/selenium-headers",
      "1.12s"
    ],
    [
      "https://pythonscraping.com/blog/second-edition-changes",
      "1.17s"
    ],
    [
      "https://pythonscraping.com/blog/javascript",
      "1.14s"
    ],
    [
      "https://pythonscraping.com/blog/second-edition",
      "1.28s"
    ],
    [
      "https://pythonscraping.com/blog/xpath-and-scrapy",
      "1.13s"
    ],
    [
      "http://pythonscraping.com/img/profile_web.png",
      "0.58s"
    ],
    [
      "https://pythonscraping.com/filter/tips",
      "0.89s"
    ],
    [
      "http://pythonscraping.com/pages/javascript/ajaxDemo.html",
      "0.57s"
    ],
    [
      "https://pythonscraping.com/comment/reply/16/7",
      "1.07s"
    ],
    [
      "https://pythonscraping.com/comment/9",
      "4.29s"
    ],
    [
      "https://pythonscraping.com/comment/7",
      "1.3s"
    ],
    [
      "https://pythonscraping.com/comment/reply/16/9",
      "1.12s"
    ],
    [
      "http://pythonscraping.com",
      "0.6s"
    ],
    [
      "http://pythonscraping.com/pages/aPage.html",
      "0.58s"
    ],
    [
      "http://pythonscraping.com/sites/default/files/lrg_0.jpg",
      "0.58s"
    ],
    [
      "http://pythonscraping.com/blog",
      "0.63s"
    ],
    [
      "http://pythonscraping.com/node/15",
      "0.61s"
    ],
    [
      "http://pythonscraping.com/node/5",
      "0.62s"
    ],
    [
      "http://pythonscraping.com/",
      "0.6s"
    ],
    [
      "http://pythonscraping.com/blog/javascript",
      "0.81s"
    ],
    [
      "http://pythonscraping.com/blog/second-edition",
      "0.84s"
    ],
    [
      "http://pythonscraping.com/blog/xpath-and-scrapy",
      "0.89s"
    ],
    [
      "http://pythonscraping.com/blog/selenium-headers",
      "2.43s"
    ],
    [
      "http://pythonscraping.com/blog/tos-and-robots",
      "1.52s"
    ],
    [
      "http://pythonscraping.com/blog/second-edition-changes",
      "0.9s"
    ],
    [
      "http://pythonscraping.com/comment/reply/16/9",
      "0.85s"
    ],
    [
      "http://pythonscraping.com/comment/reply/16/7",
      "1.05s"
    ],
    [
      "http://pythonscraping.com/comment/9",
      "0.87s"
    ],
    [
      "http://pythonscraping.com/filter/tips",
      "0.61s"
    ],
    [
      "http://pythonscraping.com/comment/7",
      "2.33s"
    ]
  ],
  "broken-links": [
    [
      "http://pythonscraping.com/wikiSpider.zip",
      "404: Not Found"
    ],
    [
      "http://www.procato.com",
      "500: Internal Server Error"
    ],
    [
      "https://www.packtpub.com/web-development/instant-web-scraping-java-instant",
      "403: Forbidden"
    ],
    [
      "http://www.procato.com/my+headers/",
      "500: Internal Server Error"
    ],
    [
      "http://www.procato.com/my+headers/as",
      "500: Internal Server Error"
    ],
    [
      "https://github.com/REMitchell/python-scraping/blob/master/chapter13/4-dragAndDrop.py",
      "404: Not Found"
    ]
  ]
}'''
    self.assertEqual(mock_input_val, self.representation.json_report())

  """test report of csv format"""
  def test_csv_report(self):
        mock_input_val ='''report-id,0moexa
website,https://pythonscraping.com/
total-links,55
external-references,"[['http://matthewritter.net', '1.27s'], ['http://webdata-scraping.com', '1.44s'], ['http://www.ryanemitchell.com/RMitchellResume.pdf', '0.59s'], ['https://en.wikipedia.org/wiki/Nguyen_v._Barnes_%26_Noble,_Inc.', '1.43s'], ['http://en.wikipedia.org/wiki/Python_%28programming_language%29', '6.13s'], ['http://gizmodo.com/5993535/holy-crap-is-this-mark-zuckerbergs-childhood-angelfire-website', '23.59s'], ['http://shop.oreilly.com/product/0636920078067.do', '2.6s'], ['https://covers.oreillystatic.com/images/0636920078067/lrg.jpg', '0.14s'], ['http://google.com', '0.32s'], ['https://en.wikipedia.org/wiki/Ticketmaster_Corp._v._Tickets.com,_Inc.', '2.34s'], ['http://shop.oreilly.com/product/0636920034391.do', '1.56s'], ['https://en.wikipedia.org/wiki/Specht_v._Netscape_Communications_Corp.', '1.72s']]"
internal-references,"[['https://pythonscraping.com/', '0.92s'], ['https://pythonscraping.com/blog', '0.9s'], ['https://pythonscraping.com/node/5', '0.92s'], ['https://pythonscraping.com/sites/default/files/lrg_0.jpg', '0.86s'], ['http://pythonscraping.com/img/lrg%20(1).jpg', '0.59s'], ['https://pythonscraping.com/node/15', '0.9s'], ['https://pythonscraping.com/blog/tos-and-robots', '1.11s'], ['https://pythonscraping.com/blog/selenium-headers', '1.12s'], ['https://pythonscraping.com/blog/second-edition-changes', '1.17s'], ['https://pythonscraping.com/blog/javascript', '1.14s'], ['https://pythonscraping.com/blog/second-edition', '1.28s'], ['https://pythonscraping.com/blog/xpath-and-scrapy', '1.13s'], ['http://pythonscraping.com/img/profile_web.png', '0.58s'], ['https://pythonscraping.com/filter/tips', '0.89s'], ['http://pythonscraping.com/pages/javascript/ajaxDemo.html', '0.57s'], ['https://pythonscraping.com/comment/reply/16/7', '1.07s'], ['https://pythonscraping.com/comment/9', '4.29s'], ['https://pythonscraping.com/comment/7', '1.3s'], ['https://pythonscraping.com/comment/reply/16/9', '1.12s'], ['http://pythonscraping.com', '0.6s'], ['http://pythonscraping.com/pages/aPage.html', '0.58s'], ['http://pythonscraping.com/sites/default/files/lrg_0.jpg', '0.58s'], ['http://pythonscraping.com/blog', '0.63s'], ['http://pythonscraping.com/node/15', '0.61s'], ['http://pythonscraping.com/node/5', '0.62s'], ['http://pythonscraping.com/', '0.6s'], ['http://pythonscraping.com/blog/javascript', '0.81s'], ['http://pythonscraping.com/blog/second-edition', '0.84s'], ['http://pythonscraping.com/blog/xpath-and-scrapy', '0.89s'], ['http://pythonscraping.com/blog/selenium-headers', '2.43s'], ['http://pythonscraping.com/blog/tos-and-robots', '1.52s'], ['http://pythonscraping.com/blog/second-edition-changes', '0.9s'], ['http://pythonscraping.com/comment/reply/16/9', '0.85s'], ['http://pythonscraping.com/comment/reply/16/7', '1.05s'], ['http://pythonscraping.com/comment/9', '0.87s'], ['http://pythonscraping.com/filter/tips', '0.61s'], ['http://pythonscraping.com/comment/7', '2.33s']]"
broken-links,"[['http://pythonscraping.com/wikiSpider.zip', '404: Not Found'], ['http://www.procato.com', '500: Internal Server Error'], ['https://www.packtpub.com/web-development/instant-web-scraping-java-instant', '403: Forbidden'], ['http://www.procato.com/my+headers/', '500: Internal Server Error'], ['http://www.procato.com/my+headers/as', '500: Internal Server Error'], ['https://github.com/REMitchell/python-scraping/blob/master/chapter13/4-dragAndDrop.py', '404: Not Found']]"
'''
        self.assertEqual(mock_input_val, self.representation.csv_report())

  """test report of html format"""
  def test_html_report(self):
        mock_input_val =True
        self.assertEqual(mock_input_val, self.representation.html_report())

if __name__ == '__main__':
    unittest.main()