"""
Simplified Tutorial API for code generation approach
"""
import json
from typing import Dict, Any

class TutorialAPI:
    """Simplified API that the LLM can call through code generation"""
    
    def __init__(self):
        self.current_step = "welcome"
        self.completed_steps = set()
        
        # Store all tutorial content in a structured way
        self.content = {
            "welcome": self._get_welcome_content(),
            "python_basics": self._get_python_basics(),
            "setup": self._get_setup_content(),
            "django_install": self._get_django_install(),
            "create_project": self._get_create_project(),
            "create_app": self._get_create_app(),
            "models": self._get_models_content(),
            "admin": self._get_admin_content(),
            "views": self._get_views_content(),
            "test": self._get_test_content(),
        }
        
        # Store code snippets separately for easy access
        self.code_snippets = {
            "models": self._get_models_code(),
            "views": self._get_views_code(),
            "urls": self._get_urls_code(),
            "template": self._get_template_code(),
            "admin": self._get_admin_code(),
        }
    
    def show(self, topic: str) -> str:
        """Show content for a specific topic"""
        if topic in self.content:
            self.completed_steps.add(self.current_step)
            self.current_step = topic
            return self.content[topic]
        elif topic in self.code_snippets:
            return f"```python\n{self.code_snippets[topic]}\n```"
        else:
            return f"Available topics: {', '.join(self.content.keys())}\nCode examples: {', '.join(self.code_snippets.keys())}"
    
    def next_step(self) -> str:
        """Suggest the next logical step"""
        flow = ["welcome", "python_basics", "setup", "django_install", 
                "create_project", "create_app", "models", "admin", "views", "test"]
        
        try:
            current_idx = flow.index(self.current_step)
            if current_idx < len(flow) - 1:
                next_topic = flow[current_idx + 1]
                return f"Ready for the next step? Type: tutorial.show('{next_topic}')"
        except ValueError:
            pass
        
        return "You've completed the tutorial! 🎉"
    
    def help(self, error: str = "") -> str:
        """Provide help for common errors"""
        error_lower = error.lower()
        
        if "django not found" in error_lower or "no module" in error_lower:
            return "Virtual environment not active! Run: source blog_env/bin/activate (Mac/Linux) or blog_env\\Scripts\\activate (Windows)"
        elif "no such table" in error_lower:
            return "Run migrations: python manage.py makemigrations && python manage.py migrate"
        elif "template" in error_lower:
            return "Check template path: blog/templates/blog/post_list.html"
        else:
            return f"Describe your error and I'll help! Common issues: virtual env, migrations, templates"
    
    def _get_welcome_content(self) -> str:
        return """
🎉 Welcome to Django Girls Tutorial Offline! 🎉

We are happy to see you here! :) In this tutorial, we will take you on a journey under the hood of web technologies, offering you a glimpse of all the bits and pieces that need to come together to make the web work as we know it.
As with all unknown things, this is going to be an adventure - but no worries, since you already worked up the courage to be here, you'll be just fine! :)

**What we'll build together:**

A personal blog! By the end, you'll have your very own blog running on your computer where you can write posts, edit them, and share your thoughts with the world.

**Our journey**:
1. Python basics - Let's write some code! (No programming experience needed)
2. Setup environment - Prepare your computer for coding
3. Install Django - Get the Django web framework
4. Create project - Create the foundation
5. Build blog app - Create the blog application
6. Make It Beautiful - Add HTML templates
7. See It Live - Run your blog locally!

**Ready to start?**

• If you're completely new to programming, type in **"learn Python basics"** to start with Python basics.
• If you're ready to jump into Django setup, say **"setup"**, or type the number of the step you want to start with.

Let's create something amazing together! 
"""

    def _get_python_basics(self) -> str:
        return """
🐍 Python Basics - Let's code!

Programming might seem scary, but it's really just giving instructions to your computer. Think of it like writing a recipe - you tell the computer step by step what to do!

**First, in Python we write and 'run' code in a code interpreter. To test out writing your first lines of code we'll start by opening a new terminal.**

- In VS Code we will do this by clicking the split terminal button (looks like two rectangles joined) in the top right of your current terminal. 
- `(TIP: Ask the assitant to explain what a terminal is if you're not sure!)`
- In the new terminal type **python3**. This will open a **code interpreter**.


**🧮 Python as a Calculator**

Try typing these into the interpreter one at a time(press Enter after each):
```python
>>> 2 + 3
>>> 4 * 5  
>>> 10 / 2
>>> 2 ** 3  # This means 2 to the power of 3
```

See? Python knows math! The computer calculated the answers for you.

**📝 Text (Strings)**

Now try typing your name in quotes:
```python
>>> "Your Name Here"
>>> "Hello " + "World"
>>> "Python" * 3  # This repeats the text 3 times!
```

Quotes tell Python "this is text, not math." We call text in programming a "string" - like a string of letters!

**💾 Variables (Storing Things)**

Variables are like labeled boxes where you store information:
```python
>>> name = "Django Girl"
>>> print(name)
>>> age = 25
>>> print(age)
```

The `=` sign doesn't mean "equals" here - it means "put this value in this box."

**📋 Lists (Multiple Things)**

Lists hold multiple items, like a shopping list:
```python
>>> favorite_colors = ["blue", "green", "purple"]
>>> print(favorite_colors[0])  # This gets the first item (we start counting at 0!)
>>> favorite_colors.append("red")  # This adds "red" to the end
>>> print(favorite_colors)
```

**🔄 Doing Things Automatically (Loops)**

Instead of greeting each friend one by one, let's use a loop:
```python
>>> friends = ["Alice", "Bob", "Carol"]
>>> for friend in friends:
...     print("Hello " + friend + "!")
```

This tells Python: "For each friend in my friends list, print hello to them."

**Try these yourself!** Play around in the Code Runner for a few minutes. Make mistakes - that's how we learn!

**When you're ready for the next step, say "I'm ready for Django setup"**

**Need help?** Ask me anything like "What's a variable?" or "How do loops work?"

Ready for Django? Type 'setup'."""

    def _get_setup_content(self) -> str:
        return """
🛠️ Environment Setup

1. Check Python: python3 --version
2. Create project folder: mkdir djangogirls-blog && cd djangogirls-blog
3. Create virtual environment: python3 -m venv blog_env
4. Activate it: source blog_env/bin/activate (Mac/Linux)
5. Upgrade pip: python -m pip install --upgrade pip

See (blog_env) in terminal? Success! Next: tutorial.show('django_install')"""

    def _get_django_install(self) -> str:
        return """📦 Installing Django

Run: pip install django
Check: python -m django --version

Success? Let's create the project: tutorial.show('create_project')"""

    def _get_create_project(self) -> str:
        return """🏗️ Create Django Project

Run: django-admin startproject mysite .
Test: python manage.py runserver
Visit: http://127.0.0.1:8000

See the rocket? 🚀 Stop server (Ctrl+C) and continue: tutorial.show('create_app')"""

    def _get_create_app(self) -> str:
        return """📝 Create Blog App

Run: python manage.py startapp blog

Add to mysite/settings.py INSTALLED_APPS:
'blog',

Next, create the Post model: tutorial.show('models')"""

    def _get_models_content(self) -> str:
        return """📋 Create Post Model

Replace blog/models.py with: tutorial.show('models_code')

Then:
1. python manage.py makemigrations blog
2. python manage.py migrate

Ready for admin? tutorial.show('admin')"""

    def _get_admin_content(self) -> str:
        return """👤 Setup Admin

1. Update blog/admin.py: tutorial.show('admin_code')
2. Create superuser: python manage.py createsuperuser
3. Run server: python manage.py runserver
4. Visit: http://127.0.0.1:8000/admin/

Add some posts! Then: tutorial.show('views')"""

    def _get_views_content(self) -> str:
        return """🎨 Create Views & Templates

1. Update blog/views.py: tutorial.show('views_code')
2. Create blog/urls.py: tutorial.show('urls_code')
3. Create template folder: mkdir -p blog/templates/blog
4. Create template: tutorial.show('template_code')
5. Update main urls.py to include blog.urls

Ready to test? tutorial.show('test')"""

    def _get_test_content(self) -> str:
        return """🚀 Test Your Blog!

Run: python manage.py runserver
Visit: http://127.0.0.1:8000

🎉 CONGRATULATIONS! You built a Django blog!

Need help with errors? tutorial.help('your error message')
Want the next steps? tutorial.next_step()"""

    # Code snippets methods
    def _get_models_code(self) -> str:
        return """from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title"""

    def _get_views_code(self) -> str:
        return """from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})"""

    def _get_urls_code(self) -> str:
        return """from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]"""

    def _get_template_code(self) -> str:
        return """<!DOCTYPE html>
<html>
<head>
    <title>Django Girls Blog</title>
    <style>
        body { font-family: Georgia; margin: 40px; background: #fafafa; }
        .header { background: #ff9400; padding: 20px 40px; color: white; }
        .post { margin-bottom: 30px; padding: 20px; background: white; 
                border-left: 5px solid #ff9400; }
    </style>
</head>
<body>
    <header class="header"><h1>Django Girls Blog</h1></header>
    <main>
        {% for post in posts %}
            <article class="post">
                <h2>{{ post.title }}</h2>
                <p>{{ post.text|linebreaksbr }}</p>
            </article>
        {% empty %}
            <p>No posts yet!</p>
        {% endfor %}
    </main>
</body>
</html>"""

    def _get_admin_code(self) -> str:
        return """from django.contrib import admin
from .models import Post

admin.site.register(Post)"""

# Create global instance
tutorial = TutorialAPI()