# context_processors.py


def language_context(request):
    full_path = request.get_full_path()
    if full_path.startswith("/en"):
        lang = "en"
        path = full_path[3:]  # Remove '/en'
    elif full_path.startswith("/fa"):
        lang = "fa"
        path = full_path[3:]  # Remove '/fa'
    else:
        lang = "none"
        path = full_path

    return {
        "lang": lang,
        "path": path,
    }
