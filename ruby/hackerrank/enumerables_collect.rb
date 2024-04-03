# frozen_string_literal: true

def rot13(secret_messages)
  secret_messages.map do |message|
    message.tr("a-z", "n-za-m")
  end
end