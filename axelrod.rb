# Ruby port of axelrod.py

require_relative 'helpers'
require_relative 'agent'
require_relative 'model'

SEED = 50

model = Axelrod.new()
model.run