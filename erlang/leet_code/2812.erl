%%%-------------------------------------------------------------------
%%% Copyright © 2010-2024 <a href="https://github.com/jerodg/">JerodG</a>
%%%
%%% This program is free software: you can redistribute it and/or modify it under the terms of the
%%% Server Side Public License (SSPL) as published by MongoDB, Inc., either version 1 of the License,
%%% or (at your option) any later version.
%%%
%%% This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
%%% even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the SSPL
%%% for more details.
%%%
%%% The above copyright notice and this permission notice shall be included in all copies or
%%% substantial portions of the Software. You should have received a copy of the SSPL along with this
%%% program. If not, see <a href="https://www.mongodb.com/licensing/server-side-public-license">SSPL</a>.
%%%-------------------------------------------------------------------
-spec maximum_safeness_factor(Grid :: [[integer()]]) -> integer().
maximum_safeness_factor(Grid) ->
  N = length(Grid),
  Score = lists:foldl(fun(_, Acc) -> lists:map(fun(_) -> N * N end, Acc) end, lists:seq(0, N - 1), lists:seq(0, N - 1)),
  bfs(Grid, Score, N).


bfs(Grid, Score, N) ->
  Q = queue:new(),
  Score1 = lists:foldl(fun(Row, Acc) -> update_score(Row, Acc, Grid, Q) end, Score, lists:seq(0, N - 1)),
  bfs_loop(Q, Score1, Grid, N).


update_score(Row, Score, Grid, Q) ->
  lists:foldl(fun(Col, Acc) -> update_cell(Row, Col, Acc, Grid, Q) end, Score, lists:seq(0, length(Grid) - 1)).


update_cell(Row, Col, Score, Grid, Q) ->
  case lists:nth(Col + 1, lists:nth(Row + 1, Grid)) of
    1 ->
      Score1 = replace(Row, Col, 0, Score),
      queue:in({Row, Col}, Q),
      Score1;
    _ -> Score
  end.


bfs_loop(Q, Score, Grid, N) ->
  case queue:is_empty(Q) of
    true -> Score;
    false ->
      {{value, {X, Y}}, Q1} = queue:out(Q),
      S = lists:nth(Y, lists:nth(X, Score)),
      Score1 = lists:foldl(fun(Dir, Acc) ->
        update_direction(X, Y, Dir, Acc, Grid, S, Q1, N) end, Score, [{0, -1}, {0, 1}, {-1, 0}, {1, 0}]),
      bfs_loop(Q1, Score1, Grid, N)
  end.


update_direction(X, Y, {DX, DY}, Score, Grid, S, Q, N) ->
  NewX = X + DX,
  NewY = Y + DY,
  case (NewX >= 0) and (NewX < N) and (NewY >= 0) and (NewY < N) and (lists:nth(NewY, lists:nth(NewX, Score)) > 1 + S) of
    true ->
      Score1 = replace(NewX, NewY, 1 + S, Score),
      queue:in({NewX, NewY}, Q),
      Score1;
    false -> Score
  end.


replace(Row, Col, Value, Matrix) ->
  lists:map(fun(R, RI) ->
    if RI =:= Row -> replace_in_row(Col, Value, R); true -> R end end, Matrix, lists:seq(0, length(Matrix) - 1)).


replace_in_row(Col, Value, Row) ->
  lists:map(fun(C, CI) -> if CI =:= Col -> Value; true -> C end end, Row, lists:seq(0, length(Row) - 1)).
