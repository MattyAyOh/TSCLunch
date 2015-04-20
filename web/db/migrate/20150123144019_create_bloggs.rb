class CreateBloggs < ActiveRecord::Migration
  def change
    create_table :bloggs do |t|
      t.string :title
      t.text :text

      t.timestamps null: false
    end
  end
end
