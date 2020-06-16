from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def calc(request):
    history = str(request.POST['history'])
    squareHistoryNum = request.POST['squareHistoryNum']
    pre = request.POST['pre']
    answer = 0
    if 'median' in request.POST:
        if len(request.POST['median']) > 0:
            median = float(request.POST['median'])
        else:
            median = 0
    if 'squareNum' in request.POST:
        squareNum = request.POST['squareNum']
        if pre == '＋':
            median = float(squareHistoryNum) + int(squareNum)
        elif pre == '－':
            median = float(squareHistoryNum) - int(squareNum)
        elif pre == '×':
            median = float(squareHistoryNum) * int(squareNum)
        elif pre == '÷':
            median = float(squareHistoryNum) / int(squareNum)
        if len(history) == 0:
            squareNumInt = int(squareNum)
            squareHistoryNum = squareNumInt
        elif pre == '．':
            squareNumInt = float(squareHistoryNum) + int(squareNum) / 10
            squareHistoryNum = squareNumInt
        pre = squareNum
        history = history + squareNum

    elif 'square' in request.POST:
        square = request.POST['square']
        if square == 'AC':
            history = ''
            pre = ''
            squareHistoryNum = ''
            median = 0
            answer = 0
        elif square == 'Ｃ':
            if pre is not None:
                pre = ''
                history = history[:-1]
                median = 0
                answer = 0
            else:
                squareHistoryNum = int(str(squareHistoryNum)[:-1])
                history = history[:-1]
                median = 0
                answer = 0
        elif square == '＝':
            answer = median
        else:
            history = history + square
            pre = square


    context = {
        'pre': pre,
        'history': history,
        'squareHistoryNum': squareHistoryNum,
        'median': median,
        'answer': answer
    }
    return render(request, 'index.html', context)