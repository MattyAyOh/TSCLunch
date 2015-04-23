# TSCLunch

## Required software
* Ruby 2+
* Rails 4+
* Rake 10+
* Sqlite3
* `mailcatcher` (See notes)

### _Notes_
* According to the [documentation](http://mailcatcher.me/), `mailcatcher` should not be included in the Gemfile. Run `gem install mailcatcher` locally to install `mailcatcher`.
* When running on Windows, the Development Kit is needed in addition to Rails. Download it [here](http://rubyinstaller.org/downloads/).
* Database conflicts can occur if there is an environment variable named `DATABASE_URL` (run `echo $DATABASE_URL` to see if you have one set). This needs to be removed or it will take precedence over the `database.yml` file.
* At the time of writing, there were no admin creation options. Roles will need to be manually updated in the database until a method exists see [this](https://github.com/MattyAyOh/TSCLunch/pull/2#issuecomment-95416409) comment.