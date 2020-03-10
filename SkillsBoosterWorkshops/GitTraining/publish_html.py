from lxml import etree
import sys

def transform(xmlPath, xslPath):
  # read xsl file
  xslRoot = etree.fromstring(open(xslPath).read())
  transform = etree.XSLT(xslRoot)
  
  # read xml
  xmlRoot = etree.fromstring(open(xmlPath).read())

  # transform xml with xslt
  transRoot = transform(xmlRoot)
  
  # return transformation result
  return transRoot

if __name__ == '__main__':
  sys.stdout = open("index.html", "w")
  print (transform('index.xml', 'index.xsl'))
