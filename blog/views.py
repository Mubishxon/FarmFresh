from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Banner, About, Products, Facts, Carousel,  Features, Team, Blog
from .forms import NewsletterForm
from django.views.generic import UpdateView, CreateView,  DeleteView
from django.urls import reverse_lazy
# Create your views here.
class CarouselUpdateView(UpdateView):
    model = Carousel
    fields = ('name', 'bio', 'img', 'price', 'price2')
    template_name = 'CarouselEdit.html'

class CarouselDeleteView(DeleteView):
    model = Carousel
    template_name = 'CarouselDelete.html'
    success_url = reverse_lazy('index')

class CarouselCreateView(CreateView):
    model = Carousel
    template_name = 'CarouselCreateView.html'
    fields = ('name', 'bio', 'img', 'price', 'price2')

def Carouseldetail(request, carousel):
    carousel = get_object_or_404(Carousel, slug=carousel)
    context = {
        'carousel': carousel
    }
    return render(request, 'carouselDetailView', context=context)

def index(request):
    banner = Banner.objects.all()
    about = About.objects.all()
    products = Products.objects.all()
    facts = Facts.objects.all()
    carousel = Carousel.objects.all()
    features = Features.objects.all()
    team = Team.objects.all()
    blog = Blog.objects.all()
    newsletter = NewsletterForm(request.POST or None)
    if request.method == "POST" and newsletter.is_valid():
        newsletter.save()
        return HttpResponse("<h2>So'rovingiz muvaffaqiyatli amalga oshirildi. Rahmat!")
    context = {
        "banner": banner,
        "about": about,
        "products": products,
        "facts": facts,
        "carousel": carousel,
        "features": features,
        "team": team,
        "blog": blog,
        "newsletter": newsletter
    }
    return render(request, 'index.html', context=context)
def about(request):
    about = About.objects.all()
    context = {
        'about': about
    }
    return render(request, 'about.html', context=context)
def blog(request):
    blog = Blog.objects.all()
    context ={
        'blog': blog
    }
    return render(request, 'blog.html', context=context)
def newsletter(request):
    newsletter =NewsletterForm(request.POST or None)
    if request.method == "POST" and newsletter.is_valid():
        newsletter.save()
        return HttpResponse("<h2>So'rovingiz muvaffaqiyatli amalga oshirildi. Rahmat!")
    context = {
        "newsletter": newsletter
    }
    return render(request, 'newsletter.html', context=context)
def detail(request):
    carousel = Carousel.objects.all()
    context = {
        'carousel': carousel
    }
    return render(request, 'detail.html', context=context)
def feature(request):
    features = Features.objects.all()
    context = {
        'features': features
    }
    return render(request, 'feature.html', context=context)

def contact(request):
    return render(request, 'contact.html', context={})
def product(request):
    products = Products.objects.all()
    context = {
        'products': products
    }
    return render(request, 'product.html', context=context)
def service(request):
    return render(request, 'service.html', context={})
def team(request):
    team = Team.objects.all()
    context = {
        'team': team
    }
    return render(request, 'team.html', context=context)
def testimonial(request):
    banner = Banner.objects.get(id=id)
    context = {
        'x': banner
    }
    return render(request, 'testimonial.html', context=context)

def bannerdetail(request, id):
    banner = Banner.objects.get(id=id)
    context = {
        'x': banner
    }
    return render(request, 'bannerdetail.html', context=context)

def aboutdetail(request, id):
    about = About.objects.get(id=id)
    context = {
        'x': about
    }
    return render(request, 'aboutdetail.html', context=context)

def productsdetail(request, id):
    products = Products.objects.get(id=id)
    context = {
        'x': products
    }
    return render(request, 'productsdetail.html', context=context)

def factsdetail(request, id):
    facts = Facts.objects.get(id=id)
    context = {
        'x': facts
    }
    return render(request, 'factsdetail.html', context=context)

def carouseldetail(request, id):
    carousel = Carousel.objects.get(id=id)
    context = {
        'x': carousel
    }
    return render(request, 'carouseldetail.html', context=context)

def featuresdetail(request, id):
    features = Features.objects.get(id=id)
    context = {
        'x': features
    }
    return render(request, 'featuresdetail.html', context=context)

def teamdetail(request, id):
    team = Team.objects.get(id=id)
    context = {
        'x': team
    }
    return render(request, 'teamdetail.html', context=context)
def blogdetail(request, id):
    blog = Blog.objects.get(id=id)
    context = {
        'x': blog
    }
    return render(request, 'blogdetail.html', context=context)