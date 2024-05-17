defmodule Solution do
  import Enum, only: [with_index: 1, count: 1]

  @spec shortest_path(grid :: [[integer]], k :: integer) :: integer
  def shortest_path(grid, k) do
    map =
      for {row, y} <- with_index(grid),
          {i, x} <- with_index(row),
          into: %{} do
        {{x, y}, i}
      end

    goal = {count(List.first(grid)) - 1, count(grid) - 1}
    dijkstra(map, %{{0, 0} => k}, goal, 0)
  end

  defp dijkstra(_map, positions, _goal, _steps) when map_size(positions) == 0, do: -1
  defp dijkstra(_map, _positions, {x, y}, steps) when steps > (x + 1) * (y + 1), do: -1

  defp dijkstra(map, positions, goal, steps) do
    if positions[goal] do
      steps
    else
      next =
        for {{x, y}, k} <- positions,
            {x, y} <- [
              {x - 1, y},
              {x + 1, y},
              {x, y - 1},
              {x, y + 1}
            ],
            Map.has_key?(map, {x, y}),
            k = k - map[{x, y}],
            k >= 0,
            reduce: %{} do
          acc -> Map.update(acc, {x, y}, k, fn v -> max(k, v) end)
        end

      dijkstra(map, next, goal, steps + 1)
    end
  end
end
