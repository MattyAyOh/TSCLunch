class Lunch < ActiveRecord::Base
  has_many :lunch_items, :class_name => 'LunchItem', dependent: :destroy
end
