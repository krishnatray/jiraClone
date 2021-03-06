# Jira Clone

### Project link Github
* https://github.com/nuthanc/jiraClone/projects/1

### Guide for reference
* https://docs.djangoproject.com/en/3.0/intro/tutorial01/
* https://github.com/nuthanc/simplesocial

### Structure sketch
* accounts
* projects 
* issues (similar to posts)
* comments

### Project setup
* conda create --name jiraEnv django
* source activate jiraEnv
* django-admin startproject jiraClone
* python manage.py startapp accounts
* python manage.py startapp projects
* python manage.py startapp issues
* python manage.py startapp comments
* Adding the apps in settings.py

### Issues setup

##### Basic
* Title
* Issue_no
* Type: Story, Bug, Task
* Status: Open, In Progress, Closed
* Details

##### Advanced
* Reporter: Dependency with Accounts
* Assignee: Dependency with Accounts
* Links to other issues
* Attachments

#### Model, Template, View and Url setup of Issues
* issues/templates/issues/issue_form.html
* project urls.py and issues urls.py
* issues models.py and views.py
* Styling issue_form using django-crispy-forms
  * https://simpleisbetterthancomplex.com/tutorial/2018/08/13/how-to-use-bootstrap-4-forms-with-django.html

#### DetailView for Issues
* issues views.py, urls.py and issue_detail.html
* Complete with issue_detail.html and start issue_list.html
* Add get_context_data in IssueDetail view for passing the className to display appropriate colors for Issue type

#### ListView for Issues
* Next loop issue_list in views.py and attach className to each issue to give colors in ListView

#### UpdateView for Issues
* views.py and urls.py
* https://docs.djangoproject.com/en/3.0/topics/class-based-views/generic-editing/

#### DeleteView for Issues
* views.py, issue_confirm_delete urls.py

#### String representation for model
* Add String representation for model so that it is displayed appropriately in the Admin page

#### Admin templates from lecture
* Project dir -> templates -> admin -> template files
* Django source code: https://github.com/django/django
* https://github.com/django/django/tree/master/django/contrib/admin/templates
* Registration page: https://github.com/django/django/tree/master/django/contrib/admin/templates/registration
* Admin page: https://github.com/django/django/tree/master/django/contrib/admin/templates/admin
* Need to have same directory structure as above since we are overriding
* base_site.html which extends admin/base.html
* We just really want to play with base_site.html
* So copy that code to admin/base_site.html(Note: Same template name should be used)

#### Changing DetailView for Admin page
* Go to particular App's(issues in our case) admin.py
* Create a class(Class name Convention: Name of model appended with Admin) which inherits from admin.ModelAdmin
* Add field attributes
* Register this class along with the model
* readonly_fields should be added in 2 places(fields and readonly_fields)

#### Adding search to admin
* Same as ordering fields, create a class with the convention mentioned there
* Add search_fields attribute
* Need to register the class along with the model

#### Adding filters to admin
* Register and class same as Adding search to Admin.
* Add list_filter attribute 

#### Adding fields to ListView
* list_display attribute in admin.py Custom class registered above

#### Editing from ListView of admin
* First they have to displayed in list_display to edit it
* Attribute of list_editable in IssueAdmin class
* Editing in ListView without going to DetailView

#### Google SignIn
* Set up Google login to sign up users on Django
* https://medium.com/@whizzoe/in-5-mins-set-up-google-login-to-sign-up-users-on-django-e71d5c38f5d5
* https://realpython.com/adding-social-authentication-to-django/
* https://django-allauth.readthedocs.io/en/latest/templates.html  
* https://dev.to/gajesh/the-complete-django-allauth-guide-la3
* https://django-allauth.readthedocs.io/en/latest/forms.html#account-forms
```python
pip install django-allauth
```
* Update settings.py
* Use the above 2 links and complete authentication
* Solved the issue of Google Auth not appearing by adding Add all sites in Social applications

#### Google Sign in problem
* django.contrib.sites.models.Site.DoesNotExist: Site matching query does not exist
* Changing the siteid worked

### Social Network Login Failure
* Go to localhost admin and Remvoe and Add localhost

### Override all-auth login
* Add account login.html in project templates
* Add static directory and css styling for login

### Add accounts app
* Ref links
```
https://django-allauth.readthedocs.io/en/latest/forms.html#login-allauth-account-forms-loginform
https://github.com/nuthanc/django_my_blog/blob/master/blog_app/forms.py

https://github.com/nuthanc/simplesocial/tree/master/accounts

https://github.com/nuthanc/django_my_blog/blob/master/blog_app/forms.py

https://wsvincent.com/django-allauth-tutorial-custom-user-model/

* Main link below
https://github.com/nuthanc/simplesocial/blob/master/posts/views.py
```

### LoginRequired Mixin for Authentication
* Ref link: https://github.com/nuthanc/django_my_blog/blob/master/blog_app/views.py
* login_url and redirect_field_name can be given(optional)

