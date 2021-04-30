from django.shortcuts import render

# Create your views here.
from os import system
import subprocess
import sys
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.http import Http404
from django.urls import reverse
from django.views import generic



def render_home(request):
    if "program" in request.POST:
        with open("program_gn.py","w") as f:
            f.write(request.POST['program'])
        with open("program_input","w") as f:
            f.write(request.POST['input'])
        with open("program_input",'r') as inp:
            with open("program_out",'w') as out:
                proc=subprocess.run(["python","program_gn.py"],
                                      stdin=inp,stdout=subprocess.PIPE)
        # with open("program_out", 'r') as out:
        #     val={"output":out.readlines()+["WHat "]}
        val={"output":proc.stdout}
        print(val)
        temp=loader.get_template("compilerhome/index.html")
        return HttpResponse(temp.render(val,request))
    else:
        temp = loader.get_template("compilerhome/index.html")
        return HttpResponse(temp.render({}, request))




