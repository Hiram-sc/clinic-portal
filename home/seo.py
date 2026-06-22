from django.http import HttpResponse

def robots_txt(request):
    
    content = """User-agent: *
Allow: /

Disallow: /admin/

Sitemap: https://drajanainagastro.com.br/sitemap.xml
"""
    return HttpResponse(content, content_type="text/plain") 