from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

# linebot api
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

# register
from django.views.generic import TemplateView

# for linebot api
from dorm_linebot import settings
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

# linebot callback function
from django.http import *
from linebot.exceptions import *

# hash
from backend.hasher import *
import base64

# sql
from .models import *

# ===================================

# web page of management for admins
class console(TemplateView):
	template_name = "console.html"

	def get(self, request):
		return render(request, "console.html")


	def post(self, request):
		return render(request, "console.html")


# login page
class register(TemplateView):
	template_name = 'register.html'

	def get(self, request):
		return render(request, 'register.html')


	def post(self, request):
		return render(request, 'register.html')

class hello(TemplateView):
	# template_name = 'hello.html'

	def get(self, request):
		# check user detail from url
		if request.session.get('is_login', None):
			print("Should be redirect")
			print(request.session.get('lvl'))
			return redirect('/console/')

		return render(request, 'hello.html', locals())


	def post(self, request):
		# update user data
		if 'complete' in request.POST:
			name = request.POST['username']
			pw = request.POST['password']

			try:
				ob = Acc.objects.get(un=name)
				salt = ob.s

				if(str(make_hash(salt, pw)) == ob.pw):
					print("MATCH and be redirect")
					request.session['is_login'] = True
					request.session['lvl'] = ob.lvl
					request.session['username'] = ob.un
					return redirect('/console/')
					pass
				else:
					message = "login failed"
	
			except:
				message = "login failed"

			
		return render(request, 'hello.html', locals())


@csrf_exempt
def callback(request):
	if request.method == 'POST':

		signature = request.META['HTTP_X_LINE_SIGNATURE']
		body = request.body.decode('utf-8')

		try:
			events = parser.parse(body, signature)
		except InvalidSignatureError:
			return HttpResponseForbidden()
		except LineBotApiError:
			return HttpResponseBadRequest()

		for event in events:
			# if isinstance(event, MessageEvent):
			#	 res = json.loads(str(event.source))
			#	 print(res['userId'])

			#	 if is_secret(event.message.text) == True:
			#		 line_bot_api.reply_message(event.reply_token,TextSendMessage(text='666' + res['userId']))
			#		 print(Ppl.objects.get(secret = event.message.text).name)
			#		 Ppl.objects.filter(secret = event.message.text).update(lineuid = res['userId'])
			#		 print(event)

			print(event)
			if isinstance(event, MessageEvent):
				if isinstance(event.message, TextMessage):
					# line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))
					# line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.source.userId))
					line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))




		return HttpResponse()
	else:
		return HttpResponseBadRequest()

def pushss(request):
	line_bot_api.push_message('U71fdc4be604bd742d2c24a729ae2c688', TextSendMessage(text="奏外"))
	return HttpResponse("已送出奏外")
