# frozen_string_literal: true

def serial_average(n)
  "#{n[0, 3]}-#{((n[4, 5].to_f + n[10, 5].to_f) / 2).round(2)}"
end