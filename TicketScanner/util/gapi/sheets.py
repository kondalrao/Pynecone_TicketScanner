import os
import pygsheets
from pcconfig import config


class GSheet():
  """Api for Google Sheets"""

  def __init__(self):
    self.secrets = {config.gapi_secrets}
    self.gc = pygsheets.authorize(self.secrets)
    self.wks = self.gc.open(config.worksheet).worksheet()

  def process_code(self, code) -> str:
    order_cell = self.wks.find(code)[0]
    order_cell_address = order_cell.address
    status_cell_address = order_cell_address - (0,1)
    status_cell = self.wks.cell(status_cell_address)

    if status_cell.value == '':
      status_cell.set_value("1")
      row = self.wks.get_row(status_cell.row)
      return f"{row[8]}: {row[17]} tkts"
    else:
      return "Tickets already given..."


gs = GSheet()
# gs.process_code("2748410")