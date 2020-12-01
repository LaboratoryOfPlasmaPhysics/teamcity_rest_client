"""Main module."""
# -*- coding: utf-8 -*-
import requests


def make_build_payload(build_id, properties, change, tags):
    return f"""
<build>
  <buildType id="{build_id}"/>
  <properties>
    {" ".join(['<property name="' + prop[0] + '" value="' + prop[1] + '"/>' for prop in properties])}
   </properties>
  <Changes>
        <change id="{change}"/>
  </Changes>
  <tags>
    {" ".join(['<tag name="' + tag + '"/>' for tag in tags])}
  </tags>
</build>
"""


def start_build(server, user, token, build_id, properties, change, tags):
    url = server + '/app/rest/buildQueue'
    auth = (user, token)
    payload = make_build_payload(build_id, properties, change, tags)
    headers = {'Content-Type': 'application/xml'}
    response = requests.post(url, data=payload, headers=headers, auth=auth)
    return response.ok
