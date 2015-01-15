from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
from sharkblazers import util
from faker.fake_factory import Factory

@csrf_exempt
def faker(request):
    count = request.GET.get("count", 1)
    if isinstance(count, basestring) is True:
        try:
            count = int(count)
        except:
            count = 1

    factory = Factory()

    lst = []
    for x in xrange(count):
        o = factory.create()
        lst.append(o)

    if count < 2:
        lst = lst[0]
    # form = BankingForm(request.POST)
    # if form.is_valid():
    #     pass
    # return HttpResponse(json.dumps({}), content_type="application/json")
    return HttpResponse(util.json(lst, indent=2), content_type="application/json")