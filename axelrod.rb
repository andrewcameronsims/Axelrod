# Ruby port of axelrod.py
require 'pry'

require_relative 'helpers'
require_relative 'agent'
require_relative 'model'

TRAITS = (0..9).to_a

model = Axelrod.new(6, 10000, 5, TRAITS)
model.run