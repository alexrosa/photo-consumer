'''
Created on Nov 15, 2016

@author: alexandre f rosa
'''
from urllib2 import urlopen
from PIL import Image
from PIL.ExifTags import TAGS
import piexif

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
        ret[decoded] = convert_and_validate(value)
    return ret

#decode data to unicode 
def convert_and_validate(value):
    if isinstance(value, tuple):
        for idx, v in enumerate(value):
            if isinstance(v, str):
                value[idx] = v.decode('utf-8', 'ignore')
    elif isinstance(value, str):
        value = value.decode('utf-8', 'ignore')
    return value
#check the string value
def is_hex(s):
    try:
        int(s, 16)
        return True
    except ValueError:
        return False

#method used to download a remote file
def downloadRemoteFile(url):
    try:
        return urlopen(url)
    except RuntimeError as re:
        raise re.message
        return None 
