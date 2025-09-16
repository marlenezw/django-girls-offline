"""
MCP Server: Django Girls Tutorial
Interactive assistant for Django Girls Tutorial - from Python basics to running a blog locally.
Improved to follow Django Girls teaching methodology more closely.
"""
import os
from mcp.server.fastmcp import FastMCP
import logging

logging.getLogger("mcp").setLevel(logging.WARNING)
logging.getLogger("fastmcp").setLevel(logging.WARNING)

mcp = FastMCP("Django Girls Tutorial")

# --------------------------------------------------------------------------------------
# WELCOME AND INTRODUCTION
# --------------------------------------------------------------------------------------

@mcp.tool(name="welcome_tutorial",   
description="Always call this first when user says hello, hi, or starts the tutorial. Use when user wants to begin.")
def welcome_tutorial() -> str:
    """Welcome message that mirrors Django Girls tutorial enthusiasm and approach."""
    return """
🎉 **Welcome to the Django Girls Tutorial!** 🎉

We are happy to see you here! :) In this tutorial, we will take you on a journey under the hood of web technologies, offering you a glimpse of all the bits and pieces that need to come together to make the web work as we know it.

As with all unknown things, this is going to be an adventure - but no worries, since you already worked up the courage to be here, you'll be just fine! :)

**What we'll build together:**
A personal blog! By the end, you'll have your very own blog running on your computer where you can write posts, edit them, and share your thoughts with the world.

**Our journey:**
1. 🐍 **Python Introduction** - Let's write some code! (No programming experience needed)
2. 🛠️ **Environment Setup** - Prepare your computer for coding
3. 📦 **Install Django** - Get the Django web framework
4. 🏗️ **Start Your Project** - Create the foundation
5. 📝 **Build Your Blog** - Create the blog application
6. 🎨 **Make It Beautiful** - Add HTML templates
7. 🚀 **See It Live** - Run your blog locally!

**Ready to start?**

• If you're completely new to programming, type in **"learn Python"** to start with Python basics.
• If you're ready to jump into Django setup, say **"setup"** to get started right away with setting up Django.

Let's create something amazing together! 
"""

# --------------------------------------------------------------------------------------
# PYTHON BASICS - Enhanced for complete beginners
# --------------------------------------------------------------------------------------

@mcp.tool(name="python_introduction",   
    description="Call this when user says 'Let's learn Python', 'python basics', 'I'm new to programming', or 'start with python'.")
def python_introduction() -> str:
    """Interactive Python introduction following Django Girls methodology."""
    return """
🐍 **Let's write some code!**

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
"""

@mcp.tool(name="explain_programming_concept",   
    description="Call this when user asks about specific programming concepts like 'what is a variable', 'explain functions', 'what are loops', etc.")
