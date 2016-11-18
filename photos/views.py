'''
Created on Nov 15, 2016

@author: alexandre f rosa
This a Controller module with 2 simple methods
1 - index (for load the first page index.html)
2 - load_and_save_data (that are responsible to save and load data from a remote source.

for the future:
You can apply a angular resource in this application 
Its possible to evaluate the solution applying REST and MongoDB for the persistent tier. 
'''

from django.shortcuts import render_to_response
from django.http.response import HttpResponse
from xml.dom.minidom import parse
from photos.utils import downloadRemoteFile, getExifData
from photos.models import Photo
from waldo.settings import URL_XML_WALDO
from django.template import context
from django.template.context import RequestContext
import json
from django.views.decorators.csrf import csrf_exempt

#Here I can see a 2 methods with that it has the basic functions to save and show the data

#basic method to start the application
def index(request):
    return render_to_response("index.html", RequestContext(request, context))

#this method is responsible for load, save and parse remote data
#It will be return a bunch of objects in a json format
@csrf_exempt
def load_and_save_data(request):
    data = downloadRemoteFile(URL_XML_WALDO)
    context = {}
    try:
        doc = parse(data)
        contents = doc.getElementsByTagName("Contents")
        total_count = 0
        processed_photo = []
        for content in contents:
            key_name = content.getElementsByTagName("Key")[0]
            last_mod = content.getElementsByTagName("LastModified")[0]
            e_tag = content.getElementsByTagName("ETag")[0]
            size = content.getElementsByTagName("Size")[0]
            #defines a url pattern for download data 
            url_photo = URL_XML_WALDO+'/'+key_name.firstChild.data
            
            #load photo before read
            photo = downloadRemoteFile(url_photo)
            
            #get de EXIF data from pic
            exif_data = getExifData(photo)
            
            #save data in a new python object
            obj_photo = Photo.objects.create(url_photo = url_photo,
                                         key= key_name.firstChild.data,
                                         last_modified= last_mod.firstChild.data,
                                         etag = e_tag.firstChild.data,
                                         size = size.firstChild.data,
                                         storage_class = 'Standard',
                                         exif_keys = exif_data)
            obj_photo.save()
            processed_photo.append('{url:'+url_photo+',name:'+key_name.firstChild.data+'}')
            total_count = total_count + 1
            print("processed file: "+str(total_count))
    except Exception as e:
        print("Application Error: "+e.message)
        context= {'error':e.message}    
    context = {'total_counted': total_count, 'photos':processed_photo}
    return HttpResponse(json.dumps(context),content_type='application/json')
    

