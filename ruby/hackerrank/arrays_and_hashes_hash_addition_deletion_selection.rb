# frozen_string_literal: true

hackerrank = Hash.new
hackerrank[543121] = 100
hackerrank.keep_if { |key, val| key.is_a? Integer }
hackerrank.delete_if { |key, val| key.even? }