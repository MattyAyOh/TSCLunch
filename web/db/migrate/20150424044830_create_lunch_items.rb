class CreateLunchItems < ActiveRecord::Migration
  def change
    create_table :lunch_items do |t|
      t.string :name, null: false
      t.boolean :vegetarian
      t.integer :lunch_id, null: false

      t.timestamps null: false
    end
  end
end
