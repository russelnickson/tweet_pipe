from django.shortcuts import render_to_response
from django.http import HttpResponse
import twitter

def tweet_pipe(request):
    return render_to_response('tweet_pipe.html')

def swapper(request):
    if 'choice' in request.GET:
        c = int (request.GET['choice'])
        if c == 1:
            return render_to_response('view_status.html')
        elif c == 2:
            return render_to_response('update_status.html')
        elif c == 3:
            client=twitter.Api()
            return render_to_response('view_tweets.html',{'status':client.GetPublicTimeline()})
        else:
            message = 'You submitted invalid option.'
            return HttpResponse(message)
    else:
        message = 'You submitted an empty form.'
        return HttpResponse(message)

def view_status(request):
    if 'username' in request.GET:
        client=twitter.Api()
        status=client.GetUserTimeline(request.GET['username'])
        return render_to_response('view_tweets.html', {'status': status})
        
def update_status(request):
    client=twitter.Api(request.GET['username'],request.GET['password'])
    client.PostUpdate(request.GET['status'])
    message = 'Status Updated'
    return HttpResponse (message)



