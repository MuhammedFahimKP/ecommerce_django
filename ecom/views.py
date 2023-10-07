from typing import Any
from django.views import generic



class Home(generic.TemplateView):
    
    template_name = "home.html"
    
     
    def get_context_data(self, *args,**kwargs) -> dict[str, Any]:
        
        context = super(Home, self).get_context_data(*args,**kwargs)
        context['list'] = [1,2,3,4,6,7]
        return context
    




# def Home(request):
#     return render(request,'base.html')