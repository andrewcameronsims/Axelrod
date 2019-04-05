# Ruby port of axelrod.py
require 'pry'

require_relative 'helpers'
require_relative 'agent'
require_relative 'model'

model = Axelrod.new(10, 100, 5, 5)
binding.pry
model.run