from django.shortcuts import render
from .models import TM_MAIN_DATA as sData
from .models import TA_DATA_RESULT as rData


def index(request):
    list = sData.objects.all().order_by('-DT')[:200]
    context = {'sData_list': list}
    return render(request, 'index.html', context)


def indexOne(request):
    list = sData.objects.all().order_by('-DT')[:200]
    blueBalls = []
    redBalls1 = []
    redBalls2 = []
    redBalls3 = []
    redBalls4 = []
    redBalls5 = []
    redBalls6 = []
    for info in list:
        blueBalls.append(int(info.BLUE_BALL))
        _rBalls = info.RED_BALL.split(',')
        redBalls1.append(int(_rBalls[0]))
        redBalls2.append(int(_rBalls[1]))
        redBalls3.append(int(_rBalls[2]))
        redBalls4.append(int(_rBalls[3]))
        redBalls5.append(int(_rBalls[4]))
        redBalls6.append(int(_rBalls[5]))

    context = {'redBalls1': redBalls1, 'redBalls2': redBalls2, 'redBalls3': redBalls3, 'redBalls4': redBalls4,
               'redBalls5': redBalls5, 'redBalls6': redBalls6, 'blueBalls': blueBalls}
    return render(request, 'indexOne.html', context)


def indexTwo(request):
    list = rData.objects.all().order_by('-DT')[:200]
    ji = []
    cha1 = []
    cha2 = []
    cha3 = []
    cha4 = []
    cha5 = []
    he = []
    for info in list:
        he.append(int(info.HE))
        ji.append(int(info.JI))
        _chas = info.CHA.split(',')
        cha1.append(int(_chas[1]))
        cha2.append(int(_chas[2]))
        cha3.append(int(_chas[3]))
        cha4.append(int(_chas[4]))
        cha5.append(int(_chas[5]))

    context = {'cha1': cha1, 'cha2': cha2, 'cha3': cha3, 'cha4': cha4,
               'cha5': cha5, 'he': he, 'ji': ji}
    return render(request, 'indexTwo.html', context)
