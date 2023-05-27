from masonite.routes import Route
from masonite.authentication import Auth

ROUTES = [
  Route.get("/", "WelcomeController@show").name("welcome"),
  Route.get("/blog", "BlogController@show"),
  ]

ROUTES += Auth.routes()
