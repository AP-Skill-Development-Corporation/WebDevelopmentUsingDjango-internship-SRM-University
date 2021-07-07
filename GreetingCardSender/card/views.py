from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import EmailMessage
from GreetingCardSender import settings
from PIL import Image
def greet_me(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')


        # sending mail
        sub = "Greetings from APSSDC!"
        body = "Hey "+ name.title()+ ", you have successfully completed the django code"
        receiver_email_id = email
        sender_email_id = settings.EMAIL_HOST_USER
        email_msg = EmailMessage(sub, body, sender_email_id, [receiver_email_id])

        #image reading
        # im = Image.open('static/img/temp_pic.jpg')
        # print('\n\n *******', im)
        email_msg.attach_file('static/img/temp_pic.jpg')
        email_msg.send()
        return HttpResponse("mail sent!!")
    return render(request, 'index.html',{})