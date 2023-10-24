def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]  # вытаскиваем IP адрес нашего клиента
    else:
        ip = request.META.get('REMOTE_ADDR')  # IP с которого к нам поступил запрос, хорошо в том случае, если клиент использует сторонние ресурсы

    return ip