
   #Donfigure heroku client for api app
   cd /src/ohana-api/
   wget -qO- https://toolbelt.heroku.com/install-ubuntu.sh | sh
   heroku login
   heroku create
   heroku config:set API_BASE_HOST=quiet-springs-1693.herokuapp.com/api
   heroku config:set API_BASE_URL=http://quiet-springs-1693.herokuapp.com/api/
   heroku config:set MAILER_URL=quiet-springs-1693.herokuapp.com
   heroku config:set DEVISE_SECRET_KEY=`cat /dev/urandom| tr -dc 'a-z0-9' | head -c 128`
   heroku addons:add mongolab
   heroku addons:add redistogo
   heroku addons:add mandrill
   heroku addons:add searchbox
   heroku config:set ELASTICSEARCH_URL=`heroku config:get SEARCHBOX_URL`
   git push heroku master
   heroku config:set SECRET_TOKEN=`cat /dev/urandom| tr -dc 'a-z0-9' | head -c 128`
   heroku run script/setup_db
   heroku open
