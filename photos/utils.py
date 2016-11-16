'''
Created on Nov 15, 2016

@author: alexandre f rosa
'''
from urllib2 import urlopen
from PIL import Image
from PIL.ExifTags import TAGS

#get the content of node (DOM OBJECT)
def getNodeText(node):
    nodelist = node.childNodes
    result = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            result.append(node.data)
    return ''.join(result)

#Get the meta-data of photo using python PILL lib
def getExifData(fn):
    ret = {}
    i = Image.open(fn)
    info = i._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    return ret

#method used to download a remote file
def downloadRemoteFile(url):
    try:
        return urlopen(url)
    except RuntimeError as re:
        raise re.message
        return None 
