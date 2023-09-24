from django.views.generic.base import ContextMixin
from .models import Category



class CategoryMixin(ContextMixin):

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        return context