[![Build Status](https://travis-ci.org/LWilsonDev/beer-list.svg?branch=master)](https://travis-ci.org/LWilsonDev/beer-list)

# The Beer List

### A place to discover beers, keep track of your favourites, and read reviews

This is a Django app, where users can log in securely, keep track of their favourite beers, and browse other user's beerlists for inspiration.
With the growing trend for craft beer and independant breweries, I wanted to create an app where users can review the beers they have tried, and keep track of their favourites.
**View the app [here](https://the-beer-list-app.herokuapp.com/)**

**View files [here](https://github.com/LWilsonDev/beer-list)**


# UX

I wanted the design of the app to reflect the current trend for craft beers, with minimalist colour scheme and modern design. I was careful to not allow too much 'feature-creep' to clutter the UX, aiming to deliver on the core purpose of the app: a place to review beers.
I wanted the app to be a pleasure to use, allowing the photos of the beers and users own uploaded photos to take center stage, rather than use lots of background images.

To keep the UX simple, I kept a similar layout and consistent style across the site's pages.



#### User stories:

- I want to browse through beers and read reviews without having to sign up
- I want to keep my own list of favourite beers, and see all the reviews I have written
- If I find a reviewer who's style/beer choices I like, I want to see all his/her reviews
- I want to use the app to keep track of the beers I have tasted, and upload my own photo of the beer to show the colour/style
- I want to search the database to find a specific beer to see how others have rated it
- If the beer I am drinking is not on the app, I want to add it
- I want to be able to search the app by beer, brewery, and country to find new beers for me to try

#### Wireframe/mockups

I created wireframe sketches on [invision](https://www.invisionapp.com/) to get an idea of layout before starting to code. They can be found [here](https://github.com/LWilsonDev/beer-list/blob/master/wireframe.jpg)

## Features

#### Homepage:

- A simple layout with animated text to introduce users to app. Scrolling down, there is a sample of the most recently added beers.
- A navbar offers login/sign up or browse all beers.
- A large search input for a quick and easy search of the database

#### All beers:

- A paginated list of all the beers in the database
- Each beer can be clicked on to see the detailed page for that beer

#### Beer Detail:

- Each beer has a detail page, showing any reviews that have been left.
- If a User is not logged in, there is a reminder to login if you want to leave a review
- If the user is logged in, they can 'like' the beer. This is an unobtrusive like button that does not require a page reload thanks to AJAX. The beer 'like' count will immediately update.
- If the user is logged in they can edit the beer details or add a review.
- Also on this page, similar beers (beers containing the same 'tags') are listed alongside, for inspiration!

#### Profile:

- Each user has a profile page where any beers they have 'liked' are listed, along with all their reviews.
- A list of similar beers to their 'likes' is displayed for inspiration.

#### People:

- A list of all users. Clicking on the username brings you to that users' profile.

#### Edit Beer:

- Only the original user who added the beer can delete a beer, but any logged-in user can update the details. This is because beers can be added with only minimal info - in order to speed up the process, but it is nice to be able to add extra details and a photo at a later date, or allow others to do so. 

#### Leave a Review

- Logged-in users can leave a review from the beer detail page. The button launches a bootstrap modal, eliminating the need to navigate away from the page.
- Reviewers can leave a full review with their own uploaded photo, or just a rating if they choose.
- Once a review is submitted, the average rating of the beer will update.
- Each review shows the username as a link - so that users can view the profile of a particular reviewer.

#### Add Beer:

- Authenticated users can add a new beer. The form is simple and uncluttered. The minimal information required is: Beer name, Brewery, Country, Strength. 
- Optionally, users can add: Photo, tags. If a photo is not provided, the default beer-list logo will act as a placeholder automatically.
- It is not possible to add a beer that has already been added. User will be shown an error message and a link to the already existing beer.

#### Login/Signup/password-reset:

- The authentication is handled using Django's built in autentication system. 
- Users can reset their password, and custom forms are styled in the same way as the rest of the app.
- New passwords will be sent to the users email address.
- I added email authentication to the default authentication system. Users can login with either their username or email address.

#### Donate

- A chance to donate £3 to the developers! This feature is included to demonstrate the implementation of a 'Stripe' payment system.
- The payment form is set in 'test mode' and a card number of 4242 4242 4242 4242, with any expiration date in the future will demonstrate how it works.

### Features yet to implement

- Search for users on the 'people' page
- A comments system, so users could comment on other users' reviews
- The option to keep your liked beer list private
- Add user profile photo

## Technologies Used

- [Python 3](https://python.org/): The backend of this project is written in python
- [Django 2](http://djangoproject.com/): This is a heavyweight framework that helps with the rapid development of larger apps, with many built-in features such as the authentication system and database integration. There are also many third-party plugins to help with different aspects of the build. For example, I used 'crispy forms' to help with the UX of the forms, and 'taggit' to implement the tag feature. 
- [Bootstrap 4](https://getbootstrap.com/): I used the latest version of Bootstrap to speed up development and keep the design consistent throughout the app.
- [Ajax](https://en.wikipedia.org/wiki/Ajax_(programming)): AJAX is used for the 'likes' to illiminate the need for a whole page refresh
- [AWS S3](https://aws.amazon.com/s3/): Amazon Simple Storage Service (Amazon S3) is an object storage service. I created a new 'bucket' to host my static files and media.
- [Travis CI](https://travis-ci.org/): Travis continious integration ensures the build is passing with each commit to Github.
- [Stripe](https://stripe.com/): For secure payment

## Testing

I used Django's built in testing framework to create a test suite. I also used 'coverage' to help show which parts of the code were being tested.

The Beer app  and the Accounts app have their own test directory. The majority of the tests are in the Beer app. As I improve my test writing, I intend to increase coverage and write more tests for each app.

The tests can be ran from the command line using:
```
python3 manage.py test

// or if using coverage:

coverage run manage.py test
```

The automated tests are seperated as follows: 

#### Test views:

##### Beer app

 - Tests for each view, making sure the correct status code returns, and the correct template is being rendered
 - 
##### Accounts app

 - Tests for each view, making sure redirects are functioning upon login and logout

#### Test models:

##### Beer app: 

test_models.py:
 - Test beer and brewery are capitalized
 - Test ratings are averaged
 - Test message is shown if no ratings
 - Test 'likes' count is added to
 - Test 'get_absolute_url' returns correctly
 

#### Test forms:

##### Beer app 

 - Test that a beer can be added
 - Test a beer cannot be added without the required fields
 - Test that the form is validated with correct message
 

##### Accounts app

 - Test that user can login


I underwent thorough manual testing of each element including:

- Once logged in, users can add a beer to the database
- If the beer is already in the database, an error is shown with a correct link
- Users will not be able to leave a review if logged out
- All links and redirects work
- The Stripe payment works
- The website was tested across different screen sizes and devices to ensure elements were displayed correctly

#### Screen sizes:

The layout was designed using a "mobile first" approach, with  changes at the medium and large breakpoints. 

On small screens, each beer takes up the full width of the screen.
On large screens, the page is divided into 2 columns - one larger containing the beer/reviews, and a side section containing links to related beers.

The navbar is a side-nav with burger-icon for small and medium screens, and is a full top-navbar with dropdown links for larger screens.

#### Bugs:

- When adding or editing a beer, any tags added at the time were not being added. The inclusion of ``` form.save_m2m() ``` after the form.save() fixed this.
- Images were not being uploaded at the time of adding a new beer. I had forgotten to include ```request.FILES``` in the line ```form = BeerCreateForm(request.POST, request.FILES)```

#### Bugs left to fix:

- I struggled to implement the code to redirect a user to the page they were on afer logging in. For example, if a user is looking at a beer and wants to leave a review, they need to login. 
- After logging in I would like the user to be redirected to the beer they were previouly looking at. At the moment, the user is redirected to the index page.  
- When a user is adding a new beer, at the moment they only get notified that the beer already exists after they submit the form. This could be annoying to the user. I would like to notify the user if the beer exists as they are typing the beer/brewery. 
- Fixing non capitalized country and beer names is tricky. I have implemented a function that checks if the county is less than 4 letters (ie. USA, UK) and makes it uppercase, and title case if longer. However, this does not work for a beer name such as 'Best IPA' which would return as 'Best Ipa'

## Deployment

The project is deployed on Heroku. I followed these steps:
```
heroku login
heroku apps create the-beer-list-app
```
- Create requirements.txt and a Procfile
- Login to Heroku and select 'PostgreSQL' addon database
- Configure new database in settings.py (using environment variables for sensitive information) and in Heroku app settings
```
git push -u heroku master
heroku ps:scale web=1
```
- Set Heroku app settings - Config Vars to IP 0.0.0.0 and PORT 5000
- Set database and AWS variables in Heroku app settings - Config Vars.

### Development/deployment:
The config vars are different for devlopment and deployment. For development, config vars will need to be set as environment variables. In my development environment I kept the environment variable in a .bashrc file, which was not included in git commits.
For development, Django will use the Sqlite database, whilst the deployed version used a postgresql database.
The settings are as follows:
```
import os

if development:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

else:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
    
```

### Static/media files

My static files, as well as any images users upload are all hosted on AWS using S3.

### To run the files locally:

- Download the files from the github repo, ensure all requirements are installed and environment variables are set up:
```
pip install -r requirements.txt

```

## Credits

This app is intended only as an educational project.


#### Photos/images:

- Beer photos are taken from various brewery websites and google images
- User images are my own, or taken from google images
- Beer List logo: I purchased a bottle icon from [iconfinder](https://www.iconfinder.com/) and edited it in Adobe Illustrator to recolour it, tweak the shape, and create the circle background

#### Acknowledgements

- Ajax code adapted from https://www.youtube.com/watch?v=wh2Nzc9wKXM&t=0s&list=PLKILtxhEt4-RT-GkrDkJDLuRPQfSK-6Yi&index=39
- CSS animation effect on title lettering adapted from https://css-tricks.com/snippets/css/typewriter-effect/
- Smooth scroll: https://www.w3schools.com/jquery/tryit.asp?filename=tryjquery_eff_animate_smoothscroll