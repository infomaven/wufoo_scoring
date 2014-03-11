# scripts/delete_all_entries.py
# for use with Django Extensions module

from wufoo_scoring.apps.wufoo_responder.models import Entry
from wufoo_scoring.apps.wufoo_responder.models import Item

def run():
    # delete foreign key dependencies first
    all_items = Item.objects.all()
    all_items.delete()
    
    all_entries = Entry.objects.all()
    all_entries.delete()
    