def explain_programming_concept(concept: str) -> str:
    """Explain programming concepts in beginner-friendly terms."""
    
    explanations = {
        "variable": """
**Variables - Your Computer's Memory Boxes 📦**

Imagine your computer's memory like a giant warehouse with labeled boxes. A variable is like putting a label on a box so you can find what you stored there later!

```python
>>> name = "Sarah"        # Put "Sarah" in a box labeled "name"
>>> favorite_number = 42  # Put 42 in a box labeled "favorite_number"
>>> print(name)           # Look in the "name" box and show me what's inside
Sarah
```

**Why use variables?**
- You don't have to remember the actual value - just the name!
- You can change what's in the box anytime
- You can use the same value multiple times without retyping it

Think of it like this: instead of saying "the person whose name starts with S and ends with h and is 5 letters long" every time, you just say "name"!
""",
        
        "function": """
**Functions - Your Code Recipes 👩‍🍳**

A function is like a recipe that you can use over and over! Once you write the recipe (function), you can "cook" (run) it anytime.

```python
>>> def greet_person(name):
...     print("Hello " + name + "!")
...     print("Welcome to our website!")

>>> greet_person("Alice")  # Using our recipe with Alice
Hello Alice!
Welcome to our website!

>>> greet_person("Bob")    # Using the same recipe with Bob
Hello Bob!
Welcome to our website!
```

**Why functions are amazing:**
- Write once, use many times
- If you need to change how greetings work, you only change it in one place
- Makes your code organized and easier to understand

It's like having a bread recipe - you don't rewrite the recipe every time you want bread!
""",
        
        "loop": """
**Loops - Making Your Computer Do Repetitive Work 🔄**

Loops tell your computer "do this same thing multiple times." It's like having a really obedient helper!

```python
>>> friends = ["Anna", "Ben", "Cara", "David"]
>>> for friend in friends:
...     print("Happy birthday " + friend + "!")

Happy birthday Anna!
Happy birthday Ben!
Happy birthday Cara!
Happy birthday David!
```

**Without a loop, you'd have to write:**
```python
>>> print("Happy birthday Anna!")
>>> print("Happy birthday Ben!")  
>>> print("Happy birthday Cara!")
>>> print("Happy birthday David!")
```

**Two main types:**
- **for loop**: "Do this for each item in my list"  
- **while loop**: "Keep doing this while something is true"

Loops are why programmers are lazy in a good way - we make the computer do the boring repetitive stuff!
""",
        
        "list": """
**Lists - Your Digital Shopping Lists 📋**

A list in Python is exactly like a shopping list - it holds multiple items in order!

```python
>>> groceries = ["apples", "bread", "milk", "cookies"]
>>> print(groceries[0])    # First item (we start counting at 0)
apples
>>> print(groceries[3])    # Fourth item
cookies
>>> groceries.append("bananas")  # Add to the end
>>> print(groceries)
['apples', 'bread', 'milk', 'cookies', 'bananas']
```

**Cool list tricks:**
```python
>>> len(groceries)         # How many items?
5
>>> groceries.remove("milk")  # Take something off the list
>>> groceries.sort()       # Put in alphabetical order
```

Lists are perfect when you have multiple related things - like a list of friends, a list of blog posts, or a list of favorite movies!
""",
        
        "string": """
**Strings - Text That Computers Understand 📝**

A string is just text - letters, numbers, spaces, and symbols all treated as text.

```python
>>> message = "Hello, world!"
>>> name = "Django Girl"
>>> number_as_text = "123"    # This is text, not a number!
>>> empty_text = ""           # This is an empty string
```

**String magic:**
```python
>>> greeting = "Hello"
>>> name = "Alice" 
>>> full_greeting = greeting + " " + name + "!"  # Joining strings
>>> print(full_greeting)
Hello Alice!

>>> "Python".upper()    # Make it UPPERCASE
PYTHON
>>> "SHOUTING".lower()  # make it lowercase
shouting
>>> len("Hello")        # Count the letters
5
```

**Why quotes matter:**
- `"42"` is text (string)
- `42` is a number
- You can do math with numbers but not with text numbers!
""",

        "error": """
**Errors - Your Computer's Way of Asking for Help 🆘**

Don't panic when you see errors! They're like your computer saying "I don't understand, can you help me?"

**Common errors and what they mean:**

**NameError** - "I don't know what that word means"
```python
>>> print(nme)  # Oops, typo!
NameError: name 'nme' is not defined
# Fix: Check your spelling!
```

**TypeError** - "You're asking me to do something impossible"
```python
>>> "hello" + 5
TypeError: can only concatenate str (not "int") to str  
# Fix: "hello" + str(5) or "hello" + "5"
```

**SyntaxError** - "Your grammar is wrong"
```python
>>> if 5 > 2
SyntaxError: invalid syntax
# Fix: if 5 > 2:  (forgot the colon!)
```

**Remember:** Every programmer sees errors all day long. They're not failures - they're learning opportunities!
"""
    }
    
    concept_lower = concept.lower()
    for key, explanation in explanations.items():
        if key in concept_lower:
            return explanation
    
    return f"""
I'd love to help explain that concept! Here are the programming concepts I can explain in simple terms:

• **variable** - storing information in labeled boxes
• **function** - reusable code recipes  
• **loop** - making the computer repeat tasks
• **list** - holding multiple items in order
• **string** - text that computers understand
• **error** - when something goes wrong (and how to fix it!)

Just ask me something like "explain variables" or "what are functions?"
"""

