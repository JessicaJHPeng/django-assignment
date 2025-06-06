# Setup Instructions

You can get started with this just like any other Django app. Everything in this project is pure Django and vanilla Javascript.

* No external JavaScript or frontend frameworks are required.
* Dynamic autocomplete + tag filtering is implemented with **vanilla JavaScript**.
* Tags and categories can be created either via admin or the JSON import.

### Requirements

* Python 3.8+
* pip (Python package manager)
* Virtualenv (recommended)

```bash
# 1. Clone the repository
git clone <your-repo-url>
cd <your-project-folder>

# 2. Set up a virtual environment
python -m venv venv
source venv/bin/activate       # On Windows use: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply database migrations
python manage.py migrate

# 5. Create an admin user (optional, for admin interface)
python manage.py createsuperuser

# 6. Run the development server
python manage.py runserver
```

---

### Import Sample Data

If you want to batch upload JSON data, you can visit `/import/` and upload a JSON file via the provided interface.
If you want to use the admin interface, you can log in with these credentials:
user jessica-admin
pass TakeHome!20250603

---

### URLs of Interest

| URL        | Description                             |
| ---------- | --------------------------------------- |
| `/admin/`  | Django admin (manage models manually)   |
| `/search/` | Tag-based product search UI             |
| `/all/`    | View all products, tags, and categories |
| `/import/`    | Import JSON files into the database |

# AI Attribution

I did not use AI to generate any part of the code. I wrote all the code myself using the documentation and some online resources as a reference, and I did not copy any one else's code. I only used ChatGPT for some assistance in commenting code (I manually reviewed all of its comments), ask questions about Django concepts and syntax, and generate products to populate the database with.


# Other Comments

- Right now, categories are set to cascade on delete, meaning if a category is deleted all of the products in that category will be too. In a real environment, there could also be another option of moving all products of a deleted category to a "Misc." category to avoid losing track of products that are still in stock.
- I considered having categories and tags be in a many-to-many relationship to each other so that each tag can only apply to a subset of categories, thus narrowing down the tag search in a real environment with thousands of tags, but the more I thought about it the more restrictive it seemed. For example, right now the 120-V and 240-V tags only apply to Electrical Components and Tools, but what if an admin wanted to make a new Machines category or add the voltage tags to Equipment? If an admin wanted to make a new category, would they have to manually select every single tag that could possibly apply to the new category? Eventually I just decided to go with my original decision of having Categories and Tags not be directly related.