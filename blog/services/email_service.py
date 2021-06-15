from django.core.mail import send_mail


def send_email_for_user_with_post(request, post, cd):
    post_url = request.build_absolute_uri(post.get_absolute_url())
    subject = '{} ({}) recommends you reading "{}"'.format(
        cd['name'], cd['email'], post.title
    )
    message = f"READ post '{post.title}' at\n\n{post_url}\n\n{cd['name']}'s comments:\n{cd['comments']}"
    sent =  send_mail(subject, message, 'admin@myblog.com', (cd['to'],), fail_silently=True) 
    return sent


    