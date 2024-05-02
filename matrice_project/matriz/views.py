from django.shortcuts import render

def home(request):
    return render(request, 'matriz/home.html')

def calculator(request):
    if request.method == 'POST':
        num1 = float(request.POST['num1'])
        num2 = float(request.POST['num2'])
        operation = request.POST['operation']
        result = 0

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 != 0:
                result = num1 / num2
            else:
                return render(request, 'matriz/calculator.html', {'error': 'Division by zero'})

        return render(request, 'matriz/calculator.html', {'result': result})

    return render(request, 'matriz/calculator.html')