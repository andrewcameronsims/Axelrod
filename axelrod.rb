# Ruby port of axelrod.py
require 'pry'

require_relative 'helpers'
require_relative 'agent'
require_relative 'model'

TRAITS = [1, 2, 3, 4, 5]

model = Axelrod.new(10, 100, 5, TRAITS)
binding.pry
model.run