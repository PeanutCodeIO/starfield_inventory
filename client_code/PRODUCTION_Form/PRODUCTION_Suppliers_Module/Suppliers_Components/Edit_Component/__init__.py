from ._anvil_designer import Edit_ComponentTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..... import component_cache

class Edit_Component(Edit_ComponentTemplate):
  def __init__(self,supplier_id = None, cmpt_id = None, switch = None, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.supplier_id = supplier_id
    self.cmpt_id = cmpt_id 
    

    # Any code you write here will run before the form opens.
    if switch != True:
      self.commodity_card.visible = False
      component_data = component_cache.get_component_data(supplier_id, cmpt_id)
      print(component_data)
  
      # Set the text for each textbox, with a check for None values or empty strings
      self.text_box_component.text = component_data['item_name'] if component_data['item_name'] else "No Data"
      self.text_box_sku.text = component_data['sku'] if component_data['sku'] else "No Data"
      self.text_area_description.text = component_data['description'] if component_data['description'] else "No Data"
      self.drop_down_primary_unit.selected_value = component_data['unit_measurement'] if component_data['unit_measurement'] else "No Data"
      
      # For numeric fields, set to 0.0 if None or empty
      self.text_box_order_minimum.text = str(component_data['order_minimun']) if component_data['order_minimun'] is not None else "0.0"
      self.text_box_item_cost.text = "{:.2f}".format(component_data['item_cost']) if component_data['item_cost'] is not None else "0.0"
      self.minimum_order_cost.text = str(component_data['minimum_order_cost']) if component_data['minimum_order_cost'] is not None else "0.0"
      self.text_box_stock_alert.text = str(component_data['low_stock_alert']) if component_data['low_stock_alert'] is not None else "0.0"
  
  
      measurements = [
      "Millimeters",
      "Centimeters",
      "Meters",
      "Milligrams",
      "Grams",
      "Kilograms",
      "Tonnes",
      "Milliliters",
      "Liters",
      "Cubic meters",
      "Square meters",
      "Pieces",
      "Units",
      "Packs",
      "Boxes",
      "Sheets",
      "Rolls",
      "Length"
      ]
      self.drop_down_primary_unit.items = measurements
    else:
      self.commodity_card.visible = True
      component_data = component_cache.get_component_data(supplier_id, cmpt_id)
      print(component_data)
  
      # Set the text for each textbox, with a check for None values or empty strings
      self.text_box_component.text = component_data['item_name'] if component_data['item_name'] else "No Data"
      self.text_box_sku.text = component_data['sku'] if component_data['sku'] else "No Data"
      self.text_area_description.text = component_data['description'] if component_data['description'] else "No Data"
      self.drop_down_primary_unit.selected_value = component_data['unit_measurement'] if component_data['unit_measurement'] else "No Data"

      #Set each textbox for the commodity card
      self.com_tb.text = component_data['commodity_name']
      self.amount_tb.text = component_data['commodity_amount']
      self.measurement_tb.text = component_data['commodity_measurement']
      self.price_tb.text = component_data['commodity_price']

      self.text_box_item_cost.enabled = False
      self.drop_down_primary_unit.enabled = False
      
      # For numeric fields, set to 0.0 if None or empty
      self.text_box_order_minimum.text = str(component_data['order_minimun']) if component_data['order_minimun'] is not None else "0.0"
      self.text_box_item_cost.text = "{:.2f}".format(component_data['item_cost']) if component_data['item_cost'] is not None else "0.0"
      self.minimum_order_cost.text = str(component_data['minimum_order_cost']) if component_data['minimum_order_cost'] is not None else "0.0"
      self.text_box_stock_alert.text = str(component_data['low_stock_alert']) if component_data['low_stock_alert'] is not None else "0.0"
  
  
      measurements = [
      "Millimeters",
      "Centimeters",
      "Meters",
      "Milligrams",
      "Grams",
      "Kilograms",
      "Tonnes",
      "Milliliters",
      "Liters",
      "Cubic meters",
      "Square meters",
      "Pieces",
      "Units",
      "Packs",
      "Boxes",
      "Sheets",
      "Rolls",
      "Length"
      ]
      self.drop_down_primary_unit.items = measurements



      return 
  def close_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('PRODUCTION_Form.PRODUCTION_Suppliers_Module.Suppliers_Components', self.supplier_id)
    pass




  
  def text_box_item_cost_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    try:
        # Ensure text box values are treated as strings
        cost_text = str(self.text_box_item_cost.text)
        minimum_order_text = str(self.text_box_order_minimum.text)

        # Use a default value of 0.0 if the text box is empty or contains non-numeric text
        cost = float(cost_text) if cost_text.strip() else 0.0
        minimum_order = float(minimum_order_text) if minimum_order_text.strip() else 0.0

        # Calculate and format the result to two decimal places
        calculated_cost = cost * minimum_order
        self.minimum_order_cost.text = "{:.2f}".format(calculated_cost)
    except ValueError:
        # Handle cases where the input cannot be converted to a float
        self.minimum_order_cost.text = ""
    except ZeroDivisionError:
        # Handle division by zero error
        self.minimum_order_cost.text = "Infinity"  # Or any other appropriate message



  def text_box_order_minimum_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    try:
        # Ensure text box values are treated as strings
        cost_text = str(self.text_box_item_cost.text)
        minimum_order_text = str(self.text_box_order_minimum.text)

        # Use a default value of 0.0 if the text box is empty or contains non-numeric text
        cost = float(cost_text) if cost_text.strip() else 0.0
        minimum_order = float(minimum_order_text) if minimum_order_text.strip() else 0.0

        # Calculate and format the result to two decimal places
        calculated_cost = cost * minimum_order
        self.minimum_order_cost.text = "{:.2f}".format(calculated_cost)
    except ValueError:
        # Handle cases where the input cannot be converted to a float
        self.minimum_order_cost.text = ""
    except ZeroDivisionError:
        # Handle division by zero error
        self.minimum_order_cost.text = "Infinity"  # Or any other appropriate message





  def button_save_click(self, **event_args):
    """This method is called when the button is clicked"""
    
    commodities = component_cache.get_component_data(self.supplier_id, self.cmpt_id)
    switch = commodities['is_commodity']

    if switch != True: 
      # Create a dictionary with all the new fields
      component_data = {
          #"supplier_id": self.supplier_id,
          "component_id": self.cmpt_id, 
          "item_name": self.text_box_component.text,
          "sku": self.text_box_sku.text,
          "description": self.text_area_description.text,
          "unit_measurement": self.drop_down_primary_unit.selected_value,
          "order_minimum": float(self.text_box_order_minimum.text) if self.text_box_order_minimum.text else 0.0,
          "item_cost": float(self.text_box_item_cost.text) if self.text_box_item_cost.text else 0.0,
          "minimum_order_cost": float(self.minimum_order_cost.text) if self.minimum_order_cost.text else 0.0 ,
          "low_stock_alert": float(self.text_box_stock_alert.text) if self.text_box_stock_alert.text else 0.0,
      }
  
      # Check if the mandatory fields are filled
      mandatory_fields = ["item_name", "description", "unit_measurement"]
  
      for field in mandatory_fields:
        if not component_data[field]:
          anvil.alert(f"Please fill out the {field.replace('_', ' ')} field.")
          return
  
      # Send the component data to the server for storage
      anvil.server.call('edit_component_commodity',self.supplier_id,  component_data, switch)
      anvil.alert("Component updated successfully.")
  
      # Refresh component data cache (if applicable)
      component_cache.refresh_supplier_components()
  
      open_form('PRODUCTION_Form.PRODUCTION_Suppliers_Module.Suppliers_Components', self.supplier_id)
    else:


      return 
    pass


  
  def cost_change_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    result = anvil.alert(title="Confirm new price change", buttons=[("Yes", True), ("No", False)])
    if result:
      new_cost = float(self.text_box_item_cost.text)
      anvil.server.call('record_cmpt_cost_change', self.supplier_id, self.cmpt_id, new_cost )
      anvil.alert("New cost has been saved")
      component_cache.refresh_supplier_components()
    else:
      return None
    pass



  def amount_tb_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    commodities = component_cache.get_component_data(self.supplier_id, self.cmpt_id)
    comm = component_cache.get_commodities(self.supplier_id)

    # Ensure text box values are treated as strings and handle empty or non-numeric input
    amount_text = str(self.amount_tb.text)
    amount = float(amount_text) if amount_text.strip() else 0.0
    price = commodities['commodity_price']

    # Calculate and display the price
    calculated_price = amount * price
    self.price_tb.text = "{:.2f}".format(calculated_price)

    # Update the item cost
    unit_price = calculated_price  # Directly use the calculated price
    self.text_box_item_cost.text = "{:.2f}".format(unit_price)

    # Handle the order minimum
    order_minimum_text = str(self.text_box_order_minimum.text)
    order_minimum = float(order_minimum_text) if order_minimum_text.strip() else 0.0
    calculated_order_cost = unit_price * order_minimum
    self.minimum_order_cost.text = "{:.2f}".format(calculated_order_cost)


