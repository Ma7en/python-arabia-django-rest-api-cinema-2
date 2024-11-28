http://127.0.0.1:8000/api/meals/meal_pk/rate_meals

http://127.0.0.1:8000/api/meals/meal_pk/rate_meals ==> post

-   request data = stars
-   request user = user or user name
-   stars + user from request
-   pk from url
-   endpoint to update/create rate for specifiec meal using Meal vieset not rate
-   views > add the custom function with @action decarator

2- Meal list API to show the average rating and number of ratings

-   models > add custom function\method in the model to calculate the avg and sum
-   serializers > add the avg and sum to the fields
