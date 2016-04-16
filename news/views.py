# -*- coding: utf-8 -*-
import json
import datetime

from django.shortcuts import render
from django.http import HttpResponse

from models import Category, News


def get_info(model, myfilter, limit=5):
    try:
        if isinstance(myfilter, dict):
            rows = model.objects.filter(**myfilter).order_by('-date').values()[: limit]
        else:
            rows = model.objects.all().order_by('-date').values()[: limit]
    except model.DoesNotExist:
        rows = []
    except:
        rows = []
    return rows


def get_news_and_fields(request, myfilter, limit=5):
    news_list = []
    for row in get_info(News, myfilter, limit):
        news_list.append(make_some_editions_with_fields(row))
    return news_list


def get_filter(params):
    filter_options = json.loads(params.get("filter", "{}"))
    news_category = params.get("category_id", None)
    has_category = news_category is not None
    if has_category:
        filter_options["category_id"] = news_category
    limit = params.get("limit", 10 if has_category else 5)
    return filter_options, limit


def get_news(request, cat_id=None):
    if request.method != "GET":
        return HttpResponse("Not supported request method", status=405)
    if bool(request.GET):
        context = {'news': get_news_and_fields(request, *get_filter(request.GET)), }
        return HttpResponse(json.dumps(context), content_type="application/json")
    else:
        news_list = get_news_and_fields(request, *get_filter({'category_id': cat_id}))
        context = {'news': news_list, 'category': list(Category.objects.all().values())}
        return render(request, 'index.html', context)


def make_some_editions_with_fields(obj):
    import os
    for key in obj.keys():
        if isinstance(obj[key], datetime.date):
            obj[key] = obj[key].strftime("%d.%m.%Y")
        elif key == 'photo':
            obj[key] = os.path.split(obj[key])[1]
        elif key.find('category') != -1:
            categ = Category.objects.values('name').filter(id=obj[key])
            if categ:
                obj[key] = categ[0]['name']
        else:
            obj[key] = obj[key]
    return obj


def set_vote(request):
    from django.db.models import F

    report_id = request.GET['id']
    vote = int(request.GET['value'])
    report = News.objects.get(id=report_id)
    report.votes = F('votes') + vote
    report.save()
    report = News.objects.get(id=report_id)
    return HttpResponse(report.votes)


def get_vote_template(request, report_id):
    info = News.objects.filter(id=report_id).values()[0]
    cat = info['category_id']
    context = {'report':  make_some_editions_with_fields(info), 'cat': cat}
    return render(request, 'voting.html', context)
