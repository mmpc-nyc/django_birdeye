# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from birdeye.cron import get_review_requests

class BirdEyeTestCase(TestCase):

    def test_get_review_requests(self):
        data = get_review_requests(600000)
        print(data)