from django.shortcuts import render

# Create your views here.

def test(request):
    return render(request, 'index.html', {"foo": "bar"})

def edit_user(request):
	return

def goal_delete_goal(request):
	try:
		req = json.loads(request.body)
		goal_id = req["goal_id"]
	except:
		return request.send_error(500)
	response = Goal().delete_goal(goal_id)
	return HttpResponse(json.dumps({"errCode": response}), content_type = "application/json")

def goal_remove_user(request):
	try:
		req = json.loads(request.body)
		goal_id = req["goal_id"]
		user_id = req["user_id"]
	except:
		return requeset.send_error(500)


	response = Goal().remove_user(goal_id, user_id)
	return HttpResponse(json.dumps({"errCode": response}), content_type = "application/json")
