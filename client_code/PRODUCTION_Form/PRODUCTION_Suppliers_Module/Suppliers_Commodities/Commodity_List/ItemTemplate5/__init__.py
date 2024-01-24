from ._anvil_designer import ItemTemplate5Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class ItemTemplate5(ItemTemplate5Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.com_lbl.text = self.item["commodity_name"]
    self.price_lbl.text = self.item["commodity_price"]
    self.amount_lbl.text = self.item["commodity_amount"]
    self.measurement_lbl.text = self.item['commodity_measurement']
    self.updated_lbl.text = self.item["date_updated"]
    
