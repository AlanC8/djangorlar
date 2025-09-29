# Python modules
from typing import Any
import datetime
# Django modules
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse


def hello_view(
    request: HttpRequest,
    *args: tuple[Any, ...],
    **kwargs: dict[str, Any]
) -> HttpResponse:
    """
    Return a simple HTML page.

    Parameters:
        request: HttpRequest
            The request object.
        *args: list
            Additional positional arguments.
        **kwargs: dict
            Additional keyword arguments.
    
    Returns:
        HttpResponse
            Rendered HTML page with a name in the context.
    """

    return render(
        request=request,
        template_name="index.html",
        status=200
    )

def users_view(
    request: HttpRequest,
    *args: tuple[Any, ...],
    **kwargs: dict[str, Any]
) -> HttpResponse:
    return render(
        request=request,
        template_name="users.html",
        context={"users": [{
            "name": "Alan",
            "surname": "Smith",
            "email": "alan@gmail.com",
            "age": 20,
            "city": "Almaty"
        }, {
            "name": "Bek",
            "surname": "Smith",
            "email": "bek@gmail.com",
            "age": 21,
            "city": "Astana"
        }, {
            "name": "Zhalgas",
            "surname": "Smith",
            "email": "zhalgas@gmail.com",
            "age": 22,
            "city": "Shymkent"
        }, {
            "name": "Zhomart",
            "surname": "Smith",
            "email": "zhomart@gmail.com",
            "age": 23,
            "city": "Karagandy"
        }]},
        status=200
    )


def city_time_view(
    request: HttpRequest,
    city_name: str = None,
    *args: tuple[Any, ...],
    **kwargs: dict[str, Any]
) -> HttpResponse:

    city_timezones = {
        "almaty": {"offset": 6, "display_name": "Almaty", "country": "Kazakhstan"},
        "calgary": {"offset": -7, "display_name": "Calgary", "country": "Canada"},
        "moscow": {"offset": 3, "display_name": "Moscow", "country": "Russia"},
        "utc": {"offset": 0, "display_name": "UTC", "country": "Universal"},
        "astana": {"offset": 6, "display_name": "Astana", "country": "Kazakhstan"},
        "shymkent": {"offset": 6, "display_name": "Shymkent", "country": "Kazakhstan"},
        "karagandy": {"offset": 6, "display_name": "Karagandy", "country": "Kazakhstan"}
    }

    available_cities = [
        {"key": "almaty", "name": "Almaty", "country": "Kazakhstan"},
        {"key": "calgary", "name": "Calgary", "country": "Canada"},
        {"key": "moscow", "name": "Moscow", "country": "Russia"},
        {"key": "utc", "name": "UTC", "country": "Universal"},
    ]

    if city_name is None:
        city_name = "almaty"

    city_key = city_name.lower().replace(" ", "").replace("-", "")

    city_info = city_timezones.get(city_key, city_timezones["almaty"])

    utc_now = datetime.datetime.now(datetime.timezone.utc)
    city_timezone = datetime.timezone(datetime.timedelta(hours=city_info["offset"]))
    city_time = utc_now.astimezone(city_timezone)

    return render(
        request=request,
        template_name="city_time.html",
        context={
            "selected_city": city_info,
            "city_time": city_time,
            "available_cities": available_cities,
            "current_path": request.path
        },
        status=200
    )


def counter_view(
    request: HttpRequest,
    *args: tuple[Any, ...],
    **kwargs: dict[str, Any]
) -> HttpResponse:

    # Get current counter value from session, default to 0
    counter = request.session.get('counter', 0)

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'increment':
            counter += 1
        elif action == 'reset':
            counter = 0

        # Save counter back to session
        request.session['counter'] = counter

        # Redirect to avoid form resubmission
        return redirect('counter')

    return render(
        request=request,
        template_name="counter.html",
        context={"counter": counter},
        status=200
    )