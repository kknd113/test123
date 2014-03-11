from django.shortcuts import render
from django.http import HttpResponse
from models import Goal, BeatMyGoalUser
from django.template import RequestContext, loader

# Create your views here

from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'index.html')


@csrf_exempt
def goal_create_goal(request):
	data = json.loads(request.body)
	title = data['title']
	description = data['description']
	creator = data['creator']
	prize = data['prize']
	private_setting = data['private_setting']
	goal_type = data['goal_type']
	response = Goal.create(title, description, creator, prize, private_setting, goal_type)
	return HttpResponse(json.dumps({"errCode": response}), content_type = "application/json")

@csrf_exempt
def goal_remove_goal(request):
	data = json.loads(request.body)
	goal_id = data["goal_id"]
	user = data["user"]
	response = Goal.remove(goal_id, user)
	return HttpResponse(json.dumps({"errCode": response}), content_type = "application/json")

@csrf_exempt
def goal_edit_goal(request):
	data = json.loads(request.body)
	goal_id = data["goal_id"]
	user = data["user"]
	edits = data["edits"]
	response = Goal.edit(goal_id, user, edits)
	return HttpResponse(json.dumps({"errCode": response}), content_type = "application/json")

@csrf_exempt
def goal_view_goal(request):
	data = json.loads(request.body)
	goal_id = data["goal_id"]
	goal = Goal.objects.get(id=goal_id)
	title = goal.title
	description = goal.description
	prize = goal.prize
	date_created = goal.date_created
	progress_value = goal.progress_value
	private_setting = goal.private_setting
	creator = goal.creator
	return HttpResponse(json.dumps({"errCode": 1, "title":title, "description":description,
		"prize":prize, "date_created":date_created,"progress_value":progress_value,
		"private_setting":private_setting,"creator":creator}), content_type = "application/json")


#def goal_remove_user(request):
#	try:
#		req = json.loads(request.body)
#		goal_id = req["goal_id"]
#		user_id = req["user_id"]
#	except:
#		return requeset.send_error(500)
#	response = Goal().remove_user(goal_id, user_id)
#	return HttpResponse(json.dumps({"errCode": response}), content_type = "application/json")

def user_login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    
    elif request.method == "POST":
        data = json.loads(request.body)
        username= data["username"]
        password= data["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/dashboard/')
        else:
            response = -6
            return HttpResponse(json.dumps({"errCode": response}), content_type = "application/json")
@csrf_exempt
def create_user(request):
    print request.method
    if request.method == "GET":
        return render(request, 'users/createUser.html')
    elif request.method == "POST":
        data = json.loads(request.body)
        username, email, password = data["username"], data["email"], data["password"]
        response = BeatMyGoalUser.create(username, email, password)

        if "errors" in response:
            return HttpResponse(json.dumps(response), 
                                content_type = "application/json")            
        else:
        	user = response['user']

        	# TODO! - this is a bad hack
        	user.backend = 'django.contrib.auth.backends.ModelBackend'
        	# authenticate(username=username, password=password)
        	login(request, user)
        	redirect = "/users/%s/" % (user.id)
        	return HttpResponse(json.dumps({"redirect" : redirect,
        		"success" : response["success"]
        		}), content_type = "application/json")

    else:
        return HttpResponse("Invalid request", status=500)


def view_user(request, uid):
	if request.method == "GET":
		user = BeatMyGoalUser.getUserById(uid)
		return render(request, 'users/viewUser.html', {
			"user" : user
		})
@csrf_exempt
def edit_user(request, uid):
	user = request.user
	#user = BeatMyGoalUser.getUserById(uid)
	if (user.is_authenticated() and user.id == uid):
		if request.method == "GET":
			return render(request, 'users/editUser.html', {
				"username": user.username,
				"email":	user.email,
			})
		elif request.method == "POST":
			data = json.loads(request.body)
			print data
			username = data['username']
			email = data['email']
			response = BeatMyGoalUser.updateUser(user, username, email)
			res = {
				"errCode" : response,
				"redirect": "/users/" + uid,
			}
			return HttpResponse(json.dumps(res), content_type = 'application/json')
	else:
		request.send_error(403)
	
def test_user(request):
	return render(request, 'testUserView.html')

@csrf_exempt
def view_user2(request):
	try:
		data = json.loads(request.body)
		user_id = data["user_id"]
	except:
		return request.send_error(500)

	user = BeatMyGoalUser.getUserById(user_id)
	user_name = user.username
	user_firstName = user.first_name
	user_lastName = user.last_name
	user_email = user.email
	return HttpResponse(json.dumps({"errCode": 1, "username" : user_name,"firstName" : user_firstName, 
									"lastName" : user_lastName, "email" : user_email}), content_type = "application/json")

@csrf_exempt
def edit_user2(request):
	try:
		data = json.loads(request.body)
		user_id = data["user_id"]
		user_name = data["user_name"]
		user_firstName = data["user_firstName"]
		user_lastName = data["user_lastName"]
		user_email = data["user_email"]
	except:
		return request.send_error(500)

	response = BeatMyGoalUser.updateUser2(user_id, user_name, user_firstName, user_lastName, user_email)
	return HttpResponse(json.dumps({"errCode": response}), content_type = "application/json")


@csrf_exempt
def delete_user(request):
	try:
		req = json.loads(request.body)
		user_id = req["user_id"]
	except:
		return request.send_error(500)
	
	response = BeatMyGoalUser.deleteUser(user_id)
	return HttpResponse(json.dumps({"errCode": response}), content_type = "application/json")


def logout(request):
    return None

