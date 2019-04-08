# frozen_string_literals: true

class Agent
  attr_reader :culture

  def initialize(traits, features, model)
    @culture = (1..features).map { |feature| traits.sample }
    @model = model
  end

  def share_culture(other_index)
    other = @model.agents[other_index]
    similarity = 0

    other.culture.each_with_index do |feature, index|
      if feature == @culture[index]
        similarity += 1
      end
    end

    interaction_probability = similarity / @culture.length

    if rand < interaction_probability
      to_share = rand(0..@culture.length - 1)
      other.culture[to_share] = @culture[to_share]
    end
  end
end