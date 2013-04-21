def set_urls(app, routes):
    """
        Connects url patterns to actions for the `app`.
    """
    for rule in routes:
        if len(rule) == 3: rule = rule + ({}, )

        url_rule, endpoint, view_func, opts = rule
        app.add_url_rule(url_rule, endpoint=endpoint, view_func=view_func, **opts)