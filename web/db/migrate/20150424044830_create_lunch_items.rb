class CreateLunchItems < ActiveRecord::Migration
  def change
    create_table :lunch_items do |t|
      t.string :name
      t.boolean :vegetarian
      t.integer :lunch_id

      t.timestamps null: false
    end
  end
end