# --------------------------------------------------------------------------------------
# SETUP AND ENVIRONMENT 
# --------------------------------------------------------------------------------------

@mcp.tool(name="setup_environment",   
    description="Call this when user says 'I'm ready for Django setup', 'let's setup', 'environment setup', or after python_introduction is complete.")
def setup_environment() -> str:
    """Guide through environment setup with clear explanations."""
    return """
🛠️ **Let's prepare your computer for Django!**

Think of this like getting your kitchen ready before cooking - we need the right tools in the right places.

You can use the Code Runner for quick experiments, but for Django setup you'll run a few commands in your regular terminal.

**Step 1: Check if Python is installed**
```bash
python3 --version
```
You should see something like "Python 3.8.5" or higher. If not, visit python.org to install Python first!

**Step 2: Create your project folder**
```bash
mkdir djangogirls-blog
cd djangogirls-blog
```
This creates a new folder called "djangogirls-blog" and enters it. Think of it as creating your project workspace!

**Step 3: Create a virtual environment**
```bash
python3 -m venv blog_env
```

**🤔 What's a virtual environment?**
Imagine you're working on different art projects - you don't want your watercolors mixing with your oil paints! A virtual environment keeps your Django project's tools separate from other projects.

**Step 4: Activate your virtual environment**

**On Mac/Linux:**
```bash
source blog_env/bin/activate
```

**On Windows:**
```bash
blog_env\\Scripts\\activate
```

**Success!** You should see `(blog_env)` at the beginning of your command line. This means you're now working inside your project's virtual environment!

**Step 5: Upgrade pip (Python's package installer)**
```bash
python -m pip install --upgrade pip
```

**When you're done with these steps, say "environment is ready"** and we'll install Django next!

**Stuck on something?** Just ask! Common issues: "python3 not found", "permission denied", or "virtual environment not activating"
"""

@mcp.tool(name="verify_environment",   
    description="Call this when user says 'environment is ready', 'check my setup', or after setup_environment steps are completed.")
def verify_environment() -> str:
    """Verify the environment setup is working correctly."""
    
    checks = {
        "python_installed": False,
        "python_version": None,
        "virtual_env_active": False,
        "pip_available": False
    }
    
    # Check Python
    result = run_shell_command("python3 --version")
    if result["success"]:
        checks["python_installed"] = True
        checks["python_version"] = result["output"].strip()
    else:
        # Try python instead of python3 (Windows)
        result = run_shell_command("python --version")
        if result["success"]:
            checks["python_installed"] = True
            checks["python_version"] = result["output"].strip()
    
    # Check if in virtual environment
    checks["virtual_env_active"] = os.environ.get("VIRTUAL_ENV") is not None
    
    # Check pip
    pip_result = run_shell_command("pip --version")
    checks["pip_available"] = pip_result["success"]
    
    status_report = "🔍 **Environment Check Results:**\n\n"
    
    if checks["python_installed"]:
        status_report += f"✅ Python is installed: {checks['python_version']}\n"
    else:
        status_report += "❌ Python not found. Please install Python from python.org\n"
    
    if checks["virtual_env_active"]:
        status_report += "✅ Virtual environment is active - great job!\n"
    else:
        status_report += "⚠️  Virtual environment not active. Run the activation command again:\n"
        status_report += "   Mac/Linux: `source blog_env/bin/activate`\n"
        status_report += "   Windows: `blog_env\\Scripts\\activate`\n"
    
    if checks["pip_available"]:
        status_report += "✅ Pip is available for installing packages\n"
    else:
        status_report += "❌ Pip not found. This usually fixes itself when virtual environment is active.\n"
    
    if checks["python_installed"] and checks["virtual_env_active"] and checks["pip_available"]:
        status_report += "\n🎉 **Everything looks great! Ready to install Django!**\n"
        status_report += "\nSay **'install Django'** to continue!"
    else:
        status_report += "\n🔧 Please fix the issues above before continuing. Need help? Just ask!"
    
    return status_report

