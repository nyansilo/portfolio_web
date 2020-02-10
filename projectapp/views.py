from django.core.paginator import Paginator
from django.db.models import Count
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.contrib import messages


from .models import Project , ProjectImages , Category




# Create your views here.

def projectlist(request):
#def projectlist(request , category_slug=None):
    #category = None
    projectlist = Project.objects.all()
    """
    categorylist = Category.objects.annotate(total_projects=Count('project'))

    if category_slug :
        category = get_object_or_404(Category ,slug=category_slug)
        projectlist = projectlist.filter(category=category)
   
    search_query = request.GET.get('q')
    if search_query :
        projectlist = projectlist.filter(
            Q(name__icontains = search_query) |
            Q(description__icontains = search_query)|
            Q(condition__icontains = search_query)|
            Q(brand__brand_name__icontains = search_query) |
            Q(category__category_name__icontains = search_query) 
        )

    paginator = Paginator(projectlist, 1) # Show 25 contacts per page
    page = request.GET.get('page')

    projectlist = paginator.get_page(page)
    """
    template = 'project/project_list.html'
    context = {'project_list' : projectlist }

    #context = {'project_list' : projectlist , 'category_list' : categorylist ,'category' : category }
    return render(request , template , context)



def projectdetail(request , project_slug):
    print(project_slug)
    projectdetail = Project.objects.get(slug=project_slug)
    projectimages = ProjectImages.objects.filter(project=projectdetail)
    template = 'project/project_detail.html'
    context = {'project_detail' : projectdetail, 'project_images' : projectimages}
    return render(request , template , context)


    