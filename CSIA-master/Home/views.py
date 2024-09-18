from ast import Pass
import json
from django.shortcuts import render,redirect

from .models import Player

from datetime import date, datetime,timedelta
# from dateutil.parser import parser

def home(request):
    if request.user.is_authenticated:
        return redirect("user_home")
    return render(request, "Login.html")


def user_home(request):
    if request.user.is_authenticated:
        return render(request, "home.html")
    else:
        return redirect("home")

def add_player(request):
    if request.user.is_authenticated:
        if request.method =="POST":
            name = request.POST.get("playerName")
            mobile = request.POST.get("mobile")
            position = request.POST.get("position")
            dob = request.POST.get("dob")
            nationality = request.POST.get("nationality")
            obj = Player.objects.all()
            if len(obj) == 0:
                p_id = 0
            else:
                p_id = obj[len(obj) -  1].p_id + 1

            player = Player.objects.create(
                p_id = p_id,
                name = str(name).lower(),
                mobile = mobile,
                position = str(position).lower(),
                dob = dob,
                nationality = str(nationality).lower(),
            )

            player.save()
            return render(request, "home.html")

def search_player(request):
    context = {}
    if request.user.is_authenticated:
        if request.method =="POST":
            name = request.POST.get("playerName")
            mobile = request.POST.get("mobile")
            position = request.POST.get("position")
            dob = request.POST.get("dob")
            nationality = request.POST.get("nationality")            
            p1 = {}
            if name:
                p1.update({'name': str(name).lower()})
            if mobile:
                p1.update({'mobile':mobile})
            if position:
                p1.update({'position':str(position).lower()})
            if dob:
                p1.update({'dob':dob})
            if nationality:
                p1.update({'nationality':str(nationality).lower()})
            print(p1)
            p1 = Player.objects.filter(**p1)
            
            # print("# of Players: " + str(len(p1)))
            context = {
                'players':p1,
            }
    return render(request, "search.html", context)
        
def update_data(request):
    if request.user.is_authenticated:
        table_data = request.POST.get('table_data')
        json_data = json.loads(table_data)
        # print(json_data)
        for each_player in json_data:
            p_items = list(each_player.values())
            # if str(each_player["Want to Delete"]).lower() == "yes":
            if (len(p_items) > 0):
                if str(p_items[6]).lower() == "yes":
                    del_row = Player.objects.get(p_id=int(p_items[0]))
                    del_row.delete()
                else:
                    update_row = Player.objects.get(p_id=int(p_items[0]))
                    update_row.name = p_items[1]
                    update_row.mobile = p_items[2]
                    update_row.position = p_items[3]                    
                    update_row.dob =  datetime.strptime(p_items[4], '%b. %d, %Y').date()
                    update_row.nationality = p_items[5]
                    update_row.save()

        return redirect('search_player')

def view_players(request, age_id=0):
    if request.user.is_authenticated:
        age_map = {
            0:(0,100),
            1:(0,11),
            2:(11,14),
            3:(14,16),
            4:(16,18),
            5:(18,99),
        }
        today = datetime.today()
        min_date = today-timedelta(days=age_map[age_id][1] * 365)
        max_date = today-timedelta(days=age_map[age_id][0] * 365)


        players = Player.objects.filter(
            dob__gte = min_date,
            dob__lte = max_date,
        )
        context = {
            "players": players
        }
        return render(request, "Viewplayers.html", context)
