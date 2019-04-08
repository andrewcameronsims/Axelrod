module GridHelper
  def get_coords(index, size)
    [index % size, index / size]
  end

  def get_index(coords, size)
    (coords[1] * size - 1) + (coords[0] + 1)
  end

  def get_neighbors(loc)
    [
      loc[0], loc[1] - 1,
      loc[0], loc[1] + 1,
      loc[0] - 1, loc[1],
      loc[0] + 1, loc[1],
      loc[0] - 1, loc[1] - 1,
      loc[0] + 1, loc[1] - 1,
      loc[0] - 1, loc[1] + 1,
      loc[0] + 1, loc[1] + 1
    ]
  end
end