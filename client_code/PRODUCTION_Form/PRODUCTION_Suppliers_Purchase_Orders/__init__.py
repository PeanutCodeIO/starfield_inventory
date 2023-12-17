from ._anvil_designer import PRODUCTION_Suppliers_Purchase_OrdersTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .Purchase_Orders import Purchase_Orders

class PRODUCTION_Suppliers_Purchase_Orders(PRODUCTION_Suppliers_Purchase_OrdersTemplate):
  def __init__(self,supplier_id = None, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.supplier_id = supplier_id

    # Any code you write here will run before the form opens.
    cmpt = Purchase_Orders()
    self.content_panel.clear()
    self.content_panel.add_component(cmpt)
    

  def new_po_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass
