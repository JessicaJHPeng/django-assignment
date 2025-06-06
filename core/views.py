from django.shortcuts import render, HttpResponse
from .models import *
import json
from django.core import serializers
from django.db.models import Q

# Simple test view to render the homepage
def test(request):
    return render(request, 'home.html')

# View to display all products, categories, and tags in a raw list
def all(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()
    return render(request, "allentries.html", {"products": products, "categories": categories, "tags": tags})

# View for product search with optional filters on description, category, and tags
def search(request):
    # Get query parameters
    query = request.GET.get('description', '')      # Text search (name or description)
    category_id = request.GET.get('category', '')    # Selected category ID
    tag_query = request.GET.get('tags', '')          # Comma-separated list of tag names
    selected_tags = [t.strip() for t in tag_query.split(',') if t.strip()]  # Cleaned list

    products = Product.objects.all()

    # Filter by name or description using Q for OR logic
    if query:
        products = products.filter(
            Q(description__icontains=query) |
            Q(name__icontains=query)
        )

    # Filter by selected category
    if category_id:
        products = products.filter(category_id=category_id)

    # Filter by all selected tags (AND logic)
    if selected_tags:
        for tag_name in selected_tags:
            products = products.filter(tags__name=tag_name)
        products = products.distinct()  # Avoid duplicate products from joins

    # Fetch all categories and tag names for the search form
    categories = Category.objects.all()
    tags = Tag.objects.values_list('name', flat=True)

    return render(request, 'search.html', {
        'products': products,
        'categories': categories,
        'tags': list(tags),
    })


# View for importing product data from an uploaded JSON file
def import_data(request):
    if request.method == 'POST' and request.FILES.get('json_file'):
        json_file = request.FILES['json_file']
        data = json.load(json_file)

        for item in data:
            # Look up or create the category
            category_name = item['category']
            category, _ = Category.objects.get_or_create(name=category_name)

            # Create the product
            product = Product.objects.create(
                name=item['name'],
                description=item['description'],
                category=category
            )

            # Look up or create each tag and associate with product
            for tag_name in item['tags']:
                tag, _ = Tag.objects.get_or_create(name=tag_name)
                product.tags.add(tag)

        return render(request, 'success.html')
    return render(request, 'import.html')
