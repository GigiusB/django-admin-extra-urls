# -*- coding: utf-8 -*-
from admin_extra_urls.extras import reverse, check_permission


def test_upload(app, admin_user):
    url = reverse('admin:demo_demomodel4_changelist')
    res = app.get(url, user=admin_user)
    res = res.click('Upload')
    form = res.forms[0]
    form['file'] = ('file', "abc".encode('utf8'))
    res = form.submit()
    assert res.status_code == 302
