import json
from urllib.parse import quote
import urllib.request
import xml.etree.ElementTree as ET
from django.core.management.base import BaseCommand
from django.conf import settings
from pycon.schedule.models import Slot

SECTIONS_URL = 'http://api.eventmobi.com/en/api/v1/events/PYCONCA2015/sections/125690'
FEEDBACK_URL_BASE = 'http://eventmobi.com/pyconca2015/agenda/125690'
BITLY_URL = 'https://api-ssl.bitly.com/v3/shorten'

def shorten_url(url):
    params = '?access_token={}&longUrl={}'.format(settings.BITLY_KEY, quote(url))
    with urllib.request.urlopen(BITLY_URL + params) as response:
        response = response.read()
    j = json.loads(response.decode('ascii'))
    return j['data']['url']

class Command(BaseCommand):
    help = 'Imports feedback URLs from EventBrite API'

    def handle(self, *args, **options):
        with urllib.request.urlopen(SECTIONS_URL) as response:
            xml = response.read()
        tree = ET.fromstring(xml)
        for child in tree.find('response').find('items').getchildren():
            eventbrite_id = child.find('id').text
            slot_id = child.find('external_id').text
            url = FEEDBACK_URL_BASE + '/' + eventbrite_id
            short_url = shorten_url(url)
            print(short_url)
            slot = Slot.objects.get(id=slot_id)
            slot.feedback_url = short_url
            slot.save()
