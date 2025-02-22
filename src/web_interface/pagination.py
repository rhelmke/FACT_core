from flask_paginate import Pagination


def get_pagination(**kwargs):
    kwargs.setdefault('record_name', 'records')
    return Pagination(
        css_framework='bootstrap4',
        link_size='sm',
        show_single_page=False,
        format_total=True,
        format_number=True,
        **kwargs,
    )


def extract_pagination_from_request(request, config):
    page = int(request.args.get('page', 1))
    per_page = request.args.get('per_page')
    if not per_page:
        per_page = int(config['database']['results-per-page'])
    else:
        per_page = int(per_page)
    offset = (page - 1) * per_page
    return page, per_page, offset