### Adding new field to existing model
* https://stackoverflow.com/questions/24311993/how-to-add-a-new-field-to-a-model-with-new-django-migrations

### Debug migrate issue
```
django.db.utils.IntegrityError: The row in table 'django_admin_log' with primary key '1' has an invalid foreign key: django_admin_log.user_id contains a value '1' that does not have a corresponding value in auth_user.id
```

```
python manage.py dbshell 
.tables
select * from django_admin_log;
select user_id from django_admin_log where id=1;
# To get column names, use the below
PRAGMA table_info(django_admin_log);

0|id|integer|1||1
1|action_time|datetime|1||0
2|object_id|text|0||0
3|object_repr|varchar(200)|1||0
4|change_message|text|1||0
5|content_type_id|integer|0||0
6|user_id|integer|1||0
7|action_flag|smallint unsigned|1||0

UPDATE django_admin_log SET user_id=5 where user_id=1;
```

```py
python manage.py shell 
from issues.models import Issue
print(Issue.objects.all())
```
* Give some default value to user which needs to be an object
* https://stackoverflow.com/questions/42733221/django-db-utils-integrityerror-not-null-constraint-failed-products-product-ima

### Deleted migration and db and started again
* Deleted the migrations and sqlite3 db
* Applied makemigrations and migrate to the whole application
* Also had to make migrations to issues
* Created superuser
* Followed the steps given in Medium link(Refer above)
* Changed SITE_ID in settings.py
* Add issues migration to eliminate table not found error

### Add model to comments
* Ref link: https://tutorial-extensions.djangogirls.org/en/homework_create_more_models/
* Create model in comments models.py
* https://stackoverflow.com/questions/1737017/django-auto-now-and-auto-now-add
* The related_name option in models.ForeignKey allows us to have access to comments from within the Issue model.
* Register Comment in comments admin.py
* Next task: Add comments in posts templates and either create Views for comments or Form in forms.py
* https://djangocentral.com/creating-comments-system-with-django/
* Create forms.py in comments
* Modify IssueDetail to issue_detail and modify url for that

### Display CommentForm in post details page
* Add post request in issue_detail function
* Pass comment_form to issue_detail.html
* Add bootstrap classes in CommentForm widgets attrs
* Clear the form after submitting by adding comment_form again, but if refresh is hit, it causes duplication
* So redirect to same page

### AJAX requests
* Ref links: 
* https://www.pluralsight.com/guides/work-with-ajax-django
* https://dev.to/coderasha/how-to-send-django-form-with-ajax-4bpo
* https://www.codingforentrepreneurs.com/blog/ajaxify-django-forms
* https://docs.djangoproject.com/en/3.0/topics/class-based-views/generic-editing/#ajax-example

### Comments AJAX request
* Include jQuery in base.html
* Add block javascript in issue_detail.html
* Give comment form an id of comment-form

### Serialize error fixed
* Tried giving instance which was empty cause save returned already to new_comment
* But ser_instance is the below
```
instance: "[{"model": "comments.comment", "pk": 56, "fields": {"content": "Another check", "issue": 4, "user": 3, "created": "2020-06-09T19:17:03.053Z", "modified": "2020-06-09T19:17:03.053Z"}}]"
```
* So need custom serialization

### Custom serialization
* Use response_data to send JSON response
* Change comment created format using strftime
* Link: https://stackoverflow.com/questions/39609234/django-ajax-response-date-and-time-format
* Change parsing in AJAX response
```json
"python.linting.pylintArgs": ["--load-plugins", "pylint_django"]
```
* Added custom serialization with response_data as object, custom serialize of User and then jsonResponse

### Refactor Comments
* Move comment jsonResponse to ajax_comment_json_response function
* Move existing comments from issue_detail to comment_list
* Move comment form from issue_detail to comment_form

### Comment delete
* https://stackoverflow.com/questions/17475324/django-deleteview-without-confirmation-template
* Need to add id to comments just like
https://github.com/realpython/django-form-fun/blob/master/part4/talk_project/static/scripts/main.js#L83
* Had to give id's to comment delete button as well as comment list main div to extract the id and hide the id
* Also, in views.py had to decode the request body as there is no data in request.DELETE or request.POST
* Had to get getCookie function from Django docs for AJAX requests

### Comments delete authorized
* https://stackoverflow.com/questions/43807625/django-ajax-return-error-messages
* Don't hide for invalid

### Refactor js in issue_detail to js folders
* Done

### Show Delete only to Created User
* Changes in comment_list.html
* The user is always attached to the request, in your templates you can do the following:
```jinja
{% if user.is_authenticated %}
{% endif %}
```
* Add proper spacing in comment_list.html after Delete button

### Comment Edit
* New file of commentEdit.js
* Changes in 
  * commentPost.js
  * comment_list.html
  * views.py of issues