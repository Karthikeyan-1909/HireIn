from django.shortcuts import render, redirect
from math import ceil
from features.models import Jobs
from features.models import UpdateProfile, Resume, Blog, Contact, Apply
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.core import mail
from django.core.mail.message import EmailMessage


def home(request):
    current_user = request.user
    print(current_user)
    allProds = []
    catprods = Jobs.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Jobs.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params = {'allProds': allProds}
    return render(request, 'job.html', params)


def job(request):
    current_user = request.user
    print(current_user)
    allProds = []
    catprods = Jobs.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Jobs.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params = {'allProds': allProds}
    return render(request, 'job.html', params)


def apply(request):
    return render(request, 'apply.html')


def applying(request):
    if request.method == "POST":
        username = request.POST.get('username')
        date = request.POST.get('date')
        email = request.POST.get('email')
        work = request.POST.get('work')
        experience = request.POST.get('experience')
        graduation_date = request.POST.get('graduation_date')
        Apply.date = date
        Apply.work = work
        Apply.experience = experience
        Apply.graduation_date = graduation_date
        apply = Apply(username=username, email=email, date=date, work=work, experience=experience,
                      graduation_date=graduation_date)
        apply.save()
        messages.info(request,
                      "Your application is applied successfully!.Please check your email for further information")
        return redirect('/')
    return render(request, 'index.html')


def profile(request):
    current_user = request.user.username
    posts = UpdateProfile.objects.filter(username=current_user)
    context = {"posts": posts}
    return render(request, 'profile.html', context)


def about(request):
    return render(request, 'about.html')


def blog(request):
    messages.info(request, " For each user only one blog is allowed")
    if request.method == "POST":
        username1 = request.user.username
        title = request.POST['title']
        blog = request.POST['blog']
        date = request.POST['date']
        Blog.title = title
        Blog.blog = blog
        Blog.date = date
        view_blog = Blog(username=username1, title=title, blog=blog, date=date)
        view_blog.save()
        messages.info(request, " Blog is Updated to My Blogs page  successfully,Go and check once")
    return render(request, 'blog.html')


def view_blog(request):
    messages.info(request, " For each user only one blog is allowed")
    current_user = request.user.username
    jobs = Blog.objects.filter(username=current_user)
    context = {"jobs": jobs}
    return render(request, 'view_blog.html', context)


def resume(request):
    if request.method == "POST":
        username1 = request.user.username
        fullname = request.POST['fullname']
        ssc = request.POST['ssc']
        inter = request.POST['inter']
        degree = request.POST['degree']
        Resume.fullname = fullname
        Resume.ssc = ssc
        Resume.inter = inter
        Resume.degree = degree

        resume_ = Resume(username=username1, fullname=fullname, ssc=ssc, inter=inter, degree=degree)
        resume_.save()
        messages.info(request,
                      " Resume is Updated to database successfully,Don't update again which may lead to mismatch the data!")
    return render(request, 'resume.html')


def resume1(request):
    return render(request, 'resume1.html')


def resume2(request):
    current_user = request.user.username
    resumes = Resume.objects.filter(username=current_user)
    context = {"resumes": resumes}

    return render(request, 'resume2.html', context)


def update_profile(request):
    if request.method == "POST":
        username1 = request.user.username
        email1 = request.user.email
        mobile = request.POST['mobile']
        address1 = request.POST['address1']
        address2 = request.POST['address2']
        bio = request.POST['bio']
        dob = request.POST['dob']
        UpdateProfile.mobile = mobile
        UpdateProfile.address1 = address1
        UpdateProfile.address2 = address2
        UpdateProfile.bio = bio
        UpdateProfile.dob = dob

        user_profile = UpdateProfile(username=username1, email=email1, mobile=mobile, address1=address1,
                                     address2=address2, bio=bio, dob=dob)
        user_profile.save()
        all_members = UpdateProfile.objects.all()
        messages.info(request, " Profile is Updated to database successfully!")
        return render(request, 'profile.html')

    return render(request, 'updateprofile.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        num = request.POST.get('num')
        desc = request.POST.get('desc')
        # print(name,email,numb,desc)
        query = Contact(name=name, email=email, num=num, desc=desc)
        query.save()
        from_email = settings.EMAIL_HOST_USER
        # Email starts here

        return redirect('/')

    return render(request, 'index.html')


