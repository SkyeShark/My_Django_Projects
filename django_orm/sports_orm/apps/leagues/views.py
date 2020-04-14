from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		"baseball_leagues": League.objects.filter(sport="Baseball"),
		"womens_leagues": League.objects.filter(name__contains="Women"),
		"hockey_leagues": League.objects.filter(sport__contains="Hockey"),
		"not_football": League.objects.exclude(sport__contains="Football"),
		"conferences": League.objects.filter(name__contains="Conference"),
		"atlantics" : League.objects.filter(name__contains="Atlantic"),
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"dallas_teams": Team.objects.filter(location="Dallas"),
		"raptors": Team.objects.filter(team_name="Raptors"),
		"city_teams": Team.objects.filter(location__contains="City"),
		"t_teams": Team.objects.filter(team_name__startswith="T"),
		"ordered_teams": Team.objects.all().order_by("location"),
		"reversed_teams": Team.objects.all().order_by("-team_name"),
		"players": Player.objects.all(),
		"coopers": Player.objects.filter(last_name="Cooper"),
		"joshuas": Player.objects.filter(first_name="Joshua"),
		"nojosh": Player.objects.exclude(first_name="Joshua").filter(last_name="Cooper"),
		"alexwyatt": Player.objects.filter(first_name="Alexander") | Player.objects.filter(first_name="Wyatt")
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")