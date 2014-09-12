Fuzzing
========

## Setting up the project environment:

0. SSH Key
    To be able to get the repo, you will have to create an ssh key[HOWTO-github](https://help.github.com/articles/generating-ssh-keys) or [HOWTO-bitbucket](https://confluence.atlassian.com/pages/viewpage.action?pageId=270827678)

1. Clone the repository:
> git clone <repo:url>

2. Get into it:
> cd fuzzing

3. Create a virtual environment ([virtualenv](http://rukbottoland.com/blog/tutorial-de-python-virtualenv/)) Suggestion (install virtualenvwrapper).
> `virtualenv <env_name>`

4. Activate the virtualenv(this is where you will install your python dep.):
> `source <env_name>/bin/activate`

5. Install python dependecies for specific environment(local/production)
> `pip install -r requirements/local/production.txt`

5. Bower(front-end packages) dependencies [bower](http://bower.io)
> `npm install bower -g`

6. Get into django project
> `cd src`

7. Install Node packages:
> `npm install`

8. Bower install (install packages described in bower.json)
> `bower install`

9. Passwords are secrets
> Some configuration passwords used by django settings are stored as environment variables. This means you have to export thos variables before running the server.
Ask the right guy them.

> VIRTUAL_ENV="<path_to_your_virtual_envirionment>"
>
> export VIRTUAL_ENV
>
> export fuzzing_KEY="<secret_key_generated_by_django.admin.py startproject"
> For testing you can use a [dummy secret key](http://www.miniwebtool.com/django-secret-key-generator/)
>
> export EMAIL_HOST_PASSWORD="" #gmail account password
>
> export TEST_/DB_ADMIN_PASS="" #your postgresql/django superuser pass


10. Now you are ready to run the application. Remember to have the virtualenv active.

> `python manage.py runserver [port] --settings=settings.local/production`


11. Static content

> Grunt is used to minify, concat and compile the static assets.

> `grunt css` combines and minifies the vendor and application css files. This two files are used in production.

> `grunt js` combines and minifies the vendor and application js files.

For development just run `grunt watch` and any changes in your javascript or sass files will be automatically, compiled.

> `grunt build` will prepare the files needed in production, such as minified css and js files.

11. If you are going to keep logs for gunicorn or nginx make a folder in the following route:
``



## Tests

<!-- We are using django_nose which provides the `nose` module with some extra utilities to work with Django.

To run execute the tests, use:
`./manage.py test tests/<folder>/<test_*.py>`
 -->


## Translations

The folder `locale` contains the languages with the `.po` files to translate.
This folder is specified in the settings file with `LOCALE_PATH`.

Run `django-admin.py makemessages -l <lang>` to generate the strings from your code and then translate them.

After that you can compile the messages by running `django-amdin.py compilemessages`.
This command compiles .po files created by `makemessages` to .mo files for use with the builtin gettext support.

Use for example [poedit](http://www.poedit.net/download.php) to open and translate the files.



## Deployment

####Services Running:

- Nginx
- Supervisor
- Gunicorn
- Postgres

