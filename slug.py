def slugify(text):
    return text.lower().replace(" ", "-").replace("_", "-").strip("-")
