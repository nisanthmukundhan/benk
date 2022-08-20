from .models import District, Account, Materials, Branch


def menu_links(request):
    links = District.objects.all()
    return dict(links=links)


def account_detail(request):
    a = Account.objects.all()
    return dict(a=a)


def meterial_detail(request):
    m = Materials.objects.all()
    return dict(m=m)
