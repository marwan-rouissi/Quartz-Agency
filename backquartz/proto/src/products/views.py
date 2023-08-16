from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from django.urls import path
from .forms import ProductForm
from .models import Product
#from main.main import main, tile, downloadPicture
from PIL import Image
from itertools import product
from os import mkdir, chdir, listdir, rmdir, rename
import os
import requests
import shutil
import mimetypes


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def product_create_view(request):
    form = ProductForm(request.POST or None)
    cwd = os.getcwd() + "/products/templates/products/img example"
    file = open(cwd + "/post.txt", "r")
    exText = file.read()
    file.close()
    file = open(cwd + "/hashtag.txt", "r")
    tag = file.read()
    file.close()


    name = get_client_ip(request)
    name = "a"+name.replace('.','a')+"a"
    


    filepath = os.getcwd() + "/backup/" + name
    
    
    if name not in listdir(os.getcwd() + "/backup"):
        mkdir(filepath)
    
    src = "main/main.py"
    dst = filepath+"/main.py"


    shutil.copyfile(src, dst)


    exHash = [""]
    for a in tag:
        if a == "\n":
            exHash.append("")
        else:
            exHash[-1] += a
    exImg = ["img"+str(a)+".png" for a in range(1,10)]
    print(get_client_ip(request))
    context = {
        'prompt':exText,
        'image_generator':exImg,
        'hashtag':exHash,
        'form': form
    }
    
    return render(request, "products/product_create.html", context)


def product_download_view(request):
    form = ProductForm(request.POST or None)


    context = {
        'form': form,
    }
    
    return render(request, "products/product_download.html", context)

def dwd(request):
    # fill these variables with real values

    client = get_client_ip(request)
    client = "a"+client.replace('.','a')+"a"
    fl_path = os.getcwd() + "/backup/" + client
    if "your_post.zip" in listdir(fl_path):
        os.remove(fl_path + "/your_post.zip")
    filename = "your_post.zip"
    for a in listdir(fl_path):
        if client in a:
            lis = a
    archName = fl_path + "/" + a
    shutil.make_archive(fl_path + "/your_post", 'zip',archName )
    print(listdir(fl_path))
    os.rename(archName, archName+" processed")

    file = fl_path + "/your_post.zip"
    fl = open(file, 'rb')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response
    

def product_created_view(request):
    form = ProductForm(request.POST or None)


    

    strform = str(form)
    listform = [[]]
    for a in strform:
        if a == "\n":
            listform.append("")
        else:
            listform[-1] += a
    prompt = ""
    image_generator = ""
    inPut = [prompt,image_generator]
    n = 0
    for a in listform:
        if "</textarea>" in a:
            inPut[n] = a.replace("</textarea>","")
            n+=1
    
    name = get_client_ip(request)
    name = "a"+name.replace('.','a')+"a"

    filepath = os.getcwd() + "/backup/" + name
    isZip = "your_post.zip" in listdir(filepath)
    finalName = name+" n"+str(len(listdir(filepath))+1-isZip)
    entirepath = filepath + "/" + finalName
    mkdir(entirepath)


    loc = {}
    exec(f"""import backup.{name}.main
textOut,geneImgOut,hashtag = backup.{name}.main.main(inPut[0],inPut[1],name)""", {"inPut":inPut, "name":name}, loc)
    textOut = loc["textOut"]
    geneImgOut = loc["geneImgOut"]
    hashtag = loc["hashtag"]
    textOut.replace(".", ".\n")
    if textOut:
        file = open(entirepath+"/post.txt", "w")
        file.write(textOut+"\n\n")
        file.close()
    if hashtag:
        file = open(entirepath+"/hashtag.txt", "w")
        for a in hashtag:
            file.write(a+"\n")
        file.close()
    if geneImgOut:
        for a in range(len(geneImgOut)):
            url = geneImgOut[a]
            typefile = ""
            for b in range(1,len(url)):
                if url[-b]==".":
                    typefile=url[-b:]
                    break
            typefile=".png"
            r = requests.get(url)
            file = open(entirepath+"/img"+str(a+1)+typefile, "wb+")
            file.write(r.content)
            file.close()
    


    context = {
        'prompt':textOut,
        'image_generator':geneImgOut,
        'hashtag':hashtag,
        'form': form

    }

    return render(request, "products/product_created.html", context)


def product_update_view(request, id=id):
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)



def product_detail_view(request, id):
    obj = get_object_or_404(Product, id=id)
    context = {
        "object": obj
    }
    return render(request, "products/product_detail.html", context)


def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "products/product_delete.html", context)
