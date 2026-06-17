from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Coral+Pixels&family=Xanh+Mono:ital@0;1&display=swap" rel="stylesheet"><style>* {background-color:#FF0000;}div {width:100%;height:100%;display:flex;align-items:center;justify-content:center;}h1 {font-family: "Xanh Mono", monospace;color:#770000;font-size:86px;margin-bottom:128px;}</style><div><h1>Hello, world. You\'re at the polls index.</h1></div>')