# --------------------------------------------------------------------------------------
# DJANGO INSTALLATION AND PROJECT CREATION
# --------------------------------------------------------------------------------------

@mcp.tool(name="install_django",   
    description="Call this when user says 'install Django', 'ready for Django', or after verify_environment shows success.")
def install_django() -> str:
    """Guide through Django installation."""
    return """
📦 **Let's install Django!**

Django is like a powerful toolkit for building websites. Instead of building everything from scratch, Django gives you pre-made components that work together beautifully!

**Install Django:**
```bash
pip install django
```

This might take a minute - Django is downloading along with everything it needs to work.

**Verify Django is installed:**
```bash
python -m django --version
```

You should see something like "5.0.1" or similar. This is Django's version number.

**🎉 Success!** Django is now installed in your virtual environment!

**What just happened?**
- `pip` is Python's package installer (like an app store for Python tools)
- We downloaded Django and all its dependencies
- Django is now available for your project, but won't interfere with other Python projects on your computer (thanks to our virtual environment!)

**Ready for the next step?** Say **"create Django project"** and we'll start building your blog!

**Having issues?** Common problems:
- "pip not found" → Make sure your virtual environment is activated
- "permission denied" → Virtual environment should fix this
- Takes forever → This is normal for the first Django install!
"""

@mcp.tool(name="create_django_project",   
    description="Call this when user says 'create Django project', 'start project', or after install_django is complete.")
def create_django_project() -> str:
    """Guide through creating the Django project."""
    return """
🏗️ **Let's create your Django project!**

**Create the project:**
```bash
django-admin startproject mysite .
```

**⚠️ Important:** Don't forget the dot (.) at the end! It tells Django "create the project files right here in my current folder."

**What just happened?**
Django just created the skeleton of your web application! Let's see what it built:

```bash
ls  # (or 'dir' on Windows)
```

You should see:
- `manage.py` - Your project's command center (like a remote control)
- `mysite/` folder with:
  - `settings.py` - Your project's configuration file
  - `urls.py` - Your website's navigation map  
  - `wsgi.py` - Helps your site talk to web servers

**Test that it works:**
```bash
python manage.py runserver
```

**🎉 If you see "Starting development server at http://127.0.0.1:8000/"**, it's working!

Open your web browser and go to: `http://127.0.0.1:8000`

You should see a "Congratulations!" page with a rocket! 🚀

**Stop the server:** Press `Ctrl+C` in your terminal when you want to stop it.

**🤔 What's happening here?**
- `manage.py` is your project manager - it can start servers, create database tables, and more
- `runserver` starts a mini web server on your computer
- `127.0.0.1:8000` means "your own computer, port 8000" 

**Ready for the next step?** Say **"create blog app"** and we'll start building your actual blog!
"""

# --------------------------------------------------------------------------------------
# BLOG APPLICATION CREATION
# --------------------------------------------------------------------------------------

@mcp.tool(name="create_blog_app",   
    description="Call this when user says 'create blog app', 'add blog', or after create_django_project is complete.")
def create_blog_app() -> str:
    """Guide through creating the blog application."""
    return """
📝 **Let's create your blog application!**

**🤔 Project vs App - What's the difference?**
- **Project (mysite)**: Your whole website - like the entire building
- **App (blog)**: One feature of your website - like one room in the building

A website can have many apps: blog, user accounts, photo gallery, etc. Today we're building the blog room!

**Create the blog app:**
```bash
python manage.py startapp blog
```

**See what was created:**
```bash
ls blog/  # (or 'dir blog' on Windows)
```

You should see files like:
- `models.py` - Where we define what our blog posts look like
- `views.py` - The logic that decides what to show users
- `admin.py` - For managing your blog from Django's admin panel

**Tell Django about your new app:**

Open `mysite/settings.py` in your code editor and find the `INSTALLED_APPS` section. It looks like:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

Add `'blog',` to the end (don't forget the comma!):

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
]
```

**💾 Save the file!**

**Why this step matters:**
This tells Django "Hey, I have a new app called 'blog' that you need to know about!" Now Django will look for models, views, and templates in your blog app.

**Ready for the next step?** Say **"create post model"** and we'll define what a blog post looks like!
"""

