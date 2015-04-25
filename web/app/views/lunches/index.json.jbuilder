json.array!(@lunches) do |lunch|
  json.extract! lunch, :id, :supplier, :sign_up_date_time, :creator
  json.url lunch_url(lunch, format: :json)
end
