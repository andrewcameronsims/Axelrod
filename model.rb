# frozen_string_literals: true

require_relative 'helpers'

class Axelrod
  attr_reader :agents

  include GridHelper

  def initialize(size, runs, features, traits)
    @size = size
    @runs = runs
    @features = features
    @traits = traits
    @agents = (1..@size ** 2).map do |agent|
      Agent.new(@traits, @features, self)
    end
  end

  def tick
    active = @agents.sample
    active_index = @agents.find_index(active)
    active_coords = get_coords(active_index, @size)
    active_neighbors = get_neighbors(active_coords)
    passive_coords = active_neighbors.sample
    passive_index = get_index(passive_coords, @size)
    active.share_culture(passive_index)
  end

  def display
    count = 0
    @agents.each do |agent|
      puts if count % @size == 0
      print agent.culture
      count += 1
      puts if count == @size ** 2
    end
  end

  def run
    puts "\nInitial state:"
    self.display
    @runs.times do
      self.tick
    end
    puts
    puts "Final state:"
    self.display
  end
end