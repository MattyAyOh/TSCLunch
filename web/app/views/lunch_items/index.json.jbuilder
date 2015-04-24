json.array!(@lunch_items) do |lunch_item|
  json.extract! lunch_item, :id, :name, :vegetarian, :lunch_id
  json.url lunch_item_url(lunch_item, format: :json)
end
