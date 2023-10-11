
def interceptor(request):
    if request.url.startswith('https://kaxmedia.cloudflareaccess.com/'):
        request.create_response(
            status_code=302,
            #headers={'Content-Type': 'text/html'},  # Optional headers dictionary
            #body='<html>Hello World!</html>'
        )
