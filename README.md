Simple test to run a React frontend served by Flask in one Heroku app.


    $git clone https://....

    $cd centaur-ploven

    $heroku create

    $heroku buildpacks:add heroku/nodejs
    $heroku buildpacks:add heroku/python


    $git push heroku master

    $heroku ps:scale web=1

