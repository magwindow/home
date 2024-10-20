from carts.models import Cart


def get_user_carts(request):
    if request.user.is_authenticated:
        return Cart.objects.filter(user=request.user)
    
    
    if not request.session.session_key:  # если нет сессионного ключа
        request.session.create()  # создаем сессионный ключ
        
    return Cart.objects.filter(session_key=request.session.session_key)