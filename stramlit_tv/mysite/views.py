from django.shortcuts import render
from datetime import datetime
# Create your views here.
from django.views.decorators.clickjacking import xframe_options_exempt


@xframe_options_exempt
def index(request,tvno=0):
    tv_list=[
        {'name':'阿里山國家森林遊樂區','tvCode':'5RAiapFv_Ak'},
        {'name':'台東多良車站 ','tvCode':'UCG1aXVO8H8'},
        {'name':'台北大稻埕碼頭','tvCode':'Ndo_8RuefH4'},
        {'name':'九份山城','tvCode':'XSD5ptYisw8'},
        ]
    tv = tv_list[tvno]
    return render(request,"index.html",locals())