# --------------------------------------------------------------------------------------
# DATABASE MODELS
# --------------------------------------------------------------------------------------

@mcp.tool(name="create_post_model",   
    description="Call this when user says 'create post model', 'define blog post', or after create_blog_app is complete.")
def create_post_model() -> str:
    """Guide through creating the Post model."""
    return """
📋 **Let's define what a blog post looks like!**

**🤔 What's a model?**
A model is like a blueprint that tells Django "here's the information I want to store about each blog post." Think of it like a form with different fields: title, content, author, date, etc.

**Open `blog/models.py` and replace everything with:**

```python
from django.db import models
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
        return self.title
```

**Let's understand each line:**

- `author = models.ForeignKey(User...)` - Links each post to a user (who wrote it)
- `title = models.CharField(max_length=200)` - Post title (up to 200 characters)
- `text = models.TextField()` - The main content (unlimited length)
- `created_date = models.DateTimeField(...)` - When the post was created
- `published_date = models.DateTimeField(...)` - When it was published (can be empty)

**The special methods:**
- `publish(self)` - A function to publish a post (sets the published date)
- `__str__(self)` - Tells Python how to display a Post (just show the title)

**💾 Save the file!**

**Create the database table:**
```bash
python manage.py makemigrations blog
```

This creates a "migration file" - like a blueprint for creating the database table.

```bash
python manage.py migrate
```

This actually creates the table in your database!

**🎉 Success!** Your database now has a table ready to store blog posts!

**Ready for the next step?** Say **"setup admin"** and we'll create a way to add blog posts through Django's admin panel!
"""

# --------------------------------------------------------------------------------------
# ADMIN INTERFACE
# --------------------------------------------------------------------------------------

@mcp.tool(name="setup_admin",   
    description="Call this when user says 'setup admin', 'admin panel', or after create_post_model is complete.")
def setup_admin() -> str:
    """Guide through setting up Django admin."""
    return """
👤 **Let's create Django's admin panel!**

**🤔 What's the admin panel?**
Django comes with a built-in admin interface - like a control panel for your website! You can add, edit, and delete blog posts without touching any code.

**Step 1: Register your Post model**

Open `blog/admin.py` and replace everything with:

```python
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

This tells Django "show the Post model in the admin panel."

**💾 Save the file!**

**Step 2: Create an admin user**
```bash
python manage.py createsuperuser
```

You'll be asked for:
- **Username**: Choose anything (like "admin" or your name)
- **Email**: Can be fake for learning (like "me@example.com")  
- **Password**: Choose something secure (you won't see the letters as you type - that's normal!)
- **Password (again)**: Type the same password

**Step 3: Test the admin panel**

Start your server:
```bash
python manage.py runserver
```

**Visit the admin panel:**
Open your browser and go to: `http://127.0.0.1:8000/admin/`

**Log in** with the username and password you just created!

**🎉 You should see:**
- A "Blog" section with "Posts"
- Click "Posts" to see your (empty) list of blog posts
- Click "Add Post" to create your first blog post!

**Create a test post:**
1. Click "Add Post"
2. Fill in a title (like "My First Post!")
3. Write some text (like "Hello, Django world!")
4. Select yourself as the author
5. Click "Save"

**🎊 Congratulations!** You just created your first blog post through Django's admin!

**Ready for the next step?** Say **"create blog views"** and we'll make these posts show up on your website!
"""

# --------------------------------------------------------------------------------------
# VIEWS AND TEMPLATES
# --------------------------------------------------------------------------------------

