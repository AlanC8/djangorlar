def search_models_callback(request):
    return [
        "users.User",
        "habits.Challenge",
        "habits.Participant",
        "habits.CheckIn",
        "habits.Notification",
        "habits.ChallengeStatus",
        "auth.Group",
    ]
    
def search_callback(request):
    return [
        {
            "title": "Django Documentation",
            "link": "https://docs.djangoproject.com/en/stable/",
            "icon": "launch", # Иконка из Material Symbols
            "target": "_blank", # Открывать в новой вкладке
        },
        {
            "title": "Unfold Documentation",
            "link": "https://unfold-admin.github.io/",
            "icon": "description",
            "target": "_blank",
        },
    ]