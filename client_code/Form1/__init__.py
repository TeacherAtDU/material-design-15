from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def submit_button_click(self, **event_args):
    # Display a popup that says 'You clicked the button'
    alert("You clicked the button")
    # Any code you write here will run before the form opens.