@mcp.tool(name="create_blog_views",   
    description="Call this when user says 'create blog views', 'show posts', or after setup_admin is complete.")
def create_blog_views() -> str:
    """Guide through creating views and templates."""
    return """
🎨 **Let's make your blog posts visible on your website!**

**🤔 How Django shows web pages:**
1. **URLs** - Map web addresses to views (like a phone book)
2. **Views** - Get data and decide what to show (like a waiter taking your order)
3. **Templates** - The HTML that users actually see (like the menu design)

**Step 1: Create the view function**

Open `blog/views.py` and replace everything with:

```python
from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
```

**What this code does:**
- Gets all published posts from the database
- Puts them in chronological order  
- Sends them to a template called 'post_list.html'

**💾 Save the file!**

**Step 2: Create template folders**
```bash
mkdir -p blog/templates/blog
```

This creates nested folders: `blog/templates/blog/`

**Step 3: Create the HTML template**

Create a new file `blog/templates/blog/post_list.html` with:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Django Girls Blog</title>
    <style>
        body {
            font-family: 'Georgia', serif;
            margin: 40px;
            background-color: #fafafa;
        }
        .header {
            background-color: #ff9400;
            margin-top: 0;
            padding: 20px 40px;
            color: white;
        }
        .post {
            margin-bottom: 30px;
            padding: 20px;
            background: white;
            border-left: 5px solid #ff9400;
        }
        .date {
            color: #828282;
        }
    </style>
</head>
<body>
    <header class="header">
        <h1>Django Girls Blog</h1>
    </header>

    <main>
        {% for post in posts %}
            <article class="post">
                <h2>{{ post.title }}</h2>
                <p class="date">Published: {{ post.published_date }}</p>
                <p>{{ post.text|linebreaksbr }}</p>
            </article>
        {% empty %}
            <p>No blog posts yet. <a href="/admin/">Add some posts in the admin!</a></p>
        {% endfor %}
    </main>
</body>
</html>
```

**💾 Save the file!**

**Step 4: Connect URLs**

Create `blog/urls.py` with:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]
```

**Step 5: Connect to main URLs**

Edit `mysite/urls.py` to look like:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]
```

**Ready for the next step?** Say **"test my blog"** and we'll see your blog in action!
"""

@mcp.tool(name="test_blog",   
    description="Call this when user says 'test my blog', 'run server', 'see my blog', or after create_blog_views is complete.")
def test_blog() -> str:
    """Guide through testing the complete blog."""
    return """
🚀 **Let's see your blog in action!**

**Start your server:**
```bash
python manage.py runserver
```

**Visit your blog:**
Open your browser and go to: `http://127.0.0.1:8000`

**🎉 What you should see:**
- Your beautiful blog homepage!
- Any posts you created in the admin should appear here
- If you haven't created posts yet, you'll see a helpful message with a link to the admin

**🎊 CONGRATULATIONS! 🎊**

You've just built a complete Django blog from scratch! Here's what you accomplished:

✅ **Learned Python basics** - Variables, functions, loops
✅ **Set up your development environment** - Virtual environment, Django installation  
✅ **Created a Django project** - Your website's foundation
✅ **Built a blog app** - A specific feature of your site
✅ **Designed database models** - How your data is structured
✅ **Set up admin interface** - Easy way to manage content
✅ **Created views and templates** - What visitors see
✅ **Connected everything with URLs** - How pages are found

**🎯 What you can do now:**
- Add more blog posts through `/admin/`
- Customize the design by editing the CSS in your template
- Add more features like comments, categories, or user profiles
- Deploy your blog online so the world can see it!

**Want to keep learning?** Django has tons more features:
- User authentication (login/logout)
- Image uploads
- Search functionality  
- RSS feeds
- And much more!

**🏆 You're officially a Django developer!** 

**Need help with anything?** Ask me about:
- "How do I customize the design?"
- "How do I add more features?"
- "What should I learn next?"
- "How do I put this online?"
"""

if __name__ == "__main__":
    mcp.run()
