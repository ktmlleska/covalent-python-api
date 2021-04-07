# :coding: utf-8
# :copyright: Copyright (c) 2021 Lluis Casals Marsol
# Copyright 2021 Lluis Casals Marsol.
# All rights reserved.
# Please see the LICENSE file that should have been included as part of this
# package.

def generate_url(base_url, url_args):
    return base_url + "/".join(url_args) + "?"