#!/usr/bin/env python

class BodyMiddleware(object):
    def process_request(self, request):
        try:
            setattr(request, "raw_post_data", getattr(request, "body"))
        except:
            pass
